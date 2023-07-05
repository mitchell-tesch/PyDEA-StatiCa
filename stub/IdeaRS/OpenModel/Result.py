# encoding: utf-8
# module IdeaRS.OpenModel.Result calls itself Result
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AbsoluteRelative(Enum, IComparable, IFormattable, IConvertible):
    """ enum AbsoluteRelative, values: Absolute (0), Relative (1) """
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

    Absolute = None
    Relative = None
    value__ = None


class FemElement(object):
    """
    FemElement()
    FemElement(node1: int, node2: int, node3: int)
    FemElement(node1: int, node2: int, node3: int, node4: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, node1=None, node2=None, node3=None, node4=None):
        """
        __new__(cls: type)
        __new__(cls: type, node1: int, node2: int, node3: int)
        __new__(cls: type, node1: int, node2: int, node3: int, node4: int)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: FemElement) -> int

Set: Type(self: FemElement) = value
"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: FemElement) -> List[int]

Set: Vertices(self: FemElement) = value
"""



class ListOfResultOfMember(List[ResultOnMember], IList[ResultOnMember], ICollection[ResultOnMember], IEnumerable[ResultOnMember], IEnumerable, IList, ICollection, IReadOnlyList[ResultOnMember], IReadOnlyCollection[ResultOnMember]):
    """ ListOfResultOfMember() """
    def GetSchema(self):
        """ GetSchema(self: ListOfResultOfMember) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        """ ReadXml(self: ListOfResultOfMember, reader: XmlReader) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: ListOfResultOfMember, writer: XmlWriter) """
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


class Loading(object):
    """
    Loading()
    Loading(loadingType: LoadingType, id: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, loadingType=None, id=None):
        """
        __new__(cls: type)
        __new__(cls: type, loadingType: LoadingType, id: int)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Loading) -> int

Set: Id(self: Loading) = value
"""

    LoadingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadingType(self: Loading) -> LoadingType

Set: LoadingType(self: Loading) = value
"""



class LoadingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadingType, values: Combination (1), LoadCase (0), ResultClass (2) """
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

    Combination = None
    LoadCase = None
    ResultClass = None
    value__ = None


class Member(object):
    """
    Member()
    Member(memberType: MemberType, id: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, memberType=None, id=None):
        """
        __new__(cls: type)
        __new__(cls: type, memberType: MemberType, id: int)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Member) -> int

Set: Id(self: Member) = value
"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: Member) -> MemberType

Set: MemberType(self: Member) = value
"""



class MemberType(Enum, IComparable, IFormattable, IConvertible):
    """ enum MemberType, values: Element1D (1), Member1D (0) """
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

    Element1D = None
    Member1D = None
    value__ = None


class MeshElement2D(object):
    """ MeshElement2D() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: MeshElement2D) -> List[int]

Set: Points(self: MeshElement2D) = value
"""



class OpenModelResult(object):
    """ OpenModelResult() """
    @staticmethod
    def LoadFromStream(xmlFileStream):
        """ LoadFromStream(xmlFileStream: Stream) -> OpenModelResult """
        pass

    @staticmethod
    def LoadFromXmlFile(xmlFileName):
        """ LoadFromXmlFile(xmlFileName: str) -> OpenModelResult """
        pass

    def SaveToXmlFile(self, xmlFileName):
        """ SaveToXmlFile(self: OpenModelResult, xmlFileName: str) -> bool """
        pass

    ResultOnMembers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultOnMembers(self: OpenModelResult) -> List[ResultOnMembers]

Set: ResultOnMembers(self: OpenModelResult) = value
"""



class PlateElements(object):
    """
    PlateElements()
    PlateElements(count: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, count=None):
        """
        __new__(cls: type)
        __new__(cls: type, count: int)
        """
        pass

    Elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elements(self: PlateElements) -> List[FemElement]

Set: Elements(self: PlateElements) = value
"""

    PlateType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlateType(self: PlateElements) -> StructuralPlateType

Set: PlateType(self: PlateElements) = value
"""

    PlateUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlateUID(self: PlateElements) -> int

Set: PlateUID(self: PlateElements) = value
"""



class PointOfID(object):
    """ PointOfID() """
    My = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: My(self: PointOfID) -> float

Set: My(self: PointOfID) = value
"""

    Mz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mz(self: PointOfID) -> float

Set: Mz(self: PointOfID) = value
"""

    N = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: N(self: PointOfID) -> float

Set: N(self: PointOfID) = value
"""



class PointResultBase(object):
    # no doc
    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: PointResultBase) -> ResultOfLoading

Set: Loading(self: PointResultBase) = value
"""



class PointResultOfNLA(PointResultBase):
    """ PointResultOfNLA() """
    AxialForce = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialForce(self: PointResultOfNLA) -> float

Set: AxialForce(self: PointResultOfNLA) = value
"""

    AxialStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialStrain(self: PointResultOfNLA) -> float

