# encoding: utf-8
# module IdeaStatiCa.Plugin.Utilities calls itself Utilities
# from IdeaStatiCa.Plugin, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IdeaStatiCaSetupTools(object):
    # no doc
    @staticmethod
    def GetIdeaStatiCaInstallDir(version):
        """ GetIdeaStatiCaInstallDir(version: str) -> str """
        pass

    IdeaStatiCaRegistryKey = 'SOFTWARE\\IDEAStatiCa'
    __all__ = [
        'GetIdeaStatiCaInstallDir',
        'IdeaStatiCaRegistryKey',
    ]


class PortFinder(object):
    # no doc
    @staticmethod
    def FindPort(minPort, maxPort):
        """ FindPort(minPort: int, maxPort: int) -> int """
        pass

    __all__ = [
        'FindPort',
    ]


class ReflectionHelper(object):
    # no doc
    @staticmethod
    def GetLoadedType(fullName):
        """ GetLoadedType(fullName: str) -> Type """
        pass

    @staticmethod
    def GetMethodInvokeArguments(args):
        """ GetMethodInvokeArguments(*args: Array[object]) -> IEnumerable[GrpcReflectionArgument] """
        pass

    @staticmethod
    def InvokeMethodFromGrpc(instance, methodName, arguments):
        """ InvokeMethodFromGrpc(instance: object, methodName: str, arguments: IEnumerable[GrpcReflectionArgument]) -> Task[object] """
        pass

    @staticmethod
    def IsSimpleType(type):
        """ IsSimpleType(type: Type) -> bool """
        pass

    __all__ = [
        'GetLoadedType',
        'GetMethodInvokeArguments',
        'InvokeMethodFromGrpc',
        'IsSimpleType',
    ]


