# encoding: utf-8
# module IdeaRS.OpenModel.Model calls itself Model
# from IdeaRS.OpenModel, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Alignment(Enum, IComparable, IFormattable, IConvertible):
    """ enum Alignment, values: Bottom (2), BottomLeft (7), BottomRight (8), Center (0), Left (3), Right (4), Top (1), TopLeft (5), TopRight (6) """
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

    Bottom = None
    BottomLeft = None
    BottomRight = None
    Center = None
    Left = None
    Right = None
    Top = None
    TopLeft = None
    TopRight = None
    value__ = None


class Tendon(OpenElementId):
    # no doc
    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: Tendon) -> ReferenceElement

Set: Material(self: Tendon) = value
"""

    NumberOfStrand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfStrand(self: Tendon) -> int

Set: NumberOfStrand(self: Tendon) = value
"""



class BondedTendon(Tendon):
    """ BondedTendon() """
    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: BondedTendon) -> Polygon3D

Set: Geometry(self: BondedTendon) = value
"""



class CheckMember(OpenElementId):
    """ CheckMember() """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CheckMember) -> str

Set: Name(self: CheckMember) = value
"""



class CheckMember1D(CheckMember):
    """ CheckMember1D() """

class DesignMember(OpenElementId):
    """ DesignMember() """
    Members = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Members(self: DesignMember) -> List[ReferenceElement]

Set: Members(self: DesignMember) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DesignMember) -> str

Set: Name(self: DesignMember) = value
"""



class DesignMemberInSubStructure(OpenObject):
    """ DesignMemberInSubStructure() """
    DesignMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignMember(self: DesignMemberInSubStructure) -> ReferenceElement

Set: DesignMember(self: DesignMemberInSubStructure) = value
"""



class Element1D(OpenElementId):
    """ Element1D() """
    CrossSectionBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionBegin(self: Element1D) -> ReferenceElement

Set: CrossSectionBegin(self: Element1D) = value
"""

    CrossSectionEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionEnd(self: Element1D) -> ReferenceElement

Set: CrossSectionEnd(self: Element1D) = value
"""

    EccentricityBeginX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EccentricityBeginX(self: Element1D) -> float

Set: EccentricityBeginX(self: Element1D) = value
"""

    EccentricityBeginY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EccentricityBeginY(self: Element1D) -> float

Set: EccentricityBeginY(self: Element1D) = value
"""

    EccentricityBeginZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EccentricityBeginZ(self: Element1D) -> float

Set: EccentricityBeginZ(self: Element1D) = value
"""

    EccentricityEndX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EccentricityEndX(self: Element1D) -> float

Set: EccentricityEndX(self: Element1D) = value
"""

    EccentricityEndY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EccentricityEndY(self: Element1D) -> float

Set: EccentricityEndY(self: Element1D) = value
"""

    EccentricityEndZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EccentricityEndZ(self: Element1D) -> float

Set: EccentricityEndZ(self: Element1D) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Element1D) -> str

Set: Name(self: Element1D) = value
"""

    RotationRx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationRx(self: Element1D) -> float

Set: RotationRx(self: Element1D) = value
"""

    Segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segment(self: Element1D) -> ReferenceElement

Set: Segment(self: Element1D) = value
"""



class Element2D(OpenElementId):
    """ Element2D() """
    EccentricityZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EccentricityZ(self: Element2D) -> float

Set: EccentricityZ(self: Element2D) = value
"""

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: Element2D) -> Element2DType

Set: ElementType(self: Element2D) = value
"""

    GeometricRegion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometricRegion(self: Element2D) -> ReferenceElement

Set: GeometricRegion(self: Element2D) = value
"""

    InnerLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerLines(self: Element2D) -> List[ReferenceElement]

Set: InnerLines(self: Element2D) = value
"""

    InnerPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerPoints(self: Element2D) -> List[ReferenceElement]

Set: InnerPoints(self: Element2D) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: Element2D) -> ReferenceElement

Set: Material(self: Element2D) = value
"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thickness(self: Element2D) -> float

Set: Thickness(self: Element2D) = value
"""



class Element2DType(Enum, IComparable, IFormattable, IConvertible):
    """ enum Element2DType, values: Shell (0), Slab (1), Wall (2) """
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

    Shell = None
    Slab = None
    value__ = None
    Wall = None


class HingeElement1D(OpenElementId):
    """ HingeElement1D() """
    HingeTypeRX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeTypeRX(self: HingeElement1D) -> HingeTypeInDirrection

Set: HingeTypeRX(self: HingeElement1D) = value
"""

    HingeTypeRY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeTypeRY(self: HingeElement1D) -> HingeTypeInDirrection

