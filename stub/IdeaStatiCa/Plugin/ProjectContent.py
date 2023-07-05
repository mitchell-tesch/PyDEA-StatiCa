# encoding: utf-8
# module IdeaStatiCa.Plugin.ProjectContent calls itself ProjectContent
# from IdeaStatiCa.Plugin, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IProjectContentStorage:
    # no doc
    def ReadData(self, contentId, outputStream):
        """ ReadData(self: IProjectContentStorage, contentId: str, outputStream: Stream) -> int """
        pass

    def WriteData(self, contentId, inputStream):
        """ WriteData(self: IProjectContentStorage, contentId: str, inputStream: Stream) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ProjectContentClientHandler(GrpcMethodInvokerHandler, IMethodInvoker, IGrpcMessageHandler, IProjectContent, IProjectContentStorage):
    """ ProjectContentClientHandler(client: IGrpcSender, logger: IPluginLogger) """
    def CopyContent(self, sourceContent):
        """ CopyContent(self: ProjectContentClientHandler, sourceContent: IProjectContent) """
        pass

    def Create(self, contentId):
        """ Create(self: ProjectContentClientHandler, contentId: str) -> Stream """
        pass

    def Delete(self, contentId):
        """ Delete(self: ProjectContentClientHandler, contentId: str) """
        pass

    def Exist(self, contentId):
        """ Exist(self: ProjectContentClientHandler, contentId: str) -> bool """
        pass

    def Get(self, contentId):
        """ Get(self: ProjectContentClientHandler, contentId: str) -> Stream """
        pass

    def GetContent(self):
        """ GetContent(self: ProjectContentClientHandler) -> List[ProjectDataItem] """
        pass

    def ReadData(self, contentId, outputStream):
        """ ReadData(self: ProjectContentClientHandler, contentId: str, outputStream: Stream) -> int """
        pass

    def WriteData(self, contentId, inputStream):
        """ WriteData(self: ProjectContentClientHandler, contentId: str, inputStream: Stream) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, client, logger):
        """ __new__(cls: type, client: IGrpcSender, logger: IPluginLogger) """
        pass


class ProjectContentServerHandler(object, IGrpcMessageHandler):
    """ ProjectContentServerHandler(projectContent: IProjectContent) """
    def HandleClientMessage(self, message, grpcSender):
        """ HandleClientMessage(self: ProjectContentServerHandler, message: GrpcMessage, grpcSender: IGrpcSender) -> Task[object] """
        pass

    def HandleServerMessage(self, message, grpcSender):
        """ HandleServerMessage(self: ProjectContentServerHandler, message: GrpcMessage, grpcSender: IGrpcSender) -> Task[object] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, projectContent):
        """ __new__(cls: type, projectContent: IProjectContent) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ContentSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentSource(self: ProjectContentServerHandler) -> IProjectContent

"""



class RemoteDataStream(MemoryStream, IDisposable):
    """ RemoteDataStream(contentId: str, storage: IProjectContentStorage) """
    def Close(self):
        """ Close(self: RemoteDataStream) """
        pass

    def CreateWaitHandle(self, *args): #cannot find CLR method
        """
        CreateWaitHandle(self: Stream) -> WaitHandle
        
            Allocates a System.Threading.WaitHandle object.
            Returns: A reference to the allocated itHandle.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RemoteDataStream, disposing: bool) """
        pass

    def EndWrite(self, asyncResult):
        """ EndWrite(self: RemoteDataStream, asyncResult: IAsyncResult) """
        pass

    def Flush(self):
        """ Flush(self: RemoteDataStream) """
        pass

    def FlushAsync(self, cancellationToken=None):
        """ FlushAsync(self: RemoteDataStream, cancellationToken: CancellationToken) -> Task """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A value of lse is usually appropriate. 
             ue to copy the current System.MarshalByRefObject object's identity to its clone, which will cause remoting client calls to be routed to the remote server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def ObjectInvariant(self, *args): #cannot find CLR method
        """
        ObjectInvariant(self: Stream)
            Provides support for a System.Diagnostics.Contracts.Contract.
        """
        pass

    def Write(self, buffer, offset, count):
        """ Write(self: RemoteDataStream, buffer: Array[Byte], offset: int, count: int) """
        pass

    def WriteAsync(self, buffer, offset, count, cancellationToken=None):
        """ WriteAsync(self: RemoteDataStream, buffer: Array[Byte], offset: int, count: int, cancellationToken: CancellationToken) -> Task """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: RemoteDataStream, value: Byte) """
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
    def __new__(self, contentId, storage):
        """ __new__(cls: type, contentId: str, storage: IProjectContentStorage) """
        pass

    ContentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentId(self: RemoteDataStream) -> str

"""



