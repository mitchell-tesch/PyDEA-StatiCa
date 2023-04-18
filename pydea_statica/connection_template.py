# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa Plugin API - Connection Template
__all__ = ['ConnectionTemplateApplySettings']


# import the iom and isapi (plugin)
from pydea_statica.idea_statica_config import *


class ConnectionTemplateApplySettings(iom_connection.ApplyConnTemplateSetting):
    def __init__(self, default_bolt_assembly, default_cleat_cross_section,
                 default_concrete_material, default_stiff_member_cross_section):
        super().DefaultBoltAssemblyID = default_bolt_assembly
        super().DefaultCleatCrossSectionID = default_cleat_cross_section
        super().DefaultConcreteMaterialID = default_concrete_material
        super().DefaultStiffMemberCrossSectionID = default_stiff_member_cross_section