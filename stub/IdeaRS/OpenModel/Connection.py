# encoding: utf-8
# module IdeaRS.OpenModel.Connection calls itself Connection
# from IdeaRS.OpenModel, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BoltGrid(object):
    """ BoltGrid() """
    AnchorLen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorLen(self: BoltGrid) -> float

Set: AnchorLen(self: BoltGrid) = value
"""

    AxisX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisX(self: BoltGrid) -> Vector3D

Set: AxisX(self: BoltGrid) = value
"""

    AxisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisY(self: BoltGrid) -> Vector3D

Set: AxisY(self: BoltGrid) = value
"""

    AxisZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisZ(self: BoltGrid) -> Vector3D

Set: AxisZ(self: BoltGrid) = value
"""

    BoltAssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltAssemblyName(self: BoltGrid) -> str

Set: BoltAssemblyName(self: BoltGrid) = value
"""

    BoltAssemblyRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltAssemblyRef(self: BoltGrid) -> str

Set: BoltAssemblyRef(self: BoltGrid) = value
"""

    BoltInteraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltInteraction(self: BoltGrid) -> BoltShearType

Set: BoltInteraction(self: BoltGrid) = value
"""

    BoreHole = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoreHole(self: BoltGrid) -> float

Set: BoreHole(self: BoltGrid) = value
"""

    ConnectedPartIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectedPartIds(self: BoltGrid) -> List[str]

Set: ConnectedPartIds(self: BoltGrid) = value
"""

    ConnectedPlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectedPlates(self: BoltGrid) -> List[int]

Set: ConnectedPlates(self: BoltGrid) = value
"""

    DiagonalHeadDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiagonalHeadDiameter(self: BoltGrid) -> float

Set: DiagonalHeadDiameter(self: BoltGrid) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: BoltGrid) -> float

Set: Diameter(self: BoltGrid) = value
"""

    HeadDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadDiameter(self: BoltGrid) -> float

Set: HeadDiameter(self: BoltGrid) = value
"""

    HeadHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadHeight(self: BoltGrid) -> float

Set: HeadHeight(self: BoltGrid) = value
"""

    HoleDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HoleDiameter(self: BoltGrid) -> float

Set: HoleDiameter(self: BoltGrid) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BoltGrid) -> int

Set: Id(self: BoltGrid) = value
"""

    IsAnchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAnchor(self: BoltGrid) -> bool

Set: IsAnchor(self: BoltGrid) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: BoltGrid) -> str

Set: Material(self: BoltGrid) = value
"""

    NutThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NutThickness(self: BoltGrid) -> float

Set: NutThickness(self: BoltGrid) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: BoltGrid) -> Point3D

Set: Origin(self: BoltGrid) = value
"""

    Positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Positions(self: BoltGrid) -> List[Point3D]

Set: Positions(self: BoltGrid) = value
"""

    ShearInThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShearInThread(self: BoltGrid) -> bool

Set: ShearInThread(self: BoltGrid) = value
"""

    Standard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Standard(self: BoltGrid) -> str

Set: Standard(self: BoltGrid) = value
"""

    TensileStressArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TensileStressArea(self: BoltGrid) -> float

Set: TensileStressArea(self: BoltGrid) = value
"""



class AnchorGrid(BoltGrid):
    """ AnchorGrid() """
    AnchorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorType(self: AnchorGrid) -> AnchorType

Set: AnchorType(self: AnchorGrid) = value
"""

    ConcreteBlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConcreteBlock(self: AnchorGrid) -> ConcreteBlock

Set: ConcreteBlock(self: AnchorGrid) = value
"""

    WasherSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WasherSize(self: AnchorGrid) -> float

Set: WasherSize(self: AnchorGrid) = value
"""



class ApplyConnTemplateSetting(object):
    """ ApplyConnTemplateSetting() """
    DefaultBoltAssemblyID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultBoltAssemblyID(self: ApplyConnTemplateSetting) -> int

Set: DefaultBoltAssemblyID(self: ApplyConnTemplateSetting) = value
"""

    DefaultCleatCrossSectionID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultCleatCrossSectionID(self: ApplyConnTemplateSetting) -> int

