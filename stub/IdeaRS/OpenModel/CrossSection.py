# encoding: utf-8
# module IdeaRS.OpenModel.CrossSection calls itself CrossSection
# from IdeaRS.OpenModel, Version=22.1.5.1060, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BoxDeltaAligment(Enum, IComparable, IFormattable, IConvertible):
    """ enum BoxDeltaAligment, values: Center (0), Left (1), Right (2) """
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

    Center = None
    Left = None
    Right = None
    value__ = None


class CrossSection(OpenElementId):
    """ CrossSection() """
    CrossSectionRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionRotation(self: CrossSection) -> float

Set: CrossSectionRotation(self: CrossSection) = value
"""

    IsInPrincipal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInPrincipal(self: CrossSection) -> bool

Set: IsInPrincipal(self: CrossSection) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CrossSection) -> str

Set: Name(self: CrossSection) = value
"""



class CrossSectionComponent(CrossSection):
    """ CrossSectionComponent() """
    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Components(self: CrossSectionComponent) -> List[CssComponent]

Set: Components(self: CrossSectionComponent) = value
"""



class CrossSectionComponentThermalData(object):
    """ CrossSectionComponentThermalData() """
    ComponentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentIndex(self: CrossSectionComponentThermalData) -> int

Set: ComponentIndex(self: CrossSectionComponentThermalData) = value
"""

    MoistureContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MoistureContent(self: CrossSectionComponentThermalData) -> float

Set: MoistureContent(self: CrossSectionComponentThermalData) = value
"""

    ThermalConductivityLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalConductivityLimit(self: CrossSectionComponentThermalData) -> ThermalConductivityLimit

Set: ThermalConductivityLimit(self: CrossSectionComponentThermalData) = value
"""



class CrossSectionCreepCoefficientAttribute(OpenAttribute):
    """ CrossSectionCreepCoefficientAttribute() """
    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Components(self: CrossSectionCreepCoefficientAttribute) -> List[CrossSectionCreepCoefficientData]

Set: Components(self: CrossSectionCreepCoefficientAttribute) = value
"""



class CrossSectionCreepCoefficientData(object):
    """ CrossSectionCreepCoefficientData() """
    ComponentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentIndex(self: CrossSectionCreepCoefficientData) -> List[int]

Set: ComponentIndex(self: CrossSectionCreepCoefficientData) = value
"""

    CreepInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreepInput(self: CrossSectionCreepCoefficientData) -> InputValueType

Set: CreepInput(self: CrossSectionCreepCoefficientData) = value
"""

    Humidity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Humidity(self: CrossSectionCreepCoefficientData) -> float

Set: Humidity(self: CrossSectionCreepCoefficientData) = value
"""

    NotionalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NotionalSize(self: CrossSectionCreepCoefficientData) -> float

Set: NotionalSize(self: CrossSectionCreepCoefficientData) = value
"""

    NotionalSizeInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NotionalSizeInput(self: CrossSectionCreepCoefficientData) -> InputValueType

Set: NotionalSizeInput(self: CrossSectionCreepCoefficientData) = value
"""

    UserCreepCoeeficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserCreepCoeeficient(self: CrossSectionCreepCoefficientData) -> Polygon2D

