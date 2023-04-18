# encoding: utf-8
# module IdeaStatiCa.Plugin.Grpc calls itself Grpc
# from IdeaStatiCa.Plugin, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def IGrpcMessageHandler(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

class ContentData(object, IMessage[ContentData], IMessage, IEquatable[ContentData], IDeepCloneable[ContentData], IBufferMessage):
    """
    ContentData()
    ContentData(other: ContentData)
    """
    def CalculateSize(self):
        """ CalculateSize(self: ContentData) -> int """
        pass

    def Clone(self):
        """ Clone(self: ContentData) -> ContentData """
        pass

    def Equals(self, other):
        """
        Equals(self: ContentData, other: object) -> bool
        Equals(self: ContentData, other: ContentData) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ContentData) -> int """
        pass

    def MergeFrom(self, *__args):
        """ MergeFrom(self: ContentData, other: ContentData)MergeFrom(self: ContentData, input: CodedInputStream) """
        pass

    def ToString(self):
        """ ToString(self: ContentData) -> str """
        pass

    def WriteTo(self, output):
        """ WriteTo(self: ContentData, output: CodedOutputStream) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: ContentData)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: ContentData) -> ByteString

Set: Data(self: ContentData) = value
"""


    DataFieldNumber = 1
    Descriptor = None
    Parser = None


class ContentRequest(object, IMessage[ContentRequest], IMessage, IEquatable[ContentRequest], IDeepCloneable[ContentRequest], IBufferMessage):
    """
    ContentRequest()
    ContentRequest(other: ContentRequest)
    """
    def CalculateSize(self):
        """ CalculateSize(self: ContentRequest) -> int """
        pass

    def Clone(self):
        """ Clone(self: ContentRequest) -> ContentRequest """
        pass

    def Equals(self, other):
        """
        Equals(self: ContentRequest, other: object) -> bool
        Equals(self: ContentRequest, other: ContentRequest) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ContentRequest) -> int """
        pass

    def MergeFrom(self, *__args):
        """ MergeFrom(self: ContentRequest, other: ContentRequest)MergeFrom(self: ContentRequest, input: CodedInputStream) """
        pass

    def ToString(self):
        """ ToString(self: ContentRequest) -> str """
        pass

    def WriteTo(self, output):
        """ WriteTo(self: ContentRequest, output: CodedOutputStream) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: ContentRequest)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BlobStorageId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlobStorageId(self: ContentRequest) -> str

Set: BlobStorageId(self: ContentRequest) = value
"""

    ContentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentId(self: ContentRequest) -> str

Set: ContentId(self: ContentRequest) = value
"""


    BlobStorageIdFieldNumber = 1
    ContentIdFieldNumber = 2
    Descriptor = None
    Parser = None


class ExistResponse(object, IMessage[ExistResponse], IMessage, IEquatable[ExistResponse], IDeepCloneable[ExistResponse], IBufferMessage):
    """
    ExistResponse()
    ExistResponse(other: ExistResponse)
    """
    def CalculateSize(self):
        """ CalculateSize(self: ExistResponse) -> int """
        pass

    def Clone(self):
        """ Clone(self: ExistResponse) -> ExistResponse """
        pass

    def Equals(self, other):
        """
        Equals(self: ExistResponse, other: object) -> bool
        Equals(self: ExistResponse, other: ExistResponse) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ExistResponse) -> int """
        pass

    def MergeFrom(self, *__args):
        """ MergeFrom(self: ExistResponse, other: ExistResponse)MergeFrom(self: ExistResponse, input: CodedInputStream) """
        pass

    def ToString(self):
        """ ToString(self: ExistResponse) -> str """
        pass

    def WriteTo(self, output):
        """ WriteTo(self: ExistResponse, output: CodedOutputStream) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: ExistResponse)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Exist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exist(self: ExistResponse) -> bool

