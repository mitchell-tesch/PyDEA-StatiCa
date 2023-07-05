# encoding: utf-8
# module IdeaRS.OpenModel.Concrete calls itself Concrete
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BeamDataEc2(object):
    """ BeamDataEc2() """
    BeamSpanLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamSpanLength(self: BeamDataEc2) -> float

Set: BeamSpanLength(self: BeamDataEc2) = value
"""

    CheckLimitDeflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckLimitDeflection(self: BeamDataEc2) -> bool

Set: CheckLimitDeflection(self: BeamDataEc2) = value
"""

    CheckLimitDeflRheoEffects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckLimitDeflRheoEffects(self: BeamDataEc2) -> bool

Set: CheckLimitDeflRheoEffects(self: BeamDataEc2) = value
"""

    DeflectionSheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeflectionSheme(self: BeamDataEc2) -> TypeDeflectionSheme

Set: DeflectionSheme(self: BeamDataEc2) = value
"""

    IsAbsValueLimitDeflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbsValueLimitDeflection(self: BeamDataEc2) -> bool

Set: IsAbsValueLimitDeflection(self: BeamDataEc2) = value
"""

    IsUserLimitDeflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserLimitDeflection(self: BeamDataEc2) -> bool

Set: IsUserLimitDeflection(self: BeamDataEc2) = value
"""

    IsYDirectionData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsYDirectionData(self: BeamDataEc2) -> bool

Set: IsYDirectionData(self: BeamDataEc2) = value
"""

    Ln = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ln(self: BeamDataEc2) -> float

Set: Ln(self: BeamDataEc2) = value
"""

    RequiredCamber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequiredCamber(self: BeamDataEc2) -> float

Set: RequiredCamber(self: BeamDataEc2) = value
"""

    TypeOfCalculation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeOfCalculation(self: BeamDataEc2) -> TypeOfCalculationDeflection

Set: TypeOfCalculation(self: BeamDataEc2) = value
"""

    TypeOfSupportLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeOfSupportLeft(self: BeamDataEc2) -> TypeOfSupportConditions

Set: TypeOfSupportLeft(self: BeamDataEc2) = value
"""

    TypeOfSupportRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeOfSupportRight(self: BeamDataEc2) -> TypeOfSupportConditions

Set: TypeOfSupportRight(self: BeamDataEc2) = value
"""

    UserLimitDeflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserLimitDeflection(self: BeamDataEc2) -> float

Set: UserLimitDeflection(self: BeamDataEc2) = value
"""

    UserLimitDeflRheoEffects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserLimitDeflRheoEffects(self: BeamDataEc2) -> float

Set: UserLimitDeflRheoEffects(self: BeamDataEc2) = value
"""

    WidthOfSupportLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WidthOfSupportLeft(self: BeamDataEc2) -> float

Set: WidthOfSupportLeft(self: BeamDataEc2) = value
"""

    WidthOfSupportRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WidthOfSupportRight(self: BeamDataEc2) -> float

Set: WidthOfSupportRight(self: BeamDataEc2) = value
"""



class CalculationSetup(OpenObject):
    """ CalculationSetup() """
    CrossSectionCharacteristics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionCharacteristics(self: CalculationSetup) -> bool

Set: CrossSectionCharacteristics(self: CalculationSetup) = value
"""

    Detailing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Detailing(self: CalculationSetup) -> bool

Set: Detailing(self: CalculationSetup) = value
"""

    Fatigue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fatigue(self: CalculationSetup) -> bool

Set: Fatigue(self: CalculationSetup) = value
"""

    MNKappaDiagram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MNKappaDiagram(self: CalculationSetup) -> bool

Set: MNKappaDiagram(self: CalculationSetup) = value
"""

    SlsCrack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlsCrack(self: CalculationSetup) -> bool

Set: SlsCrack(self: CalculationSetup) = value
"""

    SlsDeflections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlsDeflections(self: CalculationSetup) -> bool

Set: SlsDeflections(self: CalculationSetup) = value
"""

    SlsStiffnesses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlsStiffnesses(self: CalculationSetup) -> bool

Set: SlsStiffnesses(self: CalculationSetup) = value
"""

    SlsStressLimitation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlsStressLimitation(self: CalculationSetup) -> bool

Set: SlsStressLimitation(self: CalculationSetup) = value
"""

    UlsDiagram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UlsDiagram(self: CalculationSetup) -> bool

Set: UlsDiagram(self: CalculationSetup) = value
"""

    UlsInteraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UlsInteraction(self: CalculationSetup) -> bool

Set: UlsInteraction(self: CalculationSetup) = value
"""

    UlsResponse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UlsResponse(self: CalculationSetup) -> bool

Set: UlsResponse(self: CalculationSetup) = value
"""

    UlsShear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UlsShear(self: CalculationSetup) -> bool

Set: UlsShear(self: CalculationSetup) = value
"""

    UlsTorsion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UlsTorsion(self: CalculationSetup) -> bool

Set: UlsTorsion(self: CalculationSetup) = value
"""



class CheckSection(OpenElementId):
    # no doc
    CheckMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckMember(self: CheckSection) -> ReferenceElement

Set: CheckMember(self: CheckSection) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: CheckSection) -> str

Set: Description(self: CheckSection) = value
"""

    Extremes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extremes(self: CheckSection) -> List[CheckSectionExtreme]

Set: Extremes(self: CheckSection) = value
"""

    ReinfSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReinfSection(self: CheckSection) -> ReferenceElement

Set: ReinfSection(self: CheckSection) = value
"""



class CheckSectionExtreme(object):
    # no doc
    Accidental = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Accidental(self: CheckSectionExtreme) -> LoadingULS

