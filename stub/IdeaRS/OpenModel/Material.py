# encoding: utf-8
# module IdeaRS.OpenModel.Material calls itself Material
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BoltAssembly(OpenElementId):
    """ BoltAssembly() """
    BoltGrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltGrade(self: BoltAssembly) -> ReferenceElement

Set: BoltGrade(self: BoltAssembly) = value
"""

    Borehole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Borehole(self: BoltAssembly) -> float

Set: Borehole(self: BoltAssembly) = value
"""

    DiagonalHeadDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalHeadDiameter(self: BoltAssembly) -> float

Set: DiagonalHeadDiameter(self: BoltAssembly) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: BoltAssembly) -> float

Set: Diameter(self: BoltAssembly) = value
"""

    GrossArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossArea(self: BoltAssembly) -> float

Set: GrossArea(self: BoltAssembly) = value
"""

    HeadDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadDiameter(self: BoltAssembly) -> float

Set: HeadDiameter(self: BoltAssembly) = value
"""

    HeadHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadHeight(self: BoltAssembly) -> float

Set: HeadHeight(self: BoltAssembly) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BoltAssembly) -> str

Set: Name(self: BoltAssembly) = value
"""

    NutThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NutThickness(self: BoltAssembly) -> float

Set: NutThickness(self: BoltAssembly) = value
"""

    TensileStressArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TensileStressArea(self: BoltAssembly) -> float

Set: TensileStressArea(self: BoltAssembly) = value
"""

    WasherAtHead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WasherAtHead(self: BoltAssembly) -> bool

Set: WasherAtHead(self: BoltAssembly) = value
"""

    WasherAtNut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WasherAtNut(self: BoltAssembly) -> bool

Set: WasherAtNut(self: BoltAssembly) = value
"""

    WasherThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WasherThickness(self: BoltAssembly) -> float

Set: WasherThickness(self: BoltAssembly) = value
"""



class ConcAggregateType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConcAggregateType, values: Basalt (3), Limestone (1), Quartzite (0), Sandstone (2) """
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

    Basalt = None
    Limestone = None
    Quartzite = None
    Sandstone = None
    value__ = None


