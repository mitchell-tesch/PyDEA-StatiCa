# encoding: utf-8
# module IdeaRS.OpenModel.Loading calls itself Loading
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CombiInput(OpenElementId):
    """ CombiInput() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: CombiInput) -> str

Set: Description(self: CombiInput) = value
"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: CombiInput) -> List[CombiItem]

Set: Items(self: CombiInput) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CombiInput) -> str

Set: Name(self: CombiInput) = value
"""



class CombiInputEC(CombiInput):
    """ CombiInputEC() """
    TypeCalculationCombi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeCalculationCombi(self: CombiInputEC) -> TypeCalculationCombiEC

Set: TypeCalculationCombi(self: CombiInputEC) = value
"""

    TypeCombiEC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeCombiEC(self: CombiInputEC) -> TypeOfCombiEC

Set: TypeCombiEC(self: CombiInputEC) = value
"""



class CombiInputSIA(CombiInput):
    """ CombiInputSIA() """
    TypeCalculationCombi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeCalculationCombi(self: CombiInputSIA) -> TypeCalculationCombiSIA

Set: TypeCalculationCombi(self: CombiInputSIA) = value
"""

    TypeCombiSIA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeCombiSIA(self: CombiInputSIA) -> TypeOfCombiSIA

Set: TypeCombiSIA(self: CombiInputSIA) = value
"""



class CombiItem(OpenObject):
    """ CombiItem() """
    Coeff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coeff(self: CombiItem) -> float

Set: Coeff(self: CombiItem) = value
"""

    Combination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Combination(self: CombiItem) -> ReferenceElement

Set: Combination(self: CombiItem) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: CombiItem) -> int

Set: Id(self: CombiItem) = value
"""

    LoadCase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCase(self: CombiItem) -> ReferenceElement

Set: LoadCase(self: CombiItem) = value
"""



class CrossSectionComponentEdges(OpenObject):
    """ CrossSectionComponentEdges() """
    ComponentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentIndex(self: CrossSectionComponentEdges) -> int

Set: ComponentIndex(self: CrossSectionComponentEdges) = value
"""

    EdgeIndexes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeIndexes(self: CrossSectionComponentEdges) -> List[int]

Set: EdgeIndexes(self: CrossSectionComponentEdges) = value
"""



class LoadCase(OpenElementId):
    """ LoadCase() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: LoadCase) -> str

Set: Description(self: LoadCase) = value
"""

    LoadGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadGroup(self: LoadCase) -> ReferenceElement

Set: LoadGroup(self: LoadCase) = value
"""

    LoadsInPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadsInPoint(self: LoadCase) -> List[ReferenceElement]

Set: LoadsInPoint(self: LoadCase) = value
"""

    LoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadsOnLine(self: LoadCase) -> List[ReferenceElement]

Set: LoadsOnLine(self: LoadCase) = value
"""

    LoadsOnSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadsOnSurface(self: LoadCase) -> List[ReferenceElement]

Set: LoadsOnSurface(self: LoadCase) = value
"""

    LoadType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadType(self: LoadCase) -> LoadCaseType

Set: LoadType(self: LoadCase) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LoadCase) -> str

Set: Name(self: LoadCase) = value
"""

    PointLoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointLoadsOnLine(self: LoadCase) -> List[ReferenceElement]

Set: PointLoadsOnLine(self: LoadCase) = value
"""

    Settlements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settlements(self: LoadCase) -> List[ReferenceElement]

Set: Settlements(self: LoadCase) = value
"""

    StrainLoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StrainLoadsOnLine(self: LoadCase) -> List[ReferenceElement]

Set: StrainLoadsOnLine(self: LoadCase) = value
"""

    TemperatureLoadsOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureLoadsOnLine(self: LoadCase) -> List[ReferenceElement]

Set: TemperatureLoadsOnLine(self: LoadCase) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: LoadCase) -> LoadCaseSubType

Set: Type(self: LoadCase) = value
"""

    Variable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Variable(self: LoadCase) -> VariableType

