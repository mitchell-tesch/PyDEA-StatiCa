# encoding: utf-8
# module IdeaRS.OpenModel calls itself OpenModel
# from IdeaRS.OpenModel, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ConeBreakoutCheckType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConeBreakoutCheckType, values: Both (0), None (3), Shear (2), Tension (1) """
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

    Both = None
    None = None
    Shear = None
    Tension = None
    value__ = None


class ConnectionSetup(object):
    """ ConnectionSetup() """
    def InitByCode(self):
        """ InitByCode(self: ConnectionSetup) """
        pass

    AlphaCC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlphaCC(self: ConnectionSetup) -> float

Set: AlphaCC(self: ConnectionSetup) = value
"""

    AnalysisGNL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnalysisGNL(self: ConnectionSetup) -> bool

Set: AnalysisGNL(self: ConnectionSetup) = value
"""

    AnchorLengthForStiffness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorLengthForStiffness(self: ConnectionSetup) -> int

Set: AnchorLengthForStiffness(self: ConnectionSetup) = value
"""

    ApplyBearingCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyBearingCheck(self: ConnectionSetup) -> bool

Set: ApplyBearingCheck(self: ConnectionSetup) = value
"""

    ApplyBetapInfluence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyBetapInfluence(self: ConnectionSetup) -> bool

Set: ApplyBetapInfluence(self: ConnectionSetup) = value
"""

    ApplyConeBreakoutCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyConeBreakoutCheck(self: ConnectionSetup) -> ConeBreakoutCheckType

Set: ApplyConeBreakoutCheck(self: ConnectionSetup) = value
"""

    BaseMetalCapacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseMetalCapacity(self: ConnectionSetup) -> bool

Set: BaseMetalCapacity(self: ConnectionSetup) = value
"""

    BearingAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BearingAngle(self: ConnectionSetup) -> float

Set: BearingAngle(self: ConnectionSetup) = value
"""

    BearingCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BearingCheck(self: ConnectionSetup) -> bool

Set: BearingCheck(self: ConnectionSetup) = value
"""

    BoltMaxGripLengthCoeff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltMaxGripLengthCoeff(self: ConnectionSetup) -> float

Set: BoltMaxGripLengthCoeff(self: ConnectionSetup) = value
"""

    BracedSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BracedSystem(self: ConnectionSetup) -> bool

Set: BracedSystem(self: ConnectionSetup) = value
"""

    CheckDetailing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckDetailing(self: ConnectionSetup) -> bool

Set: CheckDetailing(self: ConnectionSetup) = value
"""

    ConcreteSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConcreteSetup(self: ConnectionSetup) -> ConcreteSetup

Set: ConcreteSetup(self: ConnectionSetup) = value
"""

    CondensedElementLengthFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CondensedElementLengthFactor(self: ConnectionSetup) -> float

Set: CondensedElementLengthFactor(self: ConnectionSetup) = value
"""

    CrackedConcrete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrackedConcrete(self: ConnectionSetup) -> bool

Set: CrackedConcrete(self: ConnectionSetup) = value
"""

    CrtCompCheckIS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrtCompCheckIS(self: ConnectionSetup) -> CrtCompCheckIS

Set: CrtCompCheckIS(self: ConnectionSetup) = value
"""

    DecreasingFtrd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecreasingFtrd(self: ConnectionSetup) -> float

Set: DecreasingFtrd(self: ConnectionSetup) = value
"""

    DeformationBoltHole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeformationBoltHole(self: ConnectionSetup) -> bool

Set: DeformationBoltHole(self: ConnectionSetup) = value
"""

    DevelopedFillers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DevelopedFillers(self: ConnectionSetup) -> bool

Set: DevelopedFillers(self: ConnectionSetup) = value
"""

    DistanceBetweenBolts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceBetweenBolts(self: ConnectionSetup) -> float

Set: DistanceBetweenBolts(self: ConnectionSetup) = value
"""

    DistanceBetweenBoltsEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceBetweenBoltsEdge(self: ConnectionSetup) -> float

Set: DistanceBetweenBoltsEdge(self: ConnectionSetup) = value
"""

    DistanceDiameterBetweenBP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceDiameterBetweenBP(self: ConnectionSetup) -> float

Set: DistanceDiameterBetweenBP(self: ConnectionSetup) = value
"""

    DivisionOfArcsOfRHS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DivisionOfArcsOfRHS(self: ConnectionSetup) -> int