Set: UserCreepCoeeficient(self: CrossSectionCreepCoefficientData) = value
"""



class CrossSectionFactory(object):
    # no doc
    @staticmethod
    def FillBox2(css, bu, bb, hw, b1, tw, tfu, tfb):
        """ FillBox2(css: CrossSectionParameter, bu: float, bb: float, hw: float, b1: float, tw: float, tfu: float, tfb: float) """
        pass

    @staticmethod
    def FillBoxWeb(css, bu, bb, hw, b1, *__args):
        """ FillBoxWeb(css: CrossSectionParameter, bu: float, bb: float, hw: float, b1: float, tw: float, tfu: float, tfb: float, mirrorY: bool)FillBoxWeb(css: CrossSectionParameter, bu: float, bb: float, hw: float, b1: float, h: float, tw: float, tfu: float, tfb: float, overlap: float, aligment: BoxDeltaAligment, mirrorY: bool) """
        pass

    @staticmethod
    def FillCHSPar(css, D, t):
        """ FillCHSPar(css: CrossSectionParameter, D: float, t: float) """
        pass

    @staticmethod
    def FillCircle(css, d):
        """ FillCircle(css: CrossSectionParameter, d: float) """
        pass

    @staticmethod
    def FillColdFormedC(css, Width, Height, Thickness, Radius, lip, mirrorZ):
        """ FillColdFormedC(css: CrossSectionParameter, Width: float, Height: float, Thickness: float, Radius: float, lip: float, mirrorZ: bool) """
        pass

    @staticmethod
    def FillColdFormedChannel(css, Width, Height, Thickness, Radius, mirrorZ):
        """ FillColdFormedChannel(css: CrossSectionParameter, Width: float, Height: float, Thickness: float, Radius: float, mirrorZ: bool) """
        pass

    @staticmethod
    def FillColdFormedCp(css, width, height, thickness, radius, lip, lip2, lip2Angle, mirrorZ):
        """ FillColdFormedCp(css: CrossSectionParameter, width: float, height: float, thickness: float, radius: float, lip: float, lip2: float, lip2Angle: float, mirrorZ: bool) """
        pass

    @staticmethod
    def FillColdFormedGeneral(gcf, region2D, Thickness, InsideRadius):
        """ FillColdFormedGeneral(gcf: CrossSectionGeneralColdFormed, region2D: Region2D, Thickness: float, InsideRadius: float) """
        pass

    @staticmethod
    def FillColdFormedL(css, Width, Height, Thickness, Radius, mirrorY, mirrorZ):
        """ FillColdFormedL(css: CrossSectionParameter, Width: float, Height: float, Thickness: float, Radius: float, mirrorY: bool, mirrorZ: bool) """
        pass

    @staticmethod
    def FillColdFormedLgen(css, Width, Height, Angle, Thickness, Radius, mirrorY, mirrorZ):
        """ FillColdFormedLgen(css: CrossSectionParameter, Width: float, Height: float, Angle: float, Thickness: float, Radius: float, mirrorY: bool, mirrorZ: bool) """
        pass

    @staticmethod
    def FillColdFormedOmega(css, Width, Height, FlangeWidth, Thickness, Radius, mirrorY):
        """ FillColdFormedOmega(css: CrossSectionParameter, Width: float, Height: float, FlangeWidth: float, Thickness: float, Radius: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillColdFormedRegularPolygon(css, Radius, Number, Thickness, InsideRadius):
        """ FillColdFormedRegularPolygon(css: CrossSectionParameter, Radius: float, Number: int, Thickness: float, InsideRadius: float) """
        pass

    @staticmethod
    def FillColdFormedRHS(css, Height, Width, Thickness, InsideRadius):
        """ FillColdFormedRHS(css: CrossSectionParameter, Height: float, Width: float, Thickness: float, InsideRadius: float) """
        pass

    @staticmethod
    def FillColdFormedSigma(css, Height, Width, Lip, Thickness, InsideRadius, HeightMiddle, HeightEdge, Depth, mirrorZ):
        """ FillColdFormedSigma(css: CrossSectionParameter, Height: float, Width: float, Lip: float, Thickness: float, InsideRadius: float, HeightMiddle: float, HeightEdge: float, Depth: float, mirrorZ: bool) """
        pass

    @staticmethod
    def FillColdFormedZ(css, Width, Height, Thickness, Radius, mirrorZ):
        """ FillColdFormedZ(css: CrossSectionParameter, Width: float, Height: float, Thickness: float, Radius: float, mirrorZ: bool) """
        pass

    @staticmethod
    def FillColdFormedZed(css, Width, Height, Thickness, Radius, Lip, mirrorZ):
        """ FillColdFormedZed(css: CrossSectionParameter, Width: float, Height: float, Thickness: float, Radius: float, Lip: float, mirrorZ: bool) """
        pass

    @staticmethod
    def FillComposedDblLt(css, *__args):
        """ FillComposedDblLt(css: CrossSectionParameter, h: float, b: float, th: float, sh: float, dis: float, shortLegUp: bool, mirrorY: bool)FillComposedDblLt(css: CrossSectionParameter, name: str, distance: float, shortLegUp: bool, mirrorY: bool) """
        pass

    @staticmethod
    def FillComposedDblLu(css, *__args):
        """ FillComposedDblLu(css: CrossSectionParameter, h: float, b: float, th: float, sh: float, dis: float, shortLegUp: bool, mirrorY: bool)FillComposedDblLu(css: CrossSectionParameter, name: str, distance: float, shortLegUp: bool, mirrorY: bool) """
        pass

    @staticmethod
    def FillComposedDblUc(css, name, distance):
        """ FillComposedDblUc(css: CrossSectionParameter, name: str, distance: float) """
        pass

    @staticmethod
    def FillComposedDblUo(css, *__args):
        """ FillComposedDblUo(css: CrossSectionParameter, bt: float, bb: float, h: float, tb: float, tl: float, tr: float, dis: float)FillComposedDblUo(css: CrossSectionParameter, name: str, distance: float) """
        pass

    @staticmethod
    def FillCssIarc(css, B, H, S, T, R2, tapperF, r1):
        """ FillCssIarc(css: CrossSectionParameter, B: float, H: float, S: float, T: float, R2: float, tapperF: float, r1: float) """
        pass

    @staticmethod
    def FillCssRectangleHollow(css, width, height, thickLeft, thickRight, thickTop, thickBottom):
        """ FillCssRectangleHollow(css: CrossSectionParameter, width: float, height: float, thickLeft: float, thickRight: float, thickTop: float, thickBottom: float) """
        pass

    @staticmethod
    def FillCssSteelAngle(css, B, D, t, rw, r2, C, mirrorZ):
        """ FillCssSteelAngle(css: CrossSectionParameter, B: float, D: float, t: float, rw: float, r2: float, C: float, mirrorZ: bool) """
        pass

    @staticmethod
    def FillCssSteelChannel(css, B, D, tw, tf, rw, rf, taperF):
        """ FillCssSteelChannel(css: CrossSectionParameter, B: float, D: float, tw: float, tf: float, rw: float, rf: float, taperF: float) """
        pass

    @staticmethod
    def FillCssSteelCircularHollow(css, r, t):
        """ FillCssSteelCircularHollow(css: CrossSectionParameter, r: float, t: float) """
        pass

    @staticmethod
    def FillCssSteelRectangularHollow(css, D, B, t, r1, r2, d):
        """ FillCssSteelRectangularHollow(css: CrossSectionParameter, D: float, B: float, t: float, r1: float, r2: float, d: float) """
        pass

    @staticmethod
    def FillCssTarc(css, B, H, Tw, Tf, R, R1, R2, tapperF, tapperW, mirrorY):
        """ FillCssTarc(css: CrossSectionParameter, B: float, H: float, Tw: float, Tf: float, R: float, R1: float, R2: float, tapperF: float, tapperW: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillGeneralShape(css, pt0, pt1, pt2, pt3, pt4, pt5):
        """ FillGeneralShape(css: CrossSectionParameter, pt0: float, pt1: float, pt2: float, pt3: float, pt4: float, pt5: float) """
        pass

    @staticmethod
    def FillLibraryShape(css, searchName):
        """ FillLibraryShape(css: CrossSectionParameter, searchName: str) """
        pass

    @staticmethod
    def FillOHollow(css, r, t):
        """ FillOHollow(css: CrossSectionParameter, r: float, t: float) """
        pass

    @staticmethod
    def FillRectangle(css, width, height):
        """ FillRectangle(css: CrossSectionParameter, width: float, height: float) """
        pass

    @staticmethod
    def FillRolledAngle(css, *__args):
        """ FillRolledAngle(css: CrossSectionParameter, B: float, D: float, t: float, rw: float, r2: float, C: float, mirrorZ: bool, mirrorY: bool)FillRolledAngle(css: CrossSectionParameter, name: str, mirrorZ: bool, mirrorY: bool) """
        pass

    @staticmethod
    def FillRolledChannel(css, *__args):
        """ FillRolledChannel(css: CrossSectionParameter, B: float, D: float, tw: float, tf: float, rw: float, rf: float, taperF: float, mirrorZ: bool)FillRolledChannel(css: CrossSectionParameter, name: str, mirrorZ: bool) """
        pass

    @staticmethod
    def FillRolledCHS(css, *__args):
        """ FillRolledCHS(css: CrossSectionParameter, r: float, t: float)FillRolledCHS(css: CrossSectionParameter, name: str) """
        pass

    @staticmethod
    def FillRolledI(css, *__args):
        """ FillRolledI(css: CrossSectionParameter, b: float, h: float, s: float, t: float, r2: float, tapperF: float, r1: float)FillRolledI(css: CrossSectionParameter, name: str) """
        pass

    @staticmethod
    def FillRolledRHS(css, *__args):
        """ FillRolledRHS(css: CrossSectionParameter, D: float, B: float, t: float, r1: float, r2: float, d: float)FillRolledRHS(css: CrossSectionParameter, name: str) """
        pass

    @staticmethod
    def FillRolledT(css, *__args):
        """ FillRolledT(css: CrossSectionParameter, B: float, H: float, Tw: float, Tf: float, R: float, R1: float, R2: float, tapperF: float, tapperW: float, mirrorY: bool)FillRolledT(css: CrossSectionParameter, name: str, mirrorY: bool) """
        pass

    @staticmethod
    def FillRolledTFromI(css, name, H, mirrorY):
        """ FillRolledTFromI(css: CrossSectionParameter, name: str, H: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillShapeDblL(css, h, b, th, sh, dis, shortLegUp, mirrorY):
        """ FillShapeDblL(css: CrossSectionParameter, h: float, b: float, th: float, sh: float, dis: float, shortLegUp: bool, mirrorY: bool) """
        pass

    @staticmethod
    def FillShapeDblLu(css, h, b, th, sh, dis, shortLegUp, mirrorY):
        """ FillShapeDblLu(css: CrossSectionParameter, h: float, b: float, th: float, sh: float, dis: float, shortLegUp: bool, mirrorY: bool) """
        pass

    @staticmethod
    def FillShapeDblU(css, bt, bb, h, tb, tl, tr, dis):
        """ FillShapeDblU(css: CrossSectionParameter, bt: float, bb: float, h: float, tb: float, tl: float, tr: float, dis: float) """
        pass

    @staticmethod
    def FillShapeI(css, h, btf, bbf, htf, hbf, tw):
        """ FillShapeI(css: CrossSectionParameter, h: float, btf: float, bbf: float, htf: float, hbf: float, tw: float) """
        pass

    @staticmethod
    def FillShapeIBase(css, h, btf, bbf, htf, hbf, tw, htfh, hbfh):
        """ FillShapeIBase(css: CrossSectionParameter, h: float, btf: float, bbf: float, htf: float, hbf: float, tw: float, htfh: float, hbfh: float) """
        pass

    @staticmethod
    def FillShapeL(css, h, b, th, sh):
        """ FillShapeL(css: CrossSectionParameter, h: float, b: float, th: float, sh: float) """
        pass

    @staticmethod
    def FillShapeT(css, b, h, hf, bw):
        """ FillShapeT(css: CrossSectionParameter, b: float, h: float, hf: float, bw: float) """
        pass

    @staticmethod
    def FillShapeTrapezoid1(css, h, bt, bb):
        """ FillShapeTrapezoid1(css: CrossSectionParameter, h: float, bt: float, bb: float) """
        pass

    @staticmethod
    def FillShapeTrev(css, b, h, hf, bw):
        """ FillShapeTrev(css: CrossSectionParameter, b: float, h: float, hf: float, bw: float) """
        pass

    @staticmethod
    def FillShapeTrev1(css, b, h, hf, bw, hfh1):
        """ FillShapeTrev1(css: CrossSectionParameter, b: float, h: float, hf: float, bw: float, hfh1: float) """
        pass

    @staticmethod
    def FillShapeTT(css, b, h, hf, bw, s):
        """ FillShapeTT(css: CrossSectionParameter, b: float, h: float, hf: float, bw: float, s: float) """
        pass

    @staticmethod
    def FillShapeTwh(css, b, h, hf, bwT, bwB):
        """ FillShapeTwh(css: CrossSectionParameter, b: float, h: float, hf: float, bwT: float, bwB: float) """
        pass

    @staticmethod
    def FillShapeU(css, bt, bb, h, tb, tl, tr):
        """ FillShapeU(css: CrossSectionParameter, bt: float, bb: float, h: float, tb: float, tl: float, tr: float) """
        pass

    @staticmethod
    def FillSteelTI(css, name, H, mirrorY):
        """ FillSteelTI(css: CrossSectionParameter, name: str, H: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillSteelTube(css, r, t):
        """ FillSteelTube(css: CrossSectionParameter, r: float, t: float) """
        pass

    @staticmethod
    def FillTriangle(css, h, w, fTh, webTh, webD, mirrorY):
        """ FillTriangle(css: CrossSectionParameter, h: float, w: float, fTh: float, webTh: float, webD: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillWelded2Lt(css, name, distance, shortLegUp, mirrorY):
        """ FillWelded2Lt(css: CrossSectionParameter, name: str, distance: float, shortLegUp: bool, mirrorY: bool) """
        pass

    @staticmethod
    def FillWelded2Lu(css, name, distance, shortLegUp, mirrorY):
        """ FillWelded2Lu(css: CrossSectionParameter, name: str, distance: float, shortLegUp: bool, mirrorY: bool) """
        pass

    @staticmethod
    def FillWelded2Uc(css, name, distance):
        """ FillWelded2Uc(css: CrossSectionParameter, name: str, distance: float) """
        pass

    @staticmethod
    def FillWeldedAsymI(css, bu, bb, hw, tw, tfu, tfb):
        """ FillWeldedAsymI(css: CrossSectionParameter, bu: float, bb: float, hw: float, tw: float, tfu: float, tfb: float) """
        pass

    @staticmethod
    def FillWeldedBoxDelta(css, bu, bb, hw, b1, h, tw, tfu, tfb, overlap, aligment, mirrorY):
        """ FillWeldedBoxDelta(css: CrossSectionParameter, bu: float, bb: float, hw: float, b1: float, h: float, tw: float, tfu: float, tfb: float, overlap: float, aligment: BoxDeltaAligment, mirrorY: bool) """
        pass

    @staticmethod
    def FillWeldedBoxFlange(css, bu, bb, hw, b1, tw, tfu, tfb):
        """ FillWeldedBoxFlange(css: CrossSectionParameter, bu: float, bb: float, hw: float, b1: float, tw: float, tfu: float, tfb: float) """
        pass

    @staticmethod
    def FillWeldedBoxWeb(css, bu, bb, hw, b1, tw, tfu, tfb, mirrorY):
        """ FillWeldedBoxWeb(css: CrossSectionParameter, bu: float, bb: float, hw: float, b1: float, tw: float, tfu: float, tfb: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillWeldedI(css, bu, hw, tw, tf):
        """ FillWeldedI(css: CrossSectionParameter, bu: float, hw: float, tw: float, tf: float) """
        pass

    @staticmethod
    def FillWeldedT(css, b, h, tw, tf, mirrorY):
        """ FillWeldedT(css: CrossSectionParameter, b: float, h: float, tw: float, tf: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillWeldedTriangle(css, h, w, fTh, webTh, webD, mirrorY):
        """ FillWeldedTriangle(css: CrossSectionParameter, h: float, w: float, fTh: float, webTh: float, webD: float, mirrorY: bool) """
        pass

    @staticmethod
    def FillWeldedU(css, b, hw, tw, tf, rw, rf, taperF, mirrorZ):
        """ FillWeldedU(css: CrossSectionParameter, b: float, hw: float, tw: float, tf: float, rw: float, rf: float, taperF: float, mirrorZ: bool) """
        pass

    __all__ = [
        'FillBox2',
        'FillBoxWeb',
        'FillCHSPar',
        'FillCircle',
        'FillColdFormedC',
        'FillColdFormedChannel',
        'FillColdFormedCp',
        'FillColdFormedGeneral',
        'FillColdFormedL',
        'FillColdFormedLgen',
        'FillColdFormedOmega',
        'FillColdFormedRegularPolygon',
        'FillColdFormedRHS',
        'FillColdFormedSigma',
        'FillColdFormedZ',
        'FillColdFormedZed',
        'FillComposedDblLt',
        'FillComposedDblLu',
        'FillComposedDblUc',
        'FillComposedDblUo',
        'FillCssIarc',
        'FillCssRectangleHollow',
        'FillCssSteelAngle',
        'FillCssSteelChannel',
        'FillCssSteelCircularHollow',
        'FillCssSteelRectangularHollow',
        'FillCssTarc',
        'FillGeneralShape',
        'FillLibraryShape',
        'FillOHollow',
        'FillRectangle',
        'FillRolledAngle',
        'FillRolledChannel',
        'FillRolledCHS',
        'FillRolledI',
        'FillRolledRHS',
        'FillRolledT',
        'FillRolledTFromI',
        'FillShapeDblL',
        'FillShapeDblLu',
        'FillShapeDblU',
        'FillShapeI',
        'FillShapeIBase',
        'FillShapeL',
        'FillShapeT',
        'FillShapeTrapezoid1',
        'FillShapeTrev',
        'FillShapeTrev1',
        'FillShapeTT',
        'FillShapeTwh',
        'FillShapeU',
        'FillSteelTI',
        'FillSteelTube',
        'FillTriangle',
        'FillWelded2Lt',
        'FillWelded2Lu',
        'FillWelded2Uc',
        'FillWeldedAsymI',
        'FillWeldedBoxDelta',
        'FillWeldedBoxFlange',
        'FillWeldedBoxWeb',
        'FillWeldedI',
        'FillWeldedT',
        'FillWeldedTriangle',
        'FillWeldedU',
    ]


class CrossSectionGeneralColdFormed(CrossSection):
    """ CrossSectionGeneralColdFormed() """
    Centerline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centerline(self: CrossSectionGeneralColdFormed) -> PolyLine2D

Set: Centerline(self: CrossSectionGeneralColdFormed) = value
"""

    CrossSectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionType(self: CrossSectionGeneralColdFormed) -> CrossSectionType

Set: CrossSectionType(self: CrossSectionGeneralColdFormed) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: CrossSectionGeneralColdFormed) -> ReferenceElement

Set: Material(self: CrossSectionGeneralColdFormed) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: CrossSectionGeneralColdFormed) -> float

Set: Radius(self: CrossSectionGeneralColdFormed) = value
"""

    Thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thickness(self: CrossSectionGeneralColdFormed) -> float

Set: Thickness(self: CrossSectionGeneralColdFormed) = value
"""



class CrossSectionParameter(CrossSection):
    """ CrossSectionParameter() """
    CrossSectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionType(self: CrossSectionParameter) -> CrossSectionType

Set: CrossSectionType(self: CrossSectionParameter) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: CrossSectionParameter) -> ReferenceElement

Set: Material(self: CrossSectionParameter) = value
"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: CrossSectionParameter) -> List[Parameter]

Set: Parameters(self: CrossSectionParameter) = value
"""



class CrossSectionThermalAttribute(OpenAttribute):
    """ CrossSectionThermalAttribute() """
    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Components(self: CrossSectionThermalAttribute) -> List[CrossSectionComponentThermalData]

Set: Components(self: CrossSectionThermalAttribute) = value
"""



class CrossSectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum CrossSectionType, values: BeamShapeBox (79), BeamShapeBox1 (80), BeamShapeIHaunchChamfer (76), BeamShapeIHaunchChamferAssym (77), BeamShapeIrevDegen (83), BeamShapeIrevDegenAdd (84), BeamShapeIZDegen (88), BeamShapeLDegen (89), BeamShapeRevU (78), BeamShapeTrevChamferHaunchD (82), BeamShapeTrevChamferHaunchS (81), BeamShapeTrevDegen (85), BeamShapeTrevDegenAdd (86), BeamShapeZDegen (87), Box2I (18), Box2L (21), Box2U (19), Box2U2PI (20), Box4L (22), BoxDelta (98), BoxFl (16), BoxTriangle (99), BoxWeb (17), CF2Co (100), CF2Cpo (105), CFC (93), CFCp (104), CFGeneral (103), CFL (95), CFLgen (102), CFOmega (97), CFRegPolygon (96), CFSigma (92), CFU (94), CFZ (90), CFZed (91), CHSg (34), CHSPar (101), CompositeBeamBox (53), CompositeBeamBox1 (54), CompositeBeamIgenT (55), CompositeBeamLLeft (56), CompositeBeamPlate (57), CompositeBeamRResT (58), CompositeBeamRResT1 (59), CompositeBeamRT (60), CompositeBeamShapeChamf (61), CompositeBeamShapeChamfAssym (62), CompositeBeamShapeIgen (63), CompositeBeamShapeIT (64), CompositeBeamShapeITAssym (65), CompositeBeamShapeTT (75), CompositeBeamTLeft (66), CompositeBeamTrapezoid (67), CompositeBeamTresT (68), CompositeBeamTrev (69), CompositeBeamTrevResI (70), CompositeBeamTrevResI1 (71), CompositeBeamTrevResR (72), CompositeBeamTrevResR1 (73), CompositeBeamTrevT (74), General (38), GeneralConcrete (52), GeneralSteel (51), Igh (29), Ign (28), Iw (23), Iwn (24), Lg (31), LgMirrored (32), O (26), OneComponentCss (0), Oval (37), Rect (27), RHSg (36), Rolled2I (39), RolledAngle (2), RolledCHS (5), RolledDoubleLt (10), RolledDoubleLu (11), RolledDoubleUc (8), RolledDoubleUo (7), RolledI (1), RolledIPar (13), RolledLPar (15), RolledRHS (6), RolledT (3), RolledTI (12), RolledU (4), RolledUPar (14), Sg (50), Tchamfer1 (46), Tchamfer2 (47), Tg (30), Tgrev (43), Trapezoid (40), TT (48), TT1 (49), Ttfh (41), Ttfhrev (44), Tw (25), Twh (42), Twhrev (45), Ug (33), UniqueName (1001), Zg (35) """
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

    BeamShapeBox = None
    BeamShapeBox1 = None
    BeamShapeIHaunchChamfer = None
    BeamShapeIHaunchChamferAssym = None
    BeamShapeIrevDegen = None
    BeamShapeIrevDegenAdd = None
    BeamShapeIZDegen = None
    BeamShapeLDegen = None
    BeamShapeRevU = None
    BeamShapeTrevChamferHaunchD = None
    BeamShapeTrevChamferHaunchS = None
    BeamShapeTrevDegen = None
    BeamShapeTrevDegenAdd = None
    BeamShapeZDegen = None
    Box2I = None
    Box2L = None
    Box2U = None
    Box2U2PI = None
    Box4L = None
    BoxDelta = None
    BoxFl = None
    BoxTriangle = None
    BoxWeb = None
    CF2Co = None
    CF2Cpo = None
    CFC = None
    CFCp = None
    CFGeneral = None
    CFL = None
    CFLgen = None
    CFOmega = None
    CFRegPolygon = None
    CFSigma = None
    CFU = None
    CFZ = None
    CFZed = None
    CHSg = None
    CHSPar = None
    CompositeBeamBox = None
    CompositeBeamBox1 = None
    CompositeBeamIgenT = None
    CompositeBeamLLeft = None
    CompositeBeamPlate = None
    CompositeBeamRResT = None
    CompositeBeamRResT1 = None
    CompositeBeamRT = None
    CompositeBeamShapeChamf = None
    CompositeBeamShapeChamfAssym = None
    CompositeBeamShapeIgen = None
    CompositeBeamShapeIT = None
    CompositeBeamShapeITAssym = None
    CompositeBeamShapeTT = None
    CompositeBeamTLeft = None
    CompositeBeamTrapezoid = None
    CompositeBeamTresT = None
    CompositeBeamTrev = None
    CompositeBeamTrevResI = None
    CompositeBeamTrevResI1 = None
    CompositeBeamTrevResR = None
    CompositeBeamTrevResR1 = None
    CompositeBeamTrevT = None
    General = None
    GeneralConcrete = None
    GeneralSteel = None
    Igh = None
    Ign = None
    Iw = None
    Iwn = None
    Lg = None
    LgMirrored = None
    O = None
    OneComponentCss = None
    Oval = None
    Rect = None
    RHSg = None
    Rolled2I = None
    RolledAngle = None
    RolledCHS = None
    RolledDoubleLt = None
    RolledDoubleLu = None
    RolledDoubleUc = None
    RolledDoubleUo = None
    RolledI = None
    RolledIPar = None
    RolledLPar = None
    RolledRHS = None
    RolledT = None
    RolledTI = None
    RolledU = None
    RolledUPar = None
    Sg = None
    Tchamfer1 = None
    Tchamfer2 = None
    Tg = None
    Tgrev = None
    Trapezoid = None
    TT = None
    TT1 = None
    Ttfh = None
    Ttfhrev = None
    Tw = None
    Twh = None
    Twhrev = None
    Ug = None
    UniqueName = None
    value__ = None
    Zg = None


class CssComponent(OpenObject):
    """ CssComponent() """
    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: CssComponent) -> Region2D

Set: Geometry(self: CssComponent) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: CssComponent) -> int

Set: Id(self: CssComponent) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: CssComponent) -> ReferenceElement

Set: Material(self: CssComponent) = value
"""

    Phase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Phase(self: CssComponent) -> int

Set: Phase(self: CssComponent) = value
"""



class FatigueTypeOfPrestressingSteel(Enum, IComparable, IFormattable, IConvertible):
    """ enum FatigueTypeOfPrestressingSteel, values: ExternalTendon (5), PostTensioningCurvedTendonsInSteelDucts (2), PostTensioningSingleStrandsInPlasticDucts (0), PostTensioningSplicingDevices (3), PostTensioningStraightTendonsOrCurvedTendonsInPlasticDucts (1), PreTensioning (4) """
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

    ExternalTendon = None
    PostTensioningCurvedTendonsInSteelDucts = None
    PostTensioningSingleStrandsInPlasticDucts = None
    PostTensioningSplicingDevices = None
    PostTensioningStraightTendonsOrCurvedTendonsInPlasticDucts = None
    PreTensioning = None
    value__ = None


class InputValueType(Enum, IComparable, IFormattable, IConvertible):
    """ enum InputValueType, values: Calculate (0), UserInput (1) """
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

    Calculate = None
    UserInput = None
    value__ = None


class MaterialDuct(Enum, IComparable, IFormattable, IConvertible):
    """ enum MaterialDuct, values: Metal (0), Plastic (1) """
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

    Metal = None
    Plastic = None
    value__ = None


class Parameter(OpenObject):
    # no doc
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Parameter) -> str