Set: DefaultCleatCrossSectionID(self: ApplyConnTemplateSetting) = value
"""

    DefaultConcreteMaterialID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultConcreteMaterialID(self: ApplyConnTemplateSetting) -> int

Set: DefaultConcreteMaterialID(self: ApplyConnTemplateSetting) = value
"""

    DefaultStiffMemberCrossSectionID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultStiffMemberCrossSectionID(self: ApplyConnTemplateSetting) -> int

Set: DefaultStiffMemberCrossSectionID(self: ApplyConnTemplateSetting) = value
"""

    UseMatFromOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseMatFromOrigin(self: ApplyConnTemplateSetting) -> bool

Set: UseMatFromOrigin(self: ApplyConnTemplateSetting) = value
"""



class BeamData(OpenElementId):
    """ BeamData() """
    AddedMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddedMember(self: BeamData) -> ReferenceElement

Set: AddedMember(self: BeamData) = value
"""

    AddedMemberLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddedMemberLength(self: BeamData) -> float

Set: AddedMemberLength(self: BeamData) = value
"""

    AutoAddCutByWorkplane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoAddCutByWorkplane(self: BeamData) -> bool

Set: AutoAddCutByWorkplane(self: BeamData) = value
"""

    CrossSectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionType(self: BeamData) -> str

Set: CrossSectionType(self: BeamData) = value
"""

    Cuts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cuts(self: BeamData) -> List[CutData]

Set: Cuts(self: BeamData) = value
"""

    IsAdded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAdded(self: BeamData) -> bool

Set: IsAdded(self: BeamData) = value
"""

    IsBearingMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBearingMember(self: BeamData) -> bool

Set: IsBearingMember(self: BeamData) = value
"""

    IsNegativeObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNegativeObject(self: BeamData) -> bool

Set: IsNegativeObject(self: BeamData) = value
"""

    MirrorY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MirrorY(self: BeamData) -> bool

Set: MirrorY(self: BeamData) = value
"""

    MprlName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MprlName(self: BeamData) -> str

Set: MprlName(self: BeamData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BeamData) -> str

Set: Name(self: BeamData) = value
"""

    OriginalModelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalModelId(self: BeamData) -> str

Set: OriginalModelId(self: BeamData) = value
"""

    Plates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plates(self: BeamData) -> List[PlateData]

Set: Plates(self: BeamData) = value
"""

    RefLineInCenterOfGravity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefLineInCenterOfGravity(self: BeamData) -> bool

Set: RefLineInCenterOfGravity(self: BeamData) = value
"""



class BeamLoadsImportMappingData(object):
    """ BeamLoadsImportMappingData() """
    BeamID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamID(self: BeamLoadsImportMappingData) -> int

Set: BeamID(self: BeamLoadsImportMappingData) = value
"""

    CADBeamID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CADBeamID(self: BeamLoadsImportMappingData) -> int

Set: CADBeamID(self: BeamLoadsImportMappingData) = value
"""

    CoeffVM_X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoeffVM_X(self: BeamLoadsImportMappingData) -> float

Set: CoeffVM_X(self: BeamLoadsImportMappingData) = value
"""

    CoeffVM_Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoeffVM_Y(self: BeamLoadsImportMappingData) -> float

Set: CoeffVM_Y(self: BeamLoadsImportMappingData) = value
"""

    CoeffVM_Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoeffVM_Z(self: BeamLoadsImportMappingData) -> float

Set: CoeffVM_Z(self: BeamLoadsImportMappingData) = value
"""



class BendData(object):
    """ BendData() """
    EndFaceNormal1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFaceNormal1(self: BendData) -> Vector3D