class ConcAggregateTypeSIA(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConcAggregateTypeSIA, values: AlluvialGravel (0), CrushedLimestone (1), Micaceous (2) """
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

    AlluvialGravel = None
    CrushedLimestone = None
    Micaceous = None
    value__ = None


class ConcCementClass(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConcCementClass, values: N (2), R (1), S (0) """
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

    N = None
    R = None
    S = None
    value__ = None


class ConcCementClassSIA(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConcCementClassSIA, values: N (2), R (1), S (0) """
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

    N = None
    R = None
    S = None
    value__ = None


class ConcDiagramType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConcDiagramType, values: Bilinear (0), DefinedByUser (2), Parabolic (1) """
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

    Bilinear = None
    DefinedByUser = None
    Parabolic = None
    value__ = None


class ConcFireDiagramType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConcFireDiagramType, values: ByCodeWithAutomaticTemperature (0), ByCodeWithFixedTemperature (1) """
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

    ByCodeWithAutomaticTemperature = None
    ByCodeWithFixedTemperature = None
    value__ = None


class CrackWidthRequirementsSIA(Enum, IComparable, IFormattable, IConvertible):
    """ enum CrackWidthRequirementsSIA, values: A (1), B (2), C (3), NotNecessary (0), Value (4) """
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

    A = None
    B = None
    C = None
    NotNecessary = None
    Value = None
    value__ = None


class MatAnchorProperties(object):
    """ MatAnchorProperties() """
    FLS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FLS(self: MatAnchorProperties) -> float

Set: FLS(self: MatAnchorProperties) = value
"""

    FLT = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FLT(self: MatAnchorProperties) -> float

Set: FLT(self: MatAnchorProperties) = value
"""

    KS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KS(self: MatAnchorProperties) -> float

Set: KS(self: MatAnchorProperties) = value
"""

    KSN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KSN(self: MatAnchorProperties) -> float

Set: KSN(self: MatAnchorProperties) = value
"""

    KT = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KT(self: MatAnchorProperties) -> float

Set: KT(self: MatAnchorProperties) = value
"""

    KTN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KTN(self: MatAnchorProperties) -> float

Set: KTN(self: MatAnchorProperties) = value
"""

    Uls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Uls(self: MatAnchorProperties) -> float

Set: Uls(self: MatAnchorProperties) = value
"""

    Ult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ult(self: MatAnchorProperties) -> float

Set: Ult(self: MatAnchorProperties) = value
"""



class Material(OpenElementId):
    # no doc
    E = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: E(self: Material) -> float

Set: E(self: Material) = value
"""

    G = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: G(self: Material) -> float

Set: G(self: Material) = value
"""

    IsDefaultMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefaultMaterial(self: Material) -> bool

Set: IsDefaultMaterial(self: Material) = value
"""

    LoadFromLibrary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadFromLibrary(self: Material) -> bool

Set: LoadFromLibrary(self: Material) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Material) -> str

Set: Name(self: Material) = value
"""

    OrderInCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderInCode(self: Material) -> int

Set: OrderInCode(self: Material) = value
"""

    Poisson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Poisson(self: Material) -> float

Set: Poisson(self: Material) = value
"""

    SpecificHeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificHeat(self: Material) -> float

Set: SpecificHeat(self: Material) = value
"""

    StateOfThermalConductivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateOfThermalConductivity(self: Material) -> ThermalConductivityState

Set: StateOfThermalConductivity(self: Material) = value
"""

    StateOfThermalExpansion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateOfThermalExpansion(self: Material) -> ThermalExpansionState

Set: StateOfThermalExpansion(self: Material) = value
"""

    StateOfThermalSpecificHeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateOfThermalSpecificHeat(self: Material) -> ThermalSpecificHeatState

Set: StateOfThermalSpecificHeat(self: Material) = value
"""

    StateOfThermalStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateOfThermalStrain(self: Material) -> ThermalStrainState

Set: StateOfThermalStrain(self: Material) = value
"""

    StateOfThermalStressStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateOfThermalStressStrain(self: Material) -> ThermalStressStrainState

Set: StateOfThermalStressStrain(self: Material) = value
"""

    ThermalConductivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalConductivity(self: Material) -> float

Set: ThermalConductivity(self: Material) = value
"""

    ThermalExpansion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalExpansion(self: Material) -> float

Set: ThermalExpansion(self: Material) = value
"""

    UnitMass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitMass(self: Material) -> float

Set: UnitMass(self: Material) = value
"""

    UserThermalConductivityCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserThermalConductivityCurvature(self: Material) -> Polygon2D

Set: UserThermalConductivityCurvature(self: Material) = value
"""

    UserThermalExpansionCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserThermalExpansionCurvature(self: Material) -> Polygon2D

Set: UserThermalExpansionCurvature(self: Material) = value
"""

    UserThermalSpecificHeatCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserThermalSpecificHeatCurvature(self: Material) -> Polygon2D

Set: UserThermalSpecificHeatCurvature(self: Material) = value
"""

    UserThermalStrainCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserThermalStrainCurvature(self: Material) -> Polygon2D

Set: UserThermalStrainCurvature(self: Material) = value
"""

    UserThermalStressStrainCurvature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserThermalStressStrainCurvature(self: Material) -> List[TemperatureCurve2D]

Set: UserThermalStressStrainCurvature(self: Material) = value
"""



class MatConcrete(Material):
    # no doc

class MatConcreteACI(MatConcrete):
    """ MatConcreteACI() """
    Fcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fcc(self: MatConcreteACI) -> float

Set: Fcc(self: MatConcreteACI) = value
"""



class MatConcreteAUS(MatConcrete):
    """ MatConcreteAUS() """
    Fcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fcc(self: MatConcreteAUS) -> float

Set: Fcc(self: MatConcreteAUS) = value
"""



class MatConcreteCAN(MatConcrete):
    """ MatConcreteCAN() """
    Fcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fcc(self: MatConcreteCAN) -> float

Set: Fcc(self: MatConcreteCAN) = value
"""



class MatConcreteCHN(MatConcrete):
    """ MatConcreteCHN() """
    Fck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fck(self: MatConcreteCHN) -> float

Set: Fck(self: MatConcreteCHN) = value
"""



class MatConcreteEc2(MatConcrete):
    """ MatConcreteEc2() """
    AggregateType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AggregateType(self: MatConcreteEc2) -> ConcAggregateType

Set: AggregateType(self: MatConcreteEc2) = value
"""

    CalculateDependentValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculateDependentValues(self: MatConcreteEc2) -> bool

Set: CalculateDependentValues(self: MatConcreteEc2) = value
"""

    CementClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CementClass(self: MatConcreteEc2) -> ConcCementClass

Set: CementClass(self: MatConcreteEc2) = value
"""

    DiagramType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagramType(self: MatConcreteEc2) -> ConcDiagramType

Set: DiagramType(self: MatConcreteEc2) = value
"""

    Ecm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ecm(self: MatConcreteEc2) -> float

Set: Ecm(self: MatConcreteEc2) = value
"""

    Epsc1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsc1(self: MatConcreteEc2) -> float

Set: Epsc1(self: MatConcreteEc2) = value
"""

    Epsc2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsc2(self: MatConcreteEc2) -> float

Set: Epsc2(self: MatConcreteEc2) = value
"""

    Epsc3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsc3(self: MatConcreteEc2) -> float

Set: Epsc3(self: MatConcreteEc2) = value
"""

    Epscu1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epscu1(self: MatConcreteEc2) -> float

Set: Epscu1(self: MatConcreteEc2) = value
"""

    Epscu2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epscu2(self: MatConcreteEc2) -> float

Set: Epscu2(self: MatConcreteEc2) = value
"""

    Epscu3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epscu3(self: MatConcreteEc2) -> float

Set: Epscu3(self: MatConcreteEc2) = value
"""

    Fck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fck(self: MatConcreteEc2) -> float

Set: Fck(self: MatConcreteEc2) = value
"""

    Fcm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fcm(self: MatConcreteEc2) -> float

Set: Fcm(self: MatConcreteEc2) = value
"""

    Fctk_0_05 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fctk_0_05(self: MatConcreteEc2) -> float

Set: Fctk_0_05(self: MatConcreteEc2) = value
"""

    Fctk_0_95 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fctk_0_95(self: MatConcreteEc2) -> float

Set: Fctk_0_95(self: MatConcreteEc2) = value
"""

    Fctm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fctm(self: MatConcreteEc2) -> float

Set: Fctm(self: MatConcreteEc2) = value
"""

    NFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NFactor(self: MatConcreteEc2) -> float

Set: NFactor(self: MatConcreteEc2) = value
"""

    PlainConcreteDiagram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlainConcreteDiagram(self: MatConcreteEc2) -> bool

Set: PlainConcreteDiagram(self: MatConcreteEc2) = value
"""

    SilicaFume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SilicaFume(self: MatConcreteEc2) -> bool

Set: SilicaFume(self: MatConcreteEc2) = value
"""

    StoneDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StoneDiameter(self: MatConcreteEc2) -> float

Set: StoneDiameter(self: MatConcreteEc2) = value
"""

    UserDiagram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserDiagram(self: MatConcreteEc2) -> Polygon2D

Set: UserDiagram(self: MatConcreteEc2) = value
"""



class MatConcreteHKG(MatConcrete):
    """ MatConcreteHKG() """
    Epscu2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epscu2(self: MatConcreteHKG) -> float

Set: Epscu2(self: MatConcreteHKG) = value
"""

    Fcu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fcu(self: MatConcreteHKG) -> float

Set: Fcu(self: MatConcreteHKG) = value
"""



class MatConcreteIND(MatConcrete):
    """ MatConcreteIND() """
    Fck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fck(self: MatConcreteIND) -> float

Set: Fck(self: MatConcreteIND) = value
"""



class MatConcreteRUS(MatConcrete):
    """ MatConcreteRUS() """
    Fck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fck(self: MatConcreteRUS) -> float

Set: Fck(self: MatConcreteRUS) = value
"""



class MatConcreteSIA(MatConcrete):
    """ MatConcreteSIA() """
    AggregateType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AggregateType(self: MatConcreteSIA) -> ConcAggregateTypeSIA

Set: AggregateType(self: MatConcreteSIA) = value
"""

    CalculateDependentValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculateDependentValues(self: MatConcreteSIA) -> bool

Set: CalculateDependentValues(self: MatConcreteSIA) = value
"""

    CementClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CementClass(self: MatConcreteSIA) -> ConcCementClassSIA

Set: CementClass(self: MatConcreteSIA) = value
"""

    DiagramType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagramType(self: MatConcreteSIA) -> ConcDiagramType

Set: DiagramType(self: MatConcreteSIA) = value
"""

    Ecm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ecm(self: MatConcreteSIA) -> float

Set: Ecm(self: MatConcreteSIA) = value
"""

    Epsc1d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsc1d(self: MatConcreteSIA) -> float

Set: Epsc1d(self: MatConcreteSIA) = value
"""

    Epsc2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsc2d(self: MatConcreteSIA) -> float

Set: Epsc2d(self: MatConcreteSIA) = value
"""

    Fck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fck(self: MatConcreteSIA) -> float

Set: Fck(self: MatConcreteSIA) = value
"""

    Fcm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fcm(self: MatConcreteSIA) -> float

Set: Fcm(self: MatConcreteSIA) = value
"""

    Fctk_0_05 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fctk_0_05(self: MatConcreteSIA) -> float

Set: Fctk_0_05(self: MatConcreteSIA) = value
"""

    Fctk_0_95 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fctk_0_95(self: MatConcreteSIA) -> float

Set: Fctk_0_95(self: MatConcreteSIA) = value
"""

    Fctm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fctm(self: MatConcreteSIA) -> float

Set: Fctm(self: MatConcreteSIA) = value
"""

    Nfc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nfc(self: MatConcreteSIA) -> float

Set: Nfc(self: MatConcreteSIA) = value
"""

    PlainConcreteDiagram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlainConcreteDiagram(self: MatConcreteSIA) -> bool

Set: PlainConcreteDiagram(self: MatConcreteSIA) = value
"""

    StoneDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StoneDiameter(self: MatConcreteSIA) -> float

Set: StoneDiameter(self: MatConcreteSIA) = value
"""

    Tck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tck(self: MatConcreteSIA) -> float

Set: Tck(self: MatConcreteSIA) = value
"""



class MaterialBoltGrade(Material):
    """ MaterialBoltGrade() """
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: MaterialBoltGrade) -> CountryCode