Set: AxialStrain(self: PointResultOfNLA) = value
"""

    AxialStress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialStress(self: PointResultOfNLA) -> float

Set: AxialStress(self: PointResultOfNLA) = value
"""



class PointResultOfTA(PointResultBase):
    """ PointResultOfTA() """
    Temp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Temp(self: PointResultOfTA) -> float

Set: Temp(self: PointResultOfTA) = value
"""



class PointResults(object):
    """ PointResults() """
    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: PointResults) -> Point2D

Set: Point(self: PointResults) = value
"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: PointResults) -> List[PointResultBase]

Set: Results(self: PointResults) = value
"""



class PolygonPointID(object):
    """ PolygonPointID() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: PolygonPointID) -> List[PointOfID]

Set: Points(self: PolygonPointID) = value
"""



class ResultBase(object):
    # no doc

class ResultInSection(object):
    """ ResultInSection() """
    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ResultInSection) -> float

Set: Position(self: ResultInSection) = value
"""

    ResultOfLoading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultOfLoading(self: ResultInSection) -> List[ResultOfLoading2]

Set: ResultOfLoading(self: ResultInSection) = value
"""



class ResultLocalSystemType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ResultLocalSystemType, values: Global (1), Local (0), Principle (2) """
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

    Global = None
    Local = None
    Principle = None
    value__ = None


class SectionResultBase(object):
    # no doc
    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: SectionResultBase) -> ResultOfLoading

Set: Loading(self: SectionResultBase) = value
"""



class ResultOfDeformation(SectionResultBase):
    """ ResultOfDeformation() """
    Fix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fix(self: ResultOfDeformation) -> float

Set: Fix(self: ResultOfDeformation) = value
"""

    Fiy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fiy(self: ResultOfDeformation) -> float

Set: Fiy(self: ResultOfDeformation) = value
"""

    Fiz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fiz(self: ResultOfDeformation) -> float

Set: Fiz(self: ResultOfDeformation) = value
"""

    Ux = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ux(self: ResultOfDeformation) -> float

Set: Ux(self: ResultOfDeformation) = value
"""

    Uy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Uy(self: ResultOfDeformation) -> float

Set: Uy(self: ResultOfDeformation) = value
"""

    Uz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Uz(self: ResultOfDeformation) -> float

Set: Uz(self: ResultOfDeformation) = value
"""



class ResultOfLoading2(object):
    """ ResultOfLoading2() """

class ResultOfDeformation2(ResultOfLoading2):
    """ ResultOfDeformation2() """
    Fix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fix(self: ResultOfDeformation2) -> float

Set: Fix(self: ResultOfDeformation2) = value
"""

    Fiy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fiy(self: ResultOfDeformation2) -> float

Set: Fiy(self: ResultOfDeformation2) = value
"""

    Fiz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fiz(self: ResultOfDeformation2) -> float

Set: Fiz(self: ResultOfDeformation2) = value
"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: ResultOfDeformation2) -> Loading

Set: Loading(self: ResultOfDeformation2) = value
"""

    Ux = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ux(self: ResultOfDeformation2) -> float

Set: Ux(self: ResultOfDeformation2) = value
"""

    Uy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Uy(self: ResultOfDeformation2) -> float

Set: Uy(self: ResultOfDeformation2) = value
"""

    Uz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Uz(self: ResultOfDeformation2) -> float

Set: Uz(self: ResultOfDeformation2) = value
"""



class ResultOfIncrement(object):
    """ ResultOfIncrement() """
    AxialForce = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialForce(self: ResultOfIncrement) -> float

Set: AxialForce(self: ResultOfIncrement) = value
"""

    AxialStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialStrain(self: ResultOfIncrement) -> float

Set: AxialStrain(self: ResultOfIncrement) = value
"""

    AxialStress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialStress(self: ResultOfIncrement) -> float

Set: AxialStress(self: ResultOfIncrement) = value
"""

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: ResultOfIncrement) -> int

Set: Increment(self: ResultOfIncrement) = value
"""



class ResultOfIncrement2(object):
    """ ResultOfIncrement2() """
    AxialForce = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialForce(self: ResultOfIncrement2) -> float

Set: AxialForce(self: ResultOfIncrement2) = value
"""

    AxialStrain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialStrain(self: ResultOfIncrement2) -> float

Set: AxialStrain(self: ResultOfIncrement2) = value
"""

    AxialStress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxialStress(self: ResultOfIncrement2) -> float

Set: AxialStress(self: ResultOfIncrement2) = value
"""

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: ResultOfIncrement2) -> int

Set: Increment(self: ResultOfIncrement2) = value
"""