Set: Variable(self: LoadCase) = value
"""



class LoadCaseSubType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadCaseSubType, values: PermanentPrestress (2), PermanentPrestressPretensioned (15), PermanentPrestressPrimary (16), PermanentPrimaryEffect (7), PermanentRheologic (3), PermanentSelfweight (0), PermanentSelfweightLocal (17), PermanentStandard (1), VariableDynamic (10), VariablePrimaryEffect (11), VariableStatic (9) """
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

    PermanentPrestress = None
    PermanentPrestressPretensioned = None
    PermanentPrestressPrimary = None
    PermanentPrimaryEffect = None
    PermanentRheologic = None
    PermanentSelfweight = None
    PermanentSelfweightLocal = None
    PermanentStandard = None
    value__ = None
    VariableDynamic = None
    VariablePrimaryEffect = None
    VariableStatic = None


class LoadCaseType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadCaseType, values: Accidental (2), Nonlinear (5), Permanent (0), Variable (1) """
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

    Accidental = None
    Nonlinear = None
    Permanent = None
    value__ = None
    Variable = None


class LoadDirection(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadDirection, values: InGcs (1), InLcs (0) """
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

    InGcs = None
    InLcs = None
    value__ = None


class LoadGroup(OpenElementId):
    # no doc
    Dzeta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dzeta(self: LoadGroup) -> float

Set: Dzeta(self: LoadGroup) = value
"""

    GammaGInf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaGInf(self: LoadGroup) -> float

Set: GammaGInf(self: LoadGroup) = value
"""

    GammaGSup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaGSup(self: LoadGroup) -> float

Set: GammaGSup(self: LoadGroup) = value
"""

    GammaQ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaQ(self: LoadGroup) -> float

Set: GammaQ(self: LoadGroup) = value
"""

    GroupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupType(self: LoadGroup) -> LoadGroupType

Set: GroupType(self: LoadGroup) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LoadGroup) -> str

Set: Name(self: LoadGroup) = value
"""

    Relation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Relation(self: LoadGroup) -> Relation

Set: Relation(self: LoadGroup) = value
"""



class LoadGroupEC(LoadGroup):
    """ LoadGroupEC() """
    Psi0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Psi0(self: LoadGroupEC) -> float

Set: Psi0(self: LoadGroupEC) = value
"""

    Psi1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Psi1(self: LoadGroupEC) -> float

Set: Psi1(self: LoadGroupEC) = value
"""

    Psi2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Psi2(self: LoadGroupEC) -> float

Set: Psi2(self: LoadGroupEC) = value
"""



class LoadGroupSIA(LoadGroup):
    """ LoadGroupSIA() """
    Psi0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Psi0(self: LoadGroupSIA) -> float

Set: Psi0(self: LoadGroupSIA) = value
"""

    Psi1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Psi1(self: LoadGroupSIA) -> float

Set: Psi1(self: LoadGroupSIA) = value
"""

    Psi2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Psi2(self: LoadGroupSIA) -> float

Set: Psi2(self: LoadGroupSIA) = value
"""



class LoadGroupType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadGroupType, values: Accidental (2), Fatigue (4), Permanent (0), Seismic (3), Variable (1) """
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

    Accidental = None
    Fatigue = None
    Permanent = None
    Seismic = None
    value__ = None
    Variable = None


class LoadImpulse(object):
    # no doc
    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: LoadImpulse) -> float

Set: X(self: LoadImpulse) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: LoadImpulse) -> float

Set: Y(self: LoadImpulse) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: LoadImpulse) -> float

Set: Z(self: LoadImpulse) = value
"""



class LoadInPoint(OpenElementId):
    """ LoadInPoint() """
    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: LoadInPoint) -> LoadDirection

Set: Direction(self: LoadInPoint) = value
"""

    Fx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fx(self: LoadInPoint) -> float

Set: Fx(self: LoadInPoint) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: LoadInPoint) -> float

Set: Fy(self: LoadInPoint) = value
"""

    Fz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fz(self: LoadInPoint) -> float

Set: Fz(self: LoadInPoint) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: LoadInPoint) -> ReferenceElement

Set: Geometry(self: LoadInPoint) = value
"""

    Mx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mx(self: LoadInPoint) -> float

Set: Mx(self: LoadInPoint) = value
"""

    My = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: My(self: LoadInPoint) -> float

Set: My(self: LoadInPoint) = value
"""

    Mz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mz(self: LoadInPoint) -> float

Set: Mz(self: LoadInPoint) = value
"""



class LoadOnLine(OpenElementId):
    """ LoadOnLine() """
    Bimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bimp(self: LoadOnLine) -> LoadImpulse

