# encoding: utf-8
# module IdeaRS.OpenModel.Detail.Loading calls itself Loading
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CalculationCase(OpenElementId):
    """ CalculationCase() """
    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: CalculationCase) -> bool

Set: IsActive(self: CalculationCase) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CalculationCase) -> str

Set: Name(self: CalculationCase) = value
"""



class DirectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum DirectionType, values: GlobalX (0), GlobalY (1), GlobalZ (2), LocalX (3), LocalY (4), LocalZ (5) """
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

    GlobalX = None
    GlobalY = None
    GlobalZ = None
    LocalX = None
    LocalY = None
    LocalZ = None
    value__ = None


class LoadBase(OpenObject):
    # no doc
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: LoadBase) -> int

Set: Id(self: LoadBase) = value
"""



class LineLoad(LoadBase):
    """ LineLoad() """
    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: LineLoad) -> float

Set: Angle(self: LineLoad) = value
"""

    BegFx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BegFx(self: LineLoad) -> float

Set: BegFx(self: LineLoad) = value
"""

    BegFy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BegFy(self: LineLoad) -> float

Set: BegFy(self: LineLoad) = value
"""

    BegPositionX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BegPositionX(self: LineLoad) -> float

Set: BegPositionX(self: LineLoad) = value
"""

    BegPositionY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BegPositionY(self: LineLoad) -> float

Set: BegPositionY(self: LineLoad) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: LineLoad) -> LoadDirection

Set: Direction(self: LineLoad) = value
"""

    DirectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionType(self: LineLoad) -> DirectionType

Set: DirectionType(self: LineLoad) = value
"""

    EdgePositionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgePositionType(self: LineLoad) -> EdgeOrientationType

Set: EdgePositionType(self: LineLoad) = value
"""

    EndFx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFx(self: LineLoad) -> float

Set: EndFx(self: LineLoad) = value
"""

    EndFy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFy(self: LineLoad) -> float

Set: EndFy(self: LineLoad) = value
"""

    EndPositionX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPositionX(self: LineLoad) -> float

Set: EndPositionX(self: LineLoad) = value
"""

    EndPositionY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPositionY(self: LineLoad) -> float

Set: EndPositionY(self: LineLoad) = value
"""

    GeneralLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralLine(self: LineLoad) -> PolyLine2D

Set: GeneralLine(self: LineLoad) = value
"""

    GeometryPointsPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryPointsPath(self: LineLoad) -> Polygon2D

Set: GeometryPointsPath(self: LineLoad) = value
"""

    LengthOnEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthOnEdge(self: LineLoad) -> float

Set: LengthOnEdge(self: LineLoad) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: LineLoad) -> ReferenceElement

Set: MasterComponent(self: LineLoad) = value
"""

    MasterEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterEdge(self: LineLoad) -> int

Set: MasterEdge(self: LineLoad) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: LineLoad) -> int

Set: MasterPoint(self: LineLoad) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LineLoad) -> str

Set: Name(self: LineLoad) = value
"""

    PositionOnEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionOnEdge(self: LineLoad) -> float

Set: PositionOnEdge(self: LineLoad) = value
"""

    ResultantForces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultantForces(self: LineLoad) -> str

Set: ResultantForces(self: LineLoad) = value
"""

    TypeEdgePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeEdgePosition(self: LineLoad) -> TypeEdgePosition

Set: TypeEdgePosition(self: LineLoad) = value
"""

    TypeLinePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeLinePosition(self: LineLoad) -> TypeLinePosition

Set: TypeLinePosition(self: LineLoad) = value
"""



class LoadCase(CalculationCase):
    """ LoadCase() """
    Load = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Load(self: LoadCase) -> List[LoadBase]

Set: Load(self: LoadCase) = value
"""

    LoadCaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCaseType(self: LoadCase) -> LoadCaseType

Set: LoadCaseType(self: LoadCase) = value
"""



class LoadCaseType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadCaseType, values: Permanent (0), Variable (1) """
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

    Permanent = None
    value__ = None
    Variable = None


class TypeLinePosition(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeLinePosition, values: OnWallEdge (1), Point (0), Polyline (2) """
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

    OnWallEdge = None
    Point = None
    Polyline = None
    value__ = None


