# encoding: utf-8
# module IdeaRS.OpenModel.Detail calls itself Detail
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BarEndExtendType(Enum, IComparable, IFormattable, IConvertible):
    """ enum BarEndExtendType, values: ExtendByDistance (2), ExtendToSegment (1), No (0) """
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

    ExtendByDistance = None
    ExtendToSegment = None
    No = None
    value__ = None


class Beam(Element1D, IGeometryPart):
    """ Beam() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Beam) -> List[ReferenceElement]

Set: Edges(self: Beam) = value
"""

    GeomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeomId(self: Beam) -> int

Set: GeomId(self: Beam) = value
"""

    InsertPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertPoint(self: Beam) -> int

Set: InsertPoint(self: Beam) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: Beam) -> ReferenceElement

Set: MasterComponent(self: Beam) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: Beam) -> int

Set: MasterPoint(self: Beam) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Beam) -> Vector3D

Set: Position(self: Beam) = value
"""



class Reinforcement(OpenElementId):
    # no doc
    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: Reinforcement) -> ReferenceElement

Set: Material(self: Reinforcement) = value
"""

    ReinfId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReinfId(self: Reinforcement) -> int

Set: ReinfId(self: Reinforcement) = value
"""



class ReinforcementGroup(Reinforcement):
    # no doc
    Cover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cover(self: ReinforcementGroup) -> float

Set: Cover(self: ReinforcementGroup) = value
"""

    CoverFromSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoverFromSetting(self: ReinforcementGroup) -> bool

Set: CoverFromSetting(self: ReinforcementGroup) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: ReinforcementGroup) -> float

Set: Diameter(self: ReinforcementGroup) = value
"""

    DiameterOfMandrel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiameterOfMandrel(self: ReinforcementGroup) -> float

Set: DiameterOfMandrel(self: ReinforcementGroup) = value
"""

    EndsTypeBeg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndsTypeBeg(self: ReinforcementGroup) -> LongReinfEndType

Set: EndsTypeBeg(self: ReinforcementGroup) = value
"""

    EndsTypeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndsTypeEnd(self: ReinforcementGroup) -> LongReinfEndType

Set: EndsTypeEnd(self: ReinforcementGroup) = value
"""

    NumOfBarsInLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumOfBarsInLayer(self: ReinforcementGroup) -> int

Set: NumOfBarsInLayer(self: ReinforcementGroup) = value
"""



class BentUpBar(ReinforcementGroup):
    """ BentUpBar() """
    AddAnchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddAnchor(self: BentUpBar) -> bool

Set: AddAnchor(self: BentUpBar) = value
"""

    AnchorLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorLength(self: BentUpBar) -> float

Set: AnchorLength(self: BentUpBar) = value
"""

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: BentUpBar) -> float

Set: Angle(self: BentUpBar) = value
"""

    BottomLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomLength(self: BentUpBar) -> float

Set: BottomLength(self: BentUpBar) = value
"""

    IsOnLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOnLeft(self: BentUpBar) -> bool

Set: IsOnLeft(self: BentUpBar) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: BentUpBar) -> ReferenceElement

Set: MasterComponent(self: BentUpBar) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: BentUpBar) -> float

Set: Offset(self: BentUpBar) = value
"""

    TopLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopLength(self: BentUpBar) -> float

Set: TopLength(self: BentUpBar) = value
"""



class DappedEnd(OpenElementId):
    """ DappedEnd() """
    DappedEndHaunch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DappedEndHaunch(self: DappedEnd) -> DappedEndHaunchType

Set: DappedEndHaunch(self: DappedEnd) = value
"""

    GeomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeomId(self: DappedEnd) -> int

Set: GeomId(self: DappedEnd) = value
"""

    Haunch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Haunch(self: DappedEnd) -> float

Set: Haunch(self: DappedEnd) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: DappedEnd) -> float

Set: Height(self: DappedEnd) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: DappedEnd) -> ReferenceElement

Set: MasterComponent(self: DappedEnd) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: DappedEnd) -> int

