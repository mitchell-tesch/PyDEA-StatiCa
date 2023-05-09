# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa Plugin API - Connection Element
__all__ = ['Connection']


# general imports
import json
import xml.etree.ElementTree as ET

# import the iom and isapi (plugin)
from pydea_statica.idea_statica_config import *
from pydea_statica.error_handle import *
# import ProjectItem
from pydea_statica.project_item import *
from pydea_statica.connection_template import *
from pydea_statica.connection_loading import *
from pydea_statica.connection_results import *


class Connection():
    def __init__(self, connection_client : isapi.ConnectionHiddenCheckClient, connection_info : iom_connection.ConnectionInfo):
        self.__client = connection_client
        self.__connection_info = connection_info
        self.description = self.__connection_info.Description
        self.id = self.__connection_info.Id
        self.identifier = self.__connection_info.Identifier
        self.name = self.__connection_info.Name
    
    def apply_parameters(self, parameters_json):
        self.__client.ApplyParameters(self.identifier, parameters_json)
    
    def apply_simple_template(self, template_file_path : str,
                              apply_settings : ConnectionTemplateApplySettings,
                              main_member : int, attached_members : list[int]):
        self.__client.ApplySimpleTemplate(self.identifier, template_file_path, apply_settings,
                                          main_member, attached_members)
    
    def apply_template(self, template_file_path : str,
                       apply_settings : ConnectionTemplateApplySettings):
        self.__client.ApplyTemplate(self.identifier, template_file_path, apply_settings)
    
    def calculate(self):
        self.__client.Calculate(self.identifier)
        
    def delete_all_operations(self):
        self.__client.DeleteAllOperations(self.identifier)
        
    def evaluate_expression(self, expression: str, arguments_json):
        self.__client.EvaluateExpression(self.identifier, expression, arguments_json)
    
    def export_to_template(self, file_path : str):
        self.__client.ExportToTemplate(self.identifier, file_path)
    
    def get_all_data_xml(self) -> ET.Element:
        return ET.fromstring(self.__client.GetAllConnectionData(self.identifier))
    
    def get_cost(self):
        return json.loads(self.__client.GetConnectionCost(self.identifier) or '{}')
    
    def get_loading(self) -> list[LoadingCase]:
        loading = []
        loading_json = json.loads(self.__client.GetConnectionLoadingJSON(self.identifier))
        for loading_case in loading_json:
            loading.append(LoadingCase.from_json(loading_case))
        return loading
    
    def get_model(self):
        # TODO returns IdeaRS.OpenModel.Connection ConnectionData (parsing?)
        return self.__client.GetConnectionModel(self.identifier)
    
    def get_model_xml(self) -> ET.Element:
        return ET.fromstring(self.__client.GetConnectionModelXML(self.identifier))
    
    def get_results_json(self):
        json_string = self.__client.GetCheckResultsJSON(self.identifier)
        if json_string not in  ['', ' ', 'Error']:
            return ConnectionResults(json.loads(json_string))
    
    def get_parameters_json(self):
        return json.loads(self.__client.GetParametersJSON(self.identifier) or '{}')
    
    def set_loading(self, connection_loading : list[LoadingCase]):
        loading_json = []
        for loading_case in connection_loading:
            loading_json.append(loading_case.to_json())
        self.__client.UpdateLoadingFromJson(self.identifier, json.dumps(loading_json))
        
    def set_member_cross_section(self, member_id : int, cross_section : ProjectCrossSection):
        self.__client.SetMemberCrossSection(self.identifier, member_id, cross_section.identifier)