Set: DivisionOfArcsOfRHS(self: ConnectionSetup) = value
"""

    DivisionOfSurfaceOfCHS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DivisionOfSurfaceOfCHS(self: ConnectionSetup) -> int

Set: DivisionOfSurfaceOfCHS(self: ConnectionSetup) = value
"""

    EffectiveAreaStressCoeff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveAreaStressCoeff(self: ConnectionSetup) -> float

Set: EffectiveAreaStressCoeff(self: ConnectionSetup) = value
"""

    EffectiveAreaStressCoeffAISC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveAreaStressCoeffAISC(self: ConnectionSetup) -> float

Set: EffectiveAreaStressCoeffAISC(self: ConnectionSetup) = value
"""

    ExtensionLengthRationCloseSections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLengthRationCloseSections(self: ConnectionSetup) -> float

Set: ExtensionLengthRationCloseSections(self: ConnectionSetup) = value
"""

    ExtensionLengthRationOpenSections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtensionLengthRationOpenSections(self: ConnectionSetup) -> float

Set: ExtensionLengthRationOpenSections(self: ConnectionSetup) = value
"""

    FactorPreloadBolt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FactorPreloadBolt(self: ConnectionSetup) -> float

Set: FactorPreloadBolt(self: ConnectionSetup) = value
"""

    FatigueSectionOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FatigueSectionOffset(self: ConnectionSetup) -> float

Set: FatigueSectionOffset(self: ConnectionSetup) = value
"""

    FrictionCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrictionCoefficient(self: ConnectionSetup) -> float

Set: FrictionCoefficient(self: ConnectionSetup) = value
"""

    FrictionCoefficientPbolt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrictionCoefficientPbolt(self: ConnectionSetup) -> float

Set: FrictionCoefficientPbolt(self: ConnectionSetup) = value
"""

    GammaC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaC(self: ConnectionSetup) -> float

Set: GammaC(self: ConnectionSetup) = value
"""

    GammaInst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaInst(self: ConnectionSetup) -> float

Set: GammaInst(self: ConnectionSetup) = value
"""

    GammaM3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaM3(self: ConnectionSetup) -> float

Set: GammaM3(self: ConnectionSetup) = value
"""

    GammaMu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaMu(self: ConnectionSetup) -> float

Set: GammaMu(self: ConnectionSetup) = value
"""

    JointBetaFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JointBetaFactor(self: ConnectionSetup) -> float

Set: JointBetaFactor(self: ConnectionSetup) = value
"""

    LimitDeformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LimitDeformation(self: ConnectionSetup) -> float

Set: LimitDeformation(self: ConnectionSetup) = value
"""

    LimitDeformationCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LimitDeformationCheck(self: ConnectionSetup) -> bool

Set: LimitDeformationCheck(self: ConnectionSetup) = value
"""

    LimitPlasticStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LimitPlasticStrain(self: ConnectionSetup) -> float

Set: LimitPlasticStrain(self: ConnectionSetup) = value
"""

    MaxSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxSize(self: ConnectionSetup) -> float

Set: MaxSize(self: ConnectionSetup) = value
"""

    Mdiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mdiv(self: ConnectionSetup) -> int

Set: Mdiv(self: ConnectionSetup) = value
"""

    MemberLengthRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberLengthRatio(self: ConnectionSetup) -> float

Set: MemberLengthRatio(self: ConnectionSetup) = value
"""

    MinSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinSize(self: ConnectionSetup) -> float

Set: MinSize(self: ConnectionSetup) = value
"""

    NumberIterations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberIterations(self: ConnectionSetup) -> int

Set: NumberIterations(self: ConnectionSetup) = value
"""

    NumElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumElement(self: ConnectionSetup) -> int

Set: NumElement(self: ConnectionSetup) = value
"""

    NumElementRhs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumElementRhs(self: ConnectionSetup) -> int

Set: NumElementRhs(self: ConnectionSetup) = value
"""

    OptimalCheckLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OptimalCheckLevel(self: ConnectionSetup) -> float

Set: OptimalCheckLevel(self: ConnectionSetup) = value
"""

    PretensionForceFpc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PretensionForceFpc(self: ConnectionSetup) -> float

Set: PretensionForceFpc(self: ConnectionSetup) = value
"""

    RigidBP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RigidBP(self: ConnectionSetup) -> bool

Set: RigidBP(self: ConnectionSetup) = value
"""

    SteelSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SteelSetup(self: ConnectionSetup) -> SteelSetup

Set: SteelSetup(self: ConnectionSetup) = value
"""

    StopAtLimitStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StopAtLimitStrain(self: ConnectionSetup) -> bool

Set: StopAtLimitStrain(self: ConnectionSetup) = value
"""

    WarnCheckLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarnCheckLevel(self: ConnectionSetup) -> float

