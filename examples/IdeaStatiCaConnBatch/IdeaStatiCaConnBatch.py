# Development Environment Configuration
# required for those working within the development repository
import sys, os
# import of pytabs package via examples context
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from context import pydea_statica

# general imports
import xlwings as xw
import pandas as pd
from pathlib import Path
# pydea statica imports
from pydea_statica.connection_client import *
from pydea_statica.connection_loading import *


# Batching workbook configuration
INPUT_SHEET = 'Main'
HEADER_RANGE = 'B3:BI3'

BEAM_INDEX = ['Beam1', 'Beam2', 'Beam3', 'Beam4', 'Beam5', 'Beam6']
INT_TYPES = ['Position', 'AbsPosition', 'ForceIn']


def main():
    wb = xw.Book.caller()
    working_folder = Path(wb.fullname).parent
    
    print('\nReading run data from batching workbook... ', end='')
    run_inputs = read_batching_workbook(wb)
    print('done.')
    
    run_results = process_connections(run_inputs, working_folder)
    
    print(run_results)


def read_batching_workbook(wb : xw.Book):
    '''Extract run input data from batching workbook'''
    sheet = wb.sheets(INPUT_SHEET)
    batch_input_df : pd.DataFrame = sheet.range(HEADER_RANGE).options(pd.DataFrame, header=True, expand='down').value
    # assign sequential index
    batch_input_df = batch_input_df.reset_index()
    # remove runs that are disabled
    batch_input_df = batch_input_df[batch_input_df['Include'] == 'Yes']
    # replace yes/no with bools
    batch_input_df['LoadCase.CheckEquilibrium'].replace({'Yes': True, 'No': False}, inplace=True)
    batch_input_df['LoadCase.PercentageLoad'].replace({'Yes': True, 'No': False}, inplace=True)
    # store index as batch id
    batch_input_df['BatchId'] = batch_input_df.index
    # change data types of columns that need to be integers
    for beam_id in BEAM_INDEX:
        for int_type in INT_TYPES:
            batch_input_df[f'{beam_id}.{int_type}'] = batch_input_df[f'{beam_id}.{int_type}'].fillna(0).astype(int)
    # group by connection file
    batch_input_df = batch_input_df.groupby(['IdeaConFile', 'Connection.Name']).agg(list).reset_index()
    # drop include column - not required
    batch_input_df = batch_input_df.drop(columns=['Include'])
    return batch_input_df.to_dict('records')


def process_connections(run_inputs, working_folder : Path):
    conn_client = ConnectionClient()
    
    in_conn_folder = working_folder.joinpath('in_connections')
    out_conn_folder = working_folder.joinpath('out_connections')
    
    run_results = []
    
    for _r, run in enumerate(run_inputs):
        conn_file_name = run['IdeaConFile']
        conn_name = run['Connection.Name']
        print(f"\nProcessing run {_r+1} of {len(run_inputs)}: File: {conn_file_name} > Connection: {conn_name}")
        # open connection project
        conn_file_name = run['IdeaConFile']
        conn_file = in_conn_folder.joinpath(conn_file_name)
        conn_client.open_project(str(conn_file))
        # determine connection index from name
        conn_index = 0
        for index, conn in enumerate(conn_client.connections):
            if conn_name == conn.name:
                conn_index = index
                break
        
        print(f"\t> Establishing load cases batched... ", end='')
        load_cases = []
        for _c, case_name in enumerate(run['LoadCase.Name']):
            case_check_equilibrium = run['LoadCase.CheckEquilibrium'][_c]
            case_percentage_load = run['LoadCase.PercentageLoad'][_c]
            beam_forces = []
            beam_percent_forces = []
            for _b, beam_id in enumerate(BEAM_INDEX):
                if not run[f'{beam_id}.N'][_c]:
                    continue
                beam_forces.append({'beamSegmentId': _b+1,
                                    'position': run[f'{beam_id}.Position'][_c],
                                    'n': run[f'{beam_id}.N'][_c] * 1_000,
                                    'qy': run[f'{beam_id}.Qy'][_c] * 1_000,
                                    'qz': run[f'{beam_id}.Qz'][_c] * 1_000,
                                    'mx': run[f'{beam_id}.Mx'][_c] * 1_000,
                                    'my': run[f'{beam_id}.My'][_c] * 1_000,
                                    'mz': run[f'{beam_id}.Mz'][_c] * 1_000,
                                    'absPosition': run[f'{beam_id}.AbsPosition'][_c],
                                    'forceIn': run[f'{beam_id}.ForceIn'][_c]})
                beam_percent_forces.append({'beamSegmentId': _b+1,
                                            'position': run[f'{beam_id}.Position'][_c],
                                            'n': 0.0,
                                            'qy': 0.0,
                                            'qz': 0.0,
                                            'mx': 0.0,
                                            'my': 0.0,
                                            'mz': 0.0,
                                            'absPosition': run[f'{beam_id}.AbsPosition'][_c],
                                            'forceIn': run[f'{beam_id}.ForceIn'][_c]})
            load_cases.append(LoadingCase(_c+1, case_name, beam_forces, beam_percent_forces, case_check_equilibrium, case_percentage_load))
        print('done.')
        
        print(f"\t> Creating output connection model... ", end='')
        out_conn_file = out_conn_folder.joinpath(conn_file_name)
        out_conn_file = out_conn_file.with_name(out_conn_file.stem + f'_{conn_name}' + out_conn_file.suffix)
        conn_client.save_as_project(str(out_conn_file))
        print('done.')
        
        print(f"\t> Updating connection loading cases... ", end='')
        conn_client.connections[conn_index].set_loading(load_cases)
        conn_client.save_project()
        print('done.')
        
        print(f"\t> Calculating connection model... ", end='')
        conn_client.connections[conn_index].calculate()
        print('done.')
        
        print(f"\t> Retrieving connection model results... ", end='')
        conn_results = conn_client.connections[conn_index].get_results_json()
        print('done.')
        
        run_results.append({'IdeaConFile': conn_file_name,
                            'ConnectionName': conn_name,
                            'BatchId': run['BatchId'],
                            'Results': conn_results})
        
        conn_client.close_project()
    
    return run_results


if __name__ == "__main__":
    xw.Book("./examples/IdeaStatiCaConnBatch/IdeaStatiCaConnBatch.xlsm").set_mock_caller()
    main()