class ResultOfInteractionDiagramPlane(SectionResultBase):
    """ ResultOfInteractionDiagramPlane() """
    LoadChart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadChart(self: ResultOfInteractionDiagramPlane) -> PolygonPointID

Set: LoadChart(self: ResultOfInteractionDiagramPlane) = value
"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: ResultOfInteractionDiagramPlane) -> PolygonPointID

Set: Plane(self: ResultOfInteractionDiagramPlane) = value
"""



class ResultOfInternalForces(SectionResultBase):
    """ ResultOfInternalForces() """
    Mx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mx(self: ResultOfInternalForces) -> float

Set: Mx(self: ResultOfInternalForces) = value
"""

    My = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: My(self: ResultOfInternalForces) -> float

Set: My(self: ResultOfInternalForces) = value
"""

    Mz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mz(self: ResultOfInternalForces) -> float

Set: Mz(self: ResultOfInternalForces) = value
"""

    N = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: N(self: ResultOfInternalForces) -> float

Set: N(self: ResultOfInternalForces) = value
"""

    Qy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Qy(self: ResultOfInternalForces) -> float

Set: Qy(self: ResultOfInternalForces) = value
"""

    Qz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Qz(self: ResultOfInternalForces) -> float

Set: Qz(self: ResultOfInternalForces) = value
"""



class ResultOfInternalForces2(ResultOfLoading2):
    """ ResultOfInternalForces2() """
    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: ResultOfInternalForces2) -> Loading

Set: Loading(self: ResultOfInternalForces2) = value
"""

    Mx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mx(self: ResultOfInternalForces2) -> float

Set: Mx(self: ResultOfInternalForces2) = value
"""

    My = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: My(self: ResultOfInternalForces2) -> float

Set: My(self: ResultOfInternalForces2) = value
"""

    Mz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mz(self: ResultOfInternalForces2) -> float

Set: Mz(self: ResultOfInternalForces2) = value
"""

    N = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: N(self: ResultOfInternalForces2) -> float

Set: N(self: ResultOfInternalForces2) = value
"""

    Qy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Qy(self: ResultOfInternalForces2) -> float

Set: Qy(self: ResultOfInternalForces2) = value
"""

    Qz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Qz(self: ResultOfInternalForces2) -> float

Set: Qz(self: ResultOfInternalForces2) = value
"""



class ResultOfLoading(Loading):
    """ ResultOfLoading() """
    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: ResultOfLoading) -> List[ResultOfLoadingItem]

Set: Items(self: ResultOfLoading) = value
"""



class ResultOfLoadingItem(object):
    """ ResultOfLoadingItem() """
    Coefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coefficient(self: ResultOfLoadingItem) -> float

Set: Coefficient(self: ResultOfLoadingItem) = value
"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: ResultOfLoadingItem) -> Loading

Set: Loading(self: ResultOfLoadingItem) = value
"""



class ResultOfMember2(object):
    """
    ResultOfMember2()
    ResultOfMember2(member: Member)
    """
    @staticmethod # known case of __new__
    def __new__(self, member=None):
        """
        __new__(cls: type)
        __new__(cls: type, member: Member)
        """
        pass

    Member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Member(self: ResultOfMember2) -> Member

Set: Member(self: ResultOfMember2) = value
"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: ResultOfMember2) -> List[ResultInSection]

Set: Results(self: ResultOfMember2) = value
"""



class ResultOfNLA(ResultBase):
    """ ResultOfNLA() """
    Sections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sections(self: ResultOfNLA) -> List[ResultOfNLASection]

Set: Sections(self: ResultOfNLA) = value
"""



class ResultOfNLA2(ResultOfLoading2):
    """ ResultOfNLA2() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: ResultOfNLA2) -> List[ResultOfNLAPoint]

Set: Points(self: ResultOfNLA2) = value
"""



class ResultOfNLAPoint(object):
    """ ResultOfNLAPoint() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ResultOfNLAPoint) -> int

Set: Id(self: ResultOfNLAPoint) = value
"""

    ResultOfIncrements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultOfIncrements(self: ResultOfNLAPoint) -> List[ResultOfIncrement]

Set: ResultOfIncrements(self: ResultOfNLAPoint) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: ResultOfNLAPoint) -> float

Set: X(self: ResultOfNLAPoint) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: ResultOfNLAPoint) -> float

Set: Y(self: ResultOfNLAPoint) = value
"""



class ResultOfNLAPoint2(object):
    """ ResultOfNLAPoint2() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ResultOfNLAPoint2) -> int

Set: Id(self: ResultOfNLAPoint2) = value
"""

    ResultOfIncrements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultOfIncrements(self: ResultOfNLAPoint2) -> List[ResultOfIncrement2]

Set: ResultOfIncrements(self: ResultOfNLAPoint2) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: ResultOfNLAPoint2) -> float

Set: X(self: ResultOfNLAPoint2) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: ResultOfNLAPoint2) -> float

Set: Y(self: ResultOfNLAPoint2) = value
"""