Set: Code(self: MaterialBoltGrade) = value
"""

    Elongation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elongation(self: MaterialBoltGrade) -> float

Set: Elongation(self: MaterialBoltGrade) = value
"""

    fub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fub(self: MaterialBoltGrade) -> float

Set: fub(self: MaterialBoltGrade) = value
"""

    fyb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fyb(self: MaterialBoltGrade) -> float

Set: fyb(self: MaterialBoltGrade) = value
"""

    MprlElementID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MprlElementID(self: MaterialBoltGrade) -> Guid

Set: MprlElementID(self: MaterialBoltGrade) = value
"""

    MprlTableID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MprlTableID(self: MaterialBoltGrade) -> Guid

Set: MprlTableID(self: MaterialBoltGrade) = value
"""



class MaterialBoltGradeHKG(MaterialBoltGrade):
    """ MaterialBoltGradeHKG() """
    Pbb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pbb(self: MaterialBoltGradeHKG) -> float

Set: Pbb(self: MaterialBoltGradeHKG) = value
"""

    Ps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ps(self: MaterialBoltGradeHKG) -> float

Set: Ps(self: MaterialBoltGradeHKG) = value
"""

    Pt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pt(self: MaterialBoltGradeHKG) -> float

Set: Pt(self: MaterialBoltGradeHKG) = value
"""



class MaterialStrength(OpenObject):
    """ MaterialStrength() """
    Fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fu(self: MaterialStrength) -> float

Set: Fu(self: MaterialStrength) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MaterialStrength) -> float

Set: Fy(self: MaterialStrength) = value
"""

    MaxThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxThickness(self: MaterialStrength) -> float

