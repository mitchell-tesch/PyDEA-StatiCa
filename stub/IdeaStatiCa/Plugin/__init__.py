# encoding: utf-8
# module IdeaStatiCa.Plugin calls itself Plugin
# from IdeaStatiCa.Plugin, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationBIM(object, IApplicationBIM):
    """
    ApplicationBIM()

    ApplicationBIM(logger: IPluginLogger)
    """
    def ActivateInBIM(self, items):
        """ ActivateInBIM(self: ApplicationBIM, items: List[BIMItemId]) """
        pass

    def GetActiveSelection(self):
        """ GetActiveSelection(self: ApplicationBIM) -> List[BIMItemId] """
        pass

    def GetActiveSelectionModel(self, countryCode, requestedType):
        """ GetActiveSelectionModel(self: ApplicationBIM, countryCode: CountryCode, requestedType: RequestedItemsType) -> ModelBIM """
        pass

    def GetActiveSelectionModelXML(self, countryCode, requestedType):
        """ GetActiveSelectionModelXML(self: ApplicationBIM, countryCode: CountryCode, requestedType: RequestedItemsType) -> str """
        pass

    def GetActiveSelectionModelXMLAsync(self, countryCode, requestedType):
        """ GetActiveSelectionModelXMLAsync(self: ApplicationBIM, countryCode: CountryCode, requestedType: RequestedItemsType) -> Task[str] """
        pass

    def GetApplicationName(self):
        """ GetApplicationName(self: ApplicationBIM) -> str """
        pass

    def GetModelForSelection(self, countryCode, items):
        """ GetModelForSelection(self: ApplicationBIM, countryCode: CountryCode, items: List[BIMItemsGroup]) -> List[ModelBIM] """
        pass

    def GetModelForSelectionXML(self, countryCode, items):
        """ GetModelForSelectionXML(self: ApplicationBIM, countryCode: CountryCode, items: List[BIMItemsGroup]) -> str """
        pass

    def GetModelForSelectionXMLAsync(self, countryCode, items):
        """ GetModelForSelectionXMLAsync(self: ApplicationBIM, countryCode: CountryCode, items: List[BIMItemsGroup]) -> Task[str] """
        pass

    def ImportActive(self, *args): #cannot find CLR method
        """ ImportActive(self: ApplicationBIM, countryCode: CountryCode, requestedType: RequestedItemsType) -> ModelBIM """
        pass

    def ImportSelection(self, *args): #cannot find CLR method
        """ ImportSelection(self: ApplicationBIM, countryCode: CountryCode, items: List[BIMItemsGroup]) -> List[ModelBIM] """
        pass

    def IsCAD(self):
        """ IsCAD(self: ApplicationBIM) -> bool """
        pass

    def IsDataUpToDate(self):
        """ IsDataUpToDate(self: ApplicationBIM) -> bool """
        pass

    def SelectAsync(self, items):
        """ SelectAsync(self: ApplicationBIM, items: List[BIMItemId]) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, logger=None):
        """
        __new__(cls: type)

        __new__(cls: type, logger: IPluginLogger)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ApplicationBIM) -> int



"""

    IdeaStaticaApp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdeaStaticaApp(self: ApplicationBIM) -> IIdeaStaticaApp



Set: IdeaStaticaApp(self: ApplicationBIM) = value

"""

    Progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Progress(self: ApplicationBIM) -> IProgressMessaging



Set: Progress(self: ApplicationBIM) = value

"""



class AppStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum AppStatus, values: Finished (1), Started (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Finished = None
    Started = None
    value__ = None


class AutomationHosting(object, IBIMPluginClient[ClientInterface], IDisposable):
    """ AutomationHosting[MyInterface, ClientInterface](hostedService: MyInterface, logger: IPluginLogger, eventName: str, clientUrlFormat: str, automationUrlFormat: str) """
    def Dispose(self):
        """ Dispose(self: AutomationHosting[MyInterface, ClientInterface]) """
        pass

    def NotifyBIMStatusChanged(self, *args): #cannot find CLR method
        """ NotifyBIMStatusChanged(self: AutomationHosting[MyInterface, ClientInterface], newStatus: AppStatus) """
        pass

    def RunAsync(self, id):
        """ RunAsync(self: AutomationHosting[MyInterface, ClientInterface], id: str) -> Task """
        pass

    def RunServer(self, *args): #cannot find CLR method
        """ RunServer(self: AutomationHosting[MyInterface, ClientInterface], id: str, cancellationToken: CancellationToken) """
        pass

    def Stop(self):
        """ Stop(self: AutomationHosting[MyInterface, ClientInterface]) """
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
    def __new__(self, hostedService, logger, eventName, clientUrlFormat, automationUrlFormat):
        """ __new__(cls: type, hostedService: MyInterface, logger: IPluginLogger, eventName: str, clientUrlFormat: str, automationUrlFormat: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    HostingTask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HostingTask(self: AutomationHosting[MyInterface, ClientInterface]) -> Task



Set: HostingTask(self: AutomationHosting[MyInterface, ClientInterface]) = value

"""

    MyBIM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MyBIM(self: AutomationHosting[MyInterface, ClientInterface]) -> ClientInterface



"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Service(self: AutomationHosting[MyInterface, ClientInterface]) -> MyInterface



"""

    ServiceBaseAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ServiceBaseAddress(self: AutomationHosting[MyInterface, ClientInterface]) -> str



Set: ServiceBaseAddress(self: AutomationHosting[MyInterface, ClientInterface]) = value

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: AutomationHosting[MyInterface, ClientInterface]) -> AutomationStatus