Set: Exist(self: ExistResponse) = value
"""


    Descriptor = None
    ExistFieldNumber = 1
    Parser = None


class GetEntriesRequest(object, IMessage[GetEntriesRequest], IMessage, IEquatable[GetEntriesRequest], IDeepCloneable[GetEntriesRequest], IBufferMessage):
    """
    GetEntriesRequest()
    GetEntriesRequest(other: GetEntriesRequest)
    """
    def CalculateSize(self):
        """ CalculateSize(self: GetEntriesRequest) -> int """
        pass

    def Clone(self):
        """ Clone(self: GetEntriesRequest) -> GetEntriesRequest """
        pass

    def Equals(self, other):
        """
        Equals(self: GetEntriesRequest, other: object) -> bool
        Equals(self: GetEntriesRequest, other: GetEntriesRequest) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GetEntriesRequest) -> int """
        pass

    def MergeFrom(self, *__args):
        """ MergeFrom(self: GetEntriesRequest, other: GetEntriesRequest)MergeFrom(self: GetEntriesRequest, input: CodedInputStream) """
        pass

    def ToString(self):
        """ ToString(self: GetEntriesRequest) -> str """
        pass

    def WriteTo(self, output):
        """ WriteTo(self: GetEntriesRequest, output: CodedOutputStream) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: GetEntriesRequest)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BlobStorageId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlobStorageId(self: GetEntriesRequest) -> str

Set: BlobStorageId(self: GetEntriesRequest) = value
"""


    BlobStorageIdFieldNumber = 1
    Descriptor = None
    Parser = None


class GetEntriesResponse(object, IMessage[GetEntriesResponse], IMessage, IEquatable[GetEntriesResponse], IDeepCloneable[GetEntriesResponse], IBufferMessage):
    """
    GetEntriesResponse()
    GetEntriesResponse(other: GetEntriesResponse)
    """
    def CalculateSize(self):
        """ CalculateSize(self: GetEntriesResponse) -> int """
        pass

    def Clone(self):
        """ Clone(self: GetEntriesResponse) -> GetEntriesResponse """
        pass

    def Equals(self, other):
        """
        Equals(self: GetEntriesResponse, other: object) -> bool
        Equals(self: GetEntriesResponse, other: GetEntriesResponse) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GetEntriesResponse) -> int """
        pass

    def MergeFrom(self, *__args):
        """ MergeFrom(self: GetEntriesResponse, other: GetEntriesResponse)MergeFrom(self: GetEntriesResponse, input: CodedInputStream) """
        pass

    def ToString(self):
        """ ToString(self: GetEntriesResponse) -> str """
        pass

    def WriteTo(self, output):
        """ WriteTo(self: GetEntriesResponse, output: CodedOutputStream) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: GetEntriesResponse)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ContentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentId(self: GetEntriesResponse) -> RepeatedField[str]