Set: EndFaceNormal1(self: BendData) = value
"""

    Plate1Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plate1Id(self: BendData) -> int

Set: Plate1Id(self: BendData) = value
"""

    Plate2Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plate2Id(self: BendData) -> int

Set: Plate2Id(self: BendData) = value
"""

    Point1OfSideBoundary1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point1OfSideBoundary1(self: BendData) -> Point3D

Set: Point1OfSideBoundary1(self: BendData) = value
"""

    Point1OfSideBoundary2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point1OfSideBoundary2(self: BendData) -> Point3D

Set: Point1OfSideBoundary2(self: BendData) = value
"""

    Point2OfSideBoundary1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point2OfSideBoundary1(self: BendData) -> Point3D

Set: Point2OfSideBoundary1(self: BendData) = value
"""

    Point2OfSideBoundary2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point2OfSideBoundary2(self: BendData) -> Point3D

Set: Point2OfSideBoundary2(self: BendData) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: BendData) -> float

Set: Radius(self: BendData) = value
"""



class CheckResAnchor(object):
    """ CheckResAnchor() """
    CheckStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckStatus(self: CheckResAnchor) -> bool

Set: CheckStatus(self: CheckResAnchor) = value
"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCaseId(self: CheckResAnchor) -> int

Set: LoadCaseId(self: CheckResAnchor) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CheckResAnchor) -> str

Set: Name(self: CheckResAnchor) = value
"""

    UnityCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnityCheck(self: CheckResAnchor) -> float

Set: UnityCheck(self: CheckResAnchor) = value
"""



class CheckResBolt(object):
    """ CheckResBolt() """
    CheckStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckStatus(self: CheckResBolt) -> bool

Set: CheckStatus(self: CheckResBolt) = value
"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCaseId(self: CheckResBolt) -> int

Set: LoadCaseId(self: CheckResBolt) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CheckResBolt) -> str

Set: Name(self: CheckResBolt) = value
"""

    UnityCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnityCheck(self: CheckResBolt) -> float

Set: UnityCheck(self: CheckResBolt) = value
"""



class CheckResConcreteBlock(object):
    """ CheckResConcreteBlock() """
    CheckStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckStatus(self: CheckResConcreteBlock) -> bool

Set: CheckStatus(self: CheckResConcreteBlock) = value
"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCaseId(self: CheckResConcreteBlock) -> int

Set: LoadCaseId(self: CheckResConcreteBlock) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CheckResConcreteBlock) -> str

Set: Name(self: CheckResConcreteBlock) = value
"""

    UnityCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnityCheck(self: CheckResConcreteBlock) -> float

Set: UnityCheck(self: CheckResConcreteBlock) = value
"""



class CheckResPlate(object):
    """ CheckResPlate() """
    CheckStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckStatus(self: CheckResPlate) -> bool

Set: CheckStatus(self: CheckResPlate) = value
"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: CheckResPlate) -> List[int]

Set: Items(self: CheckResPlate) = value
"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCaseId(self: CheckResPlate) -> int

Set: LoadCaseId(self: CheckResPlate) = value
"""

    MaxStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxStrain(self: CheckResPlate) -> float

Set: MaxStrain(self: CheckResPlate) = value
"""

    MaxStress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxStress(self: CheckResPlate) -> float

Set: MaxStress(self: CheckResPlate) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CheckResPlate) -> str

Set: Name(self: CheckResPlate) = value
"""



class CheckResSummary(object):
    """ CheckResSummary() """
    CheckStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckStatus(self: CheckResSummary) -> bool

Set: CheckStatus(self: CheckResSummary) = value
"""

    CheckValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckValue(self: CheckResSummary) -> float

Set: CheckValue(self: CheckResSummary) = value
"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCaseId(self: CheckResSummary) -> int

Set: LoadCaseId(self: CheckResSummary) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CheckResSummary) -> str

Set: Name(self: CheckResSummary) = value
"""

    UnityCheckMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnityCheckMessage(self: CheckResSummary) -> str

