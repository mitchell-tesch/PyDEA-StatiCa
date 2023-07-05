# encoding: utf-8
# module IdeaRS.OpenModel.Geometry3D calls itself Geometry3D
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Segment3D(OpenElementId):
    # no doc
    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Segment3D) -> ReferenceElement

Set: EndPoint(self: Segment3D) = value
"""

    LocalCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalCoordinateSystem(self: Segment3D) -> CoordSystem

Set: LocalCoordinateSystem(self: Segment3D) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Segment3D) -> ReferenceElement

Set: StartPoint(self: Segment3D) = value
"""



class ArcSegment3D(Segment3D):
    """ ArcSegment3D() """
    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: ArcSegment3D) -> ReferenceElement

Set: Point(self: ArcSegment3D) = value
"""



class CoordSystem(OpenObject):
    # no doc

class CoordSystemByPoint(CoordSystem):
    """ CoordSystemByPoint() """
    InPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InPlane(self: CoordSystemByPoint) -> Plane

Set: InPlane(self: CoordSystemByPoint) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: CoordSystemByPoint) -> Point3D

Set: Point(self: CoordSystemByPoint) = value
"""



class CoordSystemByVector(CoordSystem):
    """ CoordSystemByVector() """
    VecX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VecX(self: CoordSystemByVector) -> Vector3D

Set: VecX(self: CoordSystemByVector) = value
"""

    VecY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VecY(self: CoordSystemByVector) -> Vector3D

Set: VecY(self: CoordSystemByVector) = value
"""

    VecZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VecZ(self: CoordSystemByVector) -> Vector3D

Set: VecZ(self: CoordSystemByVector) = value
"""



class CoordSystemByZup(CoordSystem):
    """ CoordSystemByZup() """

class LineSegment3D(Segment3D):
    """ LineSegment3D() """

class Plane(Enum, IComparable, IFormattable, IConvertible):
    """ enum Plane, values: XY (0), YZ (1), ZX (2) """
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
    XY = None
    YZ = None
    ZX = None


class Point3D(OpenElementId):
    """ Point3D() """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Point3D) -> str

Set: Name(self: Point3D) = value
"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point3D) -> float

Set: X(self: Point3D) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point3D) -> float

Set: Y(self: Point3D) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Point3D) -> float

Set: Z(self: Point3D) = value
"""



class PointOnLine3D(OpenElementId):
    """ PointOnLine3D() """
    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: PointOnLine3D) -> ReferenceElement

Set: Geometry(self: PointOnLine3D) = value
"""

    IsFromStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFromStart(self: PointOnLine3D) -> bool

Set: IsFromStart(self: PointOnLine3D) = value
"""

    IsRelative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRelative(self: PointOnLine3D) -> bool

Set: IsRelative(self: PointOnLine3D) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: PointOnLine3D) -> float

Set: Position(self: PointOnLine3D) = value
"""



class Polygon3D(OpenObject):
    """ Polygon3D() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Polygon3D) -> List[Point3D]

Set: Points(self: Polygon3D) = value
"""



class PolyLine3D(OpenElementId):
    """ PolyLine3D() """
    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: PolyLine3D) -> List[ReferenceElement]

Set: Segments(self: PolyLine3D) = value
"""



class Region3D(OpenElementId):
    """ Region3D() """
    LocalCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalCoordinateSystem(self: Region3D) -> CoordSystem

Set: LocalCoordinateSystem(self: Region3D) = value
"""

    Openings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Openings(self: Region3D) -> List[ReferenceElement]

Set: Openings(self: Region3D) = value
"""

    Outline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Outline(self: Region3D) -> ReferenceElement

Set: Outline(self: Region3D) = value
"""



class Vector3D(OpenObject):
    """ Vector3D() """
    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector3D) -> float

Set: X(self: Vector3D) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector3D) -> float

Set: Y(self: Vector3D) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: Vector3D) -> float

Set: Z(self: Vector3D) = value
"""