Set: WarnCheckLevel(self: ConnectionSetup) = value
"""

    WarnPlasticStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarnPlasticStrain(self: ConnectionSetup) -> float

Set: WarnPlasticStrain(self: ConnectionSetup) = value
"""

    WeldEvaluationData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldEvaluationData(self: ConnectionSetup) -> WeldEvaluation

Set: WeldEvaluationData(self: ConnectionSetup) = value
"""



class CoordinateSystemMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum CoordinateSystemMethod, values: Cartesian (0), Polar (1) """
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

    Cartesian = None
    Polar = None
    value__ = None


class CountryCode(Enum, IComparable, IFormattable, IConvertible):
    """ enum CountryCode, values: American (8), Australia (10), Canada (9), CHN (12), ECEN (1), HKG (13), India (5), None (0), RUS (11), SIA (6) """
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

    American = None
    Australia = None
    Canada = None
    CHN = None
    ECEN = None
    HKG = None
    India = None
    None = None
    RUS = None
    SIA = None
    value__ = None


class CrossSectionConversionTable(Enum, IComparable, IFormattable, IConvertible):
    """ enum CrossSectionConversionTable, values: AdvanceDesign (5), Autodesk (2), NoUsed (0), SAP2000 (3), SCIA (1), StaadPro (4) """
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

    AdvanceDesign = None
    Autodesk = None
    NoUsed = None
    SAP2000 = None
    SCIA = None
    StaadPro = None
    value__ = None


class CrtCompCheckIS(Enum, IComparable, IFormattable, IConvertible):
    """ enum CrtCompCheckIS, values: IS456_Cl_34_4 (1), IS800_Cl_7_4 (0) """
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

    IS456_Cl_34_4 = None
    IS800_Cl_7_4 = None
    value__ = None


class OpenObject(object):
    """ OpenObject() """

class OpenAttribute(OpenObject):
    # no doc
    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Element(self: OpenAttribute) -> ReferenceElement

Set: Element(self: OpenAttribute) = value
"""



class OpenElementId(OpenObject):
    """ OpenElementId() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: OpenElementId) -> int

Set: Id(self: OpenElementId) = value
"""



class OpenModel(object):
    """ OpenModel() """
    def AddObject(self, obj):
        """
        AddObject(self: OpenModel, obj: OpenAttribute) -> int
        AddObject(self: OpenModel, obj: OpenElementId) -> int
        """
        pass

    def GetExistingObject(self, obj):
        """ GetExistingObject(self: OpenModel, obj: OpenElementId) -> OpenElementId """
        pass

    def GetMaxId(self, *__args):
        """
        GetMaxId(self: OpenModel, typeName: str) -> int
        GetMaxId(self: OpenModel, obj: OpenElementId) -> int
        GetMaxId(self: OpenModel, t: Type) -> int
        """
        pass

    def GetObject(self, element):
        """ GetObject(self: OpenModel, element: ReferenceElement) -> OpenElementId """
        pass

    @staticmethod
    def LoadFromStream(xmlFileStream):
        """ LoadFromStream(xmlFileStream: Stream) -> OpenModel """
        pass

    @staticmethod
    def LoadFromString(xmlString):
        """ LoadFromString(xmlString: str) -> OpenModel """
        pass

    @staticmethod
    def LoadFromXmlFile(xmlFileName):
        """ LoadFromXmlFile(xmlFileName: str) -> OpenModel """
        pass

    def ReferenceElementsReconstruction(self, renewReferences):
        """ ReferenceElementsReconstruction(self: OpenModel, renewReferences: bool) """
        pass

    def SaveToXmlFile(self, xmlFileName):
        """ SaveToXmlFile(self: OpenModel, xmlFileName: str) -> bool """
        pass

    ArcSegment3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArcSegment3D(self: OpenModel) -> List[ArcSegment3D]

Set: ArcSegment3D(self: OpenModel) = value
"""

    Attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attribute(self: OpenModel) -> List[OpenAttribute]

Set: Attribute(self: OpenModel) = value
"""

    Beam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Beam(self: OpenModel) -> List[Beam]

Set: Beam(self: OpenModel) = value
"""

    CheckMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckMember(self: OpenModel) -> List[CheckMember]

Set: CheckMember(self: OpenModel) = value
"""

    CombiInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CombiInput(self: OpenModel) -> List[CombiInput]

Set: CombiInput(self: OpenModel) = value
"""

    ConcreteCheckSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConcreteCheckSection(self: OpenModel) -> List[CheckSection]