"""


    BIMStatusChanged = None


class AutomationHostingGrpc(object, IGrpcCommunicationCommonInterface, IBIMPluginClient[ClientInterface], IDisposable):
    """ AutomationHostingGrpc[MyInterface, ClientInterface](hostedService: MyInterface, grpcClient: IGrpcClient, logger: IPluginLogger, eventName: str) """
    def Dispose(self):
        """ Dispose(self: AutomationHostingGrpc[MyInterface, ClientInterface]) """
        pass

    def NotifyBIMStatusChanged(self, *args): #cannot find CLR method
        """ NotifyBIMStatusChanged(self: AutomationHostingGrpc[MyInterface, ClientInterface], newStatus: AppStatus) """
        pass

    def RunAsync(self, id):
        """ RunAsync(self: AutomationHostingGrpc[MyInterface, ClientInterface], id: str) -> Task """
        pass

    def RunServer(self, *args): #cannot find CLR method
        """ RunServer(self: AutomationHostingGrpc[MyInterface, ClientInterface], id: str, cancellationToken: CancellationToken) """
        pass

    def Stop(self):
        """ Stop(self: AutomationHostingGrpc[MyInterface, ClientInterface]) """
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
    def __new__(self, hostedService, grpcClient, logger, eventName):
        """ __new__(cls: type, hostedService: MyInterface, grpcClient: IGrpcClient, logger: IPluginLogger, eventName: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    EventName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnected(self: AutomationHostingGrpc[MyInterface, ClientInterface]) -> bool



"""

    MyBIM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MyBIM(self: AutomationHostingGrpc[MyInterface, ClientInterface]) -> ClientInterface



Set: MyBIM(self: AutomationHostingGrpc[MyInterface, ClientInterface]) = value

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: AutomationHostingGrpc[MyInterface, ClientInterface]) -> AutomationStatus



"""


    BIMStatusChanged = None


class AutomationService(object, IAutomation, IClientBIM[ClientInterface], IDisposable):
    """ AutomationService[ClientInterface]() """
    def CloseProject(self):
        """ CloseProject(self: AutomationService[ClientInterface]) """
        pass

    def Dispose(self):
        """ Dispose(self: AutomationService[ClientInterface]) """
        pass

    def NotifyChange(self):
        """ NotifyChange(self: AutomationService[ClientInterface]) """
        pass

    def OpenProject(self, fileName):
        """ OpenProject(self: AutomationService[ClientInterface], fileName: str) """
        pass

    def Refresh(self):
        """ Refresh(self: AutomationService[ClientInterface]) """
        pass

    def RefreshProject(self):
        """ RefreshProject(self: AutomationService[ClientInterface]) """
        pass

    def SelectItem(self, itemId):
        """ SelectItem(self: AutomationService[ClientInterface], itemId: str) """
        pass

    def Shutdown(self):
        """ Shutdown(self: AutomationService[ClientInterface]) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BIM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BIM(self: AutomationService[ClientInterface]) -> ClientInterface



Set: BIM(self: AutomationService[ClientInterface]) = value

"""

    ProjectDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectDir(self: AutomationService[ClientInterface]) -> str



"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: AutomationService[ClientInterface]) -> AutomationStatus



"""

    TempWorkingDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempWorkingDir(self: AutomationService[ClientInterface]) -> str



"""



class AutomationStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) AutomationStatus, values: IsClient (1), Unknown (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsClient = None
    Unknown = None
    value__ = None


class BIMItemId(object):
    """ BIMItemId() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BIMItemId) -> int



Set: Id(self: BIMItemId) = value

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: BIMItemId) -> BIMItemType



Set: Type(self: BIMItemId) = value

"""



class BIMItemsGroup(object):
    """ BIMItemsGroup() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BIMItemsGroup) -> int



Set: Id(self: BIMItemsGroup) = value

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: BIMItemsGroup) -> List[BIMItemId]



Set: Items(self: BIMItemsGroup) = value

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: BIMItemsGroup) -> RequestedItemsType



Set: Type(self: BIMItemsGroup) = value

"""



class BIMItemType(Enum, IComparable, IFormattable, IConvertible):
    """ enum BIMItemType, values: BIMItemsGroup (2), Member (0), Node (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BIMItemsGroup = None
    Member = None
    Node = None
    value__ = None


class BIMPluginHosting(object, IBIMPluginHosting, IDisposable):
    """ BIMPluginHosting(factory: IBIMPluginFactory, logger: IPluginLogger, eventName: str, pluginUrlFormat: str) """
    def Dispose(self):
        """ Dispose(self: BIMPluginHosting) """
        pass

    def NotifyAppStatusChanged(self, *args): #cannot find CLR method
        """ NotifyAppStatusChanged(self: BIMPluginHosting, newStatus: AppStatus) """
        pass

    def RunAsync(self, id, workingDirectory):
        """ RunAsync(self: BIMPluginHosting, id: str, workingDirectory: str) -> Task """
        pass

    def Stop(self):
        """ Stop(self: BIMPluginHosting) """
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
    def __new__(self, factory, logger, eventName, pluginUrlFormat):
        """ __new__(cls: type, factory: IBIMPluginFactory, logger: IPluginLogger, eventName: str, pluginUrlFormat: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    HostingTask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HostingTask(self: BIMPluginHosting) -> Task



Set: HostingTask(self: BIMPluginHosting) = value

"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Service(self: BIMPluginHosting) -> IApplicationBIM



"""


    AppStatusChanged = None


class BIMPluginHostingGrpc(object, IBIMPluginHosting, IDisposable):
    """ BIMPluginHostingGrpc(factory: IBIMPluginFactory, grpcServer: IGrpcServer, logger: IPluginLogger, eventName: str) """
    def Dispose(self):
        """ Dispose(self: BIMPluginHostingGrpc) """
        pass

    def RunAsync(self, id, workingDirectory):
        """ RunAsync(self: BIMPluginHostingGrpc, id: str, workingDirectory: str) -> Task """
        pass

    def Stop(self):
        """ Stop(self: BIMPluginHostingGrpc) """
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
    def __new__(self, factory, grpcServer, logger, eventName):
        """ __new__(cls: type, factory: IBIMPluginFactory, grpcServer: IGrpcServer, logger: IPluginLogger, eventName: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    EventName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventName(self: BIMPluginHostingGrpc) -> str



Set: EventName(self: BIMPluginHostingGrpc) = value

"""

    GrpcServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrpcServer(self: BIMPluginHostingGrpc) -> GrpcReflectionServer



"""

    IdeaStaticaApp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdeaStaticaApp(self: BIMPluginHostingGrpc) -> Process



Set: IdeaStaticaApp(self: BIMPluginHostingGrpc) = value

"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Service(self: BIMPluginHostingGrpc) -> IApplicationBIM



Set: Service(self: BIMPluginHostingGrpc) = value

"""


    AppStatusChanged = None


class BIMProject(object):
    """ BIMProject() """
    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: BIMProject) -> CountryCode



Set: CountryCode(self: BIMProject) = value

"""



class IConnHiddenCheck:
    # no doc
    def AddBoltAssembly(self, boltAssemblyName):
        """ AddBoltAssembly(self: IConnHiddenCheck, boltAssemblyName: str) -> int """
        pass

    def ApplyParameters(self, connectionId, parametersJSON):
        """ ApplyParameters(self: IConnHiddenCheck, connectionId: str, parametersJSON: str) -> str """
        pass

    def ApplySimpleTemplate(self, connectionId, templateFilePath, connTemplateSetting, mainMember, attachedMembers):
        """ ApplySimpleTemplate(self: IConnHiddenCheck, connectionId: str, templateFilePath: str, connTemplateSetting: ApplyConnTemplateSetting, mainMember: int, attachedMembers: List[int]) -> str """
        pass

    def ApplyTemplate(self, connectionId, conTemplateFileName, connTemplateSetting):
        """ ApplyTemplate(self: IConnHiddenCheck, connectionId: str, conTemplateFileName: str, connTemplateSetting: ApplyConnTemplateSetting) -> str """
        pass

    def Calculate(self, connectionId):
        """ Calculate(self: IConnHiddenCheck, connectionId: str) -> ConnectionResultsData """
        pass

    def Cancel(self):
        """ Cancel(self: IConnHiddenCheck) """
        pass

    def CloseProject(self):
        """ CloseProject(self: IConnHiddenCheck) """
        pass

    def CreateConProjFromIOM(self, iomXmlFileName, iomResXmlFileName, newIdeaConFileName):
        """ CreateConProjFromIOM(self: IConnHiddenCheck, iomXmlFileName: str, iomResXmlFileName: str, newIdeaConFileName: str) """
        pass

    def DeleteAllOperations(self, connectionId):
        """ DeleteAllOperations(self: IConnHiddenCheck, connectionId: str) -> str """
        pass

    def EvaluateExpression(self, connectionId, expression, arumentsJSON):
        """ EvaluateExpression(self: IConnHiddenCheck, connectionId: str, expression: str, arumentsJSON: str) -> str """
        pass

    def ExportToTemplate(self, connectionId, conTemplateFileName):
        """ ExportToTemplate(self: IConnHiddenCheck, connectionId: str, conTemplateFileName: str) -> str """
        pass

    def GetAllConnectionData(self, connectionId):
        """ GetAllConnectionData(self: IConnHiddenCheck, connectionId: str) -> str """
        pass

    def GetBoltAssembliesInProject(self):
        """ GetBoltAssembliesInProject(self: IConnHiddenCheck) -> List[ProjectItem] """
        pass

    def GetCheckResultsJSON(self, connectionId):
        """ GetCheckResultsJSON(self: IConnHiddenCheck, connectionId: str) -> str """
        pass

    def GetCodeSetupJSON(self):
        """ GetCodeSetupJSON(self: IConnHiddenCheck) -> str """
        pass

    def GetConnectionCost(self, connectionId):
        """ GetConnectionCost(self: IConnHiddenCheck, connectionId: str) -> str """
        pass

    def GetConnectionLoadingJSON(self, connectionId):
        """ GetConnectionLoadingJSON(self: IConnHiddenCheck, connectionId: str) -> str """
        pass

    def GetConnectionModel(self, connectionId):
        """ GetConnectionModel(self: IConnHiddenCheck, connectionId: str) -> ConnectionData """
        pass

    def GetConnectionModelXML(self, connectionId):
        """ GetConnectionModelXML(self: IConnHiddenCheck, connectionId: str) -> str """
        pass

    def GetCrossSectionsInProject(self):
        """ GetCrossSectionsInProject(self: IConnHiddenCheck) -> List[ProjectItem] """
        pass

    def GetMaterialsInProject(self):
        """ GetMaterialsInProject(self: IConnHiddenCheck) -> List[ProjectItem] """
        pass

    def GetParametersJSON(self, connectionId):
        """ GetParametersJSON(self: IConnHiddenCheck, connectionId: str) -> str """
        pass

    def GetProjectInfo(self):
        """ GetProjectInfo(self: IConnHiddenCheck) -> ConProjectInfo """
        pass

    def OpenProject(self, ideaConProject):
        """ OpenProject(self: IConnHiddenCheck, ideaConProject: str) """
        pass

    def Save(self):
        """ Save(self: IConnHiddenCheck) """
        pass

    def SaveAsProject(self, newProjectFileName):
        """ SaveAsProject(self: IConnHiddenCheck, newProjectFileName: str) """
        pass

    def SetCrossSectionMaterial(self, crossSectionId, materialId):
        """ SetCrossSectionMaterial(self: IConnHiddenCheck, crossSectionId: int, materialId: int) """
        pass

    def SetMemberCrossSection(self, connectionId, memberId, crossSectionId):
        """ SetMemberCrossSection(self: IConnHiddenCheck, connectionId: str, memberId: int, crossSectionId: int) """
        pass

    def UpdateCodeSetupJSON(self, connectionSetupJSON):
        """ UpdateCodeSetupJSON(self: IConnHiddenCheck, connectionSetupJSON: str) -> str """
        pass

    def UpdateConProjFromIOM(self, iomXmlFileName, iomResXmlFileName):
        """ UpdateConProjFromIOM(self: IConnHiddenCheck, iomXmlFileName: str, iomResXmlFileName: str) """
        pass

    def UpdateLoadingFromJson(self, connectionId, loadingJSON):
        """ UpdateLoadingFromJson(self: IConnHiddenCheck, connectionId: str, loadingJSON: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ConnectionHiddenCheckClient(ClientBase[IConnHiddenCheck], ICommunicationObject, IDisposable, IConnHiddenCheck):
    """ ConnectionHiddenCheckClient(binding: Binding, remoteAddress: EndpointAddress) """
    def AddBoltAssembly(self, boltAssemblyName):
        """ AddBoltAssembly(self: ConnectionHiddenCheckClient, boltAssemblyName: str) -> int """
        pass

    def ApplyParameters(self, connectionId, parametersJSON):
        """ ApplyParameters(self: ConnectionHiddenCheckClient, connectionId: str, parametersJSON: str) -> str """
        pass

    def ApplySimpleTemplate(self, connectionId, templateFilePath, connTemplateSetting, mainMember, attachedMembers):
        """ ApplySimpleTemplate(self: ConnectionHiddenCheckClient, connectionId: str, templateFilePath: str, connTemplateSetting: ApplyConnTemplateSetting, mainMember: int, attachedMembers: List[int]) -> str """
        pass

    def ApplyTemplate(self, connectionId, conTemplateFileName, connTemplateSetting):
        """ ApplyTemplate(self: ConnectionHiddenCheckClient, connectionId: str, conTemplateFileName: str, connTemplateSetting: ApplyConnTemplateSetting) -> str """
        pass

    def Calculate(self, connectionId):
        """ Calculate(self: ConnectionHiddenCheckClient, connectionId: str) -> ConnectionResultsData """
        pass

    def Cancel(self):
        """ Cancel(self: ConnectionHiddenCheckClient) """
        pass

    def CloseProject(self):
        """ CloseProject(self: ConnectionHiddenCheckClient) """
        pass

    def CreateChannel(self, *args): #cannot find CLR method
        """
        CreateChannel(self: ClientBase[IConnHiddenCheck]) -> IConnHiddenCheck

        

            Returns a new channel to the service.

            Returns: A channel of the type of the service contract.
        """
        pass

    def CreateConProjFromIOM(self, iomXmlFileName, iomResXmlFileName, newIdeaConFileName):
        """ CreateConProjFromIOM(self: ConnectionHiddenCheckClient, iomXmlFileName: str, iomResXmlFileName: str, newIdeaConFileName: str) """
        pass

    def DeleteAllOperations(self, connectionId):
        """ DeleteAllOperations(self: ConnectionHiddenCheckClient, connectionId: str) -> str """
        pass

    def EvaluateExpression(self, connectionId, expression, arumentsJSON):
        """ EvaluateExpression(self: ConnectionHiddenCheckClient, connectionId: str, expression: str, arumentsJSON: str) -> str """
        pass

    def ExportToTemplate(self, connectionId, conTemplateFileName):
        """ ExportToTemplate(self: ConnectionHiddenCheckClient, connectionId: str, conTemplateFileName: str) -> str """
        pass

    def GetAllConnectionData(self, connectionId):
        """ GetAllConnectionData(self: ConnectionHiddenCheckClient, connectionId: str) -> str """
        pass

    def GetBoltAssembliesInProject(self):
        """ GetBoltAssembliesInProject(self: ConnectionHiddenCheckClient) -> List[ProjectItem] """
        pass

    def GetCheckResultsJSON(self, connectionId):
        """ GetCheckResultsJSON(self: ConnectionHiddenCheckClient, connectionId: str) -> str """
        pass

    def GetCodeSetupJSON(self):
        """ GetCodeSetupJSON(self: ConnectionHiddenCheckClient) -> str """
        pass

    def GetConnectionCost(self, connectionId):
        """ GetConnectionCost(self: ConnectionHiddenCheckClient, connectionId: str) -> str """
        pass

    def GetConnectionLoadingJSON(self, connectionId):
        """ GetConnectionLoadingJSON(self: ConnectionHiddenCheckClient, connectionId: str) -> str """
        pass

    def GetConnectionModel(self, connectionId):
        """ GetConnectionModel(self: ConnectionHiddenCheckClient, connectionId: str) -> ConnectionData """
        pass

    def GetConnectionModelXML(self, connectionId):
        """ GetConnectionModelXML(self: ConnectionHiddenCheckClient, connectionId: str) -> str """
        pass

    def GetCrossSectionsInProject(self):
        """ GetCrossSectionsInProject(self: ConnectionHiddenCheckClient) -> List[ProjectItem] """
        pass

    def GetDefaultValueForInitialization(self, *args): #cannot find CLR method
        """ GetDefaultValueForInitialization[T](self: ClientBase[IConnHiddenCheck]) -> T """
        pass

    def GetMaterialsInProject(self):
        """ GetMaterialsInProject(self: ConnectionHiddenCheckClient) -> List[ProjectItem] """
        pass

    def GetParametersJSON(self, connectionId):
        """ GetParametersJSON(self: ConnectionHiddenCheckClient, connectionId: str) -> str """
        pass

    def GetProjectInfo(self):
        """ GetProjectInfo(self: ConnectionHiddenCheckClient) -> ConProjectInfo """
        pass

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: ClientBase[IConnHiddenCheck], beginOperationDelegate: BeginOperationDelegate, inValues: Array[object], endOperationDelegate: EndOperationDelegate, operationCompletedCallback: SendOrPostCallback, userState: object) """
        pass

    def OpenProject(self, ideaConFileName):
        """ OpenProject(self: ConnectionHiddenCheckClient, ideaConFileName: str) """
        pass

    def Save(self):
        """ Save(self: ConnectionHiddenCheckClient) """
        pass

    def SaveAsProject(self, newProjectFileName):
        """ SaveAsProject(self: ConnectionHiddenCheckClient, newProjectFileName: str) """
        pass

    def SetCrossSectionMaterial(self, crossSectionId, materialId):
        """ SetCrossSectionMaterial(self: ConnectionHiddenCheckClient, crossSectionId: int, materialId: int) """
        pass

    def SetMemberCrossSection(self, connectionId, memberId, crossSectionId):
        """ SetMemberCrossSection(self: ConnectionHiddenCheckClient, connectionId: str, memberId: int, crossSectionId: int) """
        pass

    def UpdateCodeSetupJSON(self, connectionSetupJSON):
        """ UpdateCodeSetupJSON(self: ConnectionHiddenCheckClient, connectionSetupJSON: str) -> str """
        pass

    def UpdateConProjFromIOM(self, iomXmlFileName, iomResXmlFileName):
        """ UpdateConProjFromIOM(self: ConnectionHiddenCheckClient, iomXmlFileName: str, iomResXmlFileName: str) """
        pass

    def UpdateLoadingFromJson(self, connectionId, loadingJSON):
        """ UpdateLoadingFromJson(self: ConnectionHiddenCheckClient, connectionId: str, loadingJSON: str) -> str """
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
    def __new__(self, binding, remoteAddress):
        """ __new__(cls: type, binding: Binding, remoteAddress: EndpointAddress) """
        pass

    Channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the inner channel used to send messages to variously configured service endpoints.



"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    HiddenCalculatorId = -1


class ConnHiddenClientFactory(object, IDisposable, IConnCalculatorFactory):
    """ ConnHiddenClientFactory(ideaInstallDir: str) """
    def Create(self):
        """ Create(self: ConnHiddenClientFactory) -> ConnectionHiddenCheckClient """
        pass

    def Dispose(self):
        """ Dispose(self: ConnHiddenClientFactory) """
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
    def __new__(self, ideaInstallDir):
        """ __new__(cls: type, ideaInstallDir: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class Constants(object):
    """ Constants() """
    AutomationParam = '-automation'
    BlobStorageId = 'blobStorageId'
    CheckbotAppName = 'IdeaCheckbot.exe'
    ConCalculatorCancelEventFormat = 'IdeaStatiCa.ConnHiddenCalculatorCancel-{0}'
    ConCalculatorChangedEventFormat = 'IdeaStatiCa.ConnHiddenCalculator-{0}'
    ConnectionChangedEventFormat = 'IdeaStatiCaConnectionChanged{0}'
    ConnHiddenCalculatorUrlFormat = 'net.pipe://localhost/IdeaStatiCa.ConnHiddenCalculator{0}'
    ContentId = 'contentId'
    DefaultIdeaStaticaAutoUrlFormat = 'net.pipe://localhost/IdeaStatiCaAuto{0}'
    DefaultPluginEventName = 'IdeaStatiCaBIMPluginEvent'
    DefaultPluginUrlFormat = 'net.pipe://localhost/IdeaBIMPlugin{0}'
    GrpcPortParam = '-grpcPort'
    GrpcReflectionErrorException = 'GrpcReflectionError'
    GRPC_CHECKBOT_HANDLER_MESSAGE = 'Grpc.Handlers.CheckBot'
    GRPC_CHUNK_SIZE = 65536
    GRPC_MAX_MSG_SIZE = 20971520
    GRPC_PROJECTCONTENT_HANDLER_MESSAGE = 'Grpc.Handlers.ProjContent'
    GRPC_REFLECTION_HANDLER_MESSAGE = 'Grpc.Handlers.Reflection'
    IdeaConnectionAppName = 'IdeaConnection.exe'
    IdeaStatiCaVersion = '21.1'
    LibraryReposPath = '-libReposPath'
    MaxGrpcPort = 50500
    MemberChangedEventFormat = 'IdeaStatiCaMemberChanged{0}'
    MemberEventName = 'MemberPluginEvent'
    MemberHiddenCalculatorUrlFormat = 'net.pipe://localhost/IdeaStatiCa.MemberHiddenCalculator{0}'
    MemberUrlFormat = 'net.pipe://localhost/IdeaMember{0}'
    MemHiddenCalcCancelEventFormat = 'IdeaStatiCa.MemberHiddenCalculatorCancel-{0}'
    MemHiddenCalcChangedEventFormat = 'IdeaStatiCa.MemberHiddenCalculator-{0}'
    MinGrpcPort = 50000
    ProgressCallbackUrlFormat = 'net.pipe://localhost/IdeaStatiCaProgress{0}'
    ProjectParam = '-project'
    ViewerPluginAppName = 'IdeaStatiCa.ViewerPlugin.exe'


class ConversionDictionary(SerializableDictionary[TKey, int], IDictionary[TKey, int], ICollection[KeyValuePair[TKey, int]], IEnumerable[KeyValuePair[TKey, int]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, int], IReadOnlyCollection[KeyValuePair[TKey, int]], ISerializable, IDeserializationCallback, IXmlSerializable):
    # no doc
    def GetExEntityId(self, name):
        """ GetExEntityId(self: ConversionDictionary[TKey], name: TKey) -> int """
        pass

    def GetKey(self, *args): #cannot find CLR method
        """
        GetKey(self: ConversionDictionary[TKey], id: int) -> TKey

        GetKey(self: ConversionDictionary[TKey], name: str) -> TKey
        """
        pass

    def GetSaveKey(self, Id):
        """ GetSaveKey(self: ConversionDictionary[TKey], Id: int) -> TKey """
        pass

    def InitMerge(self, source):
        """ InitMerge(self: ConversionDictionary[TKey], source: IList[ProjectItem]) """
        pass

    def MapId(self, key):
        """ MapId(self: ConversionDictionary[TKey], key: TKey) -> int """
        pass

    def Merge(self, source):
        """ Merge(self: ConversionDictionary[TKey], source: IList[ProjectItem]) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ValueSerializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ConversionDictionaryInt(ConversionDictionary[int], IDictionary[int, int], ICollection[KeyValuePair[int, int]], IEnumerable[KeyValuePair[int, int]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[int, int], IReadOnlyCollection[KeyValuePair[int, int]], ISerializable, IDeserializationCallback, IXmlSerializable):
    """ ConversionDictionaryInt() """
    def GetKey(self, *args): #cannot find CLR method
        """
        GetKey(self: ConversionDictionaryInt, id: int) -> int

        GetKey(self: ConversionDictionaryInt, name: str) -> int
        """
        pass

    def GetSaveKey(self, Id):
        """ GetSaveKey(self: ConversionDictionaryInt, Id: int) -> int """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ValueSerializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ConversionDictionaryString(ConversionDictionary[str], IDictionary[str, int], ICollection[KeyValuePair[str, int]], IEnumerable[KeyValuePair[str, int]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[str, int], IReadOnlyCollection[KeyValuePair[str, int]], ISerializable, IDeserializationCallback, IXmlSerializable):
    """ ConversionDictionaryString() """
    def GetKey(self, *args): #cannot find CLR method
        """
        GetKey(self: ConversionDictionaryString, id: int) -> str

        GetKey(self: ConversionDictionaryString, name: str) -> str
        """
        pass

    def GetSaveKey(self, Id):
        """ GetSaveKey(self: ConversionDictionaryString, Id: int) -> str """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ValueSerializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ProjectItem(object):
    """ ProjectItem() """
    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: ProjectItem) -> int



Set: Identifier(self: ProjectItem) = value

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ProjectItem) -> str



Set: Name(self: ProjectItem) = value

"""



class CrossSectionProjectItem(ProjectItem):
    """ CrossSectionProjectItem() """
    MaterialIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialIdentifier(self: CrossSectionProjectItem) -> int



Set: MaterialIdentifier(self: CrossSectionProjectItem) = value

"""

    MaterialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialName(self: CrossSectionProjectItem) -> str



Set: MaterialName(self: CrossSectionProjectItem) = value

"""



class ErrorHandlerAttribute(Attribute, _Attribute, IServiceBehavior):
    """ ErrorHandlerAttribute(errorHandler: Type) """
    def AddBindingParameters(self, serviceDescription, serviceHostBase, endpoints, bindingParameters):
        """ AddBindingParameters(self: ErrorHandlerAttribute, serviceDescription: ServiceDescription, serviceHostBase: ServiceHostBase, endpoints: Collection[ServiceEndpoint], bindingParameters: BindingParameterCollection) """
        pass

    def ApplyDispatchBehavior(self, serviceDescription, serviceHostBase):
        """ ApplyDispatchBehavior(self: ErrorHandlerAttribute, serviceDescription: ServiceDescription, serviceHostBase: ServiceHostBase) """
        pass

    def Validate(self, serviceDescription, serviceHostBase):
        """ Validate(self: ErrorHandlerAttribute, serviceDescription: ServiceDescription, serviceHostBase: ServiceHostBase) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, errorHandler):
        """ __new__(cls: type, errorHandler: Type) """
        pass


class GrpcBimHostingFactory(object, IBimHostingFactory):
    """ GrpcBimHostingFactory() """
    def Create(self, pluginFactory, logger):
        """ Create(self: GrpcBimHostingFactory, pluginFactory: IBIMPluginFactory, logger: IPluginLogger) -> IBIMPluginHosting """
        pass

    def InitGrpcClient(self, logger):
        """ InitGrpcClient(self: GrpcBimHostingFactory, logger: IPluginLogger) -> IProgressMessaging """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IApplicationBIM:
    # no doc
    def GetActiveSelection(self):
        """ GetActiveSelection(self: IApplicationBIM) -> List[BIMItemId] """
        pass

    def GetActiveSelectionModelXML(self, countryCode, requestedType):
        """ GetActiveSelectionModelXML(self: IApplicationBIM, countryCode: CountryCode, requestedType: RequestedItemsType) -> str """
        pass

    def GetActiveSelectionModelXMLAsync(self, countryCode, requestedType):
        """ GetActiveSelectionModelXMLAsync(self: IApplicationBIM, countryCode: CountryCode, requestedType: RequestedItemsType) -> Task[str] """
        pass

    def GetApplicationName(self):
        """ GetApplicationName(self: IApplicationBIM) -> str """
        pass

    def GetModelForSelectionXML(self, countryCode, items):
        """ GetModelForSelectionXML(self: IApplicationBIM, countryCode: CountryCode, items: List[BIMItemsGroup]) -> str """
        pass

    def GetModelForSelectionXMLAsync(self, countryCode, items):
        """ GetModelForSelectionXMLAsync(self: IApplicationBIM, countryCode: CountryCode, items: List[BIMItemsGroup]) -> Task[str] """
        pass

    def IsCAD(self):
        """ IsCAD(self: IApplicationBIM) -> bool """
        pass

    def IsDataUpToDate(self):
        """ IsDataUpToDate(self: IApplicationBIM) -> bool """
        pass

    def SelectAsync(self, items):
        """ SelectAsync(self: IApplicationBIM, items: List[BIMItemId]) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IAutomation:
    # no doc
    def CloseProject(self):
        """ CloseProject(self: IAutomation) """
        pass

    def NotifyChange(self):
        """ NotifyChange(self: IAutomation) """
        pass

    def OpenProject(self, fileName):
        """ OpenProject(self: IAutomation, fileName: str) """
        pass

    def Refresh(self):
        """ Refresh(self: IAutomation) """
        pass

    def RefreshProject(self):
        """ RefreshProject(self: IAutomation) """
        pass

    def SelectItem(self, itemId):
        """ SelectItem(self: IAutomation, itemId: str) """
        pass

    def Shutdown(self):
        """ Shutdown(self: IAutomation) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ProjectDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectDir(self: IAutomation) -> str



"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: IAutomation) -> AutomationStatus



"""

    TempWorkingDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempWorkingDir(self: IAutomation) -> str



"""



class IBimHostingFactory:
    # no doc
    def Create(self, pluginFactory, logger):
        """ Create(self: IBimHostingFactory, pluginFactory: IBIMPluginFactory, logger: IPluginLogger) -> IBIMPluginHosting """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IBIMPluginClient:
    # no doc
    def RunAsync(self, id):
        """ RunAsync(self: IBIMPluginClient[T], id: str) -> Task """
        pass

    def Stop(self):
        """ Stop(self: IBIMPluginClient[T]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MyBIM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MyBIM(self: IBIMPluginClient[T]) -> T



"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: IBIMPluginClient[T]) -> AutomationStatus



"""


    BIMStatusChanged = None


class IBIMPluginFactory:
    # no doc
    def Create(self):
        """ Create(self: IBIMPluginFactory) -> IApplicationBIM """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FeaAppName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeaAppName(self: IBIMPluginFactory) -> str



"""

    IdeaStaticaAppPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdeaStaticaAppPath(self: IBIMPluginFactory) -> str



"""



class IBIMPluginHosting:
    # no doc
    def RunAsync(self, id, workingDirectory):
        """ RunAsync(self: IBIMPluginHosting, id: str, workingDirectory: str) -> Task """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Service(self: IBIMPluginHosting) -> IApplicationBIM



"""


    AppStatusChanged = None


class IClientBIM:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BIM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BIM(self: IClientBIM[B]) -> B



Set: BIM(self: IClientBIM[B]) = value

"""



class IConnCalculatorFactory:
    # no doc
    def Create(self):
        """ Create(self: IConnCalculatorFactory) -> ConnectionHiddenCheckClient """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IConnectionController:
    # no doc
    def CloseProject(self):
        """ CloseProject(self: IConnectionController) -> int """
        pass

    def OpenProject(self, fileName):
        """ OpenProject(self: IConnectionController, fileName: str) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnected(self: IConnectionController) -> bool



"""


    ConnectionAppExited = None


class IdeaConnectionController(object, IDisposable, IConnectionController):
    # no doc
    def CloseProject(self):
        """ CloseProject(self: IdeaConnectionController) -> int """
        pass

    @staticmethod
    def Create(ideaInstallDir):
        """ Create(ideaInstallDir: str) -> IConnectionController """
        pass

    def Dispose(self):
        """ Dispose(self: IdeaConnectionController) """
        pass

    def OpenProject(self, fileName):
        """ OpenProject(self: IdeaConnectionController, fileName: str) -> int """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ConnectionAppClient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnected(self: IdeaConnectionController) -> bool



"""

    UserMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ConnectionAppExited = None
    CurrentItemChangedEvent = None


class IdeaConnectionControllerGrpc(object, IDisposable, IConnectionController):
    # no doc
    def CloseProject(self):
        """ CloseProject(self: IdeaConnectionControllerGrpc) -> int """
        pass

    @staticmethod
    def Create(ideaInstallDir, logger):
        """ Create(ideaInstallDir: str, logger: IPluginLogger) -> IConnectionController """
        pass

    def Dispose(self):
        """ Dispose(self: IdeaConnectionControllerGrpc) """
        pass

    def OpenProject(self, fileName):
        """ OpenProject(self: IdeaConnectionControllerGrpc, fileName: str) -> int """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GrpcClient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UserMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ConnectionAppExited = None
    CurrentItemChangedEvent = None


class IProgressMessaging:
    # no doc
    def CancelMessage(self):
        """ CancelMessage(self: IProgressMessaging) """
        pass

    def GetCancellationFlag(self):
        """ GetCancellationFlag(self: IProgressMessaging) -> bool """
        pass

    def GetCurrentCulture(self):
        """ GetCurrentCulture(self: IProgressMessaging) -> CultureInfo """
        pass

    def GetLocalizedText(self, msg):
        """ GetLocalizedText(self: IProgressMessaging, msg: LocalisedMessage) -> str """
        pass

    def InitProgressDialog(self):
        """ InitProgressDialog(self: IProgressMessaging) """
        pass

    def SendMessage(self, severity, text):
        """ SendMessage(self: IProgressMessaging, severity: MessageSeverity, text: str) """
        pass

    def SendMessageInteractive(self, severity, text, buttons):
        """ SendMessageInteractive(self: IProgressMessaging, severity: MessageSeverity, text: str, buttons: Array[str]) -> int """
        pass

    def SendMessageLocalised(self, severity, msg):
        """ SendMessageLocalised(self: IProgressMessaging, severity: MessageSeverity, msg: LocalisedMessage) """
        pass

    def SetStage(self, stage, stageMax, name):
        """ SetStage(self: IProgressMessaging, stage: int, stageMax: int, name: str) """
        pass

    def SetStageLocalised(self, stage, stageMax, msg):
        """ SetStageLocalised(self: IProgressMessaging, stage: int, stageMax: int, msg: LocalisedMessage) """
        pass

    def SetStageProgress(self, percentage):
        """ SetStageProgress(self: IProgressMessaging, percentage: float) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IIdeaStaticaApp(IProgressMessaging):
    # no doc
    def GetAllConnectionData(self, connectionId):
        """ GetAllConnectionData(self: IIdeaStaticaApp, connectionId: int) -> str """
        pass

    def GetConnectionModel(self, connectionId):
        """ GetConnectionModel(self: IIdeaStaticaApp, connectionId: int) -> ConnectionData """
        pass

    def GetCssInMPRL(self, countryCode):
        """ GetCssInMPRL(self: IIdeaStaticaApp, countryCode: CountryCode) -> List[LibraryItem] """
        pass

    def GetCssInProject(self):
        """ GetCssInProject(self: IIdeaStaticaApp) -> List[ProjectItem] """
        pass

    def GetCssInProjectV2(self):
        """ GetCssInProjectV2(self: IIdeaStaticaApp) -> List[CrossSectionProjectItem] """
        pass

    def GetMaterialsInMPRL(self, countryCode):
        """ GetMaterialsInMPRL(self: IIdeaStaticaApp, countryCode: CountryCode) -> List[LibraryItem] """
        pass

    def GetMaterialsInProject(self):
        """ GetMaterialsInProject(self: IIdeaStaticaApp) -> List[ProjectItem] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IdeaStatiCaAppClient(ClientBase[IIdeaStaticaApp], ICommunicationObject, IDisposable, IIdeaStaticaApp, IProgressMessaging):
    """ IdeaStatiCaAppClient(id: str) """
    def CancelMessage(self):
        """ CancelMessage(self: IdeaStatiCaAppClient) """
        pass

    def CreateChannel(self, *args): #cannot find CLR method
        """
        CreateChannel(self: ClientBase[IIdeaStaticaApp]) -> IIdeaStaticaApp

        

            Returns a new channel to the service.

            Returns: A channel of the type of the service contract.
        """
        pass

    def GetAllConnectionData(self, connectionId):
        """ GetAllConnectionData(self: IdeaStatiCaAppClient, connectionId: int) -> str """
        pass

    def GetCancellationFlag(self):
        """ GetCancellationFlag(self: IdeaStatiCaAppClient) -> bool """
        pass

    def GetConnectionModel(self, connectionId):
        """ GetConnectionModel(self: IdeaStatiCaAppClient, connectionId: int) -> ConnectionData """
        pass

    def GetCssInMPRL(self, countryCode):
        """ GetCssInMPRL(self: IdeaStatiCaAppClient, countryCode: CountryCode) -> List[LibraryItem] """
        pass

    def GetCssInProject(self):
        """ GetCssInProject(self: IdeaStatiCaAppClient) -> List[ProjectItem] """
        pass

    def GetCssInProjectV2(self):
        """ GetCssInProjectV2(self: IdeaStatiCaAppClient) -> List[CrossSectionProjectItem] """
        pass

    def GetCurrentCulture(self):
        """ GetCurrentCulture(self: IdeaStatiCaAppClient) -> CultureInfo """
        pass

    def GetDefaultValueForInitialization(self, *args): #cannot find CLR method
        """ GetDefaultValueForInitialization[T](self: ClientBase[IIdeaStaticaApp]) -> T """
        pass

    def GetLocalizedText(self, msg):
        """ GetLocalizedText(self: IdeaStatiCaAppClient, msg: LocalisedMessage) -> str """
        pass

    def GetMaterialsInMPRL(self, countryCode):
        """ GetMaterialsInMPRL(self: IdeaStatiCaAppClient, countryCode: CountryCode) -> List[LibraryItem] """
        pass

    def GetMaterialsInProject(self):
        """ GetMaterialsInProject(self: IdeaStatiCaAppClient) -> List[ProjectItem] """
        pass

    def InitProgressDialog(self):
        """ InitProgressDialog(self: IdeaStatiCaAppClient) """
        pass

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: ClientBase[IIdeaStaticaApp], beginOperationDelegate: BeginOperationDelegate, inValues: Array[object], endOperationDelegate: EndOperationDelegate, operationCompletedCallback: SendOrPostCallback, userState: object) """
        pass

    def SendMessage(self, severity, *__args):
        """ SendMessage(self: IdeaStatiCaAppClient, severity: MessageSeverity, text: str)SendMessage(self: IdeaStatiCaAppClient, severity: MessageSeverity, msg: LocalisedMessage) """
        pass

    def SendMessageInteractive(self, severity, text, buttons):
        """ SendMessageInteractive(self: IdeaStatiCaAppClient, severity: MessageSeverity, text: str, buttons: Array[str]) -> int """
        pass

    def SendMessageLocalised(self, severity, msg):
        """ SendMessageLocalised(self: IdeaStatiCaAppClient, severity: MessageSeverity, msg: LocalisedMessage) """
        pass

    def SetStage(self, stage, stageMax, *__args):
        """ SetStage(self: IdeaStatiCaAppClient, stage: int, stageMax: int, name: str)SetStage(self: IdeaStatiCaAppClient, stage: int, stageMax: int, msg: LocalisedMessage) """
        pass

    def SetStageLocalised(self, stage, stageMax, msg):
        """ SetStageLocalised(self: IdeaStatiCaAppClient, stage: int, stageMax: int, msg: LocalisedMessage) """
        pass

    def SetStageProgress(self, percentage):
        """ SetStageProgress(self: IdeaStatiCaAppClient, percentage: float) """
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
    def __new__(self, id):
        """ __new__(cls: type, id: str) """
        pass

    Channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the inner channel used to send messages to variously configured service endpoints.



"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IdeaStatiCaClient(ClientBase[T], ICommunicationObject, IDisposable):
    """ IdeaStatiCaClient[T](binding: Binding, remoteAddress: EndpointAddress) """
    def CreateChannel(self, *args): #cannot find CLR method
        """
        CreateChannel(self: ClientBase[T]) -> T

        

            Returns a new channel to the service.

            Returns: A channel of the type of the service contract.
        """
        pass

    def GetDefaultValueForInitialization(self, *args): #cannot find CLR method
        """ GetDefaultValueForInitialization[T](self: ClientBase[T]) -> T """
        pass

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: ClientBase[T], beginOperationDelegate: BeginOperationDelegate, inValues: Array[object], endOperationDelegate: EndOperationDelegate, operationCompletedCallback: SendOrPostCallback, userState: object) """
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
    def __new__(self, binding, remoteAddress):
        """ __new__(cls: type, binding: Binding, remoteAddress: EndpointAddress) """
        pass

    Channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the inner channel used to send messages to variously configured service endpoints.



"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Service(self: IdeaStatiCaClient[T]) -> T



"""



class IMemberCalculatorFactory:
    # no doc
    def Create(self):
        """ Create(self: IMemberCalculatorFactory) -> MemberHiddenCheckClient """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMemberHiddenCheck:
    # no doc
    def Calculate(self, subStructureId):
        """ Calculate(self: IMemberHiddenCheck, subStructureId: int) -> str """
        pass

    def Cancel(self):
        """ Cancel(self: IMemberHiddenCheck) """
        pass

    def CloseProject(self):
        """ CloseProject(self: IMemberHiddenCheck) """
        pass

    def OpenProject(self, projectLocation):
        """ OpenProject(self: IMemberHiddenCheck, projectLocation: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IProgressCallback:
    # no doc
    def ExceptionMessage(self, function, message):
        """ ExceptionMessage(self: IProgressCallback, function: str, message: str) """
        pass

    def IterationMessage(self, percent, message, iteration):
        """ IterationMessage(self: IProgressCallback, percent: float, message: str, iteration: str) """
        pass

    def ProgressMessage(self, percent, message):
        """ ProgressMessage(self: IProgressCallback, percent: float, message: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISEventArgs(EventArgs):
    """ ISEventArgs() """
    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: ISEventArgs) -> AppStatus



Set: Status(self: ISEventArgs) = value

"""



class ISEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ ISEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ISEventHandler, sender: object, e: ISEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate

        

            Combines this System.Delegate with the specified System.Delegate to 

             form a new delegate.

        

        

            follow: The delegate to combine with this delegate.

            Returns: A delegate that is the new root of the System.MulticastDelegate 

             invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object

        

            Dynamically invokes (late-bound) the method represented by the 

             current delegate.

        

        

            args: An array of objects that are the arguments to pass to the method 

             represented by the current delegate.  

         -or-  

         ll, if the method 

             represented by the current delegate does not require arguments.

        

            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ISEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo

        

            Returns a static method represented by the current 

             System.MulticastDelegate.

        

            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ISEventHandler, sender: object, e: ISEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate

        

            Removes an element from the invocation list of this 

             System.MulticastDelegate that is equal to the specified delegate.

        

        

            value: The delegate to search for in the invocation list.

            Returns: If value is found in the invocation list for this instance, then a 

             new System.Delegate without value in its invocation list; otherwise, 

             this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class LibraryItem(object):
    """ LibraryItem() """
    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Group(self: LibraryItem) -> str



Set: Group(self: LibraryItem) = value

"""

    GroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupId(self: LibraryItem) -> str



Set: GroupId(self: LibraryItem) = value

"""

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: LibraryItem) -> str



Set: Identifier(self: LibraryItem) = value

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LibraryItem) -> str



Set: Name(self: LibraryItem) = value

"""



class LocalisedMessage(Enum, IComparable, IFormattable, IConvertible):
    """ enum LocalisedMessage, values: CancellingImport (7), ConvertingModelFromXML (17), CreatingConnection (8), FinishingImport (20), ImportFailed (12), ImportingConnections (2), ImportingGroups (0), ImportingIOMObject (9), ImportingMembers (1), ImportingStructuralModel (10), ImportStarted (11), InternalImport (14), InternalSync (3), Member (15), ModelImport (6), ModelPostProcess (13), ProcessingConnection (19), ProcessingSubstructure (18), SavingData (16), SavingProject (5), SciaSDKError (21), SyncingModel (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CancellingImport = None
    ConvertingModelFromXML = None
    CreatingConnection = None
    FinishingImport = None
    ImportFailed = None
    ImportingConnections = None
    ImportingGroups = None
    ImportingIOMObject = None
    ImportingMembers = None
    ImportingStructuralModel = None
    ImportStarted = None
    InternalImport = None
    InternalSync = None
    Member = None
    ModelImport = None
    ModelPostProcess = None
    ProcessingConnection = None
    ProcessingSubstructure = None
    SavingData = None
    SavingProject = None
    SciaSDKError = None
    SyncingModel = None
    value__ = None


class MemberHiddenCheckClient(ClientBase[IMemberHiddenCheck], ICommunicationObject, IDisposable, IMemberHiddenCheck):
    """ MemberHiddenCheckClient(binding: Binding, remoteAddress: EndpointAddress) """
    def Calculate(self, subStructureId):
        """ Calculate(self: MemberHiddenCheckClient, subStructureId: int) -> str """
        pass

    def Cancel(self):
        """ Cancel(self: MemberHiddenCheckClient) """
        pass

    def CloseProject(self):
        """ CloseProject(self: MemberHiddenCheckClient) """
        pass

    def CreateChannel(self, *args): #cannot find CLR method
        """
        CreateChannel(self: ClientBase[IMemberHiddenCheck]) -> IMemberHiddenCheck

        

            Returns a new channel to the service.

            Returns: A channel of the type of the service contract.
        """
        pass

    def GetDefaultValueForInitialization(self, *args): #cannot find CLR method
        """ GetDefaultValueForInitialization[T](self: ClientBase[IMemberHiddenCheck]) -> T """
        pass

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: ClientBase[IMemberHiddenCheck], beginOperationDelegate: BeginOperationDelegate, inValues: Array[object], endOperationDelegate: EndOperationDelegate, operationCompletedCallback: SendOrPostCallback, userState: object) """
        pass

    def OpenProject(self, projectLocation):
        """ OpenProject(self: MemberHiddenCheckClient, projectLocation: str) """
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
    def __new__(self, binding, remoteAddress):
        """ __new__(cls: type, binding: Binding, remoteAddress: EndpointAddress) """
        pass

    Channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the inner channel used to send messages to variously configured service endpoints.



"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    HiddenCalculatorId = -1


class MemberHiddenClientFactory(object, IMemberCalculatorFactory):
    """ MemberHiddenClientFactory(ideaInstallDir: str) """
    def Create(self):
        """ Create(self: MemberHiddenClientFactory) -> MemberHiddenCheckClient """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, ideaInstallDir):
        """ __new__(cls: type, ideaInstallDir: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class MessageSeverity(Enum, IComparable, IFormattable, IConvertible):
    """ enum MessageSeverity, values: Error (2), Info (0), Warning (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Error = None
    Info = None
    value__ = None
    Warning = None


class ModelBIM(object):
    """ ModelBIM() """
    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: ModelBIM) -> List[BIMItemId]



