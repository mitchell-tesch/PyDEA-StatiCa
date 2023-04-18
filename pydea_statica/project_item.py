# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa Plugin API - ProjectItem
__all__ = ['ProjectBoltAssembly', 'ProjectCrossSection', 'ProjectMaterial']

# import the iom and isapi (plugin)
from pydea_statica.idea_statica_config import *

class ProjectItem():
    def __init__(self, item : isapi.ProjectItem, item_type):
        self.identifier = item.Identifier
        self.name = item.Name
        self.type = item_type

class ProjectBoltAssembly(ProjectItem):
    def __init__(self, item : isapi.ProjectItem):
        super().__init__(item, 'BoltAssembly')

class ProjectCrossSection(ProjectItem):
    def __init__(self, item : isapi.ProjectItem):
        super().__init__(item, 'CrossSection')

class ProjectMaterial(ProjectItem):
    def __init__(self, item : isapi.ProjectItem):
        super().__init__(item, 'Material')