Set: ConcreteCheckSection(self: OpenModel) = value
"""

    ConcreteSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConcreteSetup(self: OpenModel) -> ConcreteSetup

Set: ConcreteSetup(self: OpenModel) = value
"""

    ConnectionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionPoint(self: OpenModel) -> List[ConnectionPoint]

Set: ConnectionPoint(self: OpenModel) = value
"""

    Connections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Connections(self: OpenModel) -> List[ConnectionData]

Set: Connections(self: OpenModel) = value
"""

    ConnectionSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionSetup(self: OpenModel) -> ConnectionSetup

Set: ConnectionSetup(self: OpenModel) = value
"""

    CrossSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSection(self: OpenModel) -> List[CrossSection]

Set: CrossSection(self: OpenModel) = value
"""

    DappedEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DappedEnd(self: OpenModel) -> List[DappedEnd]

Set: DappedEnd(self: OpenModel) = value
"""

    DesignMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignMember(self: OpenModel) -> List[DesignMember]

Set: DesignMember(self: OpenModel) = value
"""

    Element1D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Element1D(self: OpenModel) -> List[Element1D]

Set: Element1D(self: OpenModel) = value
"""

    Element2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Element2D(self: OpenModel) -> List[Element2D]

Set: Element2D(self: OpenModel) = value
"""

    HingeElement1D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeElement1D(self: OpenModel) -> List[HingeElement1D]

Set: HingeElement1D(self: OpenModel) = value
"""

    InitialImperfectionOfPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialImperfectionOfPoint(self: OpenModel) -> List[InitialImperfectionOfPoint]

Set: InitialImperfectionOfPoint(self: OpenModel) = value
"""

    ISDModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ISDModel(self: OpenModel) -> List[ISDModel]

Set: ISDModel(self: OpenModel) = value
"""

    LineSegment3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSegment3D(self: OpenModel) -> List[LineSegment3D]

Set: LineSegment3D(self: OpenModel) = value
"""

    LineSupportSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSupportSegment(self: OpenModel) -> List[LineSupportSegment]

Set: LineSupportSegment(self: OpenModel) = value
"""

    LoadCase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCase(self: OpenModel) -> List[LoadCase]

Set: LoadCase(self: OpenModel) = value
"""

    LoadGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadGroup(self: OpenModel) -> List[LoadGroup]

Set: LoadGroup(self: OpenModel) = value
"""

    LoadsInPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadsInPoint(self: OpenModel) -> List[LoadInPoint]

Set: LoadsInPoint(self: OpenModel) = value
"""

    LoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadsOnLine(self: OpenModel) -> List[LoadOnLine]

Set: LoadsOnLine(self: OpenModel) = value
"""

    LoadsOnSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadsOnSurface(self: OpenModel) -> List[LoadOnSurface]

Set: LoadsOnSurface(self: OpenModel) = value
"""

    MatConcrete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatConcrete(self: OpenModel) -> List[MatConcrete]

Set: MatConcrete(self: OpenModel) = value
"""

    MatPrestressSteel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatPrestressSteel(self: OpenModel) -> List[MatPrestressSteel]

Set: MatPrestressSteel(self: OpenModel) = value
"""

    MatReinforcement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatReinforcement(self: OpenModel) -> List[MatReinforcement]

Set: MatReinforcement(self: OpenModel) = value
"""

    MatSteel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatSteel(self: OpenModel) -> List[MatSteel]

Set: MatSteel(self: OpenModel) = value
"""

    Member1D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Member1D(self: OpenModel) -> List[Member1D]

Set: Member1D(self: OpenModel) = value
"""

    Member2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Member2D(self: OpenModel) -> List[Member2D]

Set: Member2D(self: OpenModel) = value
"""

    Opening = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Opening(self: OpenModel) -> List[Opening]

Set: Opening(self: OpenModel) = value
"""

    OriginSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginSettings(self: OpenModel) -> OriginSettings

Set: OriginSettings(self: OpenModel) = value
"""

    PatchDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatchDevice(self: OpenModel) -> List[PatchDevice]

Set: PatchDevice(self: OpenModel) = value
"""

    Point3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point3D(self: OpenModel) -> List[Point3D]

Set: Point3D(self: OpenModel) = value
"""

    PointLoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointLoadsOnLine(self: OpenModel) -> List[PointLoadOnLine]

Set: PointLoadsOnLine(self: OpenModel) = value
"""

    PointOnLine3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointOnLine3D(self: OpenModel) -> List[PointOnLine3D]

Set: PointOnLine3D(self: OpenModel) = value
"""

    PointSupportNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointSupportNode(self: OpenModel) -> List[PointSupportNode]