Set: Name(self: Parameter) = value
"""



class ParameterBool(Parameter):
    """ ParameterBool() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParameterBool) -> bool

Set: Value(self: ParameterBool) = value
"""



class ParameterDouble(Parameter):
    """ ParameterDouble() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParameterDouble) -> float

Set: Value(self: ParameterDouble) = value
"""



class ParameterInt(Parameter):
    """ ParameterInt() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParameterInt) -> int

Set: Value(self: ParameterInt) = value
"""



class ParameterReferenceElement(Parameter):
    """ ParameterReferenceElement() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParameterReferenceElement) -> ReferenceElement

Set: Value(self: ParameterReferenceElement) = value
"""



class ParameterString(Parameter):
    """ ParameterString() """
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParameterString) -> str

Set: Value(self: ParameterString) = value
"""



class ReinforcedBar(OpenObject):
    """ ReinforcedBar() """
    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: ReinforcedBar) -> float

Set: Diameter(self: ReinforcedBar) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: ReinforcedBar) -> ReferenceElement

Set: Material(self: ReinforcedBar) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: ReinforcedBar) -> Point2D

Set: Point(self: ReinforcedBar) = value
"""



class ReinforcedCrossSection(OpenElementId):
    """ ReinforcedCrossSection() """
    Bars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bars(self: ReinforcedCrossSection) -> List[ReinforcedBar]

Set: Bars(self: ReinforcedCrossSection) = value
"""

    CrossSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSection(self: ReinforcedCrossSection) -> ReferenceElement