Set: UnityCheckMessage(self: CheckResSummary) = value
"""



class CheckResWeld(object):
    """ CheckResWeld() """
    CheckStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckStatus(self: CheckResWeld) -> bool

Set: CheckStatus(self: CheckResWeld) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: CheckResWeld) -> int

Set: Id(self: CheckResWeld) = value
"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: CheckResWeld) -> List[int]

Set: Items(self: CheckResWeld) = value
"""

    LoadCaseId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadCaseId(self: CheckResWeld) -> int

Set: LoadCaseId(self: CheckResWeld) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CheckResWeld) -> str

Set: Name(self: CheckResWeld) = value
"""

    UnityCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnityCheck(self: CheckResWeld) -> float

Set: UnityCheck(self: CheckResWeld) = value
"""



class ConcreteBlock(object):
    """ ConcreteBlock() """
    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: ConcreteBlock) -> float

Set: Height(self: ConcreteBlock) = value
"""

    Lenght = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lenght(self: ConcreteBlock) -> float

Set: Lenght(self: ConcreteBlock) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: ConcreteBlock) -> str

Set: Material(self: ConcreteBlock) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: ConcreteBlock) -> float

Set: Width(self: ConcreteBlock) = value
"""



class ConcreteBlockData(object):
    """ ConcreteBlockData() """
    AxisX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisX(self: ConcreteBlockData) -> Vector3D

Set: AxisX(self: ConcreteBlockData) = value
"""

    AxisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisY(self: ConcreteBlockData) -> Vector3D

Set: AxisY(self: ConcreteBlockData) = value
"""

    AxisZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisZ(self: ConcreteBlockData) -> Vector3D

Set: AxisZ(self: ConcreteBlockData) = value
"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: ConcreteBlockData) -> Point3D

Set: Center(self: ConcreteBlockData) = value
"""

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: ConcreteBlockData) -> float

Set: Depth(self: ConcreteBlockData) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ConcreteBlockData) -> int

Set: Id(self: ConcreteBlockData) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: ConcreteBlockData) -> str

Set: Material(self: ConcreteBlockData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ConcreteBlockData) -> str

Set: Name(self: ConcreteBlockData) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: ConcreteBlockData) -> Point3D

Set: Origin(self: ConcreteBlockData) = value
"""

    OriginalModelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalModelId(self: ConcreteBlockData) -> str

Set: OriginalModelId(self: ConcreteBlockData) = value
"""

    OutlinePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutlinePoints(self: ConcreteBlockData) -> List[Point2D]

Set: OutlinePoints(self: ConcreteBlockData) = value
"""

    Region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Region(self: ConcreteBlockData) -> str

Set: Region(self: ConcreteBlockData) = value
"""



class ConnectedMember(OpenElementId):
    """ ConnectedMember() """
    IsContinuous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsContinuous(self: ConnectedMember) -> bool

Set: IsContinuous(self: ConnectedMember) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: ConnectedMember) -> float

Set: Length(self: ConnectedMember) = value
"""

    MemberId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberId(self: ConnectedMember) -> ReferenceElement

Set: MemberId(self: ConnectedMember) = value
"""

    OriginalModelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalModelId(self: ConnectedMember) -> str

Set: OriginalModelId(self: ConnectedMember) = value
"""



class ConnectionCheckRes(object):
    """ ConnectionCheckRes() """
    CheckResAnchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckResAnchor(self: ConnectionCheckRes) -> List[CheckResAnchor]

Set: CheckResAnchor(self: ConnectionCheckRes) = value
"""

    CheckResBolt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckResBolt(self: ConnectionCheckRes) -> List[CheckResBolt]

Set: CheckResBolt(self: ConnectionCheckRes) = value
"""

    CheckResConcreteBlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckResConcreteBlock(self: ConnectionCheckRes) -> List[CheckResConcreteBlock]