Set: PointSupportNode(self: OpenModel) = value
"""

    PolyLine3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PolyLine3D(self: OpenModel) -> List[PolyLine3D]

Set: PolyLine3D(self: OpenModel) = value
"""

    ProjectData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectData(self: OpenModel) -> ProjectData

Set: ProjectData(self: OpenModel) = value
"""

    ProjectDataConcrete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectDataConcrete(self: OpenModel) -> ProjectDataConcrete

Set: ProjectDataConcrete(self: OpenModel) = value
"""

    RebarGeneral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarGeneral(self: OpenModel) -> List[RebarGeneral]

Set: RebarGeneral(self: OpenModel) = value
"""

    RebarShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarShape(self: OpenModel) -> List[RebarShape]

Set: RebarShape(self: OpenModel) = value
"""

    RebarSingle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarSingle(self: OpenModel) -> List[RebarSingle]

Set: RebarSingle(self: OpenModel) = value
"""

    RebarStirrups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarStirrups(self: OpenModel) -> List[RebarStirrups]

Set: RebarStirrups(self: OpenModel) = value
"""

    Region3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Region3D(self: OpenModel) -> List[Region3D]

Set: Region3D(self: OpenModel) = value
"""

    ReinforcedCrossSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReinforcedCrossSection(self: OpenModel) -> List[ReinforcedCrossSection]

Set: ReinforcedCrossSection(self: OpenModel) = value
"""

    Reinforcement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reinforcement(self: OpenModel) -> List[Reinforcement]

Set: Reinforcement(self: OpenModel) = value
"""

    ResultClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultClass(self: OpenModel) -> List[ResultClass]

Set: ResultClass(self: OpenModel) = value
"""

    RigidLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RigidLink(self: OpenModel) -> List[RigidLink]

Set: RigidLink(self: OpenModel) = value
"""

    Settlements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settlements(self: OpenModel) -> List[Settlement]

Set: Settlements(self: OpenModel) = value
"""

    Span = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Span(self: OpenModel) -> List[Span]

Set: Span(self: OpenModel) = value
"""

    StrainLoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StrainLoadsOnLine(self: OpenModel) -> List[StrainLoadOnLine]

Set: StrainLoadsOnLine(self: OpenModel) = value
"""

    SubStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubStructure(self: OpenModel) -> List[SubStructure]

Set: SubStructure(self: OpenModel) = value
"""

    Taper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Taper(self: OpenModel) -> List[Taper]

Set: Taper(self: OpenModel) = value
"""

    TemperatureLoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureLoadsOnLine(self: OpenModel) -> List[TemperatureLoadOnLine]

Set: TemperatureLoadsOnLine(self: OpenModel) = value
"""

    Tendon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tendon(self: OpenModel) -> List[Tendon]

Set: Tendon(self: OpenModel) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: OpenModel) -> int

Set: Version(self: OpenModel) = value
"""

    Wall = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wall(self: OpenModel) -> List[Wall]

Set: Wall(self: OpenModel) = value
"""



class OpenModelClassAttribute(Attribute, _Attribute):
    """
    OpenModelClassAttribute(structuralModelClassType: str, structuralModelContainerType: str, openModelListType: Type)
    OpenModelClassAttribute(structuralModelClassType: str, openModelListType: Type)
    OpenModelClassAttribute(structuralModelClassType: str, structuralModelContainerType: str)
    OpenModelClassAttribute(structuralModelClassType: str)
    OpenModelClassAttribute(openModelListType: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, structuralModelClassType: str, structuralModelContainerType: str, openModelListType: Type)
        __new__(cls: type, structuralModelClassType: str, openModelListType: Type)
        __new__(cls: type, structuralModelClassType: str, structuralModelContainerType: str)
        __new__(cls: type, structuralModelClassType: str)
        __new__(cls: type, openModelListType: Type)
        """
        pass

    OpenModelListType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpenModelListType(self: OpenModelClassAttribute) -> Type

Set: OpenModelListType(self: OpenModelClassAttribute) = value
"""

    StructuralModelClassType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructuralModelClassType(self: OpenModelClassAttribute) -> str

Set: StructuralModelClassType(self: OpenModelClassAttribute) = value
"""

    StructuralModelContainerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructuralModelContainerType(self: OpenModelClassAttribute) -> str

Set: StructuralModelContainerType(self: OpenModelClassAttribute) = value
"""



class OpenModelContainer(object):
    """ OpenModelContainer() """
    OpenModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpenModel(self: OpenModelContainer) -> OpenModel

