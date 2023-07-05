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
HEADER_RANGE = 'B3:D3'

RESULTS_START = 'F4'


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
    # drop include column - not required
    batch_input_df = batch_input_df.drop(columns=['Include'])
    return batch_input_df.to_dict('records')


def process_connections(run_inputs, working_folder : Path):
    conn_client = ConnectionClient()
    in_conn_folder = working_folder.joinpath('in_connections')
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
        print(f"\t> Calculating connection model... this can take a few minutes...", end='')
        conn_client.connections[conn_index].calculate()
        conn_client.save_project()
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
    xw.Book("./examples/IdeaStatiCaDesignResistanceBatch/IdeaStatiCaConnDesignResistanceBatch.xlsm").set_mock_caller()
    main()