Set: Items(self: ModelBIM) = value

"""

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Messages(self: ModelBIM) -> OpenMessages



Set: Messages(self: ModelBIM) = value

"""

    Model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Model(self: ModelBIM) -> OpenModel



Set: Model(self: ModelBIM) = value

"""

    Project = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Project(self: ModelBIM) -> str



Set: Project(self: ModelBIM) = value

"""

    RequestedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequestedItems(self: ModelBIM) -> RequestedItemsType



Set: RequestedItems(self: ModelBIM) = value

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: ModelBIM) -> OpenModelResult



Set: Results(self: ModelBIM) = value

"""



class ProgressSender(ClientBase[IProgressCallback], ICommunicationObject, IDisposable, IProgressCallback):
    """ ProgressSender(id: str) """
    def CreateChannel(self, *args): #cannot find CLR method
        """
        CreateChannel(self: ClientBase[IProgressCallback]) -> IProgressCallback

        

            Returns a new channel to the service.

            Returns: A channel of the type of the service contract.
        """
        pass

    def ExceptionMessage(self, function, message):
        """ ExceptionMessage(self: ProgressSender, function: str, message: str) """
        pass

    def GetDefaultValueForInitialization(self, *args): #cannot find CLR method
        """ GetDefaultValueForInitialization[T](self: ClientBase[IProgressCallback]) -> T """
        pass

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: ClientBase[IProgressCallback], beginOperationDelegate: BeginOperationDelegate, inValues: Array[object], endOperationDelegate: EndOperationDelegate, operationCompletedCallback: SendOrPostCallback, userState: object) """
        pass

    def IterationMessage(self, percent, message, iteration):
        """ IterationMessage(self: ProgressSender, percent: float, message: str, iteration: str) """
        pass

    def ProgressMessage(self, percent, message):
        """ ProgressMessage(self: ProgressSender, percent: float, message: str) """
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
    def __new__(self, id):
        """ __new__(cls: type, id: str) """
        pass

    Channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the inner channel used to send messages to variously configured service endpoints.