Set: CrossSection(self: ReinforcedCrossSection) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ReinforcedCrossSection) -> str

Set: Name(self: ReinforcedCrossSection) = value
"""

    Stirrups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stirrups(self: ReinforcedCrossSection) -> List[Stirrup]

Set: Stirrups(self: ReinforcedCrossSection) = value
"""

    TendonBars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TendonBars(self: ReinforcedCrossSection) -> List[TendonBar]

Set: TendonBars(self: ReinforcedCrossSection) = value
"""

    TendonDucts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TendonDucts(self: ReinforcedCrossSection) -> List[TendonDuct]

Set: TendonDucts(self: ReinforcedCrossSection) = value
"""



class Stirrup(OpenObject):
    """ Stirrup() """
    AnchorageLenght = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorageLenght(self: Stirrup) -> float

Set: AnchorageLenght(self: Stirrup) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Stirrup) -> float

Set: Diameter(self: Stirrup) = value
"""

    DiameterOfMandrel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiameterOfMandrel(self: Stirrup) -> float

Set: DiameterOfMandrel(self: Stirrup) = value
"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: Stirrup) -> float

Set: Distance(self: Stirrup) = value
"""

    Geometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Geometry(self: Stirrup) -> PolyLine2D

Set: Geometry(self: Stirrup) = value
"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: Stirrup) -> bool

