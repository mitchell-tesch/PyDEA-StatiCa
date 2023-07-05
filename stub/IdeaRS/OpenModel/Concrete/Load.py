# encoding: utf-8
# module IdeaRS.OpenModel.Concrete.Load calls itself Load
# from IdeaRS.OpenModel, Version=23.0.2.1543, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CssComponentLoading(object):
    """ CssComponentLoading() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: CssComponentLoading) -> int

Set: Id(self: CssComponentLoading) = value
"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: CssComponentLoading) -> List[CssComponentTimeLoading]

Set: Loading(self: CssComponentLoading) = value
"""



class CssComponentTimeLoading(object):
    """ CssComponentTimeLoading() """
    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: CssComponentTimeLoading) -> SectionResultBase

Set: Loading(self: CssComponentTimeLoading) = value
"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: CssComponentTimeLoading) -> float

Set: Time(self: CssComponentTimeLoading) = value
"""



class CssEffectType(Enum, IComparable, IFormattable, IConvertible):
    """ enum CssEffectType, values: DeformationPlane (1), InternalForce (0) """
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

    DeformationPlane = None
    InternalForce = None
    value__ = None


class FatigueLoading(object):
    """ FatigueLoading() """
    MaxLoading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxLoading(self: FatigueLoading) -> LoadingULS

Set: MaxLoading(self: FatigueLoading) = value
"""

    MinLoading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinLoading(self: FatigueLoading) -> LoadingULS

Set: MinLoading(self: FatigueLoading) = value
"""



class LoadingSLS(object):
    """ LoadingSLS() """
    InternalForces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForces(self: LoadingSLS) -> ResultOfInternalForces

Set: InternalForces(self: LoadingSLS) = value
"""

    InternalForcesImperfection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForcesImperfection(self: LoadingSLS) -> ResultOfInternalForces

Set: InternalForcesImperfection(self: LoadingSLS) = value
"""

    InternalForcesVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForcesVariable(self: LoadingSLS) -> ResultOfInternalForces

Set: InternalForcesVariable(self: LoadingSLS) = value
"""



class LoadingULS(object):
    """ LoadingULS() """
    InternalForces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForces(self: LoadingULS) -> ResultOfInternalForces

Set: InternalForces(self: LoadingULS) = value
"""

    InternalForces2ndOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForces2ndOrder(self: LoadingULS) -> ResultOfInternalForces

Set: InternalForces2ndOrder(self: LoadingULS) = value
"""

    InternalForcesBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForcesBegin(self: LoadingULS) -> ResultOfInternalForces

Set: InternalForcesBegin(self: LoadingULS) = value
"""

    InternalForcesEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForcesEnd(self: LoadingULS) -> ResultOfInternalForces

Set: InternalForcesEnd(self: LoadingULS) = value
"""

    InternalForcesImperfection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForcesImperfection(self: LoadingULS) -> ResultOfInternalForces

Set: InternalForcesImperfection(self: LoadingULS) = value
"""

    InternalForcesVariable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalForcesVariable(self: LoadingULS) -> ResultOfInternalForces

Set: InternalForcesVariable(self: LoadingULS) = value
"""



class PrestressInputType(Enum, IComparable, IFormattable, IConvertible):
    """ enum PrestressInputType, values: AfterLongTermLosses (3), AfterTransfer (1) """
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

    AfterLongTermLosses = None
    AfterTransfer = None
    value__ = None


class PrestressLoading(object):
    """ PrestressLoading() """
    PrimaryForces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryForces(self: PrestressLoading) -> ResultOfInternalForces

Set: PrimaryForces(self: PrestressLoading) = value
"""

    SecondaryForces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryForces(self: PrestressLoading) -> ResultOfInternalForces

Set: SecondaryForces(self: PrestressLoading) = value
"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: PrestressLoading) -> float

Set: Time(self: PrestressLoading) = value
"""



class StageLoading(object):
    """ StageLoading() """
    PermanentForces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PermanentForces(self: StageLoading) -> ResultOfInternalForces

Set: PermanentForces(self: StageLoading) = value
"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: StageLoading) -> float

Set: Time(self: StageLoading) = value
"""



class StagesLoading(OpenObject):
    """ StagesLoading() """
    CssComponentLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CssComponentLoad(self: StagesLoading) -> List[CssComponentLoading]

Set: CssComponentLoad(self: StagesLoading) = value
"""

    CssEffectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CssEffectType(self: StagesLoading) -> CssEffectType

Set: CssEffectType(self: StagesLoading) = value
"""

    PermanentLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PermanentLoad(self: StagesLoading) -> List[StageLoading]

Set: PermanentLoad(self: StagesLoading) = value
"""

    PrestressInputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrestressInputType(self: StagesLoading) -> PrestressInputType

Set: PrestressInputType(self: StagesLoading) = value
"""

    PrestressLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrestressLoad(self: StagesLoading) -> List[PrestressLoading]

Set: PrestressLoad(self: StagesLoading) = value
"""

    TendonComponentLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TendonComponentLoad(self: StagesLoading) -> List[TendonComponentLoading]

Set: TendonComponentLoad(self: StagesLoading) = value
"""



class TendonComponentLoading(object):
    """ TendonComponentLoading() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: TendonComponentLoading) -> int

Set: Id(self: TendonComponentLoading) = value
"""

    Loading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loading(self: TendonComponentLoading) -> TendonLoading

Set: Loading(self: TendonComponentLoading) = value
"""



class TendonLoading(object):
    # no doc

class TendonLossesLoading(TendonLoading):
    """ TendonLossesLoading() """
    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: TendonLossesLoading) -> float

Set: Time(self: TendonLossesLoading) = value
"""



class TendonStressLoading(TendonLoading):
    """ TendonStressLoading() """
    Stresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stresses(self: TendonStressLoading) -> List[TendonTimeStressLoading]

Set: Stresses(self: TendonStressLoading) = value
"""



class TendonTimeStressLoading(object):
    """ TendonTimeStressLoading() """
    Stress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stress(self: TendonTimeStressLoading) -> float

Set: Stress(self: TendonTimeStressLoading) = value
"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: TendonTimeStressLoading) -> float

Set: Time(self: TendonTimeStressLoading) = value
"""



