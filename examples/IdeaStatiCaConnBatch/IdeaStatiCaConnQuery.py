# Development Environment Configuration
# required for those working within the development repository
import sys, os
# import of pytabs package via examples context
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from context import pydea_statica
from pathlib import Path


from pydea_statica.connection_client import *


CONN_FILE = "./examples/IdeaStatiCaConnBatch/in_connections/TestFile.ideaCon"
CALCULATE = False


def main():
    conn_client = ConnectionClient()
    conn_file = Path(CONN_FILE)
    
    
    conn_client.open_project(str(conn_file))
    
    project_dict = {'code_setup': conn_client.get_code_setup(),
                    'cross_sections': conn_client.get_cross_sections(),
                    'bolt_assemblies': conn_client.get_bolt_assemblies(),
                    'materials': conn_client.get_materials()}
    
    connections_dict = {}
    for conn in conn_client.connections:
        connections_dict[conn.name] = {'model': conn.get_model(),
                                       'model_xml': conn.get_model_xml(),
                                       'all_data' : conn.get_all_data_xml(),
                                       'loading': conn.get_loading(),
                                       'cost' : conn.get_cost()}
        if CALCULATE:
            conn.calculate()
            connections_dict[conn.name].update({'results': conn.get_results_json()})

    conn_client.close_project()
    
    input('Any key to exit...')

if __name__ == "__main__":
    main()