class ResultOfNLASection(object):
    """ ResultOfNLASection() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: ResultOfNLASection) -> List[ResultOfNLAPoint]

Set: Points(self: ResultOfNLASection) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ResultOfNLASection) -> float

Set: Position(self: ResultOfNLASection) = value
"""



class ResultOnMember(object):
    """
    ResultOnMember()
    ResultOnMember(member: Member, resultType: ResultType)
    """
    @staticmethod # known case of __new__
    def __new__(self, member=None, resultType=None):
        """
        __new__(cls: type)
        __new__(cls: type, member: Member, resultType: ResultType)
        """
        pass

    LocalSystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalSystemType(self: ResultOnMember) -> ResultLocalSystemType

Set: LocalSystemType(self: ResultOnMember) = value
"""

    Member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Member(self: ResultOnMember) -> Member

Set: Member(self: ResultOnMember) = value
"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: ResultOnMember) -> List[ResultBase]

Set: Results(self: ResultOnMember) = value
"""

    ResultType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultType(self: ResultOnMember) -> ResultType

Set: ResultType(self: ResultOnMember) = value
"""



class ResultOnMembers(object):
    """ ResultOnMembers() """
    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: ResultOnMembers) -> Loading

Set: Loading(self: ResultOnMembers) = value
"""

    Members = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Members(self: ResultOnMembers) -> List[ResultOnMember]

Set: Members(self: ResultOnMembers) = value
"""



class ResultOnMembers2(object):
    """
    ResultOnMembers2()
    ResultOnMembers2(resultType: ResultType)
    """
    @staticmethod # known case of __new__
    def __new__(self, resultType=None):
        """
        __new__(cls: type)
        __new__(cls: type, resultType: ResultType)
        """
        pass

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: ResultOnMembers2) -> List[ResultOfMember2]

Set: Results(self: ResultOnMembers2) = value
"""

    ResultType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultType(self: ResultOnMembers2) -> ResultType

Set: ResultType(self: ResultOnMembers2) = value
"""



class ResultOnMesh(object):
    """ ResultOnMesh() """
    Displacement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Displacement(self: ResultOnMesh) -> List[Array[float]]

Set: Displacement(self: ResultOnMesh) = value
"""

    Nodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nodes(self: ResultOnMesh) -> List[Array[float]]

Set: Nodes(self: ResultOnMesh) = value
"""

    PlatesElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlatesElement(self: ResultOnMesh) -> List[PlateElements]

Set: PlatesElement(self: ResultOnMesh) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ResultOnMesh) -> List[float]

Set: Value(self: ResultOnMesh) = value
"""



class ResultOnMeshType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ResultOnMeshType, values: FondationStress (26), OverallCheck (100), Strain (22), StrainCheck (23), Stress (24) """
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

    FondationStress = None
    OverallCheck = None
    Strain = None
    StrainCheck = None
    Stress = None
    value__ = None


class ResultOnSection(ResultBase):
    """ ResultOnSection() """
    AbsoluteRelative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsoluteRelative(self: ResultOnSection) -> AbsoluteRelative

Set: AbsoluteRelative(self: ResultOnSection) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ResultOnSection) -> float

Set: Position(self: ResultOnSection) = value
"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: ResultOnSection) -> List[SectionResultBase]

Set: Results(self: ResultOnSection) = value
"""



class ResultPoint(object):
    """ ResultPoint() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ResultPoint) -> int

Set: Id(self: ResultPoint) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: ResultPoint) -> Point3D

Set: Point(self: ResultPoint) = value
"""



class ResultType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ResultType, values: CrossSectionMesh (5), CrossSectionNLA (2), CrossSectionTA (3), Deformation (1), InteractionDiagram (4), InternalForces (0) """
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

    CrossSectionMesh = None
    CrossSectionNLA = None
    CrossSectionTA = None
    Deformation = None
    InteractionDiagram = None
    InternalForces = None
    value__ = None


class SectionResultMesh(SectionResultBase):
    """ SectionResultMesh() """
    Elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elements(self: SectionResultMesh) -> List[MeshElement2D]

Set: Elements(self: SectionResultMesh) = value
"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: SectionResultMesh) -> List[Point2D]

Set: Points(self: SectionResultMesh) = value
"""



class SectionResultOnPoints(SectionResultBase):
    """ SectionResultOnPoints() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: SectionResultOnPoints) -> List[PointResults]

Set: Points(self: SectionResultOnPoints) = value
"""



class StructuralPlateType(Enum, IComparable, IFormattable, IConvertible):
    """ enum StructuralPlateType, values: SteelPlate (0), Weld (1) """
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

    SteelPlate = None
    value__ = None
    Weld = None


