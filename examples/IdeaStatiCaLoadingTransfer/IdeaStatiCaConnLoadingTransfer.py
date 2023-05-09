# Development Environment Configuration
# required for those working within the development repository
import sys, os
# import of pytabs package via examples context
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from context import pydea_statica

# general imports
import math
import xlwings as xw
import pandas as pd
from pathlib import Path
import xml.etree.ElementTree as ET

# pydea statica imports
from pydea_statica.connection_client import *
from pydea_statica.connection_loading import *


# Batching workbook configuration
INPUT_SHEET = 'Main'
HEADER_RANGE = 'B3:X3'

BEAM_INDEX = ['Member1', 'Member2', 'Member3', 'Member4', 'Member5', 'Member6']
STR_TYPES = ['Name', 'Start', 'End']

RESULTS_START = 'Z4'


def main():
    wb = xw.Book.caller()
    working_folder = Path(wb.fullname).parent
    
    print('\nReading run data from batching workbook... ', end='')
    run_inputs = read_batching_workbook(wb)
    print('done.')
    
    run_results = process_connections(run_inputs, working_folder)
    
    print(f"\nWriting connection check results...")
    write_run_results(wb, run_results)
    
    wb.save()


def read_batching_workbook(wb : xw.Book):
    '''Extract run input data from batching workbook'''
    sheet = wb.sheets(INPUT_SHEET)
    batch_input_df : pd.DataFrame = sheet.range(HEADER_RANGE).options(pd.DataFrame, header=True, expand='down').value
    # assign sequential index
    batch_input_df = batch_input_df.reset_index()
    # remove runs that are disabled
    batch_input_df = batch_input_df[batch_input_df['Include'] == 'Yes']
    # store index as batch id
    batch_input_df['BatchId'] = batch_input_df.index
    # change data types of columns that need to be strings for member names
    for beam_id in BEAM_INDEX:
        for int_type in STR_TYPES:
            batch_input_df[f'{beam_id}.{int_type}'] = batch_input_df[f'{beam_id}.{int_type}'].fillna('').astype(str).replace(r'\.0', '', regex=True)
    # drop include column - not required
    batch_input_df = batch_input_df.drop(columns=['Include'])
    return batch_input_df.to_dict('records')