Set: IsClosed(self: Stirrup) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: Stirrup) -> ReferenceElement

Set: Material(self: Stirrup) = value
"""

    ShearCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShearCheck(self: Stirrup) -> bool

Set: ShearCheck(self: Stirrup) = value
"""

    TorsionCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TorsionCheck(self: Stirrup) -> bool

Set: TorsionCheck(self: Stirrup) = value
"""



class TendonBar(OpenObject):
    """ TendonBar() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: TendonBar) -> int

Set: Id(self: TendonBar) = value
"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: TendonBar) -> ReferenceElement

Set: Material(self: TendonBar) = value
"""

    NumStrandsInTendon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumStrandsInTendon(self: TendonBar) -> int

Set: NumStrandsInTendon(self: TendonBar) = value
"""

    Phase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Phase(self: TendonBar) -> int

Set: Phase(self: TendonBar) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: TendonBar) -> Point2D

Set: Point(self: TendonBar) = value
"""

    PrestressingOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrestressingOrder(self: TendonBar) -> int

Set: PrestressingOrder(self: TendonBar) = value
"""

    PrestressReinforcementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrestressReinforcementType(self: TendonBar) -> FatigueTypeOfPrestressingSteel

Set: PrestressReinforcementType(self: TendonBar) = value
"""

    TendonDuct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TendonDuct(self: TendonBar) -> TendonDuct

Set: TendonDuct(self: TendonBar) = value
"""

    TendonType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TendonType(self: TendonBar) -> TendonBarType

Set: TendonType(self: TendonBar) = value
"""



class TendonBarType(Enum, IComparable, IFormattable, IConvertible):
    """ enum TendonBarType, values: Posttensioned (0), Pretensioned (1) """
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

    Posttensioned = None
    Pretensioned = None
    value__ = None


class TendonDuct(OpenObject):
    """ TendonDuct() """
    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: TendonDuct) -> float

Set: Diameter(self: TendonDuct) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: TendonDuct) -> int

Set: Id(self: TendonDuct) = value
"""

    IsDebondingTube = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDebondingTube(self: TendonDuct) -> bool

Set: IsDebondingTube(self: TendonDuct) = value
"""

    MaterialDuct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialDuct(self: TendonDuct) -> MaterialDuct

Set: MaterialDuct(self: TendonDuct) = value
"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: TendonDuct) -> Point2D

Set: Point(self: TendonDuct) = value
"""



class ThermalConductivityLimit(Enum, IComparable, IFormattable, IConvertible):
    """ enum ThermalConductivityLimit, values: Lower (1), Upper (0) """
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

    Lower = None
    Upper = None
    value__ = None