Set: MaxThickness(self: MaterialStrength) = value
"""



class MaterialStrengthProperty(OpenObject):
    """ MaterialStrengthProperty() """
    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: List(self: MaterialStrengthProperty) -> List[MaterialStrength]

Set: List(self: MaterialStrengthProperty) = value
"""



class MatPrestressSteel(Material):
    # no doc
    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: MatPrestressSteel) -> float

Set: Area(self: MatPrestressSteel) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: MatPrestressSteel) -> float

Set: Diameter(self: MatPrestressSteel) = value
"""

    EquivalentDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EquivalentDiameter(self: MatPrestressSteel) -> float

Set: EquivalentDiameter(self: MatPrestressSteel) = value
"""

    NumberOfWires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfWires(self: MatPrestressSteel) -> int

Set: NumberOfWires(self: MatPrestressSteel) = value
"""



class MatPrestressSteelEc2(MatPrestressSteel):
    """ MatPrestressSteelEc2() """
    Agt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Agt(self: MatPrestressSteelEc2) -> float

Set: Agt(self: MatPrestressSteelEc2) = value
"""

    DiagramType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagramType(self: MatPrestressSteelEc2) -> ReinfDiagramType

Set: DiagramType(self: MatPrestressSteelEc2) = value
"""

    Epsuk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsuk(self: MatPrestressSteelEc2) -> float

Set: Epsuk(self: MatPrestressSteelEc2) = value
"""

    Fm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fm(self: MatPrestressSteelEc2) -> float