Set: HingeTypeRY(self: HingeElement1D) = value
"""

    HingeTypeRZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeTypeRZ(self: HingeElement1D) -> HingeTypeInDirrection

Set: HingeTypeRZ(self: HingeElement1D) = value
"""

    HingeTypeX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeTypeX(self: HingeElement1D) -> HingeTypeInDirrection

Set: HingeTypeX(self: HingeElement1D) = value
"""

    HingeTypeY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeTypeY(self: HingeElement1D) -> HingeTypeInDirrection

Set: HingeTypeY(self: HingeElement1D) = value
"""

    HingeTypeZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeTypeZ(self: HingeElement1D) -> HingeTypeInDirrection

Set: HingeTypeZ(self: HingeElement1D) = value
"""

    InitialStiffnessRX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialStiffnessRX(self: HingeElement1D) -> float

Set: InitialStiffnessRX(self: HingeElement1D) = value
"""

    InitialStiffnessRY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialStiffnessRY(self: HingeElement1D) -> float

Set: InitialStiffnessRY(self: HingeElement1D) = value
"""

    InitialStiffnessRZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialStiffnessRZ(self: HingeElement1D) -> float

Set: InitialStiffnessRZ(self: HingeElement1D) = value
"""

    InitialStiffnessX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialStiffnessX(self: HingeElement1D) -> float

Set: InitialStiffnessX(self: HingeElement1D) = value
"""

    InitialStiffnessY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialStiffnessY(self: HingeElement1D) -> float

Set: InitialStiffnessY(self: HingeElement1D) = value
"""

    InitialStiffnessZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialStiffnessZ(self: HingeElement1D) -> float

Set: InitialStiffnessZ(self: HingeElement1D) = value
"""



class HingeTypeInDirrection(Enum, IComparable, IFormattable, IConvertible):
    """ enum HingeTypeInDirrection, values: Flexible (2), FullHinge (1), NoHinge (0), Nonlinear (3) """
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

    Flexible = None
    FullHinge = None
    NoHinge = None
    Nonlinear = None
    value__ = None


class InitialImperfectionOfPoint(OpenElementId):
    """ InitialImperfectionOfPoint() """
    Displacement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Displacement(self: InitialImperfectionOfPoint) -> Vector3D

Set: Displacement(self: InitialImperfectionOfPoint) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: InitialImperfectionOfPoint) -> ReferenceElement

Set: Point(self: InitialImperfectionOfPoint) = value
"""



class LineSupportSegment(OpenElementId):
    """ LineSupportSegment() """
    FlexibleStiffnessRX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessRX(self: LineSupportSegment) -> float

Set: FlexibleStiffnessRX(self: LineSupportSegment) = value
"""

    FlexibleStiffnessRY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessRY(self: LineSupportSegment) -> float

Set: FlexibleStiffnessRY(self: LineSupportSegment) = value
"""

    FlexibleStiffnessRZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessRZ(self: LineSupportSegment) -> float

Set: FlexibleStiffnessRZ(self: LineSupportSegment) = value
"""

    FlexibleStiffnessX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessX(self: LineSupportSegment) -> float

Set: FlexibleStiffnessX(self: LineSupportSegment) = value
"""

    FlexibleStiffnessY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessY(self: LineSupportSegment) -> float

Set: FlexibleStiffnessY(self: LineSupportSegment) = value
"""

    FlexibleStiffnessZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessZ(self: LineSupportSegment) -> float

Set: FlexibleStiffnessZ(self: LineSupportSegment) = value
"""

    LocalCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalCoordinateSystem(self: LineSupportSegment) -> CoordSystem

Set: LocalCoordinateSystem(self: LineSupportSegment) = value
"""

    Segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segment(self: LineSupportSegment) -> ReferenceElement

Set: Segment(self: LineSupportSegment) = value
"""

    SupportTypeRX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeRX(self: LineSupportSegment) -> SupportTypeInDirrection

Set: SupportTypeRX(self: LineSupportSegment) = value
"""

    SupportTypeRY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeRY(self: LineSupportSegment) -> SupportTypeInDirrection

Set: SupportTypeRY(self: LineSupportSegment) = value
"""

    SupportTypeRZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeRZ(self: LineSupportSegment) -> SupportTypeInDirrection

