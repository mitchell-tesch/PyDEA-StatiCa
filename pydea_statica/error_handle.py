# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa - Error Handling
__all__ = ['PydeaStatiCaError']

class Error(Exception):
    """Error base class for non-exit exceptions"""
    pass


class PydeaStatiCaError(Error):
    """General Pydea.StatiCa API Error Class"""
    def __init__(self, value : int, message : str):
        self.value : int = value
        self.message : str = message