"""


    ContentIdFieldNumber = 1
    Descriptor = None
    Parser = None


class GrpcBlobStorageClient(object, IDisposable):
    """ GrpcBlobStorageClient(logger: IPluginLogger, port: int, host: str, chunkSize: int, maxDataLength: int) """
    def DeleteAsync(self, blobStorageId, contentId):
        """ DeleteAsync(self: GrpcBlobStorageClient, blobStorageId: str, contentId: str) -> Task """
        pass

    def Dispose(self):
        """ Dispose(self: GrpcBlobStorageClient) """
        pass

    def ExistAsync(self, blobStorageId, contentId):
        """ ExistAsync(self: GrpcBlobStorageClient, blobStorageId: str, contentId: str) -> Task[bool] """
        pass

    def GetEntriesAsync(self, blobStorageId):
        """ GetEntriesAsync(self: GrpcBlobStorageClient, blobStorageId: str) -> Task[List[str]] """
        pass

    def ReadAsync(self, blobStorageId, contentId):
        """ ReadAsync(self: GrpcBlobStorageClient, blobStorageId: str, contentId: str) -> Task[Stream] """
        pass

    def WriteAsync(self, blobStorageId, contentId, content):
        """ WriteAsync(self: GrpcBlobStorageClient, blobStorageId: str, contentId: str, content: Stream) -> Task """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger, port, host, chunkSize, maxDataLength):
        """ __new__(cls: type, logger: IPluginLogger, port: int, host: str, chunkSize: int, maxDataLength: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class GrpcBlobStorageService(object):
    # no doc
    @staticmethod
    def BindService(*__args):
        """
        BindService(serviceImpl: GrpcBlobStorageServiceBase) -> ServerServiceDefinition
        BindService(serviceBinder: ServiceBinderBase, serviceImpl: GrpcBlobStorageServiceBase)
        """
        pass

    Descriptor = None
    GrpcBlobStorageServiceBase = None
    GrpcBlobStorageServiceClient = None
    __all__ = [
        'BindService',
        'GrpcBlobStorageServiceBase',
        'GrpcBlobStorageServiceClient',
    ]


class GrpcClient(object, IGrpcClient, IGrpcCommunicator, IGrpcService, IGrpcSender):
    """ GrpcClient(logger: IPluginLogger, maxDataLength: int) """
    def RegisterHandler(self, handlerId, handler):
        """ RegisterHandler(self: GrpcClient, handlerId: str, handler: IGrpcMessageHandler) """
        pass

    def SendMessageAsync(self, message):
        """ SendMessageAsync(self: GrpcClient, message: GrpcMessage) -> Task """
        pass

    def StartAsync(self, clientId, port):
        """ StartAsync(self: GrpcClient, clientId: str, port: int) -> Task """
        pass

    def StopAsync(self):
        """ StopAsync(self: GrpcClient) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger, maxDataLength):
        """ __new__(cls: type, logger: IPluginLogger, maxDataLength: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ClientID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClientID(self: GrpcClient) -> str

"""

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Host(self: GrpcClient) -> str

"""

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnected(self: GrpcClient) -> bool

"""

    Port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Port(self: GrpcClient) -> int

"""


    ClientConnected = None
    ClientDisconnected = None
    Logger = None


class GrpcMessage(object, IMessage[GrpcMessage], IMessage, IEquatable[GrpcMessage], IDeepCloneable[GrpcMessage], IBufferMessage):
    """
    GrpcMessage()
    GrpcMessage(other: GrpcMessage)
    """
    def CalculateSize(self):
        """ CalculateSize(self: GrpcMessage) -> int """
        pass

    def Clone(self):
        """ Clone(self: GrpcMessage) -> GrpcMessage """
        pass

    def Equals(self, other):
        """
        Equals(self: GrpcMessage, other: object) -> bool
        Equals(self: GrpcMessage, other: GrpcMessage) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GrpcMessage) -> int """
        pass

    def MergeFrom(self, *__args):
        """ MergeFrom(self: GrpcMessage, other: GrpcMessage)MergeFrom(self: GrpcMessage, input: CodedInputStream) """
        pass

    def ToString(self):
        """ ToString(self: GrpcMessage) -> str """
        pass

    def WriteTo(self, output):
        """ WriteTo(self: GrpcMessage, output: CodedOutputStream) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: GrpcMessage)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Buffer(self: GrpcMessage) -> ByteString

Set: Buffer(self: GrpcMessage) = value
"""

    ClientId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClientId(self: GrpcMessage) -> str

Set: ClientId(self: GrpcMessage) = value
"""

    Compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Compression(self: GrpcMessage) -> bool

Set: Compression(self: GrpcMessage) = value
"""

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: GrpcMessage) -> str

Set: Data(self: GrpcMessage) = value
"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: GrpcMessage) -> str

Set: DataType(self: GrpcMessage) = value
"""

    MessageName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MessageName(self: GrpcMessage) -> str

Set: MessageName(self: GrpcMessage) = value
"""

    MessageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MessageType(self: GrpcMessage) -> MessageType

Set: MessageType(self: GrpcMessage) = value
"""

    OperationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OperationId(self: GrpcMessage) -> str

Set: OperationId(self: GrpcMessage) = value
"""


    BufferFieldNumber = 7
    ClientIdFieldNumber = 3
    CompressionFieldNumber = 8
    DataFieldNumber = 2
    DataTypeFieldNumber = 5
    Descriptor = None
    MessageNameFieldNumber = 1
    MessageTypeFieldNumber = 6
    OperationIdFieldNumber = 4
    Parser = None
    Types = None


class GrpcReflectionServiceContractReflection(object):
    # no doc
    Descriptor = None
    __all__ = []


class GrpcReflectionServiceFactory(object):
    """ GrpcReflectionServiceFactory() """
    @staticmethod
    def CreateInstance(methodInvoker):
        """ CreateInstance[T](methodInvoker: IMethodInvoker) -> T """
        pass


class GrpcServer(object, IGrpcServer, IGrpcCommunicator):
    """ GrpcServer(logger: IPluginLogger, blobStorageProvider: IBlobStorageProvider, maxDataLength: int, chunkSize: int) """
    def StartAsync(self, clientId, port):
        """ StartAsync(self: GrpcServer, clientId: str, port: int) -> Task """
        pass

    def StopAsync(self):
        """ StopAsync(self: GrpcServer) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger, blobStorageProvider, maxDataLength, chunkSize):
        """ __new__(cls: type, logger: IPluginLogger, blobStorageProvider: IBlobStorageProvider, maxDataLength: int, chunkSize: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ClientID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClientID(self: GrpcServer) -> str

"""

    GrpcService = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrpcService(self: GrpcServer) -> GrpcService

"""

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Host(self: GrpcServer) -> str

"""

    Port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Port(self: GrpcServer) -> int

"""


    Logger = None


class GrpcService(object):
    # no doc
    @staticmethod
    def BindService(*__args):
        """
        BindService(serviceImpl: GrpcServiceBase) -> ServerServiceDefinition
        BindService(serviceBinder: ServiceBinderBase, serviceImpl: GrpcServiceBase)
        """
        pass

    Descriptor = None
    GrpcServiceBase = None
    GrpcServiceClient = None
    __all__ = [
        'BindService',
        'GrpcServiceBase',
        'GrpcServiceClient',
    ]


class IGrpcCommunicator:
    # no doc
    def StartAsync(self, clientId, port):
        """ StartAsync(self: IGrpcCommunicator, clientId: str, port: int) -> Task """
        pass

    def StopAsync(self):
        """ StopAsync(self: IGrpcCommunicator) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Host(self: IGrpcCommunicator) -> str

"""

    Port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Port(self: IGrpcCommunicator) -> int

"""



class IGrpcSender:
    # no doc
    def SendMessageAsync(self, message):
        """ SendMessageAsync(self: IGrpcSender, message: GrpcMessage) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IGrpcService(IGrpcSender):
    # no doc
    def RegisterHandler(self, handlerId, handler):
        """ RegisterHandler(self: IGrpcService, handlerId: str, handler: IGrpcMessageHandler) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnected(self: IGrpcService) -> bool

"""



class IGrpcClient(IGrpcCommunicator, IGrpcService, IGrpcSender):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IGrpcServer(IGrpcCommunicator):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GrpcService = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrpcService(self: IGrpcServer) -> GrpcService

"""



class VoidResponse(object, IMessage[VoidResponse], IMessage, IEquatable[VoidResponse], IDeepCloneable[VoidResponse], IBufferMessage):
    """
    VoidResponse()
    VoidResponse(other: VoidResponse)
    """
    def CalculateSize(self):
        """ CalculateSize(self: VoidResponse) -> int """
        pass

    def Clone(self):
        """ Clone(self: VoidResponse) -> VoidResponse """
        pass

    def Equals(self, other):
        """
        Equals(self: VoidResponse, other: object) -> bool
        Equals(self: VoidResponse, other: VoidResponse) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: VoidResponse) -> int """
        pass

    def MergeFrom(self, *__args):
        """ MergeFrom(self: VoidResponse, other: VoidResponse)MergeFrom(self: VoidResponse, input: CodedInputStream) """
        pass

    def ToString(self):
        """ ToString(self: VoidResponse) -> str """
        pass

    def WriteTo(self, output):
        """ WriteTo(self: VoidResponse, output: CodedOutputStream) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: VoidResponse)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Descriptor = None
    Parser = None


# variables with complex values