Set: Bimp(self: LoadOnLine) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: LoadOnLine) -> LoadDirection

Set: Direction(self: LoadOnLine) = value
"""

    Eimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Eimp(self: LoadOnLine) -> LoadImpulse

Set: Eimp(self: LoadOnLine) = value
"""

    ExY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExY(self: LoadOnLine) -> float

Set: ExY(self: LoadOnLine) = value
"""

    ExYEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExYEnd(self: LoadOnLine) -> float

Set: ExYEnd(self: LoadOnLine) = value
"""

    ExZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExZ(self: LoadOnLine) -> float

Set: ExZ(self: LoadOnLine) = value
"""

    ExZEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExZEnd(self: LoadOnLine) -> float

Set: ExZEnd(self: LoadOnLine) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: LoadOnLine) -> ReferenceElement

Set: Geometry(self: LoadOnLine) = value
"""

    LoadProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadProjection(self: LoadOnLine) -> LoadProjection

Set: LoadProjection(self: LoadOnLine) = value
"""

    RelativeBeginPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeBeginPosition(self: LoadOnLine) -> float

Set: RelativeBeginPosition(self: LoadOnLine) = value
"""

    RelativeEndPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeEndPosition(self: LoadOnLine) -> float

Set: RelativeEndPosition(self: LoadOnLine) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: LoadOnLine) -> LoadType

Set: Type(self: LoadOnLine) = value
"""



class LoadOnSurface(OpenElementId):
    """ LoadOnSurface() """
    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: LoadOnSurface) -> LoadDirection

Set: Direction(self: LoadOnSurface) = value
"""

    Fx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fx(self: LoadOnSurface) -> float

Set: Fx(self: LoadOnSurface) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: LoadOnSurface) -> float

Set: Fy(self: LoadOnSurface) = value
"""

    Fz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fz(self: LoadOnSurface) -> float

Set: Fz(self: LoadOnSurface) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: LoadOnSurface) -> Region3D

Set: Geometry(self: LoadOnSurface) = value
"""



class LoadProjection(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadProjection, values: Length (0), Projection (1) """
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

    Length = None
    Projection = None
    value__ = None


class LoadType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadType, values: LoadForce (0), LoadMoment (1) """
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

    LoadForce = None
    LoadMoment = None
    value__ = None


class PointLoadOnLine(OpenElementId):
    """ PointLoadOnLine() """
    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: PointLoadOnLine) -> LoadDirection

Set: Direction(self: PointLoadOnLine) = value
"""

    Ey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ey(self: PointLoadOnLine) -> float

Set: Ey(self: PointLoadOnLine) = value
"""

    Ez = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ez(self: PointLoadOnLine) -> float

Set: Ez(self: PointLoadOnLine) = value
"""

    Fx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fx(self: PointLoadOnLine) -> float

Set: Fx(self: PointLoadOnLine) = value
"""

    Fy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fy(self: PointLoadOnLine) -> float

Set: Fy(self: PointLoadOnLine) = value
"""

    Fz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fz(self: PointLoadOnLine) -> float

Set: Fz(self: PointLoadOnLine) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: PointLoadOnLine) -> ReferenceElement

Set: Geometry(self: PointLoadOnLine) = value
"""

    Mx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mx(self: PointLoadOnLine) -> float

Set: Mx(self: PointLoadOnLine) = value
"""

    My = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: My(self: PointLoadOnLine) -> float

Set: My(self: PointLoadOnLine) = value
"""

    Mz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mz(self: PointLoadOnLine) -> float

Set: Mz(self: PointLoadOnLine) = value
"""

    RelativePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativePosition(self: PointLoadOnLine) -> float

Set: RelativePosition(self: PointLoadOnLine) = value
"""



class Relation(Enum, IComparable, IFormattable, IConvertible):
    """ enum Relation, values: Exclusive (1), Standard (0) """
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

    Exclusive = None
    Standard = None
    value__ = None


class ResultClass(OpenElementId):
    """ ResultClass() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ResultClass) -> str

Set: Description(self: ResultClass) = value
"""

    IdConstructionStage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdConstructionStage(self: ResultClass) -> int