Set: Accidental(self: CheckSectionExtreme) = value
"""

    Characteristic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Characteristic(self: CheckSectionExtreme) -> LoadingSLS

Set: Characteristic(self: CheckSectionExtreme) = value
"""

    Fatigue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fatigue(self: CheckSectionExtreme) -> FatigueLoading

Set: Fatigue(self: CheckSectionExtreme) = value
"""

    Frequent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Frequent(self: CheckSectionExtreme) -> LoadingSLS

Set: Frequent(self: CheckSectionExtreme) = value
"""

    Fundamental = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fundamental(self: CheckSectionExtreme) -> LoadingULS

Set: Fundamental(self: CheckSectionExtreme) = value
"""

    QuasiPermanent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuasiPermanent(self: CheckSectionExtreme) -> LoadingSLS

Set: QuasiPermanent(self: CheckSectionExtreme) = value
"""



class ColumnData(object):
    """ ColumnData() """
    CalculateY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculateY(self: ColumnData) -> bool

Set: CalculateY(self: ColumnData) = value
"""

    CalculateZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculateZ(self: ColumnData) -> bool

Set: CalculateZ(self: ColumnData) = value
"""

    EffectiveLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveLength(self: ColumnData) -> InputValue

Set: EffectiveLength(self: ColumnData) = value
"""

    FemL0Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FemL0Y(self: ColumnData) -> float

Set: FemL0Y(self: ColumnData) = value
"""

    FemL0Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FemL0Z(self: ColumnData) -> float

Set: FemL0Z(self: ColumnData) = value
"""

    FemLenghtFromFlexibleSupport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FemLenghtFromFlexibleSupport(self: ColumnData) -> bool

Set: FemLenghtFromFlexibleSupport(self: ColumnData) = value
"""

    ImperfectionDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImperfectionDirection(self: ColumnData) -> ImperfectionDirection

Set: ImperfectionDirection(self: ColumnData) = value
"""

    ImperfectionsInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImperfectionsInput(self: ColumnData) -> InputValue

Set: ImperfectionsInput(self: ColumnData) = value
"""

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: L(self: ColumnData) -> float

Set: L(self: ColumnData) = value
"""

    L0Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: L0Y(self: ColumnData) -> float

Set: L0Y(self: ColumnData) = value
"""

    L0Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: L0Z(self: ColumnData) -> float

Set: L0Z(self: ColumnData) = value
"""

    SecondOrderEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondOrderEffectInput(self: ColumnData) -> InputValue

Set: SecondOrderEffectInput(self: ColumnData) = value
"""

    SupportBottomY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportBottomY(self: ColumnData) -> SupportType

Set: SupportBottomY(self: ColumnData) = value
"""

    SupportBottomZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportBottomZ(self: ColumnData) -> SupportType

Set: SupportBottomZ(self: ColumnData) = value
"""

    SupportTopY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTopY(self: ColumnData) -> SupportType

Set: SupportTopY(self: ColumnData) = value
"""

    SupportTopZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTopZ(self: ColumnData) -> SupportType

Set: SupportTopZ(self: ColumnData) = value
"""



class ColumnDataEc2(ColumnData):
    """ ColumnDataEc2() """
    BracedY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BracedY(self: ColumnDataEc2) -> bool

Set: BracedY(self: ColumnDataEc2) = value
"""

    BracedZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BracedZ(self: ColumnDataEc2) -> bool

Set: BracedZ(self: ColumnDataEc2) = value
"""

    Calculation2ndOrderEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Calculation2ndOrderEffect(self: ColumnDataEc2) -> bool

Set: Calculation2ndOrderEffect(self: ColumnDataEc2) = value
"""

    EffectConsidered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectConsidered(self: ColumnDataEc2) -> EffectConsideredType

Set: EffectConsidered(self: ColumnDataEc2) = value
"""

    GeometricImperfectionsSLS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometricImperfectionsSLS(self: ColumnDataEc2) -> bool

Set: GeometricImperfectionsSLS(self: ColumnDataEc2) = value
"""

    GeometricImperfectionsULS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometricImperfectionsULS(self: ColumnDataEc2) -> bool

Set: GeometricImperfectionsULS(self: ColumnDataEc2) = value
"""

    NumberOfVerticalMembersY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfVerticalMembersY(self: ColumnDataEc2) -> int

Set: NumberOfVerticalMembersY(self: ColumnDataEc2) = value
"""

    NumberOfVerticalMembersZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfVerticalMembersZ(self: ColumnDataEc2) -> int

Set: NumberOfVerticalMembersZ(self: ColumnDataEc2) = value
"""

    SecondOrderEffectMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondOrderEffectMethod(self: ColumnDataEc2) -> SecondOrderEffectMethodEc2

Set: SecondOrderEffectMethod(self: ColumnDataEc2) = value
"""

    TotalL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalL(self: ColumnDataEc2) -> float

Set: TotalL(self: ColumnDataEc2) = value
"""

    UserValuec0Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserValuec0Y(self: ColumnDataEc2) -> float

Set: UserValuec0Y(self: ColumnDataEc2) = value
"""

    UserValuec0Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserValuec0Z(self: ColumnDataEc2) -> float

Set: UserValuec0Z(self: ColumnDataEc2) = value
"""

    UserValuecY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserValuecY(self: ColumnDataEc2) -> float

Set: UserValuecY(self: ColumnDataEc2) = value
"""

    UserValuecZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserValuecZ(self: ColumnDataEc2) -> float

Set: UserValuecZ(self: ColumnDataEc2) = value
"""

    ValueTypeOfc0Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueTypeOfc0Y(self: ColumnDataEc2) -> ValueTypec0