Set: Fm(self: MatPrestressSteelEc2) = value
"""

    Fp01 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fp01(self: MatPrestressSteelEc2) -> float

Set: Fp01(self: MatPrestressSteelEc2) = value
"""

    Fp01k = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fp01k(self: MatPrestressSteelEc2) -> float

Set: Fp01k(self: MatPrestressSteelEc2) = value
"""

    Fpk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fpk(self: MatPrestressSteelEc2) -> float

Set: Fpk(self: MatPrestressSteelEc2) = value
"""

    Fr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fr(self: MatPrestressSteelEc2) -> float

Set: Fr(self: MatPrestressSteelEc2) = value
"""

    Production = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Production(self: MatPrestressSteelEc2) -> ProductionType

Set: Production(self: MatPrestressSteelEc2) = value
"""

    SurfaceCharacteristic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceCharacteristic(self: MatPrestressSteelEc2) -> SurfaceCharacteristicType

Set: SurfaceCharacteristic(self: MatPrestressSteelEc2) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: MatPrestressSteelEc2) -> PrestressSteelType

Set: Type(self: MatPrestressSteelEc2) = value
"""



class MatPrestressSteelSIA(MatPrestressSteel):
    """ MatPrestressSteelSIA() """
    DiagramType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagramType(self: MatPrestressSteelSIA) -> ReinfDiagramType

Set: DiagramType(self: MatPrestressSteelSIA) = value
"""

    Epsud = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsud(self: MatPrestressSteelSIA) -> float

Set: Epsud(self: MatPrestressSteelSIA) = value
"""

    Epsuk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsuk(self: MatPrestressSteelSIA) -> float

Set: Epsuk(self: MatPrestressSteelSIA) = value
"""

    Fp01k = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fp01k(self: MatPrestressSteelSIA) -> float

Set: Fp01k(self: MatPrestressSteelSIA) = value
"""

    Fpd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fpd(self: MatPrestressSteelSIA) -> float

Set: Fpd(self: MatPrestressSteelSIA) = value
"""

    Fpk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fpk(self: MatPrestressSteelSIA) -> float

Set: Fpk(self: MatPrestressSteelSIA) = value
"""

    SurfaceCharacteristic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceCharacteristic(self: MatPrestressSteelSIA) -> SurfaceCharacteristicTypeSIA

Set: SurfaceCharacteristic(self: MatPrestressSteelSIA) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: MatPrestressSteelSIA) -> PrestressSteelTypeSIA

Set: Type(self: MatPrestressSteelSIA) = value
"""



class MatReinforcement(Material):
    # no doc
    BarSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarSurface(self: MatReinforcement) -> ReinfBarSurface

Set: BarSurface(self: MatReinforcement) = value
"""



class MatReinforcementACI(MatReinforcement):
    """ MatReinforcementACI() """
    Epssu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epssu(self: MatReinforcementACI) -> float

Set: Epssu(self: MatReinforcementACI) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MatReinforcementACI) -> float

Set: Fy(self: MatReinforcementACI) = value
"""



class MatReinforcementAUS(MatReinforcement):
    """ MatReinforcementAUS() """
    Epssu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epssu(self: MatReinforcementAUS) -> float