Set: IdConstructionStage(self: ResultClass) = value
"""

    ListItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ListItem(self: ResultClass) -> List[SelectionItemForResults]

Set: ListItem(self: ResultClass) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ResultClass) -> str

Set: Name(self: ResultClass) = value
"""

    Nonlinear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nonlinear(self: ResultClass) -> bool

Set: Nonlinear(self: ResultClass) = value
"""

    TypeResultClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeResultClass(self: ResultClass) -> TypeResultsClass

Set: TypeResultClass(self: ResultClass) = value
"""

    TypeUpdateResultClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeUpdateResultClass(self: ResultClass) -> TypeUpdateResultClass

Set: TypeUpdateResultClass(self: ResultClass) = value
"""



class SelectionItemForResults(OpenElementId):
    """ SelectionItemForResults() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Coeff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coeff(self: SelectionItemForResults) -> float

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SelectionItemForResults) -> str

"""

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: SelectionItemForResults) -> ReferenceElement

Set: Item(self: SelectionItemForResults) = value
"""

    TypeClassEvaluation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeClassEvaluation(self: SelectionItemForResults) -> TypeClassEvaluation

Set: TypeClassEvaluation(self: SelectionItemForResults) = value
"""

    TypeOfLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeOfLoad(self: SelectionItemForResults) -> str

"""



class Settlement(OpenElementId):
    """ Settlement() """
    Support = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Support(self: Settlement) -> ReferenceElement

Set: Support(self: Settlement) = value
"""

    ValueRx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueRx(self: Settlement) -> float

Set: ValueRx(self: Settlement) = value
"""

    ValueRy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueRy(self: Settlement) -> float

Set: ValueRy(self: Settlement) = value
"""

    ValueRz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueRz(self: Settlement) -> float

Set: ValueRz(self: Settlement) = value
"""

    ValueX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueX(self: Settlement) -> float

Set: ValueX(self: Settlement) = value
"""

    ValueY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueY(self: Settlement) -> float

Set: ValueY(self: Settlement) = value
"""

    ValueZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueZ(self: Settlement) -> float

Set: ValueZ(self: Settlement) = value
"""



class StrainImpulse(object):
    # no doc
    EpsX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EpsX(self: StrainImpulse) -> float

Set: EpsX(self: StrainImpulse) = value
"""

    GammaXY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaXY(self: StrainImpulse) -> float

Set: GammaXY(self: StrainImpulse) = value
"""

    GammaXZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GammaXZ(self: StrainImpulse) -> float

Set: GammaXZ(self: StrainImpulse) = value
"""

    PhiX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhiX(self: StrainImpulse) -> float

Set: PhiX(self: StrainImpulse) = value
"""

    PhiY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhiY(self: StrainImpulse) -> float

Set: PhiY(self: StrainImpulse) = value
"""

    PhiZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhiZ(self: StrainImpulse) -> float

Set: PhiZ(self: StrainImpulse) = value
"""



class StrainLoadOnLine(OpenElementId):
    """ StrainLoadOnLine() """
    Bimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bimp(self: StrainLoadOnLine) -> StrainImpulse

Set: Bimp(self: StrainLoadOnLine) = value
"""

    Eimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Eimp(self: StrainLoadOnLine) -> StrainImpulse

Set: Eimp(self: StrainLoadOnLine) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: StrainLoadOnLine) -> ReferenceElement

Set: Geometry(self: StrainLoadOnLine) = value
"""

    RelativeBeginPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeBeginPosition(self: StrainLoadOnLine) -> float

Set: RelativeBeginPosition(self: StrainLoadOnLine) = value
"""

    RelativeEndPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeEndPosition(self: StrainLoadOnLine) -> float

Set: RelativeEndPosition(self: StrainLoadOnLine) = value
"""



class TemperatureDirection(Enum, IComparable, IFormattable, IConvertible):
    """ enum TemperatureDirection, values: EveryWhere (0), SpecifiedEdges (1) """
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

    EveryWhere = None
    SpecifiedEdges = None
    value__ = None


class TemperatureLoadOnLine(OpenElementId):
    """ TemperatureLoadOnLine() """
    ConvectionCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConvectionCoefficient(self: TemperatureLoadOnLine) -> float

Set: ConvectionCoefficient(self: TemperatureLoadOnLine) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: TemperatureLoadOnLine) -> TemperatureDirection

Set: Direction(self: TemperatureLoadOnLine) = value
"""

    DirectionEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionEdges(self: TemperatureLoadOnLine) -> List[CrossSectionComponentEdges]

