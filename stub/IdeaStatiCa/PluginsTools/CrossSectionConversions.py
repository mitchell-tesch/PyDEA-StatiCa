# encoding: utf-8
# module IdeaStatiCa.PluginsTools.CrossSectionConversions calls itself CrossSectionConversions
# from IdeaStatiCa.Plugin, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Conversion(object):
    # no doc
    def Convert(self, text):
        """ Convert(self: Conversion, text: str) -> str """
        pass

    def IsMatch(self, txt):
        """ IsMatch(self: Conversion, txt: str) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, pattern: str) """
        pass

    MatchRegex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CssConversionBuilder(object):
    """ CssConversionBuilder(logger: IPluginLogger) """
    def Build(self):
        """ Build(self: CssConversionBuilder) -> CssConversions """
        pass

    def Register(self, convertor):
        """ Register(self: CssConversionBuilder, convertor: ICssConvertor) -> CssConversionBuilder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger):
        """ __new__(cls: type, logger: IPluginLogger) """
        pass


class CssConversions(object):
    # no doc
    def ConvertCrossSectionName(self, originalName):
        """ ConvertCrossSectionName(self: CssConversions, originalName: str) -> str """
        pass


class CustomConversion(Conversion):
    """ CustomConversion(pattern: str, func: Func[str, Regex, str]) """
    def Convert(self, text):
        """ Convert(self: CustomConversion, text: str) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pattern, func):
        """ __new__(cls: type, pattern: str, func: Func[str, Regex, str]) """
        pass

    MatchRegex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ICssConvertor:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Conversions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Conversions(self: ICssConvertor) -> IEnumerable[Conversion]

"""



class RegexReplace(Conversion):
    """
    RegexReplace(pattern: str, replace: str)
    RegexReplace(pattern: str, find: str, replace: str)
    """
    def Convert(self, text):
        """ Convert(self: RegexReplace, text: str) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pattern, *__args):
        """
        __new__(cls: type, pattern: str, replace: str)
        __new__(cls: type, pattern: str, find: str, replace: str)
        """
        pass

    MatchRegex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