Set: ValueTypeOfc0Y(self: ColumnDataEc2) = value
"""

    ValueTypeOfc0Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueTypeOfc0Z(self: ColumnDataEc2) -> ValueTypec0

Set: ValueTypeOfc0Z(self: ColumnDataEc2) = value
"""

    ValueTypeOfcY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueTypeOfcY(self: ColumnDataEc2) -> ValueTypec

Set: ValueTypeOfcY(self: ColumnDataEc2) = value
"""

    ValueTypeOfcZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueTypeOfcZ(self: ColumnDataEc2) -> ValueTypec

Set: ValueTypeOfcZ(self: ColumnDataEc2) = value
"""



class ConcreteMemberData(OpenAttribute):
    """ ConcreteMemberData() """
    CalculationSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculationSetup(self: ConcreteMemberData) -> CalculationSetup

Set: CalculationSetup(self: ConcreteMemberData) = value
"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: ConcreteMemberData) -> ConcreteMemberType

Set: MemberType(self: ConcreteMemberData) = value
"""

    TimeAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeAxis(self: ConcreteMemberData) -> TimeAxis

Set: TimeAxis(self: ConcreteMemberData) = value
"""

    TwoWaySlabType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TwoWaySlabType(self: ConcreteMemberData) -> TwoWaySlabType

Set: TwoWaySlabType(self: ConcreteMemberData) = value
"""



class ConcreteMemberDataEc2(ConcreteMemberData):
    """ ConcreteMemberDataEc2() """
    BeamData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamData(self: ConcreteMemberDataEc2) -> BeamDataEc2

Set: BeamData(self: ConcreteMemberDataEc2) = value
"""

    CoeffKxForWmax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoeffKxForWmax(self: ConcreteMemberDataEc2) -> float

Set: CoeffKxForWmax(self: ConcreteMemberDataEc2) = value
"""

    ColumnData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnData(self: ConcreteMemberDataEc2) -> ColumnDataEc2

Set: ColumnData(self: ConcreteMemberDataEc2) = value
"""

    CreepCoeffInfinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreepCoeffInfinity(self: ConcreteMemberDataEc2) -> float

Set: CreepCoeffInfinity(self: ConcreteMemberDataEc2) = value
"""

    CreepCoeffInfinityValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreepCoeffInfinityValue(self: ConcreteMemberDataEc2) -> InputValue

Set: CreepCoeffInfinityValue(self: ConcreteMemberDataEc2) = value
"""

    DeflectionRequirement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeflectionRequirement(self: ConcreteMemberDataEc2) -> DeflectionRequirementEc2

Set: DeflectionRequirement(self: ConcreteMemberDataEc2) = value
"""

    ExposureClassesData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExposureClassesData(self: ConcreteMemberDataEc2) -> ExposureClassesDataEc2

Set: ExposureClassesData(self: ConcreteMemberDataEc2) = value
"""

    MemberImportance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberImportance(self: ConcreteMemberDataEc2) -> MemberImportance

Set: MemberImportance(self: ConcreteMemberDataEc2) = value
"""

    RelativeHumidity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeHumidity(self: ConcreteMemberDataEc2) -> float

Set: RelativeHumidity(self: ConcreteMemberDataEc2) = value
"""



class ConcreteMemberType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConcreteMemberType, values: Beam (1), BeamSlab (4), Column (2), HollowCoreSlab (8), NoDefined (0), Plate (32), TwoWaySlab (16), Wall (64) """
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

    Beam = None
    BeamSlab = None
    Column = None
    HollowCoreSlab = None
    NoDefined = None
    Plate = None
    TwoWaySlab = None
    value__ = None
    Wall = None


class ConcreteSetup(OpenElementId):
    # no doc
    SetupValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetupValues(self: ConcreteSetup) -> List[SetupValue]

Set: SetupValues(self: ConcreteSetup) = value
"""



class ConcreteSetupEc2(ConcreteSetup):
    """ ConcreteSetupEc2() """
    Annex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Annex(self: ConcreteSetupEc2) -> NationalAnnexCode

Set: Annex(self: ConcreteSetupEc2) = value
"""

    Nad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nad(self: ConcreteSetupEc2) -> NadStrategyConcrete

Set: Nad(self: ConcreteSetupEc2) = value
"""



class DeflectionRequirementEc2(Enum, IComparable, IFormattable, IConvertible):
    """ enum DeflectionRequirementEc2, values: Advanced (1), Normal (0) """
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

    Advanced = None
    Normal = None
    value__ = None


class EffectConsideredType(Enum, IComparable, IFormattable, IConvertible):
    """ enum EffectConsideredType, values: BracingSystem (1), IsolatedMember (0) """
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

    BracingSystem = None
    IsolatedMember = None
    value__ = None


class ExposureClassEc2(Enum, IComparable, IFormattable, IConvertible):
    """ enum ExposureClassEc2, values: X0 (0), XA1 (15), XA2 (16), XA3 (17), XC1 (1), XC2 (2), XC3 (3), XC4 (4), XD1 (5), XD2 (6), XD3 (7), XF1 (11), XF2 (12), XF3 (13), XF4 (14), XS1 (8), XS2 (9), XS3 (10) """
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

    value__ = None
    X0 = None
    XA1 = None
    XA2 = None
    XA3 = None
    XC1 = None
    XC2 = None
    XC3 = None
    XC4 = None
    XD1 = None
    XD2 = None
    XD3 = None
    XF1 = None
    XF2 = None
    XF3 = None
    XF4 = None
    XS1 = None
    XS2 = None
    XS3 = None


class ExposureClassesDataEc2(object):
    """ ExposureClassesDataEc2() """
    Carbonation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Carbonation(self: ExposureClassesDataEc2) -> ExposureClassEc2