Set: MasterPoint(self: DappedEnd) = value
"""

    Outline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Outline(self: DappedEnd) -> ReferenceElement

Set: Outline(self: DappedEnd) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: DappedEnd) -> Vector3D

Set: Position(self: DappedEnd) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: DappedEnd) -> float

Set: Rotation(self: DappedEnd) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: DappedEnd) -> float

Set: Width(self: DappedEnd) = value
"""



class DappedEndHaunchType(Enum, IComparable, IFormattable, IConvertible):
    """ enum DappedEndHaunchType, values: Both (3), Left (1), None (0), Right (2) """
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
    Left = None
    None = None
    Right = None
    value__ = None


class EdgeOrientationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum EdgeOrientationType, values: FromBegin (0), FromEnd (1) """
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

    FromBegin = None
    FromEnd = None
    value__ = None


class EdgePositionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum EdgePositionType, values: PartEdgeFromBegin (1), PartEdgeFromEnd (2), PartEdgeToSegment (3), WholeLength (0) """
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

    PartEdgeFromBegin = None
    PartEdgeFromEnd = None
    PartEdgeToSegment = None
    value__ = None
    WholeLength = None


class Hanging(Reinforcement):
    """ Hanging() """
    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: Hanging) -> float

Set: Angle(self: Hanging) = value
"""

    BottomLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomLength(self: Hanging) -> float

Set: BottomLength(self: Hanging) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Hanging) -> float

Set: Diameter(self: Hanging) = value
"""

    DiameterOfMandrel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiameterOfMandrel(self: Hanging) -> float

Set: DiameterOfMandrel(self: Hanging) = value
"""

    EdgeOrientationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeOrientationType(self: Hanging) -> EdgeOrientationType

Set: EdgeOrientationType(self: Hanging) = value
"""

    EndsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndsType(self: Hanging) -> LongReinfEndType

Set: EndsType(self: Hanging) = value
"""

    HangingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HangingType(self: Hanging) -> HangingType

Set: HangingType(self: Hanging) = value
"""

    LegsLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegsLength(self: Hanging) -> float

Set: LegsLength(self: Hanging) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: Hanging) -> ReferenceElement

Set: MasterComponent(self: Hanging) = value
"""

    MasterEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterEdge(self: Hanging) -> ReferenceElement

Set: MasterEdge(self: Hanging) = value
"""

    PositionOnEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionOnEdge(self: Hanging) -> float

Set: PositionOnEdge(self: Hanging) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Hanging) -> float

Set: Radius(self: Hanging) = value
"""

    UpperLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperLength(self: Hanging) -> float

Set: UpperLength(self: Hanging) = value
"""



class HangingAroundPatch(Reinforcement):
    """ HangingAroundPatch() """
    BottomPartLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomPartLength(self: HangingAroundPatch) -> float

Set: BottomPartLength(self: HangingAroundPatch) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: HangingAroundPatch) -> float

Set: Diameter(self: HangingAroundPatch) = value
"""

    DiameterOfMandrel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiameterOfMandrel(self: HangingAroundPatch) -> float

Set: DiameterOfMandrel(self: HangingAroundPatch) = value
"""

    DistanceFromPatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceFromPatch(self: HangingAroundPatch) -> float

Set: DistanceFromPatch(self: HangingAroundPatch) = value
"""

    EndsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndsType(self: HangingAroundPatch) -> LongReinfEndType

Set: EndsType(self: HangingAroundPatch) = value
"""

    InclinedPartsAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InclinedPartsAngle(self: HangingAroundPatch) -> float

Set: InclinedPartsAngle(self: HangingAroundPatch) = value
"""

    InclinedPartsLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InclinedPartsLength(self: HangingAroundPatch) -> float

Set: InclinedPartsLength(self: HangingAroundPatch) = value
"""

    IsMirrored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMirrored(self: HangingAroundPatch) -> bool

Set: IsMirrored(self: HangingAroundPatch) = value
"""

    LegsLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegsLength(self: HangingAroundPatch) -> float

Set: LegsLength(self: HangingAroundPatch) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: HangingAroundPatch) -> ReferenceElement

Set: MasterComponent(self: HangingAroundPatch) = value
"""

    NumOfBarsInLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumOfBarsInLayer(self: HangingAroundPatch) -> int

