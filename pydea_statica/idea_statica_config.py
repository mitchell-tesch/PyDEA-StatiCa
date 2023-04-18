# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa Configuration - API DLL handler
__all__ = ['iom', 'iom_connection', 'isapi', 'pydea_config']

# general library imports
import pydea_statica.pydea_statica_config as config
import warnings
import sys
# import pythonnet clr-loader
import clr


# Mock for pdoc pipeline where dependency is not available
# reference: https://blog.rtwilson.com/how-to-make-your-sphinx-documentation-compile-with-readthedocs-when-youre-using-numpy-and-scipy/
MOCK_MODULES = ['IdeaRS.OpenModel', 'IdeaStatiCa.Plugin']
class Mock(object):
    __qualname__ = 'mock'
    
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            # return type(name, (), {})
            return None
        else:
            return Mock()


# read pydea_statica_config.ini file
pydea_config = config.read_config()
idea_statica_path = pydea_config['IDEA.StatiCa']['INSTALL_PATH']

# pythonnet clr-loader try import of IdeaRS.OpenModel and IdeaStatiCa.Plugin else load Mock
warnings.filterwarnings('default')
try:
    sys.path.append(idea_statica_path)
    clr.AddReference('IdeaRS.OpenModel')
    clr.AddReference('IdeaStatiCa.Plugin')
    import IdeaRS.OpenModel as iom
    import IdeaRS.OpenModel.Connection as iom_connection
    import IdeaStatiCa.Plugin as isapi
except:
    for mod_name in MOCK_MODULES:
        sys.modules[mod_name] = Mock()
    import IdeaRS.OpenModel as iom
    import IdeaRS.OpenModel.Connection as iom_connection
    import IdeaStatiCa.Plugin as isapi
    warnings.warn("IDEA.StatiCa OpenModel and PlugIn DLL files not found in configured location, check pydea_statica_config.ini", ImportWarning)