Set: Carbonation(self: ExposureClassesDataEc2) = value
"""

    CarbonationCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CarbonationCheck(self: ExposureClassesDataEc2) -> bool

Set: CarbonationCheck(self: ExposureClassesDataEc2) = value
"""

    ChemicalAttack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChemicalAttack(self: ExposureClassesDataEc2) -> ExposureClassEc2

Set: ChemicalAttack(self: ExposureClassesDataEc2) = value
"""

    ChemicalAttackCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChemicalAttackCheck(self: ExposureClassesDataEc2) -> bool

Set: ChemicalAttackCheck(self: ExposureClassesDataEc2) = value
"""

    Chlorides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chlorides(self: ExposureClassesDataEc2) -> ExposureClassEc2

Set: Chlorides(self: ExposureClassesDataEc2) = value
"""

    ChloridesCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChloridesCheck(self: ExposureClassesDataEc2) -> bool

Set: ChloridesCheck(self: ExposureClassesDataEc2) = value
"""

    ChloridesFromSea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChloridesFromSea(self: ExposureClassesDataEc2) -> ExposureClassEc2

Set: ChloridesFromSea(self: ExposureClassesDataEc2) = value
"""

    ChloridesFromSeaCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChloridesFromSeaCheck(self: ExposureClassesDataEc2) -> bool

Set: ChloridesFromSeaCheck(self: ExposureClassesDataEc2) = value
"""

    FreezeAttack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FreezeAttack(self: ExposureClassesDataEc2) -> ExposureClassEc2

Set: FreezeAttack(self: ExposureClassesDataEc2) = value
"""

    FreezeAttackCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FreezeAttackCheck(self: ExposureClassesDataEc2) -> bool

Set: FreezeAttackCheck(self: ExposureClassesDataEc2) = value
"""

    NoCorrosionCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NoCorrosionCheck(self: ExposureClassesDataEc2) -> bool

Set: NoCorrosionCheck(self: ExposureClassesDataEc2) = value
"""



class ImperfectionDirection(Enum, IComparable, IFormattable, IConvertible):
    """ enum ImperfectionDirection, values: BiggerSlenderner (1), Both (3), BothDirections (0), FromSetup (4), MomentResultant (2) """
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

    BiggerSlenderner = None
    Both = None
    BothDirections = None
    FromSetup = None
    MomentResultant = None
    value__ = None


class InputValue(Enum, IComparable, IFormattable, IConvertible):
    """ enum InputValue, values: Calculated (0), CalculatedFEM (2), UserInput (1) """
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

    Calculated = None
    CalculatedFEM = None
    UserInput = None
    value__ = None


class MemberImportance(Enum, IComparable, IFormattable, IConvertible):
    """ enum MemberImportance, values: Major (0), Minor (1) """
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

    Major = None
    Minor = None
    value__ = None


class NadSetupValue(object):
    # no doc
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: NadSetupValue) -> int

Set: Id(self: NadSetupValue) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: NadSetupValue) -> bool

Set: IsActive(self: NadSetupValue) = value
"""



class NadSetupValueBool(NadSetupValue):
    """ NadSetupValueBool() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NadSetupValueBool) -> bool

Set: Value(self: NadSetupValueBool) = value
"""



class NadSetupValueDouble(NadSetupValue):
    """ NadSetupValueDouble() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NadSetupValueDouble) -> float

Set: Value(self: NadSetupValueDouble) = value
"""



class NadSetupValueFloat(NadSetupValue):
    """ NadSetupValueFloat() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NadSetupValueFloat) -> Single

Set: Value(self: NadSetupValueFloat) = value
"""



class NadSetupValueInt(NadSetupValue):
    """ NadSetupValueInt() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NadSetupValueInt) -> int

Set: Value(self: NadSetupValueInt) = value
"""



class NadSetupValueLong(NadSetupValue):
    """ NadSetupValueLong() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NadSetupValueLong) -> Int64

Set: Value(self: NadSetupValueLong) = value
"""



class NadSetupValueShort(NadSetupValue):
    """ NadSetupValueShort() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NadSetupValueShort) -> Int16

Set: Value(self: NadSetupValueShort) = value
"""



class NadStrategyConcrete(object):
    # no doc
    SetupValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetupValues(self: NadStrategyConcrete) -> List[NadSetupValue]

Set: SetupValues(self: NadStrategyConcrete) = value
"""



class NationalAnnexCode(Enum, IComparable, IFormattable, IConvertible):
    """ enum NationalAnnexCode, values: Austrian (3), Belgian (6), British (8), Czech (1), Dutch (5), French (7), German (4), NoAnnex (0), Polish (10), Singapore (9), Slovak (2) """
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

    Austrian = None
    Belgian = None
    British = None
    Czech = None
    Dutch = None
    French = None
    German = None
    NoAnnex = None
    Polish = None
    Singapore = None
    Slovak = None
    value__ = None


class ProjectDataConcrete(OpenObject):
    """ ProjectDataConcrete() """
    DesignWorkingLife = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignWorkingLife(self: ProjectDataConcrete) -> int

Set: DesignWorkingLife(self: ProjectDataConcrete) = value
"""



class ProjectDataConcreteEc2(ProjectDataConcrete):
    """ ProjectDataConcreteEc2() """
    CodeEN1992_2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeEN1992_2(self: ProjectDataConcreteEc2) -> bool

Set: CodeEN1992_2(self: ProjectDataConcreteEc2) = value
"""

    CodeEN1992_3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeEN1992_3(self: ProjectDataConcreteEc2) -> bool

Set: CodeEN1992_3(self: ProjectDataConcreteEc2) = value
"""