Set: SupportTypeRZ(self: LineSupportSegment) = value
"""

    SupportTypeX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeX(self: LineSupportSegment) -> SupportTypeInDirrection

Set: SupportTypeX(self: LineSupportSegment) = value
"""

    SupportTypeY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeY(self: LineSupportSegment) -> SupportTypeInDirrection

Set: SupportTypeY(self: LineSupportSegment) = value
"""

    SupportTypeZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeZ(self: LineSupportSegment) -> SupportTypeInDirrection

Set: SupportTypeZ(self: LineSupportSegment) = value
"""



class Member1D(OpenElementId):
    """ Member1D() """
    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alignment(self: Member1D) -> Alignment

Set: Alignment(self: Member1D) = value
"""

    CrossSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSection(self: Member1D) -> ReferenceElement

Set: CrossSection(self: Member1D) = value
"""

    Elements1D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elements1D(self: Member1D) -> List[ReferenceElement]

Set: Elements1D(self: Member1D) = value
"""

    HingeBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeBegin(self: Member1D) -> ReferenceElement

Set: HingeBegin(self: Member1D) = value
"""

    HingeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HingeEnd(self: Member1D) -> ReferenceElement

Set: HingeEnd(self: Member1D) = value
"""

    Member1DType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Member1DType(self: Member1D) -> Member1DType

Set: Member1DType(self: Member1D) = value
"""

    MirrorY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MirrorY(self: Member1D) -> bool

Set: MirrorY(self: Member1D) = value
"""

    MirrorZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MirrorZ(self: Member1D) -> bool

Set: MirrorZ(self: Member1D) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Member1D) -> str

Set: Name(self: Member1D) = value
"""

    Taper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Taper(self: Member1D) -> ReferenceElement

Set: Taper(self: Member1D) = value
"""



class Member1DType(Enum, IComparable, IFormattable, IConvertible):
    """ enum Member1DType, values: Beam (0), BeamSlab (4), Column (1), Rib (3), Truss (2) """
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
    Rib = None
    Truss = None
    value__ = None


class Member2D(OpenElementId):
    """ Member2D() """
    Elements2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elements2D(self: Member2D) -> List[ReferenceElement]

Set: Elements2D(self: Member2D) = value
"""

    Members1D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Members1D(self: Member2D) -> List[ReferenceElement]

Set: Members1D(self: Member2D) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Member2D) -> str

Set: Name(self: Member2D) = value
"""



class PointSupportNode(OpenElementId):
    """ PointSupportNode() """
    FlexibleStiffnessRX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessRX(self: PointSupportNode) -> float

Set: FlexibleStiffnessRX(self: PointSupportNode) = value
"""

    FlexibleStiffnessRY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessRY(self: PointSupportNode) -> float

Set: FlexibleStiffnessRY(self: PointSupportNode) = value
"""

    FlexibleStiffnessRZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessRZ(self: PointSupportNode) -> float

Set: FlexibleStiffnessRZ(self: PointSupportNode) = value
"""

    FlexibleStiffnessX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessX(self: PointSupportNode) -> float

Set: FlexibleStiffnessX(self: PointSupportNode) = value
"""

    FlexibleStiffnessY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessY(self: PointSupportNode) -> float

Set: FlexibleStiffnessY(self: PointSupportNode) = value
"""

    FlexibleStiffnessZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlexibleStiffnessZ(self: PointSupportNode) -> float

Set: FlexibleStiffnessZ(self: PointSupportNode) = value
"""

    LocalCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalCoordinateSystem(self: PointSupportNode) -> CoordSystemByVector

Set: LocalCoordinateSystem(self: PointSupportNode) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: PointSupportNode) -> ReferenceElement

Set: Point(self: PointSupportNode) = value
"""

    SupportTypeRX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeRX(self: PointSupportNode) -> SupportTypeInDirrection

Set: SupportTypeRX(self: PointSupportNode) = value
"""

    SupportTypeRY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeRY(self: PointSupportNode) -> SupportTypeInDirrection

Set: SupportTypeRY(self: PointSupportNode) = value
"""

    SupportTypeRZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeRZ(self: PointSupportNode) -> SupportTypeInDirrection

Set: SupportTypeRZ(self: PointSupportNode) = value
"""

    SupportTypeX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeX(self: PointSupportNode) -> SupportTypeInDirrection

Set: SupportTypeX(self: PointSupportNode) = value
"""

    SupportTypeY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeY(self: PointSupportNode) -> SupportTypeInDirrection