Set: CheckResConcreteBlock(self: ConnectionCheckRes) = value
"""

    CheckResPlate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckResPlate(self: ConnectionCheckRes) -> List[CheckResPlate]

Set: CheckResPlate(self: ConnectionCheckRes) = value
"""

    CheckResSummary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckResSummary(self: ConnectionCheckRes) -> List[CheckResSummary]

Set: CheckResSummary(self: ConnectionCheckRes) = value
"""

    CheckResWeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckResWeld(self: ConnectionCheckRes) -> List[CheckResWeld]

Set: CheckResWeld(self: ConnectionCheckRes) = value
"""

    ConnectionID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionID(self: ConnectionCheckRes) -> Guid

Set: ConnectionID(self: ConnectionCheckRes) = value
"""

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Messages(self: ConnectionCheckRes) -> OpenMessages

Set: Messages(self: ConnectionCheckRes) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ConnectionCheckRes) -> str

Set: Name(self: ConnectionCheckRes) = value
"""



class ConnectionData(object):
    """ ConnectionData() """
    AnchorGrids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorGrids(self: ConnectionData) -> List[AnchorGrid]

Set: AnchorGrids(self: ConnectionData) = value
"""

    Beams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Beams(self: ConnectionData) -> List[BeamData]

Set: Beams(self: ConnectionData) = value
"""

    BoltGrids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoltGrids(self: ConnectionData) -> List[BoltGrid]

Set: BoltGrids(self: ConnectionData) = value
"""

    ConcreteBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConcreteBlocks(self: ConnectionData) -> List[ConcreteBlockData]

Set: ConcreteBlocks(self: ConnectionData) = value
"""

    ConenctionPointId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConenctionPointId(self: ConnectionData) -> int

Set: ConenctionPointId(self: ConnectionData) = value
"""

    CutBeamByBeams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutBeamByBeams(self: ConnectionData) -> List[CutBeamByBeamData]

Set: CutBeamByBeams(self: ConnectionData) = value
"""

    FoldedPlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FoldedPlates(self: ConnectionData) -> List[FoldedPlateData]

Set: FoldedPlates(self: ConnectionData) = value
"""

    Plates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plates(self: ConnectionData) -> List[PlateData]

Set: Plates(self: ConnectionData) = value
"""

    Welds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Welds(self: ConnectionData) -> List[WeldData]

Set: Welds(self: ConnectionData) = value
"""



class ConnectionInfo(object):
    """ ConnectionInfo() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ConnectionInfo) -> str

Set: Description(self: ConnectionInfo) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ConnectionInfo) -> int

Set: Id(self: ConnectionInfo) = value
"""

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: ConnectionInfo) -> str

Set: Identifier(self: ConnectionInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ConnectionInfo) -> str

Set: Name(self: ConnectionInfo) = value
"""



class ConnectionLoadInfo(object):
    """ ConnectionLoadInfo() """
    BeamMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeamMapping(self: ConnectionLoadInfo) -> List[BeamLoadsImportMappingData]

Set: BeamMapping(self: ConnectionLoadInfo) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ConnectionLoadInfo) -> str

Set: Description(self: ConnectionLoadInfo) = value
"""



class ConnectionPoint(OpenElementId):
    """ ConnectionPoint() """
    BearingMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BearingMember(self: ConnectionPoint) -> ReferenceElement

Set: BearingMember(self: ConnectionPoint) = value
"""

    ConnectedMembers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectedMembers(self: ConnectionPoint) -> List[ConnectedMember]

Set: ConnectedMembers(self: ConnectionPoint) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ConnectionPoint) -> str

Set: Name(self: ConnectionPoint) = value
"""

    Node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Node(self: ConnectionPoint) -> ReferenceElement

Set: Node(self: ConnectionPoint) = value
"""

    NodeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeId(self: ConnectionPoint) -> int

Set: NodeId(self: ConnectionPoint) = value
"""

    NodeIdSerialize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeIdSerialize(self: ConnectionPoint) -> int

Set: NodeIdSerialize(self: ConnectionPoint) = value
"""

    ProjectFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectFileName(self: ConnectionPoint) -> str