class SecondOrderEffectMethodEc2(Enum, IComparable, IFormattable, IConvertible):
    """ enum SecondOrderEffectMethodEc2, values: NominalCurvature (1), NominalStiffness (0) """
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

    NominalCurvature = None
    NominalStiffness = None
    value__ = None


class SetupValue(object):
    # no doc
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: SetupValue) -> int

Set: Id(self: SetupValue) = value
"""



class SetupValueBool(SetupValue):
    """ SetupValueBool() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: SetupValueBool) -> bool

Set: Value(self: SetupValueBool) = value
"""



class SetupValueDouble(SetupValue):
    """ SetupValueDouble() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: SetupValueDouble) -> float

Set: Value(self: SetupValueDouble) = value
"""



class SetupValueEc2(Enum, IComparable, IFormattable, IConvertible):
    """ enum SetupValueEc2, values: AllowCheckInAgeLess3Days (152), AlphaCw (32), AnchorageDetailType (122), BentUpBarsReduction (154), BLRPRecisionCheckValue (201), CalculateShrinkage (205), CalculateSrMaxAccUserSettings (135), CalculationOfStressLimitationK1 (207), CalculationOfStressLimitationK2 (208), CalculationOfStressLimitationK3 (209), CheckCrackedCss (74), CheckCrossSectionCrackedIfOneCracked_7_2_Chapter (102), CoeffCrdc (28), CoefficientOfTensionConcrete (195), CoeffK1 (29), CoeffKl (49), CoeffKp (33), CoeffNi (104), CoeffNi1 (31), CoeffNi1_EN2_2 (183), CoeffVmin (30), CracksPassThrough (159), CracWidthNationalAnnex (160), CrossSectionCrackedPlate (134), DecompressionLimit (77), DecompressionLimit_2 (78), DecompressionLimit_3 (167), DetailingBracketMethodType (120), DivisionStrain (70), EndOfCuring (71), Equation629 (171), Equation631 (172), FatigueJointCohesion (175), FatigueMethod (133), FindOnly2DPlaneDeformation (196), HighStrengthConcrete (163), ImperfectionDirection (110), IncreaseJointResistance (170), InnerPerimeter (164), InteractionDiagramCheckType (9), InteractionDiagramDivision (112), InteractionDiagramExportType (146), InterpolationCurve (111), IsSetMrForULSMNKappaDiagram (156), IsSetPrecissionForNullForces (147), IterationPrecission (7), IterationSteps (8), JointShearStressType (138), LimitCheckValue (0), LimitDeflectionAdvanced (106), LimitDeflectionNormal (105), LimitDeflectionValue (108), LimitLeverArm (165), LinearStiffnessForDeflection (109), MaxBentUpReinfDist (178), MaxDisplayCheckValue (1), MaxHorReinfDistWall (83), MaxHorReinfDistWall_EN2_2 (188), MaxLengthOfZone (107), MaxLongReinfDist (37), MaxLongReinfPercBeam (35), MaxLongReinfPercBeam_EN2_2 (185), MaxLongReinfPercColumn (43), MaxMainReinfDistSlab (89), MaxMainReinfDistSlab_EN2_2 (186), MaxMainReinfPercSlab (87), MaxReinfDistDeepBeam (85), MaxShearReinfDistBeam (40), MaxShearReinfDistColumn (46), MaxShearReinfDistSlab (180), MaxShearReinfPercBeam (39), MaxShearReinfTransDist (41), MaxShearReinfTransDistSlab (181), MaxTransReinfDistSlab (90), MaxTransReinfDistSlab_EN2_2 (187), MaxVertReinfDistWall (81), MaxVertReinfPercWall (80), MinAnchLenShear (121), MinDuctHorDist (97), MinDuctVertDist (96), MinHorReinfPercWall (82), MinLongReinfDiamColumn (44), MinLongReinfDist (36), MinLongReinfPercBeam (34), MinLongReinfPercBeam_EN2_2 (184), MinLongReinfPercColumn (42), MinMainReinfPercSlab (86), MinNoBarCircColumn (45), MinReinfPercDeepBeam (84), MinReinfPercDeepBeam_EN2_2 (189), MinShearReinfDiamColumn (47), MinShearReinfDiamColumn_EN2_2 (182), MinShearReinfPercBeam (38), MinShearReinfPercSlab (179), MinTendonHorDist (95), MinTendonVertDist (94), MinTransReinfPercSlab (88), MinVertReinfPercWall (79), ModulusType (61), ModulusTypeLongTermEffects (137), NA_1_Wmax_Ec2 (150), NA_2_4_2_2_Gamma_p_fav (66), NA_2_4_2_2_Gamma_p_unfav (67), NA_5_10_2_1_1_K1 (98), NA_5_10_2_1_1_K2 (99), NA_5_10_3_2_K7 (100), NA_5_10_3_2_K8 (101), NA_5_10_9_r_inf_post (65), NA_5_10_9_r_inf_pre (63), NA_5_10_9_r_sup_post (64), NA_5_10_9_r_sup_pre (62), NA_5_2_5_Theta0 (55), NA_5_5_K1 (140), NA_5_5_K2 (141), NA_5_5_K3 (142), NA_5_5_K4 (143), NA_5_5_K5 (144), NA_5_5_K5_fck_BiggerThan_50MPa (190), NA_5_5_K6 (145), NA_5_5_K6_fck_BiggerThan_50MPa (191), NA_5_8_6_3_GammaCe (56), NA_6_5_2_3_Ni (113), NA_6_5_4_4_K1 (114), NA_6_5_4_4_K2 (115), NA_6_5_4_4_K3 (116), NA_7_2_K1 (11), NA_7_2_K2 (12), NA_7_2_K3 (13), NA_7_2_K4 (14), NA_7_2_K5 (15), NA_7_3_1_DecompressionDistance (68), NA_7_3_1_Wmax_Ec2_1_1 (10), NA_7_3_1_Wmax_Ec2_2 (73), NA_7_3_4_K1 (192), NA_7_3_4_K2 (193), NA_7_3_4_K3 (16), NA_7_3_4_K4 (17), NA_8_3_2_MinDiameterOfMandrel (103), NA_Alphacc_92_1_1 (19), NA_Alphacc_92_2 (23), NA_Alphaccpl_92_1_1 (21), NA_Alphact_92_1_1 (20), NA_Alphact_92_2 (24), NA_Alphactpl_92_1_1 (22), NA_CoeffEpsudByEpsuk (5), NA_CoeffEpsudByEpsuk_p (6), NA_EN1992_3_7_3_1_112_x_min (157), NA_EN1992_3_CrackWidth (158), NA_EN1992_3_CrackWidth_XA2_XA3_XF2_XF3_XF4 (206), NA_GammaC (2), NA_GammaC_BLR (198), NA_GammaCfat (124), NA_GammaFfat (123), NA_GammaS (3), NA_GammaS_BLR (199), NA_GammaSfat (125), NA_GammaSP (4), NA_GammaSP_BLR (200), NA_GammaSPfat (126), NA_J_3_2_K1 (117), NA_J_3_3_K2 (118), NA_k_p (57), NA_K1Fatigue (131), NA_K2Fatigue (166), NA_LimitCharacteristic (92), NA_LimitInfrequent (93), NA_LimitQuasiPermanent (91), NA_LoadDuration (18), NA_NCyclesFatigue (130), NA_NN_112_Gamma_sd (194), NA_Table7_101DE_1992_2 (173), NA_Table7_102DE_1992_2 (174), NA_Table7_103DE_1992_2 (177), NA_TableFatigue6101N (129), NA_TableFatigue63N (127), NA_TableFatigue63N_1992_2 (168), NA_TableFatigue64N (128), NA_TableFatigue64N_1992_2 (169), NeglectRedistributionOfMoments (149), NonlinearCreep (151), NoResistanceOfConcreteInTension1D (148), NoResistanceOfConcreteInTension2D (203), NoTendonExclusion (162), NumberPartsOfDM (204), PlaneDiagramCount (69), SaTMethodType (119), SetupTable45n1991_2 (132), SimplifiedCssModel (197), StressLimit_TypeFctm (48), StrutAngleOptimalization (155), SubintervalsPerDecade (139), Table74N (76), Table74N_1992_1_1 (176), TableJointParameters (136), Theta (25), Theta_c (51), Theta_max_f (54), Theta_min_c (53), Theta_min_t (52), Theta_t (50), ThetaMax (27), ThetaMin (26), TypeOfInitialstateOfCSS (153), TypeSLSCalculation (202), UseGammalt (72), UserValuesForShear (75), VestigalResistance (161), WeakenedByBars (58), WeakenedByDucts (60), WeakenedByTendons (59) """
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

    AllowCheckInAgeLess3Days = None
    AlphaCw = None
    AnchorageDetailType = None
    BentUpBarsReduction = None
    BLRPRecisionCheckValue = None
    CalculateShrinkage = None
    CalculateSrMaxAccUserSettings = None
    CalculationOfStressLimitationK1 = None
    CalculationOfStressLimitationK2 = None
    CalculationOfStressLimitationK3 = None
    CheckCrackedCss = None
    CheckCrossSectionCrackedIfOneCracked_7_2_Chapter = None
    CoeffCrdc = None
    CoefficientOfTensionConcrete = None
    CoeffK1 = None
    CoeffKl = None
    CoeffKp = None
    CoeffNi = None
    CoeffNi1 = None
    CoeffNi1_EN2_2 = None
    CoeffVmin = None
    CracksPassThrough = None
    CracWidthNationalAnnex = None
    CrossSectionCrackedPlate = None
    DecompressionLimit = None
    DecompressionLimit_2 = None
    DecompressionLimit_3 = None
    DetailingBracketMethodType = None
    DivisionStrain = None
    EndOfCuring = None
    Equation629 = None
    Equation631 = None
    FatigueJointCohesion = None
    FatigueMethod = None
    FindOnly2DPlaneDeformation = None
    HighStrengthConcrete = None
    ImperfectionDirection = None
    IncreaseJointResistance = None
    InnerPerimeter = None
    InteractionDiagramCheckType = None
    InteractionDiagramDivision = None
    InteractionDiagramExportType = None
    InterpolationCurve = None
    IsSetMrForULSMNKappaDiagram = None
    IsSetPrecissionForNullForces = None
    IterationPrecission = None
    IterationSteps = None
    JointShearStressType = None
    LimitCheckValue = None
    LimitDeflectionAdvanced = None
    LimitDeflectionNormal = None
    LimitDeflectionValue = None
    LimitLeverArm = None
    LinearStiffnessForDeflection = None
    MaxBentUpReinfDist = None
    MaxDisplayCheckValue = None
    MaxHorReinfDistWall = None
    MaxHorReinfDistWall_EN2_2 = None
    MaxLengthOfZone = None
    MaxLongReinfDist = None
    MaxLongReinfPercBeam = None
    MaxLongReinfPercBeam_EN2_2 = None
    MaxLongReinfPercColumn = None
    MaxMainReinfDistSlab = None
    MaxMainReinfDistSlab_EN2_2 = None
    MaxMainReinfPercSlab = None
    MaxReinfDistDeepBeam = None
    MaxShearReinfDistBeam = None
    MaxShearReinfDistColumn = None
    MaxShearReinfDistSlab = None
    MaxShearReinfPercBeam = None
    MaxShearReinfTransDist = None
    MaxShearReinfTransDistSlab = None
    MaxTransReinfDistSlab = None
    MaxTransReinfDistSlab_EN2_2 = None
    MaxVertReinfDistWall = None
    MaxVertReinfPercWall = None
    MinAnchLenShear = None
    MinDuctHorDist = None
    MinDuctVertDist = None
    MinHorReinfPercWall = None
    MinLongReinfDiamColumn = None
    MinLongReinfDist = None
    MinLongReinfPercBeam = None
    MinLongReinfPercBeam_EN2_2 = None
    MinLongReinfPercColumn = None
    MinMainReinfPercSlab = None
    MinNoBarCircColumn = None
    MinReinfPercDeepBeam = None
    MinReinfPercDeepBeam_EN2_2 = None
    MinShearReinfDiamColumn = None
    MinShearReinfDiamColumn_EN2_2 = None
    MinShearReinfPercBeam = None
    MinShearReinfPercSlab = None
    MinTendonHorDist = None
    MinTendonVertDist = None
    MinTransReinfPercSlab = None
    MinVertReinfPercWall = None
    ModulusType = None
    ModulusTypeLongTermEffects = None
    NA_1_Wmax_Ec2 = None
    NA_2_4_2_2_Gamma_p_fav = None
    NA_2_4_2_2_Gamma_p_unfav = None
    NA_5_10_2_1_1_K1 = None
    NA_5_10_2_1_1_K2 = None
    NA_5_10_3_2_K7 = None
    NA_5_10_3_2_K8 = None
    NA_5_10_9_r_inf_post = None
    NA_5_10_9_r_inf_pre = None
    NA_5_10_9_r_sup_post = None
    NA_5_10_9_r_sup_pre = None
    NA_5_2_5_Theta0 = None
    NA_5_5_K1 = None
    NA_5_5_K2 = None
    NA_5_5_K3 = None
    NA_5_5_K4 = None
    NA_5_5_K5 = None
    NA_5_5_K5_fck_BiggerThan_50MPa = None
    NA_5_5_K6 = None
    NA_5_5_K6_fck_BiggerThan_50MPa = None
    NA_5_8_6_3_GammaCe = None
    NA_6_5_2_3_Ni = None
    NA_6_5_4_4_K1 = None
    NA_6_5_4_4_K2 = None
    NA_6_5_4_4_K3 = None
    NA_7_2_K1 = None
    NA_7_2_K2 = None
    NA_7_2_K3 = None
    NA_7_2_K4 = None
    NA_7_2_K5 = None
    NA_7_3_1_DecompressionDistance = None
    NA_7_3_1_Wmax_Ec2_1_1 = None
    NA_7_3_1_Wmax_Ec2_2 = None
    NA_7_3_4_K1 = None
    NA_7_3_4_K2 = None
    NA_7_3_4_K3 = None
    NA_7_3_4_K4 = None
    NA_8_3_2_MinDiameterOfMandrel = None
    NA_Alphaccpl_92_1_1 = None
    NA_Alphacc_92_1_1 = None
    NA_Alphacc_92_2 = None
    NA_Alphactpl_92_1_1 = None
    NA_Alphact_92_1_1 = None
    NA_Alphact_92_2 = None
    NA_CoeffEpsudByEpsuk = None
    NA_CoeffEpsudByEpsuk_p = None
    NA_EN1992_3_7_3_1_112_x_min = None
    NA_EN1992_3_CrackWidth = None
    NA_EN1992_3_CrackWidth_XA2_XA3_XF2_XF3_XF4 = None
    NA_GammaC = None
    NA_GammaCfat = None
    NA_GammaC_BLR = None
    NA_GammaFfat = None
    NA_GammaS = None
    NA_GammaSfat = None
    NA_GammaSP = None
    NA_GammaSPfat = None
    NA_GammaSP_BLR = None
    NA_GammaS_BLR = None
    NA_J_3_2_K1 = None
    NA_J_3_3_K2 = None
    NA_K1Fatigue = None
    NA_K2Fatigue = None
    NA_k_p = None
    NA_LimitCharacteristic = None
    NA_LimitInfrequent = None
    NA_LimitQuasiPermanent = None
    NA_LoadDuration = None
    NA_NCyclesFatigue = None
    NA_NN_112_Gamma_sd = None
    NA_Table7_101DE_1992_2 = None
    NA_Table7_102DE_1992_2 = None
    NA_Table7_103DE_1992_2 = None
    NA_TableFatigue6101N = None
    NA_TableFatigue63N = None
    NA_TableFatigue63N_1992_2 = None
    NA_TableFatigue64N = None
    NA_TableFatigue64N_1992_2 = None
    NeglectRedistributionOfMoments = None
    NonlinearCreep = None
    NoResistanceOfConcreteInTension1D = None
    NoResistanceOfConcreteInTension2D = None
    NoTendonExclusion = None
    NumberPartsOfDM = None
    PlaneDiagramCount = None
    SaTMethodType = None
    SetupTable45n1991_2 = None
    SimplifiedCssModel = None
    StressLimit_TypeFctm = None
    StrutAngleOptimalization = None
    SubintervalsPerDecade = None
    Table74N = None
    Table74N_1992_1_1 = None
    TableJointParameters = None
    Theta = None
    ThetaMax = None
    ThetaMin = None
    Theta_c = None
    Theta_max_f = None
    Theta_min_c = None
    Theta_min_t = None
    Theta_t = None
    TypeOfInitialstateOfCSS = None
    TypeSLSCalculation = None
    UseGammalt = None
    UserValuesForShear = None
    value__ = None
    VestigalResistance = None
    WeakenedByBars = None
    WeakenedByDucts = None
    WeakenedByTendons = None


class SetupValueFloat(SetupValue):
    """ SetupValueFloat() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: SetupValueFloat) -> Single