Set: OpenModel(self: OpenModelContainer) = value
"""

    OpenModelResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpenModelResult(self: OpenModelContainer) -> OpenModelResult

Set: OpenModelResult(self: OpenModelContainer) = value
"""



class OpenModelPropertyAttribute(Attribute, _Attribute):
    """ OpenModelPropertyAttribute(structuralModelName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, structuralModelName):
        """ __new__(cls: type, structuralModelName: str) """
        pass

    StructuralModelName = None


class OriginSettings(OpenObject):
    """ OriginSettings() """
    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Author(self: OriginSettings) -> str

Set: Author(self: OriginSettings) = value
"""

    CheckEquilibrium = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckEquilibrium(self: OriginSettings) -> bool

Set: CheckEquilibrium(self: OriginSettings) = value
"""

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: OriginSettings) -> CountryCode

Set: CountryCode(self: OriginSettings) = value
"""

    CrossSectionConversionTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionConversionTable(self: OriginSettings) -> CrossSectionConversionTable

Set: CrossSectionConversionTable(self: OriginSettings) = value
"""

    DateOfCreate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateOfCreate(self: OriginSettings) -> DateTime

Set: DateOfCreate(self: OriginSettings) = value
"""

    ImportRecommendedWelds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportRecommendedWelds(self: OriginSettings) -> bool

Set: ImportRecommendedWelds(self: OriginSettings) = value
"""

    ProjectDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectDescription(self: OriginSettings) -> str

Set: ProjectDescription(self: OriginSettings) = value
"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectName(self: OriginSettings) -> str

Set: ProjectName(self: OriginSettings) = value
"""



class PreloadedBoltsLoadType(Enum, IComparable, IFormattable, IConvertible):
    """ enum PreloadedBoltsLoadType, values: Dynamic (1), Static (0) """
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

    Dynamic = None
    Static = None
    value__ = None


class ProjectData(OpenObject):
    """ ProjectData() """
    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Author(self: ProjectData) -> str

Set: Author(self: ProjectData) = value
"""

    CodeDependentData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeDependentData(self: ProjectData) -> object

Set: CodeDependentData(self: ProjectData) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: ProjectData) -> DateTime

Set: Date(self: ProjectData) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ProjectData) -> str

Set: Description(self: ProjectData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ProjectData) -> str

Set: Name(self: ProjectData) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: ProjectData) -> str

Set: Number(self: ProjectData) = value
"""



class ProjectDataEc(OpenObject):
    """ ProjectDataEc() """
    AnnexCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnnexCode(self: ProjectDataEc) -> NationalAnnexCode

Set: AnnexCode(self: ProjectDataEc) = value
"""

    FatigueAnnexNN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FatigueAnnexNN(self: ProjectDataEc) -> bool

Set: FatigueAnnexNN(self: ProjectDataEc) = value
"""

    FatigueCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FatigueCheck(self: ProjectDataEc) -> bool

Set: FatigueCheck(self: ProjectDataEc) = value
"""



class ReferenceElement(object):
    """
    ReferenceElement()
    ReferenceElement(element: OpenElementId)
    """
    @staticmethod # known case of __new__
    def __new__(self, element=None):
        """
        __new__(cls: type)
        __new__(cls: type, element: OpenElementId)
        """
        pass

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Element(self: ReferenceElement) -> OpenElementId

Set: Element(self: ReferenceElement) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ReferenceElement) -> int

Set: Id(self: ReferenceElement) = value
"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: ReferenceElement) -> str

Set: TypeName(self: ReferenceElement) = value
"""



class SteelSetup(object):
    # no doc
    def FrictionCoefficientPboltDefault(self):
        """ FrictionCoefficientPboltDefault(self: SteelSetup) -> float """
        pass


class SteelSetupAISC(SteelSetup):
    """ SteelSetupAISC() """
    BoltBearing_Omega = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltBearing_Omega(self: SteelSetupAISC) -> float

Set: BoltBearing_Omega(self: SteelSetupAISC) = value
"""

    BoltBearing_Phi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltBearing_Phi(self: SteelSetupAISC) -> float

Set: BoltBearing_Phi(self: SteelSetupAISC) = value
"""

    BoltSlipRes_Omega = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltSlipRes_Omega(self: SteelSetupAISC) -> float

Set: BoltSlipRes_Omega(self: SteelSetupAISC) = value
"""

    BoltSlipRes_Phi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltSlipRes_Phi(self: SteelSetupAISC) -> float

Set: BoltSlipRes_Phi(self: SteelSetupAISC) = value
"""

    BoltTensileShearCombined_Omega = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltTensileShearCombined_Omega(self: SteelSetupAISC) -> float