"""

    Service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class RequestedItemsType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RequestedItemsType, values: Connections (0), SingleConnection (2), Substructure (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Connections = None
    SingleConnection = None
    Substructure = None
    value__ = None


class SerializableDictionary(Dictionary[TKey, TVal], IDictionary[TKey, TVal], ICollection[KeyValuePair[TKey, TVal]], IEnumerable[KeyValuePair[TKey, TVal]], IEnumerable, IDictionary, ICollection, IReadOnlyDictionary[TKey, TVal], IReadOnlyCollection[KeyValuePair[TKey, TVal]], ISerializable, IDeserializationCallback, IXmlSerializable):
    """
    SerializableDictionary[TKey, TVal]()

    SerializableDictionary[TKey, TVal](dictionary: IDictionary[TKey, TVal])

    SerializableDictionary[TKey, TVal](comparer: IEqualityComparer[TKey])

    SerializableDictionary[TKey, TVal](capacity: int)

    SerializableDictionary[TKey, TVal](dictionary: IDictionary[TKey, TVal], comparer: IEqualityComparer[TKey])

    SerializableDictionary[TKey, TVal](capacity: int, comparer: IEqualityComparer[TKey])
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, dictionary: IDictionary[TKey, TVal])

        __new__(cls: type, comparer: IEqualityComparer[TKey])

        __new__(cls: type, capacity: int)

        __new__(cls: type, dictionary: IDictionary[TKey, TVal], comparer: IEqualityComparer[TKey])

        __new__(cls: type, capacity: int, comparer: IEqualityComparer[TKey])

        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ValueSerializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Tools(object):
    # no doc
    @staticmethod
    def ConnectionDataFromXml(xml):
        """ ConnectionDataFromXml(xml: str) -> ConnectionData """
        pass

    @staticmethod
    def ConnectionDataToXml(model):
        """ ConnectionDataToXml(model: ConnectionData) -> str """
        pass

    @staticmethod
    def ModelFromFile(filePath):
        """ ModelFromFile(filePath: str) -> ModelBIM """
        pass

    @staticmethod
    def ModelFromXml(xml):
        """ ModelFromXml(xml: str) -> ModelBIM """
        pass

    @staticmethod
    def ModelsFromFile(filePath):
        """ ModelsFromFile(filePath: str) -> List[ModelBIM] """
        pass

    @staticmethod
    def ModelsFromXml(xml):
        """ ModelsFromXml(xml: str) -> List[ModelBIM] """
        pass

    @staticmethod
    def ModelToFile(model, filePath):
        """ ModelToFile(model: List[ModelBIM], filePath: str)ModelToFile(model: ModelBIM, filePath: str) """
        pass

    @staticmethod
    def ModelToXml(model):
        """
        ModelToXml(model: List[ModelBIM]) -> str

        ModelToXml(model: ModelBIM) -> str
        """
        pass

    @staticmethod
    def OpenModelContainerFromFile(filePath):
        """ OpenModelContainerFromFile(filePath: str) -> OpenModelContainer """
        pass

    @staticmethod
    def OpenModelContainerFromXml(xml):
        """ OpenModelContainerFromXml(xml: str) -> OpenModelContainer """
        pass

    @staticmethod
    def OpenModelContainerToFile(model, filePath):
        """ OpenModelContainerToFile(model: OpenModelContainer, filePath: str) """
        pass

    @staticmethod
    def OpenModelContainerToXml(model):
        """ OpenModelContainerToXml(model: OpenModelContainer) -> str """
        pass

    @staticmethod
    def ProjectFromFile(filePath):
        """ ProjectFromFile(filePath: str) -> BIMProject """
        pass

    @staticmethod
    def ProjectFromXml(xml):
        """ ProjectFromXml(xml: str) -> BIMProject """
        pass

    @staticmethod
    def ProjectToFile(project, filePath):
        """ ProjectToFile(project: BIMProject, filePath: str) """
        pass

    @staticmethod
    def ProjectToXml(project):
        """ ProjectToXml(project: BIMProject) -> str """
        pass

    __all__ = [
        'ConnectionDataFromXml',
        'ConnectionDataToXml',
        'ModelFromFile',
        'ModelFromXml',
        'ModelsFromFile',
        'ModelsFromXml',
        'ModelToFile',
        'ModelToXml',
        'OpenModelContainerFromFile',
        'OpenModelContainerFromXml',
        'OpenModelContainerToFile',
        'OpenModelContainerToXml',
        'ProjectFromFile',
        'ProjectFromXml',
        'ProjectToFile',
        'ProjectToXml',
    ]


class WcfErrorHandler(object, IErrorHandler):
    """ WcfErrorHandler() """
    def HandleError(self, error):
        """ HandleError(self: WcfErrorHandler, error: Exception) -> bool """
        pass

    @staticmethod
    def InitLogger(logger):
        """ InitLogger(logger: IPluginLogger) """
        pass

    def ProvideFault(self, error, version, fault):
        """ ProvideFault(self: WcfErrorHandler, error: Exception, version: MessageVersion, fault: Message) -> Message """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Logger = None


# variables with complex values