Set: Value(self: SetupValueFloat) = value
"""



class SetupValueInt(SetupValue):
    """ SetupValueInt() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: SetupValueInt) -> int

Set: Value(self: SetupValueInt) = value
"""



class SetupValueLong(SetupValue):
    """ SetupValueLong() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: SetupValueLong) -> Int64

Set: Value(self: SetupValueLong) = value
"""



class SetupValueShort(SetupValue):
    """ SetupValueShort() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: SetupValueShort) -> Int16

Set: Value(self: SetupValueShort) = value
"""



class StagedCheckSection(CheckSection):
    """ StagedCheckSection() """
    StagesLoading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StagesLoading(self: StagedCheckSection) -> StagesLoading

Set: StagesLoading(self: StagedCheckSection) = value
"""



class StagedCheckSectionExtreme(CheckSectionExtreme):
    """ StagedCheckSectionExtreme() """
    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: StagedCheckSectionExtreme) -> float

Set: Time(self: StagedCheckSectionExtreme) = value
"""



class StandardCheckSection(CheckSection):
    """ StandardCheckSection() """

class StandardCheckSectionExtreme(CheckSectionExtreme):
    """ StandardCheckSectionExtreme() """

class SupportType(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) SupportType, values: Hinge (2), HingeHinge (2), HingeNoSupport (3), NoSupport (1), Rigid (4), RigidHinge (6), RigidNoSupport (5), RigidRigid (4) """
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

    Hinge = None
    HingeHinge = None
    HingeNoSupport = None
    NoSupport = None
    Rigid = None
    RigidHinge = None
    RigidNoSupport = None
    RigidRigid = None
    value__ = None