Set: BoltTensileShearCombined_Omega(self: SteelSetupAISC) = value
"""

    BoltTensileShearCombined_Phi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltTensileShearCombined_Phi(self: SteelSetupAISC) -> float

Set: BoltTensileShearCombined_Phi(self: SteelSetupAISC) = value
"""

    BoltTensileShear_Omega = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltTensileShear_Omega(self: SteelSetupAISC) -> float

Set: BoltTensileShear_Omega(self: SteelSetupAISC) = value
"""

    BoltTensileShear_Phi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltTensileShear_Phi(self: SteelSetupAISC) -> float

Set: BoltTensileShear_Phi(self: SteelSetupAISC) = value
"""

    FilletWelds_Omega = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilletWelds_Omega(self: SteelSetupAISC) -> float

Set: FilletWelds_Omega(self: SteelSetupAISC) = value
"""

    FilletWelds_Phi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilletWelds_Phi(self: SteelSetupAISC) -> float

Set: FilletWelds_Phi(self: SteelSetupAISC) = value
"""

    MaterialFy_Omega = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialFy_Omega(self: SteelSetupAISC) -> float

Set: MaterialFy_Omega(self: SteelSetupAISC) = value
"""

    MaterialFy_Phi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialFy_Phi(self: SteelSetupAISC) -> float

Set: MaterialFy_Phi(self: SteelSetupAISC) = value
"""

    ReductionFactorShear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReductionFactorShear(self: SteelSetupAISC) -> float

Set: ReductionFactorShear(self: SteelSetupAISC) = value
"""

    ReductionFactorTension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReductionFactorTension(self: SteelSetupAISC) -> float

Set: ReductionFactorTension(self: SteelSetupAISC) = value
"""



class SteelSetupAUS(SteelSetup):
    """ SteelSetupAUS() """
    def FrictionCoefficientPboltDefault(self):
        """ FrictionCoefficientPboltDefault(self: SteelSetupAUS) -> float """
        pass

    Anchor_Fiar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Anchor_Fiar(self: SteelSetupAUS) -> float

Set: Anchor_Fiar(self: SteelSetupAUS) = value
"""

    Bolt_Fib = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bolt_Fib(self: SteelSetupAUS) -> float

Set: Bolt_Fib(self: SteelSetupAUS) = value
"""

    Bolt_Fip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bolt_Fip(self: SteelSetupAUS) -> float

Set: Bolt_Fip(self: SteelSetupAUS) = value
"""

    CrtBearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrtBearing(self: SteelSetupAUS) -> float

Set: CrtBearing(self: SteelSetupAUS) = value
"""

    Structural_Fi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structural_Fi(self: SteelSetupAUS) -> float

Set: Structural_Fi(self: SteelSetupAUS) = value
"""

    Weld_Fiw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weld_Fiw(self: SteelSetupAUS) -> float

Set: Weld_Fiw(self: SteelSetupAUS) = value
"""



class SteelSetupCISC(SteelSetup):
    """ SteelSetupCISC() """
    Anchor_Fiar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Anchor_Fiar(self: SteelSetupCISC) -> float

Set: Anchor_Fiar(self: SteelSetupCISC) = value
"""

    Bolt_Fib = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bolt_Fib(self: SteelSetupCISC) -> float

Set: Bolt_Fib(self: SteelSetupCISC) = value
"""

    Structural_Fi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structural_Fi(self: SteelSetupCISC) -> float

Set: Structural_Fi(self: SteelSetupCISC) = value
"""

    Weld_Fiw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weld_Fiw(self: SteelSetupCISC) -> float

Set: Weld_Fiw(self: SteelSetupCISC) = value
"""



class SteelSetupECEN(SteelSetup):
    """ SteelSetupECEN() """
    GammaM0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaM0(self: SteelSetupECEN) -> float

Set: GammaM0(self: SteelSetupECEN) = value
"""

    GammaM1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaM1(self: SteelSetupECEN) -> float

Set: GammaM1(self: SteelSetupECEN) = value
"""

    GammaM2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaM2(self: SteelSetupECEN) -> float

Set: GammaM2(self: SteelSetupECEN) = value
"""

    GammaMfi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaMfi(self: SteelSetupECEN) -> float

Set: GammaMfi(self: SteelSetupECEN) = value
"""

    GammaMu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaMu(self: SteelSetupECEN) -> float