Set: NumOfBarsInLayer(self: HangingAroundPatch) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: HangingAroundPatch) -> float

Set: Rotation(self: HangingAroundPatch) = value
"""



class HangingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum HangingType, values: AngleAnchorLShapedBranches (3), AngleAnchorStraightBranches (2), StraightAnchorLShapedBranches (1), StraightAnchorSingleBar (4), StraightAnchorStraightBranches (0) """
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

    AngleAnchorLShapedBranches = None
    AngleAnchorStraightBranches = None
    StraightAnchorLShapedBranches = None
    StraightAnchorSingleBar = None
    StraightAnchorStraightBranches = None
    value__ = None


class IGeometryPart:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: IGeometryPart) -> List[ReferenceElement]

Set: Edges(self: IGeometryPart) = value
"""



class InclinedReinfBarType(Enum, IComparable, IFormattable, IConvertible):
    """ enum InclinedReinfBarType, values: FullLength (1), InputByLength (0) """
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

    FullLength = None
    InputByLength = None
    value__ = None


class ISDImportSettings(object):
    """ ISDImportSettings() """
    UseWizard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseWizard(self: ISDImportSettings) -> bool

Set: UseWizard(self: ISDImportSettings) = value
"""



class ISDModel(OpenElementId):
    """ ISDModel() """
    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: ISDModel) -> List[ReferenceElement]

Set: Geometry(self: ISDModel) = value
"""

    ISDType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ISDType(self: ISDModel) -> ISDType

Set: ISDType(self: ISDModel) = value
"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: ISDModel) -> List[ReferenceElement]

Set: Loading(self: ISDModel) = value
"""

    Reinforcement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reinforcement(self: ISDModel) -> List[ReferenceElement]

Set: Reinforcement(self: ISDModel) = value
"""

    Setting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Setting(self: ISDModel) -> ISDSetting

Set: Setting(self: ISDModel) = value
"""



class ISDSetting(object):
    """ ISDSetting() """
    Cover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cover(self: ISDSetting) -> float

Set: Cover(self: ISDSetting) = value
"""



class ISDType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ISDType, values: Diaphragm (3), FrameJoint (2), Member1D (1), Wall (0) """
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

    Diaphragm = None
    FrameJoint = None
    Member1D = None
    value__ = None
    Wall = None


class LineSupport(OpenElementId):
    """ LineSupport() """
    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: LineSupport) -> LoadDirection

Set: Direction(self: LineSupport) = value
"""

    EdgePositionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgePositionType(self: LineSupport) -> EdgeOrientationType

Set: EdgePositionType(self: LineSupport) = value
"""

    GeneralLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralLine(self: LineSupport) -> PolyLine2D

Set: GeneralLine(self: LineSupport) = value
"""

    GeometryPointsPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryPointsPath(self: LineSupport) -> Polygon2D

Set: GeometryPointsPath(self: LineSupport) = value
"""

    GeomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeomId(self: LineSupport) -> int

Set: GeomId(self: LineSupport) = value
"""

    IsPressureOnlyY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPressureOnlyY(self: LineSupport) -> bool

Set: IsPressureOnlyY(self: LineSupport) = value
"""

    IsUserStiffnessX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserStiffnessX(self: LineSupport) -> bool

Set: IsUserStiffnessX(self: LineSupport) = value
"""

    IsUserStiffnessY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserStiffnessY(self: LineSupport) -> bool

Set: IsUserStiffnessY(self: LineSupport) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: LineSupport) -> ReferenceElement

Set: MasterComponent(self: LineSupport) = value
"""

    MasterEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterEdge(self: LineSupport) -> int

Set: MasterEdge(self: LineSupport) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LineSupport) -> str

Set: Name(self: LineSupport) = value
"""

    OnWallEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnWallEdge(self: LineSupport) -> bool

Set: OnWallEdge(self: LineSupport) = value
"""

    PositionOnEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionOnEdge(self: LineSupport) -> float

