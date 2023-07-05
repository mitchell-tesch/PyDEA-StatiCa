# encoding: utf-8
# module IdeaStatiCa.Plugin.Grpc.Services calls itself Services
# from IdeaStatiCa.Plugin, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GrpcBlobStorageService(GrpcBlobStorageServiceBase):
    """ GrpcBlobStorageService(logger: IPluginLogger, blobStorageProvider: IBlobStorageProvider, chunkSize: int) """
    def Delete(self, request, context):
        """ Delete(self: GrpcBlobStorageService, request: ContentRequest, context: ServerCallContext) -> Task[VoidResponse] """
        pass

    def Exist(self, request, context):
        """ Exist(self: GrpcBlobStorageService, request: ContentRequest, context: ServerCallContext) -> Task[ExistResponse] """
        pass

    def GetEntries(self, request, context):
        """ GetEntries(self: GrpcBlobStorageService, request: GetEntriesRequest, context: ServerCallContext) -> Task[GetEntriesResponse] """
        pass

    def Read(self, request, responseStream, context):
        """ Read(self: GrpcBlobStorageService, request: ContentRequest, responseStream: IServerStreamWriter[ContentData], context: ServerCallContext) -> Task """
        pass

    def Write(self, requestStream, context):
        """ Write(self: GrpcBlobStorageService, requestStream: IAsyncStreamReader[ContentData], context: ServerCallContext) -> Task[VoidResponse] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger, blobStorageProvider, chunkSize):
        """ __new__(cls: type, logger: IPluginLogger, blobStorageProvider: IBlobStorageProvider, chunkSize: int) """
        pass


class GrpcService(GrpcServiceBase, IGrpcService, IGrpcSender):
    """ GrpcService(logger: IPluginLogger, maxDataLength: int) """
    def ConnectAsync(self, requestStream, responseStream, context):
        """ ConnectAsync(self: GrpcService, requestStream: IAsyncStreamReader[GrpcMessage], responseStream: IServerStreamWriter[GrpcMessage], context: ServerCallContext) -> Task """
        pass

    def HandleMessageAsync(self, *args): #cannot find CLR method
        """ HandleMessageAsync(self: GrpcService, message: GrpcMessage) -> Task """
        pass

    def RegisterHandler(self, handlerId, handler):
        """ RegisterHandler(self: GrpcService, handlerId: str, handler: IGrpcMessageHandler) """
        pass

    def SendMessageAsync(self, message):
        """ SendMessageAsync(self: GrpcService, message: GrpcMessage) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger, maxDataLength):
        """ __new__(cls: type, logger: IPluginLogger, maxDataLength: int) """
        pass

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnected(self: GrpcService) -> bool

Set: IsConnected(self: GrpcService) = value
"""


    ClientConnected = None
    ClientDisconnected = None