Set: GammaMu(self: SteelSetupECEN) = value
"""



class SteelSetupHKG(SteelSetup):
    """ SteelSetupHKG() """
    def FrictionCoefficientPboltDefault(self):
        """ FrictionCoefficientPboltDefault(self: SteelSetupHKG) -> float """
        pass


class SteelSetupIND(SteelSetup):
    """ SteelSetupIND() """
    def FrictionCoefficientPboltDefault(self):
        """ FrictionCoefficientPboltDefault(self: SteelSetupIND) -> float """
        pass

    GammaM0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaM0(self: SteelSetupIND) -> float

Set: GammaM0(self: SteelSetupIND) = value
"""

    GammaM1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaM1(self: SteelSetupIND) -> float

Set: GammaM1(self: SteelSetupIND) = value
"""

    GammaMb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaMb(self: SteelSetupIND) -> float

Set: GammaMb(self: SteelSetupIND) = value
"""

    GammaMf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaMf(self: SteelSetupIND) -> float

Set: GammaMf(self: SteelSetupIND) = value
"""

    GammaMw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaMw(self: SteelSetupIND) -> float

Set: GammaMw(self: SteelSetupIND) = value
"""



class SteelSetupRUS(SteelSetup):
    """ SteelSetupRUS() """
    def FrictionCoefficientPboltDefault(self):
        """ FrictionCoefficientPboltDefault(self: SteelSetupRUS) -> float """
        pass

    Anchor_Fiar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Anchor_Fiar(self: SteelSetupRUS) -> float

Set: Anchor_Fiar(self: SteelSetupRUS) = value
"""

    Bolt_Fib = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bolt_Fib(self: SteelSetupRUS) -> float

Set: Bolt_Fib(self: SteelSetupRUS) = value
"""

    Bolt_Fip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bolt_Fip(self: SteelSetupRUS) -> float

Set: Bolt_Fip(self: SteelSetupRUS) = value
"""

    CrtBearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrtBearing(self: SteelSetupRUS) -> float

Set: CrtBearing(self: SteelSetupRUS) = value
"""

    PreloadedBoltsLoadType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreloadedBoltsLoadType(self: SteelSetupRUS) -> PreloadedBoltsLoadType

Set: PreloadedBoltsLoadType(self: SteelSetupRUS) = value
"""

    Structural_Fi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Structural_Fi(self: SteelSetupRUS) -> float

Set: Structural_Fi(self: SteelSetupRUS) = value
"""

    WeldingTypeSNIP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldingTypeSNIP(self: SteelSetupRUS) -> WeldingTypeSNIP

Set: WeldingTypeSNIP(self: SteelSetupRUS) = value
"""

    Weld_Fiw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weld_Fiw(self: SteelSetupRUS) -> float

Set: Weld_Fiw(self: SteelSetupRUS) = value
"""



class Symmetry(Enum, IComparable, IFormattable, IConvertible):
    """ enum Symmetry, values: Asymmetrical (2), NotAvailable (0), Symmetrical (1) """
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

    Asymmetrical = None
    NotAvailable = None
    Symmetrical = None
    value__ = None


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
    def DeserializeModel(xml):
        """ DeserializeModel[T](xml: str) -> T """
        pass

    @staticmethod
    def DeserializeModelFromFile(xmlFileName):
        """ DeserializeModelFromFile[T](xmlFileName: str) -> T """
        pass

    @staticmethod
    def DeserializeModelFromStream(stream):
        """ DeserializeModelFromStream[T](stream: Stream) -> T """
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
    def SerializeModel(model):
        """ SerializeModel[T](model: T) -> str """
        pass

    @staticmethod
    def SerializeModelToFile(model, filePath):
        """ SerializeModelToFile[T](model: T, filePath: str) """
        pass

    __all__ = [
        'ConnectionDataFromXml',
        'ConnectionDataToXml',
        'DeserializeModel',
        'DeserializeModelFromFile',
        'DeserializeModelFromStream',
        'OpenModelContainerFromFile',
        'OpenModelContainerFromXml',
        'OpenModelContainerToFile',
        'OpenModelContainerToXml',
        'SerializeModel',
        'SerializeModelToFile',
    ]


class WeldEvaluation(Enum, IComparable, IFormattable, IConvertible):
    """ enum WeldEvaluation, values: ApplyPlasticWelds (4), ForceResultant (1), MaxForceElement (0) """
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

    ApplyPlasticWelds = None
    ForceResultant = None
    MaxForceElement = None
    value__ = None


class WeldingTypeSNIP(Enum, IComparable, IFormattable, IConvertible):
    """ enum WeldingTypeSNIP, values: Automatic (3), AutomaticAndMachine (2), Manual (0), ManualSmallRodDiam (1) """
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

    Automatic = None
    AutomaticAndMachine = None
    Manual = None
    ManualSmallRodDiam = None
    value__ = None


# variables with complex values