Set: ProjectFileName(self: ConnectionPoint) = value
"""



class ConnectionResultsData(object):
    """ ConnectionResultsData() """
    ConnectionCheckRes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionCheckRes(self: ConnectionResultsData) -> List[ConnectionCheckRes]

Set: ConnectionCheckRes(self: ConnectionResultsData) = value
"""



class ConProjectInfo(object):
    """ ConProjectInfo() """
    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Author(self: ConProjectInfo) -> str

Set: Author(self: ConProjectInfo) = value
"""

    Connections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Connections(self: ConProjectInfo) -> List[ConnectionInfo]

Set: Connections(self: ConProjectInfo) = value
"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: ConProjectInfo) -> DateTime

Set: Date(self: ConProjectInfo) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ConProjectInfo) -> str

Set: Description(self: ConProjectInfo) = value
"""

    DesignCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignCode(self: ConProjectInfo) -> str

Set: DesignCode(self: ConProjectInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ConProjectInfo) -> str

Set: Name(self: ConProjectInfo) = value
"""

    ProjectNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectNumber(self: ConProjectInfo) -> str

Set: ProjectNumber(self: ConProjectInfo) = value
"""



class CutBeamByBeamData(object):
    """ CutBeamByBeamData() """
    CutPart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutPart(self: CutBeamByBeamData) -> CutPart

Set: CutPart(self: CutBeamByBeamData) = value
"""

    CuttingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CuttingObject(self: CutBeamByBeamData) -> ReferenceElement

Set: CuttingObject(self: CutBeamByBeamData) = value
"""

    IsWeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWeld(self: CutBeamByBeamData) -> bool

Set: IsWeld(self: CutBeamByBeamData) = value
"""

    Method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Method(self: CutBeamByBeamData) -> CutMethod

Set: Method(self: CutBeamByBeamData) = value
"""

    ModifiedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedObject(self: CutBeamByBeamData) -> ReferenceElement

Set: ModifiedObject(self: CutBeamByBeamData) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: CutBeamByBeamData) -> float

Set: Offset(self: CutBeamByBeamData) = value
"""

    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Orientation(self: CutBeamByBeamData) -> CutOrientation

Set: Orientation(self: CutBeamByBeamData) = value
"""

    PlaneOnCuttingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaneOnCuttingObject(self: CutBeamByBeamData) -> DistanceComparison

Set: PlaneOnCuttingObject(self: CutBeamByBeamData) = value
"""

    WeldThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldThickness(self: CutBeamByBeamData) -> float

Set: WeldThickness(self: CutBeamByBeamData) = value
"""

    WeldType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldType(self: CutBeamByBeamData) -> WeldType

Set: WeldType(self: CutBeamByBeamData) = value
"""



class CutData(object):
    """ CutData() """
    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: CutData) -> CutOrientation

Set: Direction(self: CutData) = value
"""

    NormalVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalVector(self: CutData) -> Vector3D

Set: NormalVector(self: CutData) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: CutData) -> float

Set: Offset(self: CutData) = value
"""

    PlanePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanePoint(self: CutData) -> Point3D

Set: PlanePoint(self: CutData) = value
"""



class CutMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum CutMethod, values: BoundingBox (0), Mitre (2), Surface (1), SurfaceAll (3) """
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

    BoundingBox = None
    Mitre = None
    Surface = None
    SurfaceAll = None
    value__ = None


class CutOrientation(Enum, IComparable, IFormattable, IConvertible):
    """ enum CutOrientation, values: Default (0), Parallel (1), Perpendicular (2) """
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

    Default = None
    Parallel = None
    Perpendicular = None
    value__ = None


class CutPart(Enum, IComparable, IFormattable, IConvertible):
    """ enum CutPart, values: Begin (0), End (1) """
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

    Begin = None
    End = None
    value__ = None


class DistanceComparison(Enum, IComparable, IFormattable, IConvertible):
    """ enum DistanceComparison, values: Closer (0), Farther (1), Same (2) """
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

    Closer = None
    Farther = None
    Same = None
    value__ = None


class FoldedPlateData(object):
    """ FoldedPlateData() """
    Bends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bends(self: FoldedPlateData) -> List[BendData]

Set: Bends(self: FoldedPlateData) = value
"""

    Plates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plates(self: FoldedPlateData) -> List[PlateData]

