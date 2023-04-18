# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa Plugin API - Connection Hidden Client
__all__ = ['ConnectionClient']


# general imports
import os
import errno
from pathlib import Path
import json

# import the iom and isapi (plugin)
from pydea_statica.idea_statica_config import *
from pydea_statica.error_handle import *
from pydea_statica.connection import *
from pydea_statica.project_item import *
from pydea_statica.connection_code_setup import *


class ConnectionClient():
    def __init__(self):
        self.pydea_config = pydea_config
        self.idea_statica_path = pydea_config['IDEA.StatiCa']['INSTALL_PATH']
        self.project_open = False
        self.project_file_path = ''
        # create client factory - for creation and disposal of client
        self.factory = isapi.ConnHiddenClientFactory(self.idea_statica_path)
        # attempt creation of client
        try:
            self.client : isapi.ConnectionHiddenCheckClient = self.factory.Create()
        except:
            raise PydeaStatiCaError(-1, 'Failed to create ConnectionHiddenCheckClient.')
        
        self.connections : list[Connection] = []

    def add_bolt_assembly(self, bolt_assembly_name : str):
        self.client.AddBoltAssembly(bolt_assembly_name)
    
    def close_project(self):
        # try close of project
        try:
            self.client.CloseProject()
        except:
            raise PydeaStatiCaError(-1, 'Failed to save as specified Connection project (.ideaCon) file ')
        # clear project open status and file path
        self.project_open = False
        self.project_file_path = ''

    def create_project_from_iom(self, iom_xml_file_path : str, iom_res_xml_file_path : str, new_idea_con_file_path : str):
        try:
            self.client.CreateConProjFromIOM(iom_xml_file_path, iom_res_xml_file_path, new_idea_con_file_path)
        except:
            raise PydeaStatiCaError(-1, 'Failed to create Connection project (.ideaCon) from specified IOM XML files.')
        # update project open status and file path
        self.project_open = True
        self.project_file_path = new_idea_con_file_path
        # retrieve project information
        self.__get_project_info()
        # retrieve connections
        self.__get_connections()

    def get_bolt_assemblies(self):
        items = self.client.GetBoltAssembliesInProject()
        return [ProjectBoltAssembly(item) for item in items]
    
    def get_code_setup(self) -> CodeSetup:
        code_setup_json : CodeSetupJson = json.loads(self.client.GetCodeSetupJSON())
        return CodeSetup(code_setup_json)
    
    def get_cross_sections(self):
        items = self.client.GetCrossSectionsInProject()
        return [ProjectCrossSection(item) for item in items]

    def get_materials(self):
        items = self.client.GetMaterialsInProject()
        return [ProjectMaterial(item) for item in items]

    def open_project(self, file_path : str):
        if not Path(file_path).is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        try:
            self.client.OpenProject(file_path)
        except:
            raise PydeaStatiCaError(-1, 'Failed to open specified Connection project (.ideaCon) file ')
        # update project open status and file path
        self.project_open = True
        self.project_file_path = file_path
        # retrieve project information
        self.__get_project_info()
        # retrieve connections
        self.__get_connections()

    def __get_project_info(self):
        self.__project_info : iom_connection.ConProjectInfo = self.client.GetProjectInfo()
        self.project_author : str = self.__project_info.Author
        self.__connections : [iom_connection.ConnectionInfo] = self.__project_info.Connections
        self.project_date = self.__project_info.Date
        self.project_description : str = self.__project_info.Description
        self.project_design_code : str = self.__project_info.DesignCode
        self.project_name :str = self.__project_info.Name
        self.project_number : str = self.__project_info.ProjectNumber
    
    def __get_connections(self):
        for connection in self.__connections:
            self.connections.append(Connection(self.client, connection))
    
    def save_project(self):
        self.client.Save()
    
    def save_as_project(self, file_path : str):
        # try project save as
        try:
            self.client.SaveAsProject(file_path)
        except:
            raise PydeaStatiCaError(-1, 'Failed to save as specified Connection project (.ideaCon) file.')
        # update project file path
        self.project_file_path = file_path
    
    def set_code_setup(self, code_setup_json):
        self.client.UpdateCodeSetupJSON(code_setup_json)
    
    def set_cross_section_material(self, cross_section : ProjectCrossSection, material : ProjectMaterial):
        self.client.SetCrossSectionMaterial(cross_section.identifier, material.identifier)
    
    def update_connection_from_iom(self, iom_xml_file_path : str, iom_res_xml_file_path : str):
        self.client.UpdateConProjFromIOM(iom_xml_file_path, iom_res_xml_file_path)
        # retrieve project information
        self.__get_project_info()
        # retrieve connections
        self.__get_connections()