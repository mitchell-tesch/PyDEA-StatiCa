# encoding: utf-8
# module IdeaRS.OpenModel.Parameters calls itself Parameters
# from IdeaRS.OpenModel, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MprlRecord(object):
    """ MprlRecord() """
    ItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemId(self: MprlRecord) -> Guid

Set: ItemId(self: MprlRecord) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MprlRecord) -> str

Set: Name(self: MprlRecord) = value
"""

    TableId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableId(self: MprlRecord) -> Guid

Set: TableId(self: MprlRecord) = value
"""



class BoltParam(MprlRecord):
    """ BoltParam() """
    Angles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angles(self: BoltParam) -> NumberGroups

Set: Angles(self: BoltParam) = value
"""

    BoltInteraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltInteraction(self: BoltParam) -> BoltShearType

Set: BoltInteraction(self: BoltParam) = value
"""

    Cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cols(self: BoltParam) -> NumberGroups

Set: Cols(self: BoltParam) = value
"""

    ColsGridType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColsGridType(self: BoltParam) -> ConnectorGridType

Set: ColsGridType(self: BoltParam) = value
"""

    ColsNegative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColsNegative(self: BoltParam) -> NumberGroups

Set: ColsNegative(self: BoltParam) = value
"""

    ColsPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColsPosition(self: BoltParam) -> PositionRelatedTo

Set: ColsPosition(self: BoltParam) = value
"""

    ColsSymmetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColsSymmetry(self: BoltParam) -> Symmetry

Set: ColsSymmetry(self: BoltParam) = value
"""

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystem(self: BoltParam) -> CoordinateSystemMethod

Set: CoordinateSystem(self: BoltParam) = value
"""

    Counts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Counts(self: BoltParam) -> IList[int]

Set: Counts(self: BoltParam) = value
"""

    PolarInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PolarInput(self: BoltParam) -> PolarInputType

Set: PolarInput(self: BoltParam) = value
"""

    PolarPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PolarPosition(self: BoltParam) -> PositionRelatedTo

Set: PolarPosition(self: BoltParam) = value
"""

    Positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Positions(self: BoltParam) -> List[Point]

Set: Positions(self: BoltParam) = value
"""

    Radii = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radii(self: BoltParam) -> NumberGroups

Set: Radii(self: BoltParam) = value
"""

    Rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rows(self: BoltParam) -> NumberGroups

Set: Rows(self: BoltParam) = value
"""

    RowsGridType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowsGridType(self: BoltParam) -> ConnectorGridType

Set: RowsGridType(self: BoltParam) = value
"""

    RowsNegative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowsNegative(self: BoltParam) -> NumberGroups

Set: RowsNegative(self: BoltParam) = value
"""

    RowsPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowsPosition(self: BoltParam) -> PositionRelatedTo

Set: RowsPosition(self: BoltParam) = value
"""

    RowsSymmetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowsSymmetry(self: BoltParam) -> Symmetry

Set: RowsSymmetry(self: BoltParam) = value
"""

    ShearInThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShearInThread(self: BoltParam) -> bool

Set: ShearInThread(self: BoltParam) = value
"""



class AnchorParam(BoltParam):
    """ AnchorParam() """
    AnchorTypeData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorTypeData(self: AnchorParam) -> AnchorType

Set: AnchorTypeData(self: AnchorParam) = value
"""

    AnchorTypeSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorTypeSize(self: AnchorParam) -> float

Set: AnchorTypeSize(self: AnchorParam) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: AnchorParam) -> float

Set: Length(self: AnchorParam) = value
"""



class AnchorType(Enum, IComparable, IFormattable, IConvertible):
    """ enum AnchorType, values: Straight (0), WasherPlateCircular (1), WasherPlateRectangular (2) """
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

    Straight = None
    value__ = None
    WasherPlateCircular = None
    WasherPlateRectangular = None


class BoltShearType(Enum, IComparable, IFormattable, IConvertible):
    """ enum BoltShearType, values: Bearing (0), Friction (2), Interaction (1) """
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
    Friction = None
    Interaction = None
    value__ = None


class ConnectorGridType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConnectorGridType, values: FirstShifted (5), FirstShiftedFull (1), FirstShiftedShort (4), Full (3), Regular (0), SecondShifted (10), SecondShiftedFull (2), SecondShiftedShort (8), Short (12) """
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

    FirstShifted = None
    FirstShiftedFull = None
    FirstShiftedShort = None
    Full = None
    Regular = None
    SecondShifted = None
    SecondShiftedFull = None
    SecondShiftedShort = None
    Short = None
    value__ = None


class CrossSectionParam(MprlRecord):
    """ CrossSectionParam() """

class MaterialParam(MprlRecord):
    """ MaterialParam() """

class NumberGroups(List[List[ValueCount]], IList[List[ValueCount]], ICollection[List[ValueCount]], IEnumerable[List[ValueCount]], IEnumerable, IList, ICollection, IReadOnlyList[List[ValueCount]], IReadOnlyCollection[List[ValueCount]]):
    """ NumberGroups() """
    @staticmethod
    def Create(*__args):
        """
        Create(list: List[ValueCount]) -> NumberGroups
        Create(*positions: Array[str]) -> NumberGroups
        Create(value: float) -> NumberGroups
        Create(value: float, count: int) -> NumberGroups
        Create(positions: IEnumerable[float]) -> NumberGroups
        Create(*positions: Array[float]) -> NumberGroups
        """
        pass

    @staticmethod
    def CreateGroups(positions):
        """
        CreateGroups(positions: IEnumerable[float]) -> NumberGroups
        CreateGroups(*positions: Array[float]) -> NumberGroups
        """
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


class PolarInputType(Enum, IComparable, IFormattable, IConvertible):
    """ enum PolarInputType, values: ByAngle (1), ByCount (0) """
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

    ByAngle = None
    ByCount = None
    value__ = None


class PositionRelatedTo(Enum, IComparable, IFormattable, IConvertible):
    """ enum PositionRelatedTo, values: Axis (0), LeftSide (3), Profile (2), RightSide (4), TopOfSteel (1) """
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

    Axis = None
    LeftSide = None
    Profile = None
    RightSide = None
    TopOfSteel = None
    value__ = None


class ValueCount(object):
    """ ValueCount() """
    @staticmethod
    def Create(value, count=None):
        """
        Create(value: float) -> ValueCount
        Create(value: float, count: int) -> ValueCount
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ValueCount) -> int

Set: Count(self: ValueCount) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ValueCount) -> float

Set: Value(self: ValueCount) = value
"""



class WeldParam(MprlRecord):
    """ WeldParam() """
    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: WeldParam) -> float

Set: Size(self: WeldParam) = value
"""

    WeldType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldType(self: WeldParam) -> WeldType

Set: WeldType(self: WeldParam) = value
"""



class WeldType(Enum, IComparable, IFormattable, IConvertible):
    """ enum WeldType, values: Bevel (4), DoubleFillet (3), LeftFillet (1), None (0), RightFillet (2) """
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

    Bevel = None
    DoubleFillet = None
    LeftFillet = None
    None = None
    RightFillet = None
    value__ = None


