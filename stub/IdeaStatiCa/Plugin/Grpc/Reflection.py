# encoding: utf-8
# module IdeaStatiCa.Plugin.Grpc.Reflection calls itself Reflection
# from IdeaStatiCa.Plugin, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Extensions(object):
    # no doc
    @staticmethod
    def FromVal(src, value):
        """
        FromVal(src: GrpcReflectionArgument, value: object) -> GrpcReflectionArgument
        FromVal(src: GrpcReflectionCallbackData, value: object) -> GrpcReflectionCallbackData
        """
        pass

    __all__ = [
        'FromVal',
    ]


class GrpcMethodInvokerHandler(object, IMethodInvoker, IGrpcMessageHandler):
    """ GrpcMethodInvokerHandler(handlerName: str, grpcSender: IGrpcSender, logger: IPluginLogger) """
    def HandleClientMessage(self, message, grpcSender):
        """ HandleClientMessage(self: GrpcMethodInvokerHandler, message: GrpcMessage, grpcSender: IGrpcSender) -> Task[object] """
        pass

    def HandleServerMessage(self, message, grpcSender):
        """ HandleServerMessage(self: GrpcMethodInvokerHandler, message: GrpcMessage, grpcSender: IGrpcSender) -> Task[object] """
        pass

    def InvokeMethod(self, methodName, returnType, arguments):
        """ InvokeMethod[T](self: GrpcMethodInvokerHandler, methodName: str, returnType: Type, *arguments: Array[object]) -> T """
        pass

    def SendMessageDataSync(self, grpcMessage):
        """ SendMessageDataSync(self: GrpcMethodInvokerHandler, grpcMessage: GrpcMessage) -> GrpcMessage """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, handlerName, grpcSender, logger):
        """ __new__(cls: type, handlerName: str, grpcSender: IGrpcSender, logger: IPluginLogger) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GrpcSender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrpcSender(self: GrpcMethodInvokerHandler) -> IGrpcSender

"""


    HandlerName = None


class GrpcReflectionArgument(object):
    """
    GrpcReflectionArgument(type: str, value: object)
    GrpcReflectionArgument()
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None, value=None):
        """
        __new__(cls: type, type: str, value: object)
        __new__(cls: type)
        """
        pass

    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParameterType(self: GrpcReflectionArgument) -> str

Set: ParameterType(self: GrpcReflectionArgument) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GrpcReflectionArgument) -> object

Set: Value(self: GrpcReflectionArgument) = value
"""



class GrpcReflectionCallbackData(object):
    """
    GrpcReflectionCallbackData()
    GrpcReflectionCallbackData(type: str, value: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: str, value: object)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GrpcReflectionCallbackData) -> object

Set: Value(self: GrpcReflectionCallbackData) = value
"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueType(self: GrpcReflectionCallbackData) -> str

Set: ValueType(self: GrpcReflectionCallbackData) = value
"""



class GrpcReflectionInvokeData(object):
    """ GrpcReflectionInvokeData() """
    MethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodName(self: GrpcReflectionInvokeData) -> str

Set: MethodName(self: GrpcReflectionInvokeData) = value
"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: GrpcReflectionInvokeData) -> IEnumerable[GrpcReflectionArgument]

Set: Parameters(self: GrpcReflectionInvokeData) = value
"""



class GrpcReflectionMessageHandler(object, IGrpcMessageHandler[object], IGrpcMessageHandler):
    """ GrpcReflectionMessageHandler(instance: object, logger: IPluginLogger) """
    def HandleClientMessage(self, message, client):
        """ HandleClientMessage(self: GrpcReflectionMessageHandler, message: GrpcMessage, client: IGrpcSender) -> Task[object] """
        pass

    def HandleServerMessage(self, message, grpcSender):
        """ HandleServerMessage(self: GrpcReflectionMessageHandler, message: GrpcMessage, grpcSender: IGrpcSender) -> Task[object] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, instance, logger):
        """ __new__(cls: type, instance: object, logger: IPluginLogger) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsSynchronous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronous(self: GrpcReflectionMessageHandler) -> bool

"""



class GrpcReflectionMethodAttribute(Attribute, _Attribute):
    """ GrpcReflectionMethodAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class GrpcReflectionServer(GrpcServer, IGrpcServer, IGrpcCommunicator):
    """ GrpcReflectionServer(instance: object, logger: IPluginLogger, blobStorageProvider: IBlobStorageProvider, maxDataLength: int, chunkSize: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, instance, logger, blobStorageProvider, maxDataLength, chunkSize):
        """ __new__(cls: type, instance: object, logger: IPluginLogger, blobStorageProvider: IBlobStorageProvider, maxDataLength: int, chunkSize: int) """
        pass


class GrpcReflectionServiceAttribute(Attribute, _Attribute):
    """ GrpcReflectionServiceAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class GrpcServiceBasedReflectionClient(GrpcClient, IGrpcClient, IGrpcCommunicator, IGrpcService, IGrpcSender):
    """ GrpcServiceBasedReflectionClient[IReflectionService](logger: IPluginLogger) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger):
        """ __new__(cls: type, logger: IPluginLogger) """
        pass

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Service(self: GrpcServiceBasedReflectionClient[IReflectionService]) -> IReflectionService

"""


    Logger = None


class GrpcServiceClient(object):
    """ GrpcServiceClient[ServiceType](handlerName: str, grpcService: IGrpcService, logger: IPluginLogger) """
    @staticmethod # known case of __new__
    def __new__(self, handlerName, grpcService, logger):
        """ __new__(cls: type, handlerName: str, grpcService: IGrpcService, logger: IPluginLogger) """
        pass

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Service(self: GrpcServiceClient[ServiceType]) -> ServiceType

"""


    HandlerName = None


class IMethodInvoker:
    # no doc
    def InvokeMethod(self, methodName, returnType, arguments):
        """ InvokeMethod[T](self: IMethodInvoker, methodName: str, returnType: Type, *arguments: Array[object]) -> T """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMethodTask:
    # no doc
    def SendMessageDataSync(self, grpcMessage):
        """ SendMessageDataSync(self: IMethodTask, grpcMessage: GrpcMessage) -> GrpcMessage """
        pass

    def SetResult(self, message):
        """ SetResult(self: IMethodTask, message: GrpcMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class MethodTask(object, IMethodTask):
    """ MethodTask(logger: IPluginLogger, grpcSender: IGrpcSender, operationId: str) """
    def SendMessageDataSync(self, grpcMessage):
        """ SendMessageDataSync(self: MethodTask, grpcMessage: GrpcMessage) -> GrpcMessage """
        pass

    def SetResult(self, message):
        """ SetResult(self: MethodTask, message: GrpcMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger, grpcSender, operationId):
        """ __new__(cls: type, logger: IPluginLogger, grpcSender: IGrpcSender, operationId: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GrpcSender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrpcSender(self: MethodTask) -> IGrpcSender

"""


    OperationId = None