Set: PositionOnEdge(self: LineSupport) = value
"""

    Rz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rz(self: LineSupport) -> bool

Set: Rz(self: LineSupport) = value
"""

    StiffnessRz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StiffnessRz(self: LineSupport) -> float

Set: StiffnessRz(self: LineSupport) = value
"""

    StiffnessX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StiffnessX(self: LineSupport) -> float

Set: StiffnessX(self: LineSupport) = value
"""

    StiffnessY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StiffnessY(self: LineSupport) -> float

Set: StiffnessY(self: LineSupport) = value
"""

    SupportLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportLength(self: LineSupport) -> float

Set: SupportLength(self: LineSupport) = value
"""

    TypeEdgePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeEdgePosition(self: LineSupport) -> TypeEdgePosition

Set: TypeEdgePosition(self: LineSupport) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: LineSupport) -> bool

Set: X(self: LineSupport) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: LineSupport) -> bool

Set: Y(self: LineSupport) = value
"""



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


class LongReinfEndType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LongReinfEndType, values: Bend (1), ContinuousBar (5), ContinuousBarOutside (6), Hook (2), Hook180DegreeACI (8), Hook90DegreeACI (7), Loop (3), None (0), WeldedTransverseBar (4) """
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

    Bend = None
    ContinuousBar = None
    ContinuousBarOutside = None
    Hook = None
    Hook180DegreeACI = None
    Hook90DegreeACI = None
    Loop = None
    None = None
    value__ = None
    WeldedTransverseBar = None


class Opening(OpenElementId):
    """ Opening() """
    GeomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeomId(self: Opening) -> int

Set: GeomId(self: Opening) = value
"""

    InsertPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertPoint(self: Opening) -> int

Set: InsertPoint(self: Opening) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: Opening) -> ReferenceElement

Set: MasterComponent(self: Opening) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: Opening) -> int

Set: MasterPoint(self: Opening) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Opening) -> str

Set: Name(self: Opening) = value
"""

    Outline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Outline(self: Opening) -> ReferenceElement

Set: Outline(self: Opening) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Opening) -> Vector3D

Set: Position(self: Opening) = value
"""



class OpeningCirc(Opening):
    """ OpeningCirc() """
    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: OpeningCirc) -> float

Set: Diameter(self: OpeningCirc) = value
"""



class OpeningRect(Opening):
    """ OpeningRect() """
    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: OpeningRect) -> float

Set: Height(self: OpeningRect) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: OpeningRect) -> float

Set: Width(self: OpeningRect) = value
"""



class OpeningRectOffsets(Opening):
    """ OpeningRectOffsets() """
    OffsetX1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetX1(self: OpeningRectOffsets) -> float

Set: OffsetX1(self: OpeningRectOffsets) = value
"""

    OffsetX2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetX2(self: OpeningRectOffsets) -> float

Set: OffsetX2(self: OpeningRectOffsets) = value
"""

    OffsetY1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetY1(self: OpeningRectOffsets) -> float

Set: OffsetY1(self: OpeningRectOffsets) = value
"""

    OffsetY2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetY2(self: OpeningRectOffsets) -> float

Set: OffsetY2(self: OpeningRectOffsets) = value
"""

    X1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X1(self: OpeningRectOffsets) -> float

Set: X1(self: OpeningRectOffsets) = value
"""

    X2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X2(self: OpeningRectOffsets) -> float

Set: X2(self: OpeningRectOffsets) = value
"""

    Y1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y1(self: OpeningRectOffsets) -> float

Set: Y1(self: OpeningRectOffsets) = value
"""

    Y2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y2(self: OpeningRectOffsets) -> float

Set: Y2(self: OpeningRectOffsets) = value
"""



class PatchDevice(OpenElementId):
    """ PatchDevice() """
    GeomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeomId(self: PatchDevice) -> int

Set: GeomId(self: PatchDevice) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: PatchDevice) -> ReferenceElement

Set: MasterComponent(self: PatchDevice) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: PatchDevice) -> int

Set: MasterPoint(self: PatchDevice) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: PatchDevice) -> Vector3D

Set: Position(self: PatchDevice) = value
"""



class PatchLoad(PatchDevice):
    """ PatchLoad() """