class TimeAxis(OpenObject):
    """ TimeAxis() """
    CreepTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreepTime(self: TimeAxis) -> float

Set: CreepTime(self: TimeAxis) = value
"""

    Times = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Times(self: TimeAxis) -> List[TimePoint]

Set: Times(self: TimeAxis) = value
"""



class TimePoint(OpenObject):
    """ TimePoint() """
    Age = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Age(self: TimePoint) -> float

Set: Age(self: TimePoint) = value
"""

    AllowCheckInAgeLess3Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowCheckInAgeLess3Days(self: TimePoint) -> bool

Set: AllowCheckInAgeLess3Days(self: TimePoint) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: TimePoint) -> str

Set: Description(self: TimePoint) = value
"""

    Fix2DRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fix2DRotation(self: TimePoint) -> bool

Set: Fix2DRotation(self: TimePoint) = value
"""

    LastConstructionStage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastConstructionStage(self: TimePoint) -> bool

Set: LastConstructionStage(self: TimePoint) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: TimePoint) -> str

Set: Name(self: TimePoint) = value
"""

    Prestressing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prestressing(self: TimePoint) -> bool

Set: Prestressing(self: TimePoint) = value
"""

    Stage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stage(self: TimePoint) -> bool

Set: Stage(self: TimePoint) = value
"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: TimePoint) -> float

Set: Time(self: TimePoint) = value
"""