Set: SupportTypeY(self: PointSupportNode) = value
"""

    SupportTypeZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportTypeZ(self: PointSupportNode) -> SupportTypeInDirrection

Set: SupportTypeZ(self: PointSupportNode) = value
"""



class PretensionedTendonGroup(Tendon):
    """ PretensionedTendonGroup() """
    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: PretensionedTendonGroup) -> List[PretensionedTendonGroupItem]

Set: Items(self: PretensionedTendonGroup) = value
"""



class PretensionedTendonGroupItem(Tendon):
    """ PretensionedTendonGroupItem() """
    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: PretensionedTendonGroupItem) -> Polygon3D

Set: Geometry(self: PretensionedTendonGroupItem) = value
"""



class RebarBase(OpenElementId):
    # no doc
    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: RebarBase) -> float

Set: Diameter(self: RebarBase) = value
"""

    GroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupId(self: RebarBase) -> int

Set: GroupId(self: RebarBase) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: RebarBase) -> ReferenceElement

Set: Material(self: RebarBase) = value
"""

    RebarAllocationElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarAllocationElement(self: RebarBase) -> ReferenceElement

Set: RebarAllocationElement(self: RebarBase) = value
"""

    RebarParentElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarParentElement(self: RebarBase) -> ReferenceElement

Set: RebarParentElement(self: RebarBase) = value
"""

    RebarShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarShape(self: RebarBase) -> ReferenceElement

Set: RebarShape(self: RebarBase) = value
"""



class RebarGeneral(RebarBase):
    """ RebarGeneral() """
    PlaneNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaneNormal(self: RebarGeneral) -> Vector3D

Set: PlaneNormal(self: RebarGeneral) = value
"""

    RebarType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebarType(self: RebarGeneral) -> RebarGeneralType

Set: RebarType(self: RebarGeneral) = value
"""



class RebarGeneralType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RebarGeneralType, values: NotDefined (0), Single (1), Stirrup (2) """
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

    NotDefined = None
    Single = None
    Stirrup = None
    value__ = None


class RebarHookBase(OpenObject):
    # no doc
    AxisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisY(self: RebarHookBase) -> Vector3D

Set: AxisY(self: RebarHookBase) = value
"""

    Reverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reverse(self: RebarHookBase) -> bool

Set: Reverse(self: RebarHookBase) = value
"""



class RebarHookBend(RebarHookBase):
    """ RebarHookBend() """
    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: RebarHookBend) -> float

Set: Angle(self: RebarHookBend) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: RebarHookBend) -> float

Set: Length(self: RebarHookBend) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: RebarHookBend) -> float

Set: Radius(self: RebarHookBend) = value
"""



class RebarPatternBase(OpenElementId):
    # no doc
    EndPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPosition(self: RebarPatternBase) -> float

Set: EndPosition(self: RebarPatternBase) = value
"""

    Relative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Relative(self: RebarPatternBase) -> bool

Set: Relative(self: RebarPatternBase) = value
"""

    StartPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPosition(self: RebarPatternBase) -> float

Set: StartPosition(self: RebarPatternBase) = value
"""



class RebarPoint3D(Point3D):
    """ RebarPoint3D() """
    BendRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BendRadius(self: RebarPoint3D) -> float

Set: BendRadius(self: RebarPoint3D) = value
"""



class RebarPolyLine3D(OpenObject):
    """ RebarPolyLine3D() """
    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: RebarPolyLine3D) -> List[RebarSegment3DBase]

Set: Segments(self: RebarPolyLine3D) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: RebarPolyLine3D) -> RebarPoint3D

Set: StartPoint(self: RebarPolyLine3D) = value
"""



class RebarSegment3DBase(OpenObject):
    # no doc
    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: RebarSegment3DBase) -> RebarPoint3D

Set: EndPoint(self: RebarSegment3DBase) = value
"""



class RebarSegment3DArc3Pts(RebarSegment3DBase):
    """ RebarSegment3DArc3Pts() """
    ThirdPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThirdPoint(self: RebarSegment3DArc3Pts) -> Point3D

Set: ThirdPoint(self: RebarSegment3DArc3Pts) = value
"""



class RebarSegment3DLine(RebarSegment3DBase):
    """ RebarSegment3DLine() """

class RebarShape(OpenElementId):
    """ RebarShape() """
    EndHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndHook(self: RebarShape) -> RebarHookBase