class PatchSupport(PatchDevice):
    """ PatchSupport() """

class ReinfAroundOpening(ReinforcementGroup):
    """ ReinfAroundOpening() """
    AnchorLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorLength(self: ReinfAroundOpening) -> float

Set: AnchorLength(self: ReinfAroundOpening) = value
"""

    DiagonalDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalDiameter(self: ReinfAroundOpening) -> float

Set: DiagonalDiameter(self: ReinfAroundOpening) = value
"""

    DiagonalDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalDistance(self: ReinfAroundOpening) -> float

Set: DiagonalDistance(self: ReinfAroundOpening) = value
"""

    DiagonalEndsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalEndsType(self: ReinfAroundOpening) -> LongReinfEndType

Set: DiagonalEndsType(self: ReinfAroundOpening) = value
"""

    DiagonalLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalLength(self: ReinfAroundOpening) -> float

Set: DiagonalLength(self: ReinfAroundOpening) = value
"""

    DiagonalNumOfBarsInLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalNumOfBarsInLayer(self: ReinfAroundOpening) -> int

Set: DiagonalNumOfBarsInLayer(self: ReinfAroundOpening) = value
"""

    DiagonalNumOfLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalNumOfLayers(self: ReinfAroundOpening) -> int

Set: DiagonalNumOfLayers(self: ReinfAroundOpening) = value
"""

    DiagonalReinforcement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalReinforcement(self: ReinfAroundOpening) -> bool

Set: DiagonalReinforcement(self: ReinfAroundOpening) = value
"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: ReinfAroundOpening) -> float

Set: Distance(self: ReinfAroundOpening) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: ReinfAroundOpening) -> ReferenceElement

Set: MasterComponent(self: ReinfAroundOpening) = value
"""

    NumOfLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumOfLayers(self: ReinfAroundOpening) -> int

Set: NumOfLayers(self: ReinfAroundOpening) = value
"""



class ReinfBarByPolyline(ReinforcementGroup):
    """ ReinfBarByPolyline() """
    BarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarDistance(self: ReinfBarByPolyline) -> Vector3D

Set: BarDistance(self: ReinfBarByPolyline) = value
"""

    BarShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarShape(self: ReinfBarByPolyline) -> ReferenceElement

Set: BarShape(self: ReinfBarByPolyline) = value
"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: ReinfBarByPolyline) -> float

Set: Distance(self: ReinfBarByPolyline) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: ReinfBarByPolyline) -> ReferenceElement

Set: MasterComponent(self: ReinfBarByPolyline) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: ReinfBarByPolyline) -> int

Set: MasterPoint(self: ReinfBarByPolyline) = value
"""

    NumOfLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumOfLayers(self: ReinfBarByPolyline) -> int

Set: NumOfLayers(self: ReinfBarByPolyline) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ReinfBarByPolyline) -> Vector3D

Set: Position(self: ReinfBarByPolyline) = value
"""



class ReinfBarByTwoPoints(ReinforcementGroup):
    """ ReinfBarByTwoPoints() """
    BarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarDistance(self: ReinfBarByTwoPoints) -> Vector3D

Set: BarDistance(self: ReinfBarByTwoPoints) = value
"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: ReinfBarByTwoPoints) -> float

Set: Distance(self: ReinfBarByTwoPoints) = value
"""

    MasterComponent1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent1(self: ReinfBarByTwoPoints) -> ReferenceElement

Set: MasterComponent1(self: ReinfBarByTwoPoints) = value
"""

    MasterComponent2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent2(self: ReinfBarByTwoPoints) -> ReferenceElement

Set: MasterComponent2(self: ReinfBarByTwoPoints) = value
"""

    MasterPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint1(self: ReinfBarByTwoPoints) -> int

Set: MasterPoint1(self: ReinfBarByTwoPoints) = value
"""

    MasterPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint2(self: ReinfBarByTwoPoints) -> int

Set: MasterPoint2(self: ReinfBarByTwoPoints) = value
"""

    NumOfLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumOfLayers(self: ReinfBarByTwoPoints) -> int

Set: NumOfLayers(self: ReinfBarByTwoPoints) = value
"""

    Position1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position1(self: ReinfBarByTwoPoints) -> Vector3D