def process_connections(run_inputs, working_folder : Path):
    conn_client = ConnectionClient()
    loading_conn_client = ConnectionClient()
    
    in_conn_folder = working_folder.joinpath('in_connections')
    out_conn_folder = working_folder.joinpath('out_connections')
    
    run_results = []
    
    for _r, run in enumerate(run_inputs):
        # open connection model
        conn_file_name = run['ConnFile']
        conn_name = run['ConnName']
        print(f"\nProcessing run {_r+1} of {len(run_inputs)}):")
        print(f"\t> File: {conn_file_name}")
        print(f"\t> Connection: {conn_name}")
        # open connection project
        conn_file = in_conn_folder.joinpath(conn_file_name)
        conn_client.open_project(str(conn_file))
        # determine connection index from name
        conn_index = 0
        for index, conn in enumerate(conn_client.connections):
            if conn_name == conn.name:
                conn_index = index
                break
        # determine beam index from model data xml
        root : ET.Element = conn_client.connections[conn_index].get_model_xml()
        beam_index = {}
        for beam in root.findall('./Beams/BeamData'):
            beam_index[beam.find('Name').text] = int(beam.find('Id').text)
        print(f"\t\t> No. of members: {len(beam_index)} {tuple(beam_index)}")
        
        # open loading source model
        print(f"\t> Reading loading source model... ")
        loading_conn_file_name = run['LoadingConnFile']
        loading_conn_name = run['LoadingConnName']
        print(f"\t\t> Loading file: {loading_conn_file_name}")
        print(f"\t\t> Connection: {loading_conn_name}")
        # open loading connection project
        loading_conn_file = in_conn_folder.joinpath(loading_conn_file_name)
        loading_conn_client.open_project(str(loading_conn_file))
        # determine connection index from name
        loading_conn_index = 0
        for index, conn in enumerate(loading_conn_client.connections):
            if loading_conn_name == conn.name:
                loading_conn_index = index
                break
        # determine beam index from model data xml
        root : ET.Element = loading_conn_client.connections[loading_conn_index].get_model_xml()
        loading_beam_index = {}
        for _b, beam in enumerate(root.findall('./Beams/BeamData')):
            loading_beam_index[beam.find('Name').text] = _b
        print(f"\t\t> No. of members: {len(loading_beam_index)} {tuple(loading_beam_index)}")
        # reading loading
        loading_source = loading_conn_client.connections[loading_conn_index].get_loading()
        print(f"\t\t> No. of loading cases: {len(loading_source)}")
        # close loading source model
        loading_conn_client.close_project()
        
        # map source loading to connection model
        print(f"\t> Mapping source loading to connection... ")
        # read input mapping from workbook
        load_mapping = {}
        for beam_num in BEAM_INDEX:
            if not run[f'{beam_num}.Name']:
                continue
            load_mapping[run[f'{beam_num}.Name']] = []
            for position in ['Start', 'End']:
                if run[f'{beam_num}.{position}']:
                    load_mapping[run[f'{beam_num}.Name']].append(run[f'{beam_num}.{position}'])
        # establish new loading json for each source case
        loading = []
        for source_case in loading_source:
            beam_forces = []
            beam_percent_forces = []
            for dest_member, source_members in load_mapping.items():
                dest_seg_id = beam_index[dest_member]
                for source_member in source_members:
                    source_seg_id = loading_beam_index[source_member]
                    beam_forces.append({'beamSegmentId': dest_seg_id,
                                        'position': source_case.segment_forces[source_seg_id]['position'],
                                        'n': source_case.segment_forces[source_seg_id]['n'],
                                        'qy': source_case.segment_forces[source_seg_id]['qy'],
                                        'qz': source_case.segment_forces[source_seg_id]['qz'],
                                        'mx': source_case.segment_forces[source_seg_id]['mx'],
                                        'my': source_case.segment_forces[source_seg_id]['my'],
                                        'mz': source_case.segment_forces[source_seg_id]['mz'],
                                        'absPosition': source_case.segment_forces[source_seg_id]['absPosition'],
                                        'forceIn': source_case.segment_forces[source_seg_id]['forceIn']})
                    beam_percent_forces.append({'beamSegmentId': dest_seg_id,
                                                'position': source_case.percentage_segment_forces[source_seg_id]['position'],
                                                'n': source_case.percentage_segment_forces[source_seg_id]['n'],
                                                'qy': source_case.percentage_segment_forces[source_seg_id]['qy'],
                                                'qz': source_case.percentage_segment_forces[source_seg_id]['qz'],
                                                'mx': source_case.percentage_segment_forces[source_seg_id]['mx'],
                                                'my': source_case.percentage_segment_forces[source_seg_id]['my'],
                                                'mz': source_case.percentage_segment_forces[source_seg_id]['mz'],
                                                'absPosition': source_case.percentage_segment_forces[source_seg_id]['absPosition'],
                                                'forceIn': source_case.percentage_segment_forces[source_seg_id]['forceIn']})
            loading.append(LoadingCase(source_case.id, source_case.name, 
                                       beam_forces, beam_percent_forces, 
                                       source_case.check_equilibrium, source_case.percentage_load))
        
        print(f"\t> Creating output connection model... ", end='')
        out_conn_file = out_conn_folder.joinpath(conn_file_name)
        out_conn_file = out_conn_file.with_name(out_conn_file.stem + f'_{conn_name}' + out_conn_file.suffix)
        print('done.')
        
        print(f"\t> Updating connection loading cases... ", end='')
        conn_client.connections[conn_index].set_loading(loading)
        print('done.')

        print(f"\t> Calculating connection model... this can take a few minutes...", end='')
        conn_client.save_as_project(str(out_conn_file))
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
    
    conn_client.factory.Dispose()
    loading_conn_client.factory.Dispose()
    
    return run_results


def write_run_results(wb : xw.Book, run_results):
    sheet = wb.sheets(INPUT_SHEET)
    
    for run in run_results:
        results_out = ['', math.inf, 0.0, 0.0, True, False]
        if run['Results']:
            total_capacity = run['Results'].totalCapacity.__dict__
            for result in total_capacity.values():
                if result['appliedLoadPercentage'] < results_out[1]:
                    results_out = [result['loadCase'],
                                   result['appliedLoadPercentage'],
                                   result['maxPlateEps'],
                                   result['maxWeldEps'],
                                   result['singularityDetected'],
                                   result['checkStatus']]
        else:
            results_out = ['Unavailable', '', '', '', '', '']
            print(f"\t> Note: Run {run['BatchId'] + 1} has no Design Resistance (DR) results, check connection {run['ConnectionName']} in {run['IdeaConFile']}.")
        
        for col, result in enumerate(results_out):
                sheet.range(RESULTS_START).offset(row_offset=run['BatchId'], column_offset=col).value = result

if __name__ == "__main__":
    xw.Book("./examples/IdeaStatiCaLoadingTransfer/IdeaStatiCaConnLoadingTransfer.xlsm").set_mock_caller()
    main()