Set: EndHook(self: RebarShape) = value
"""

    SourceGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceGeometry(self: RebarShape) -> RebarPolyLine3D

Set: SourceGeometry(self: RebarShape) = value
"""

    StartHook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartHook(self: RebarShape) -> RebarHookBase

Set: StartHook(self: RebarShape) = value
"""



class RebarSingle(RebarBase):
    """ RebarSingle() """
    RotationXrad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationXrad(self: RebarSingle) -> float

Set: RotationXrad(self: RebarSingle) = value
"""

    Translation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Translation(self: RebarSingle) -> Vector3D

Set: Translation(self: RebarSingle) = value
"""



class RebarStirrupPattern(RebarPatternBase):
    """ RebarStirrupPattern() """
    AddFirstStirrup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddFirstStirrup(self: RebarStirrupPattern) -> bool

Set: AddFirstStirrup(self: RebarStirrupPattern) = value
"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: RebarStirrupPattern) -> float

Set: Distance(self: RebarStirrupPattern) = value
"""

    Translation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Translation(self: RebarStirrupPattern) -> Vector3D

Set: Translation(self: RebarStirrupPattern) = value
"""



class RebarStirrups(RebarBase):
    """ RebarStirrups() """
    Patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Patterns(self: RebarStirrups) -> List[RebarStirrupPattern]

Set: Patterns(self: RebarStirrups) = value
"""



class RigidLink(OpenElementId):
    """ RigidLink() """
    MasterNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MasterNode(self: RigidLink) -> ReferenceElement

Set: MasterNode(self: RigidLink) = value
"""

    RigidRX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RigidRX(self: RigidLink) -> bool

Set: RigidRX(self: RigidLink) = value
"""

    RigidRY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RigidRY(self: RigidLink) -> bool

Set: RigidRY(self: RigidLink) = value
"""

    RigidRZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RigidRZ(self: RigidLink) -> bool

Set: RigidRZ(self: RigidLink) = value
"""

    RigidX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RigidX(self: RigidLink) -> bool

Set: RigidX(self: RigidLink) = value
"""

    RigidZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RigidZ(self: RigidLink) -> bool

Set: RigidZ(self: RigidLink) = value
"""

    SlaveNodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlaveNodes(self: RigidLink) -> List[ReferenceElement]

Set: SlaveNodes(self: RigidLink) = value
"""



class Span(OpenElementId):
    """ Span() """
    EndCrossSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndCrossSection(self: Span) -> ReferenceElement

Set: EndCrossSection(self: Span) = value
"""

    EndPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPosition(self: Span) -> float

Set: EndPosition(self: Span) = value
"""

    StartCrossSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCrossSection(self: Span) -> ReferenceElement

Set: StartCrossSection(self: Span) = value
"""

    StartPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPosition(self: Span) -> float

Set: StartPosition(self: Span) = value
"""



class SubStructure(OpenElementId):
    """ SubStructure() """
    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: SubStructure) -> SubStructureGeometry

Set: Geometry(self: SubStructure) = value
"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: SubStructure) -> SubStructureLoading

Set: Loading(self: SubStructure) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SubStructure) -> str

Set: Name(self: SubStructure) = value
"""



class SubStructureGeometry(OpenObject):
    """ SubStructureGeometry() """
    ConnectionPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionPoints(self: SubStructureGeometry) -> List[ReferenceElement]

Set: ConnectionPoints(self: SubStructureGeometry) = value
"""

    RealMembers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RealMembers(self: SubStructureGeometry) -> List[DesignMemberInSubStructure]

Set: RealMembers(self: SubStructureGeometry) = value
"""

    TheoreticalMembers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TheoreticalMembers(self: SubStructureGeometry) -> List[DesignMemberInSubStructure]

Set: TheoreticalMembers(self: SubStructureGeometry) = value
"""



class SubStructureLoading(OpenObject):
    """ SubStructureLoading() """
    LoadCases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCases(self: SubStructureLoading) -> List[ReferenceElement]

Set: LoadCases(self: SubStructureLoading) = value
"""



class SupportTypeInDirrection(Enum, IComparable, IFormattable, IConvertible):
    """ enum SupportTypeInDirrection, values: Flexible (2), FlexiblePressOnly (4), Free (1), Rigid (0), RigidPressOnly (3) """
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

    Flexible = None
    FlexiblePressOnly = None
    Free = None
    Rigid = None
    RigidPressOnly = None
    value__ = None


class Taper(OpenElementId):
    """ Taper() """
    Spans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spans(self: Taper) -> List[ReferenceElement]

Set: Spans(self: Taper) = value
"""