Set: Position1(self: ReinfBarByTwoPoints) = value
"""

    Position2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position2(self: ReinfBarByTwoPoints) -> Vector3D

Set: Position2(self: ReinfBarByTwoPoints) = value
"""



class ReinfBarInclined(ReinforcementGroup):
    """ ReinfBarInclined() """
    AddBarOnBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddBarOnBottom(self: ReinfBarInclined) -> bool

Set: AddBarOnBottom(self: ReinfBarInclined) = value
"""

    AddBarOnTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddBarOnTop(self: ReinfBarInclined) -> bool

Set: AddBarOnTop(self: ReinfBarInclined) = value
"""

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: ReinfBarInclined) -> float

Set: Angle(self: ReinfBarInclined) = value
"""

    BottomLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomLength(self: ReinfBarInclined) -> float

Set: BottomLength(self: ReinfBarInclined) = value
"""

    InclinedReinfBarType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InclinedReinfBarType(self: ReinfBarInclined) -> InclinedReinfBarType

Set: InclinedReinfBarType(self: ReinfBarInclined) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: ReinfBarInclined) -> ReferenceElement

Set: MasterComponent(self: ReinfBarInclined) = value
"""

    MasterEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterEdge(self: ReinfBarInclined) -> ReferenceElement

Set: MasterEdge(self: ReinfBarInclined) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: ReinfBarInclined) -> ReferenceElement

Set: MasterPoint(self: ReinfBarInclined) = value
"""

    TopLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopLength(self: ReinfBarInclined) -> float

Set: TopLength(self: ReinfBarInclined) = value
"""



class ReinfBarOnEdge(ReinforcementGroup):
    """ ReinfBarOnEdge() """
    AnchorLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorLength(self: ReinfBarOnEdge) -> float

Set: AnchorLength(self: ReinfBarOnEdge) = value
"""

    BarDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarDistance(self: ReinfBarOnEdge) -> Vector3D

Set: BarDistance(self: ReinfBarOnEdge) = value
"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: ReinfBarOnEdge) -> float

Set: Distance(self: ReinfBarOnEdge) = value
"""

    EdgePositionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgePositionType(self: ReinfBarOnEdge) -> EdgePositionType

Set: EdgePositionType(self: ReinfBarOnEdge) = value
"""

    ExtendDistanceBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendDistanceBegin(self: ReinfBarOnEdge) -> float

Set: ExtendDistanceBegin(self: ReinfBarOnEdge) = value
"""

    ExtendDistanceEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendDistanceEnd(self: ReinfBarOnEdge) -> float

Set: ExtendDistanceEnd(self: ReinfBarOnEdge) = value
"""

    ExtendTypeBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendTypeBegin(self: ReinfBarOnEdge) -> BarEndExtendType

Set: ExtendTypeBegin(self: ReinfBarOnEdge) = value
"""

    ExtendTypeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendTypeEnd(self: ReinfBarOnEdge) -> BarEndExtendType

Set: ExtendTypeEnd(self: ReinfBarOnEdge) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: ReinfBarOnEdge) -> float

Set: Length(self: ReinfBarOnEdge) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: ReinfBarOnEdge) -> ReferenceElement

Set: MasterComponent(self: ReinfBarOnEdge) = value
"""

    MasterEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterEdge(self: ReinfBarOnEdge) -> ReferenceElement

Set: MasterEdge(self: ReinfBarOnEdge) = value
"""

    NumOfLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumOfLayers(self: ReinfBarOnEdge) -> int

Set: NumOfLayers(self: ReinfBarOnEdge) = value
"""

    PositionOnEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PositionOnEdge(self: ReinfBarOnEdge) -> float

Set: PositionOnEdge(self: ReinfBarOnEdge) = value
"""



class ReinfBarOnMoreEdges(ReinforcementGroup):
    """ ReinfBarOnMoreEdges() """
    Covers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Covers(self: ReinfBarOnMoreEdges) -> List[float]

Set: Covers(self: ReinfBarOnMoreEdges) = value
"""

    LengthFromFirstIntersection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthFromFirstIntersection(self: ReinfBarOnMoreEdges) -> float