Set: DirectionEdges(self: TemperatureLoadOnLine) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: TemperatureLoadOnLine) -> ReferenceElement

Set: Geometry(self: TemperatureLoadOnLine) = value
"""

    RadiationCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiationCoefficient(self: TemperatureLoadOnLine) -> float

Set: RadiationCoefficient(self: TemperatureLoadOnLine) = value
"""

    RelativeBeginPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeBeginPosition(self: TemperatureLoadOnLine) -> float

Set: RelativeBeginPosition(self: TemperatureLoadOnLine) = value
"""

    RelativeEndPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeEndPosition(self: TemperatureLoadOnLine) -> float

Set: RelativeEndPosition(self: TemperatureLoadOnLine) = value
"""

    TemperatureCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureCurve(self: TemperatureLoadOnLine) -> Polygon2D

Set: TemperatureCurve(self: TemperatureLoadOnLine) = value
"""



class TypeCalculationCombiEC(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeCalculationCombiEC, values: Code610 (2), Code610ab (3), Envelope (1), Linear (0), NonLinear (4) """
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

    Code610 = None
    Code610ab = None
    Envelope = None
    Linear = None
    NonLinear = None
    value__ = None


class TypeCalculationCombiSIA(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeCalculationCombiSIA, values: Code (2), Envelope (1), Linear (0) """
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
    Envelope = None
    Linear = None
    value__ = None


class TypeClassEvaluation(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeClassEvaluation, values: eLinCombi (1), eLoadCase (0), eNonLinCombi (2) """
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

    eLinCombi = None
    eLoadCase = None
    eNonLinCombi = None
    value__ = None


class TypeDuration(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeDuration, values: InstantaneousTerm (3), LongTerm (0), MediumTerm (1), ShortTerm (2) """
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

    InstantaneousTerm = None
    LongTerm = None
    MediumTerm = None
    ShortTerm = None
    value__ = None


class TypeOfCombiEC(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeOfCombiEC, values: Accidental (2), Accidental_2 (3), Fatigue (8), Seismic (4), SLS_Char (5), SLS_Freq (6), SLS_Quasi (7), ULS (0), ULS_SET_C (1) """
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

    Accidental = None
    Accidental_2 = None
    Fatigue = None
    Seismic = None
    SLS_Char = None
    SLS_Freq = None
    SLS_Quasi = None
    ULS = None
    ULS_SET_C = None
    value__ = None


class TypeOfCombiSIA(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeOfCombiSIA, values: Accidental (2), Fatigue (8), SLS_Char (5), SLS_Freq (6), SLS_Quasi (7), ULS (0) """
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

    Accidental = None
    Fatigue = None
    SLS_Char = None
    SLS_Freq = None
    SLS_Quasi = None
    ULS = None
    value__ = None


class TypeResultsClass(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeResultsClass, values: CheckClassBridgeLoadRating (10), CheckClassFireResistance (9), FatigueResultsClass (8), SLSCharacteristicsCheckClass (5), SLSDeflectionResultsClass (6), SLSFrequentCheckClass (3), SLSQuasiPermanentCheckClass (4), SLSResultsClass (1), ULSAccidentalResultsClass (7), ULSCheckClass (2), ULSResultsClass (0) """
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

    CheckClassBridgeLoadRating = None
    CheckClassFireResistance = None
    FatigueResultsClass = None
    SLSCharacteristicsCheckClass = None
    SLSDeflectionResultsClass = None
    SLSFrequentCheckClass = None
    SLSQuasiPermanentCheckClass = None
    SLSResultsClass = None
    ULSAccidentalResultsClass = None
    ULSCheckClass = None
    ULSResultsClass = None
    value__ = None


class TypeUpdateResultClass(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeUpdateResultClass, values: DoNotUpdate (1), Update (0) """
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

    DoNotUpdate = None
    Update = None
    value__ = None


class VariableType(Enum, IComparable, IFormattable, IConvertible):
    """ enum VariableType, values: MobileEnvelope (1), NotSet (3), Seismicity (2), Standard (0) """
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

    MobileEnvelope = None
    NotSet = None
    Seismicity = None
    Standard = None
    value__ = None


