# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper

# general library imports
import os
import configparser


# location of pytabs configuration file
PYDEA_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pydea_statica_config.ini')


def read_config():
    """Read PYDEA.StatiCa configuration file"""
    pydea_config  = configparser.ConfigParser()
    pydea_config.read(PYDEA_CONFIG_PATH)
    return pydea_config