Set: LengthFromFirstIntersection(self: ReinfBarOnMoreEdges) = value
"""

    LengthFromLastIntersection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthFromLastIntersection(self: ReinfBarOnMoreEdges) -> float

Set: LengthFromLastIntersection(self: ReinfBarOnMoreEdges) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: ReinfBarOnMoreEdges) -> ReferenceElement

Set: MasterComponent(self: ReinfBarOnMoreEdges) = value
"""

    MasterEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterEdges(self: ReinfBarOnMoreEdges) -> List[ReferenceElement]

Set: MasterEdges(self: ReinfBarOnMoreEdges) = value
"""

    WholeFirstEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WholeFirstEdge(self: ReinfBarOnMoreEdges) -> bool

Set: WholeFirstEdge(self: ReinfBarOnMoreEdges) = value
"""

    WholeLastEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WholeLastEdge(self: ReinfBarOnMoreEdges) -> bool

Set: WholeLastEdge(self: ReinfBarOnMoreEdges) = value
"""



class ReinfFabric(Reinforcement):
    """ ReinfFabric() """
    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: ReinfFabric) -> float

Set: Angle(self: ReinfFabric) = value
"""

    Cover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cover(self: ReinfFabric) -> float

Set: Cover(self: ReinfFabric) = value
"""

    CoverFromSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoverFromSetting(self: ReinfFabric) -> bool

Set: CoverFromSetting(self: ReinfFabric) = value
"""

    DiameterX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiameterX(self: ReinfFabric) -> float

Set: DiameterX(self: ReinfFabric) = value
"""

    DiameterY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiameterY(self: ReinfFabric) -> float

Set: DiameterY(self: ReinfFabric) = value
"""

    DistanceX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceX(self: ReinfFabric) -> float

Set: DistanceX(self: ReinfFabric) = value
"""

    DistanceY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceY(self: ReinfFabric) -> float

Set: DistanceY(self: ReinfFabric) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: ReinfFabric) -> ReferenceElement

Set: MasterComponent(self: ReinfFabric) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: ReinfFabric) -> int

Set: Number(self: ReinfFabric) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ReinfFabric) -> Vector3D

Set: Position(self: ReinfFabric) = value
"""

    SeparatelyPerWall = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SeparatelyPerWall(self: ReinfFabric) -> bool

Set: SeparatelyPerWall(self: ReinfFabric) = value
"""



class TypeEdgePosition(Enum, IComparable, IFormattable, IConvertible):
    """ enum TypeEdgePosition, values: PartEdge (1), PartEdgeFromEnd (4), PartEdgeToEndEdge (2), PartEdgeToSegment (3), WholeLength (0) """
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

    PartEdge = None
    PartEdgeFromEnd = None
    PartEdgeToEndEdge = None
    PartEdgeToSegment = None
    value__ = None
    WholeLength = None


class Wall(Element2D, IGeometryPart):
    """ Wall() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Wall) -> List[ReferenceElement]

Set: Edges(self: Wall) = value
"""

    GeomId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeomId(self: Wall) -> int

Set: GeomId(self: Wall) = value
"""

    InsertPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertPoint(self: Wall) -> int

Set: InsertPoint(self: Wall) = value
"""

    MasterComponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterComponent(self: Wall) -> ReferenceElement

Set: MasterComponent(self: Wall) = value
"""

    MasterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterPoint(self: Wall) -> int

Set: MasterPoint(self: Wall) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Wall) -> Vector3D

Set: Position(self: Wall) = value
"""



class WallRect(Wall, IGeometryPart):
    """ WallRect() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: WallRect) -> float

Set: Height(self: WallRect) = value
"""

    Offset1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset1(self: WallRect) -> float

Set: Offset1(self: WallRect) = value
"""

    Offset2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset2(self: WallRect) -> float

Set: Offset2(self: WallRect) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: WallRect) -> float

Set: Width(self: WallRect) = value
"""



# variables with complex values