Set: Epssu(self: MatReinforcementAUS) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MatReinforcementAUS) -> float

Set: Fy(self: MatReinforcementAUS) = value
"""



class MatReinforcementCAN(MatReinforcement):
    """ MatReinforcementCAN() """
    Epssu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epssu(self: MatReinforcementCAN) -> float

Set: Epssu(self: MatReinforcementCAN) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MatReinforcementCAN) -> float

Set: Fy(self: MatReinforcementCAN) = value
"""



class MatReinforcementCHN(MatReinforcement):
    """ MatReinforcementCHN() """
    Epssu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epssu(self: MatReinforcementCHN) -> float

Set: Epssu(self: MatReinforcementCHN) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MatReinforcementCHN) -> float

Set: Fy(self: MatReinforcementCHN) = value
"""



class MatReinforcementEc2(MatReinforcement):
    """ MatReinforcementEc2() """
    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Class(self: MatReinforcementEc2) -> ReinfClass

Set: Class(self: MatReinforcementEc2) = value
"""

    CoeffFtkByFyk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoeffFtkByFyk(self: MatReinforcementEc2) -> float

Set: CoeffFtkByFyk(self: MatReinforcementEc2) = value
"""

    DiagramType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagramType(self: MatReinforcementEc2) -> ReinfDiagramType

Set: DiagramType(self: MatReinforcementEc2) = value
"""

    Epsuk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epsuk(self: MatReinforcementEc2) -> float

Set: Epsuk(self: MatReinforcementEc2) = value
"""

    Fabrication = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fabrication(self: MatReinforcementEc2) -> ReinfFabrication

Set: Fabrication(self: MatReinforcementEc2) = value
"""

    Ftk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ftk(self: MatReinforcementEc2) -> float

Set: Ftk(self: MatReinforcementEc2) = value
"""

    Fyk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fyk(self: MatReinforcementEc2) -> float

Set: Fyk(self: MatReinforcementEc2) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: MatReinforcementEc2) -> ReinfType

Set: Type(self: MatReinforcementEc2) = value
"""

    UserDiagram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserDiagram(self: MatReinforcementEc2) -> Polygon2D

Set: UserDiagram(self: MatReinforcementEc2) = value
"""



class MatReinforcementHKG(MatReinforcement):
    """ MatReinforcementHKG() """
    Epssu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epssu(self: MatReinforcementHKG) -> float

Set: Epssu(self: MatReinforcementHKG) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MatReinforcementHKG) -> float

Set: Fy(self: MatReinforcementHKG) = value
"""



class MatReinforcementIND(MatReinforcement):
    """ MatReinforcementIND() """
    Epssu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epssu(self: MatReinforcementIND) -> float

Set: Epssu(self: MatReinforcementIND) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MatReinforcementIND) -> float

Set: Fy(self: MatReinforcementIND) = value
"""



class MatReinforcementRUS(MatReinforcement):
    """ MatReinforcementRUS() """
    Epssu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Epssu(self: MatReinforcementRUS) -> float

Set: Epssu(self: MatReinforcementRUS) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: MatReinforcementRUS) -> float

Set: Fy(self: MatReinforcementRUS) = value
"""



class MatSteel(Material):
    # no doc

class MatSteelAISC(MatSteel):
    """ MatSteelAISC() """
    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelAISC) -> float

Set: fu(self: MatSteelAISC) = value
"""

    fu40 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu40(self: MatSteelAISC) -> float

Set: fu40(self: MatSteelAISC) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelAISC) -> float

Set: fy(self: MatSteelAISC) = value
"""

    fy40 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy40(self: MatSteelAISC) -> float

Set: fy40(self: MatSteelAISC) = value
"""



class MatSteelAUS(MatSteel):
    """ MatSteelAUS() """
    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelAUS) -> float

Set: fu(self: MatSteelAUS) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelAUS) -> float

Set: fy(self: MatSteelAUS) = value
"""

    MaterialStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialStrength(self: MatSteelAUS) -> MaterialStrengthProperty

Set: MaterialStrength(self: MatSteelAUS) = value
"""

    PhiOMFu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhiOMFu(self: MatSteelAUS) -> float

Set: PhiOMFu(self: MatSteelAUS) = value
"""

    PhiOMFy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhiOMFy(self: MatSteelAUS) -> float