Set: Plates(self: FoldedPlateData) = value
"""



class FormulasType(Enum, IComparable, IFormattable, IConvertible):
    """ enum FormulasType, values: All (2), Disabled (0), Extreme (1) """
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

    All = None
    Disabled = None
    Extreme = None
    value__ = None


class IdeaConImportSettings(object):
    """ IdeaConImportSettings() """
    AmericanSubcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmericanSubcode(self: IdeaConImportSettings) -> str

Set: AmericanSubcode(self: IdeaConImportSettings) = value
"""

    BimAppCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BimAppCode(self: IdeaConImportSettings) -> str

Set: BimAppCode(self: IdeaConImportSettings) = value
"""

    CanChangeDesignCodeInWizard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanChangeDesignCodeInWizard(self: IdeaConImportSettings) -> bool

Set: CanChangeDesignCodeInWizard(self: IdeaConImportSettings) = value
"""

    ConnectionFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionFileName(self: IdeaConImportSettings) -> str

Set: ConnectionFileName(self: IdeaConImportSettings) = value
"""

    DefaultBoltAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultBoltAssembly(self: IdeaConImportSettings) -> str

Set: DefaultBoltAssembly(self: IdeaConImportSettings) = value
"""

    DefaultSteelMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultSteelMaterial(self: IdeaConImportSettings) -> str

Set: DefaultSteelMaterial(self: IdeaConImportSettings) = value
"""

    DefaultWeldMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultWeldMaterial(self: IdeaConImportSettings) -> str

Set: DefaultWeldMaterial(self: IdeaConImportSettings) = value
"""

    DesignCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignCode(self: IdeaConImportSettings) -> str

Set: DesignCode(self: IdeaConImportSettings) = value
"""

    ExportAllLinearCombination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportAllLinearCombination(self: IdeaConImportSettings) -> bool

Set: ExportAllLinearCombination(self: IdeaConImportSettings) = value
"""

    OnePageWizard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnePageWizard(self: IdeaConImportSettings) -> bool

Set: OnePageWizard(self: IdeaConImportSettings) = value
"""

    OrderMembersById = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderMembersById(self: IdeaConImportSettings) -> bool

Set: OrderMembersById(self: IdeaConImportSettings) = value
"""

    ProjectDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectDescription(self: IdeaConImportSettings) -> str

Set: ProjectDescription(self: IdeaConImportSettings) = value
"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectName(self: IdeaConImportSettings) -> str

Set: ProjectName(self: IdeaConImportSettings) = value
"""

    RunningApplication = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RunningApplication(self: IdeaConImportSettings) -> str

Set: RunningApplication(self: IdeaConImportSettings) = value
"""

    StartIdeaStaticaApp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartIdeaStaticaApp(self: IdeaConImportSettings) -> bool

Set: StartIdeaStaticaApp(self: IdeaConImportSettings) = value
"""

    UserWizardBrand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserWizardBrand(self: IdeaConImportSettings) -> str

Set: UserWizardBrand(self: IdeaConImportSettings) = value
"""

    UseWizard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseWizard(self: IdeaConImportSettings) -> bool

Set: UseWizard(self: IdeaConImportSettings) = value
"""

    WaitForExit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WaitForExit(self: IdeaConImportSettings) -> bool

Set: WaitForExit(self: IdeaConImportSettings) = value
"""



class IdeaSMemberImportSettings(IdeaConImportSettings):
    """ IdeaSMemberImportSettings() """

class PlateData(OpenElementId):
    """ PlateData() """
    AxisX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisX(self: PlateData) -> Vector3D