class TwoWaySlabType(Enum, IComparable, IFormattable, IConvertible):
    """ enum TwoWaySlabType, values: DeepBeam (2), ShellAsPlate (3), ShellAsWall (4), Slab (0), Wall (1) """
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

    DeepBeam = None
    ShellAsPlate = None
    ShellAsWall = None
    Slab = None
    value__ = None
    Wall = None


class TypeDeflectionSheme(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeDeflectionSheme, values: DeflectionSheme_I (0), DeflectionSheme_II (1), DeflectionSheme_III (2), DeflectionSheme_IV (3), DeflectionSheme_IX (8), DeflectionSheme_V (4), DeflectionSheme_VI (5), DeflectionSheme_VII (6), DeflectionSheme_VIII (7), DeflectionSheme_X (9), DeflectionSheme_XI (10) """
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

    DeflectionSheme_I = None
    DeflectionSheme_II = None
    DeflectionSheme_III = None
    DeflectionSheme_IV = None
    DeflectionSheme_IX = None
    DeflectionSheme_V = None
    DeflectionSheme_VI = None
    DeflectionSheme_VII = None
    DeflectionSheme_VIII = None
    DeflectionSheme_X = None
    DeflectionSheme_XI = None
    value__ = None


class TypeOfCalculationDeflection(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeOfCalculationDeflection, values: BothOfThem (3), CheckSlenderness (0), CheckSlendernessContinueDirectCalculation (1), DirectCalculation (2) """
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

    BothOfThem = None
    CheckSlenderness = None
    CheckSlendernessContinueDirectCalculation = None
    DirectCalculation = None
    value__ = None


class TypeOfSupportConditions(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeOfSupportConditions, values: Bearing (3), Cantilever (4), Continuous (1), FullyRestrained (2), NonContinuous (0) """
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

    Bearing = None
    Cantilever = None
    Continuous = None
    FullyRestrained = None
    NonContinuous = None
    value__ = None


class ValueTypec(Enum, IComparable, IFormattable, IConvertible):
    """ enum ValueTypec, values: ConstantCurvatureDistribution (1), SinusoidalCurvatureDistribution (2), UserDefined (0) """
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

    ConstantCurvatureDistribution = None
    SinusoidalCurvatureDistribution = None
    UserDefined = None
    value__ = None


class ValueTypec0(Enum, IComparable, IFormattable, IConvertible):
    """ enum ValueTypec0, values: ConstantDistributionMoment (1), ParabolicDistributionMoment (2), TriangularDistributionMoment (3), UserDefined (0) """
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

    ConstantDistributionMoment = None
    ParabolicDistributionMoment = None
    TriangularDistributionMoment = None
    UserDefined = None
    value__ = None


# variables with complex values