Set: PhiOMFy(self: MatSteelAUS) = value
"""



class MatSteelCHN(MatSteel):
    """ MatSteelCHN() """
    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelCHN) -> float

Set: fu(self: MatSteelCHN) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelCHN) -> float

Set: fy(self: MatSteelCHN) = value
"""

    MaterialStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialStrength(self: MatSteelCHN) -> MaterialStrengthProperty

Set: MaterialStrength(self: MatSteelCHN) = value
"""

    PhiOMFu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhiOMFu(self: MatSteelCHN) -> float

Set: PhiOMFu(self: MatSteelCHN) = value
"""

    PhiOMFy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhiOMFy(self: MatSteelCHN) -> float

Set: PhiOMFy(self: MatSteelCHN) = value
"""



class MatSteelCISC(MatSteel):
    """ MatSteelCISC() """
    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelCISC) -> float

Set: fu(self: MatSteelCISC) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelCISC) -> float

Set: fy(self: MatSteelCISC) = value
"""



class MatSteelEc2(MatSteel):
    """ MatSteelEc2() """
    DiagramType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagramType(self: MatSteelEc2) -> SteelDiagramType

Set: DiagramType(self: MatSteelEc2) = value
"""

    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelEc2) -> float

Set: fu(self: MatSteelEc2) = value
"""

    fu40 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu40(self: MatSteelEc2) -> float

Set: fu40(self: MatSteelEc2) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelEc2) -> float

Set: fy(self: MatSteelEc2) = value
"""

    fy40 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy40(self: MatSteelEc2) -> float

Set: fy40(self: MatSteelEc2) = value
"""

    MaterialStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialStrength(self: MatSteelEc2) -> MaterialStrengthProperty

Set: MaterialStrength(self: MatSteelEc2) = value
"""

    UserDiagram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserDiagram(self: MatSteelEc2) -> Polygon2D

Set: UserDiagram(self: MatSteelEc2) = value
"""



class MatSteelHKG(MatSteel):
    """ MatSteelHKG() """
    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelHKG) -> float

Set: fu(self: MatSteelHKG) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelHKG) -> float

Set: fy(self: MatSteelHKG) = value
"""

    GammaOVfu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaOVfu(self: MatSteelHKG) -> float

Set: GammaOVfu(self: MatSteelHKG) = value
"""

    GammaOVfy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaOVfy(self: MatSteelHKG) -> float

Set: GammaOVfy(self: MatSteelHKG) = value
"""

    MaterialStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialStrength(self: MatSteelHKG) -> MaterialStrengthProperty

Set: MaterialStrength(self: MatSteelHKG) = value
"""



class MatSteelIND(MatSteel):
    """ MatSteelIND() """
    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelIND) -> float

Set: fu(self: MatSteelIND) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelIND) -> float

Set: fy(self: MatSteelIND) = value
"""

    GammaOVfu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaOVfu(self: MatSteelIND) -> float

Set: GammaOVfu(self: MatSteelIND) = value
"""

    GammaOVfy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaOVfy(self: MatSteelIND) -> float

Set: GammaOVfy(self: MatSteelIND) = value
"""

    MaterialStrength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialStrength(self: MatSteelIND) -> MaterialStrengthProperty

Set: MaterialStrength(self: MatSteelIND) = value
"""



class MatSteelRUS(MatSteel):
    """ MatSteelRUS() """
    fu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fu(self: MatSteelRUS) -> float

Set: fu(self: MatSteelRUS) = value
"""

    fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: fy(self: MatSteelRUS) -> float

Set: fy(self: MatSteelRUS) = value
"""

    GammaM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaM(self: MatSteelRUS) -> float

