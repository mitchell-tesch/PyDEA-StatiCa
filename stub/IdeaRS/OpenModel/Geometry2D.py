# encoding: utf-8
# module IdeaRS.OpenModel.Geometry2D calls itself Geometry2D
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Segment2D(OpenObject):
    # no doc
    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Segment2D) -> Point2D

Set: EndPoint(self: Segment2D) = value
"""



class ArcSegment2D(Segment2D):
    """ ArcSegment2D() """
    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: ArcSegment2D) -> Point2D

Set: Point(self: ArcSegment2D) = value
"""



class LineSegment2D(Segment2D):
    """ LineSegment2D() """

class Point(object):
    """ Point(x: float, y: float) """
    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """
        __new__(cls: type, x: float, y: float)
        __new__[Point]() -> Point
        """
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point) -> float

Set: X(self: Point) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point) -> float

Set: Y(self: Point) = value
"""



class Point2D(OpenObject):
    """ Point2D() """
    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Point2D) -> float

Set: X(self: Point2D) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Point2D) -> float

Set: Y(self: Point2D) = value
"""



class Polygon2D(OpenObject):
    """ Polygon2D() """
    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Polygon2D) -> List[Point2D]

Set: Points(self: Polygon2D) = value
"""



class PolyLine2D(OpenObject):
    """ PolyLine2D() """
    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: PolyLine2D) -> List[Segment2D]

Set: Segments(self: PolyLine2D) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: PolyLine2D) -> Point2D

Set: StartPoint(self: PolyLine2D) = value
"""



class Region2D(OpenObject):
    """ Region2D() """
    Openings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Openings(self: Region2D) -> List[PolyLine2D]

Set: Openings(self: Region2D) = value
"""

    Outline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Outline(self: Region2D) -> PolyLine2D

Set: Outline(self: Region2D) = value
"""



class SectionCharacteristics(object):
    """ SectionCharacteristics() """
    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: SectionCharacteristics) -> float

Set: A(self: SectionCharacteristics) = value
"""

    Ay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ay(self: SectionCharacteristics) -> float

Set: Ay(self: SectionCharacteristics) = value
"""

    Az = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Az(self: SectionCharacteristics) -> float

Set: Az(self: SectionCharacteristics) = value
"""

    Cgy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cgy(self: SectionCharacteristics) -> float

Set: Cgy(self: SectionCharacteristics) = value
"""

    Cgz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cgz(self: SectionCharacteristics) -> float

Set: Cgz(self: SectionCharacteristics) = value
"""

    Dyz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dyz(self: SectionCharacteristics) -> float

Set: Dyz(self: SectionCharacteristics) = value
"""

    E = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: E(self: SectionCharacteristics) -> float

Set: E(self: SectionCharacteristics) = value
"""

    It = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: It(self: SectionCharacteristics) -> float

Set: It(self: SectionCharacteristics) = value
"""

    Iw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Iw(self: SectionCharacteristics) -> float

Set: Iw(self: SectionCharacteristics) = value
"""

    Iy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Iy(self: SectionCharacteristics) -> float

Set: Iy(self: SectionCharacteristics) = value
"""

    Iz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Iz(self: SectionCharacteristics) -> float

Set: Iz(self: SectionCharacteristics) = value
"""

    Rgy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rgy(self: SectionCharacteristics) -> float

Set: Rgy(self: SectionCharacteristics) = value
"""

    Rgz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rgz(self: SectionCharacteristics) -> float

Set: Rgz(self: SectionCharacteristics) = value
"""

    Sy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sy(self: SectionCharacteristics) -> float

Set: Sy(self: SectionCharacteristics) = value
"""

    Sz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sz(self: SectionCharacteristics) -> float

Set: Sz(self: SectionCharacteristics) = value
"""

    Wely = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wely(self: SectionCharacteristics) -> float

Set: Wely(self: SectionCharacteristics) = value
"""

    Welz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Welz(self: SectionCharacteristics) -> float

Set: Welz(self: SectionCharacteristics) = value
"""

    Wply = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wply(self: SectionCharacteristics) -> float

Set: Wply(self: SectionCharacteristics) = value
"""

    Wplz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wplz(self: SectionCharacteristics) -> float

Set: Wplz(self: SectionCharacteristics) = value
"""

    Y0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y0(self: SectionCharacteristics) -> float

Set: Y0(self: SectionCharacteristics) = value
"""

    Z0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z0(self: SectionCharacteristics) -> float

Set: Z0(self: SectionCharacteristics) = value
"""



class TemperatureCurve2D(Polygon2D):
    """ TemperatureCurve2D() """
    Temperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Temperature(self: TemperatureCurve2D) -> float

Set: Temperature(self: TemperatureCurve2D) = value
"""



class Vector2D(OpenObject):
    """ Vector2D() """
    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: Vector2D) -> float

Set: X(self: Vector2D) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: Vector2D) -> float

Set: Y(self: Vector2D) = value
"""