Set: AxisX(self: PlateData) = value
"""

    AxisY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisY(self: PlateData) -> Vector3D

Set: AxisY(self: PlateData) = value
"""

    AxisZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisZ(self: PlateData) -> Vector3D

Set: AxisZ(self: PlateData) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: PlateData) -> Region2D

Set: Geometry(self: PlateData) = value
"""

    IsNegativeObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNegativeObject(self: PlateData) -> bool

Set: IsNegativeObject(self: PlateData) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: PlateData) -> str

Set: Material(self: PlateData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PlateData) -> str

Set: Name(self: PlateData) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: PlateData) -> Point3D

Set: Origin(self: PlateData) = value
"""

    OriginalModelId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalModelId(self: PlateData) -> str

Set: OriginalModelId(self: PlateData) = value
"""

    OutlinePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutlinePoints(self: PlateData) -> List[Point2D]

Set: OutlinePoints(self: PlateData) = value
"""

    Region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Region(self: PlateData) -> str

Set: Region(self: PlateData) = value
"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thickness(self: PlateData) -> float

Set: Thickness(self: PlateData) = value
"""



class ReportSettings(object):
    """ ReportSettings() """
    CultureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CultureName(self: ReportSettings) -> str

Set: CultureName(self: ReportSettings) = value
"""

    Formulas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Formulas(self: ReportSettings) -> FormulasType

Set: Formulas(self: ReportSettings) = value
"""

    PlatesDrawings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlatesDrawings(self: ReportSettings) -> bool

Set: PlatesDrawings(self: ReportSettings) = value
"""

    ReportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReportType(self: ReportSettings) -> ReportType

Set: ReportType(self: ReportSettings) = value
"""

    ResultsPictures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultsPictures(self: ReportSettings) -> bool

Set: ResultsPictures(self: ReportSettings) = value
"""

    SymbolExplanations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolExplanations(self: ReportSettings) -> bool

Set: SymbolExplanations(self: ReportSettings) = value
"""

    TheoreticalBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TheoreticalBackground(self: ReportSettings) -> bool

Set: TheoreticalBackground(self: ReportSettings) = value
"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unit(self: ReportSettings) -> UnitType

Set: Unit(self: ReportSettings) = value
"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Views(self: ReportSettings) -> bool

Set: Views(self: ReportSettings) = value
"""



class ReportType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ReportType, values: Brief (0), Detailed (1) """
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

    Brief = None
    Detailed = None
    value__ = None


class UnitType(Enum, IComparable, IFormattable, IConvertible):
    """ enum UnitType, values: Imperial (1), Metric (0) """
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

    Imperial = None
    Metric = None
    value__ = None


class WeldData(object):
    """ WeldData() """
    ConnectedPartIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectedPartIds(self: WeldData) -> List[str]

Set: ConnectedPartIds(self: WeldData) = value
"""

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: End(self: WeldData) -> Point3D

Set: End(self: WeldData) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: WeldData) -> int

Set: Id(self: WeldData) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: WeldData) -> str

Set: Material(self: WeldData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: WeldData) -> str

Set: Name(self: WeldData) = value
"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Start(self: WeldData) -> Point3D

Set: Start(self: WeldData) = value
"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thickness(self: WeldData) -> float

Set: Thickness(self: WeldData) = value
"""

    WeldType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldType(self: WeldData) -> WeldType

Set: WeldType(self: WeldData) = value
"""



class WeldType(Enum, IComparable, IFormattable, IConvertible):
    """ enum WeldType, values: Bevel (4), Contact (128), DoubleFillet (2), Fillet (1), FilletRear (64), Intermittent (256), LengthAtHaunch (32), NotSpecified (0), Plug (16), Square (8) """
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
    Contact = None
    DoubleFillet = None
    Fillet = None
    FilletRear = None
    Intermittent = None
    LengthAtHaunch = None
    NotSpecified = None
    Plug = None
    Square = None
    value__ = None