Set: GammaM(self: MatSteelRUS) = value
"""



class PrestressSteelType(Enum, IComparable, IFormattable, IConvertible):
    """ enum PrestressSteelType, values: CompactedStrand (5), IndentedWire (1), PlainRoundBar (3), PlainRoundWire (0), RibbedBar (4), Strand (2) """
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

    CompactedStrand = None
    IndentedWire = None
    PlainRoundBar = None
    PlainRoundWire = None
    RibbedBar = None
    Strand = None
    value__ = None


class PrestressSteelTypeSIA(Enum, IComparable, IFormattable, IConvertible):
    """ enum PrestressSteelTypeSIA, values: Bar (2), Strand (1), Wire (0) """
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

    Bar = None
    Strand = None
    value__ = None
    Wire = None


class ProductionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ProductionType, values: ColdDrawn (2), HotRolledAndProcessed (0), LowRelaxation (4), Patented (1), StressRelieved (3) """
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

    ColdDrawn = None
    HotRolledAndProcessed = None
    LowRelaxation = None
    Patented = None
    StressRelieved = None
    value__ = None


class ReinfBarSurface(Enum, IComparable, IFormattable, IConvertible):
    """ enum ReinfBarSurface, values: Ribbed (1), Smooth (0) """
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

    Ribbed = None
    Smooth = None
    value__ = None


class ReinfClass(Enum, IComparable, IFormattable, IConvertible):
    """ enum ReinfClass, values: A (0), B (1), C (2) """
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

    A = None
    B = None
    C = None
    value__ = None


class ReinfDiagramType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ReinfDiagramType, values: BilinerWithAnInclinedTopBranch (0), BilinerWithOutAnInclinedTopBranch (1), DefinedByUser (2) """
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

    BilinerWithAnInclinedTopBranch = None
    BilinerWithOutAnInclinedTopBranch = None
    DefinedByUser = None
    value__ = None


class ReinfFabrication(Enum, IComparable, IFormattable, IConvertible):
    """ enum ReinfFabrication, values: ColdWorked (1), HotRolled (0) """
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

    ColdWorked = None
    HotRolled = None
    value__ = None


class ReinfFireDiagramType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ReinfFireDiagramType, values: FireBilinerWithAnInclinedTopBranch (0), FireBilinerWithOutAnInclinedTopBranch (1) """
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

    FireBilinerWithAnInclinedTopBranch = None
    FireBilinerWithOutAnInclinedTopBranch = None
    value__ = None


class ReinfType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ReinfType, values: Bars (0), DecoiledRods (1), LatticeGirders (3), WireFabrics (2) """
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

    Bars = None
    DecoiledRods = None
    LatticeGirders = None
    value__ = None
    WireFabrics = None


class SteelDiagramType(Enum, IComparable, IFormattable, IConvertible):
    """ enum SteelDiagramType, values: Bilinear (0), DefinedByUser (5) """
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

    Bilinear = None
    DefinedByUser = None
    value__ = None


class SurfaceCharacteristicType(Enum, IComparable, IFormattable, IConvertible):
    """ enum SurfaceCharacteristicType, values: Indented (1), Plain (0), Ribbed (2) """
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

    Indented = None
    Plain = None
    Ribbed = None
    value__ = None


class SurfaceCharacteristicTypeSIA(Enum, IComparable, IFormattable, IConvertible):
    """ enum SurfaceCharacteristicTypeSIA, values: Indented (1), Plain (0), Ribbed (2) """
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

    Indented = None
    Plain = None
    Ribbed = None
    value__ = None


class ThermalConductivityState(Enum, IComparable, IFormattable, IConvertible):
    """ enum ThermalConductivityState, values: Code (1), None (0), User (5) """
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

    Code = None
    None = None
    User = None
    value__ = None


class ThermalExpansionState(Enum, IComparable, IFormattable, IConvertible):
    """ enum ThermalExpansionState, values: Code (1), None (0), User (5) """
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

    Code = None
    None = None
    User = None
    value__ = None


class ThermalSpecificHeatState(Enum, IComparable, IFormattable, IConvertible):
    """ enum ThermalSpecificHeatState, values: Code (1), None (0), User (5) """
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

    Code = None
    None = None
    User = None
    value__ = None


class ThermalStrainState(Enum, IComparable, IFormattable, IConvertible):
    """ enum ThermalStrainState, values: Code (1), None (0), User (5) """
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

    Code = None
    None = None
    User = None
    value__ = None


class ThermalStressStrainState(Enum, IComparable, IFormattable, IConvertible):
    """ enum ThermalStressStrainState, values: Code (1), None (0), User (5) """
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

    Code = None
    None = None
    User = None
    value__ = None


