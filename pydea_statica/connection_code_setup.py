# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa Plugin API - Connection Code Setup Data Structures
__all__ = ['CodeSetup', 'CodeSetupJson']

# TODO
from typing import TypedDict, Optional


class SteelSetup(TypedDict):
    gammaM0 : float
    gammaM1 : float
    gammaM2 : float
    gammaMfi : float
    gammaMu : float


class ConcreteSetup(TypedDict):
    pass


class CodeSetupJson(TypedDict):
    steelSetup : SteelSetup
    concreteSetup : Optional[ConcreteSetup]
    stopAtLimitStrain : bool
    weldEvaluationData : int
    checkDetailing : bool
    applyConeBreakoutCheck : int
    pretensionForceFpc : float
    gammaInst : float
    gammaC : float
    gammaM3 : float
    anchorLengthForStiffness : int
    jointBetaFactor : float
    effectiveAreaStressCoeff : int
    effectiveAreaStressCoeffAISC : int
    frictionCoefficient : float
    limitPlasticStrain : float
    limitDeformation : float
    limitDeformationCheck : bool
    analysisGNL : bool
    warnPlasticStrain : float
    warnCheckLevel : float
    optimalCheckLevel : float
    distanceBetweenBolts : float
    distanceDiameterBetweenBP : float
    distanceBetweenBoltsEdge : float
    bearingAngle : float
    decreasingFtrd : float
    bracedSystem : bool
    bearingCheck : bool
    applyBetapInfluence : bool
    memberLengthRatio : float
    divisionOfSurfaceOfCHS : int
    divisionOfArcsOfRHS : int
    numElement : int
    numberIterations : int
    mdiv : int
    minSize : float
    maxSize : float
    numElementRhs : int
    rigidBP : bool
    alphaCC : float
    crackedConcrete : bool
    developedFillers : bool
    deformationBoltHole : bool
    extensionLengthRationOpenSections : float
    extensionLengthRationCloseSections : float
    factorPreloadBolt : float
    baseMetalCapacity : bool
    applyBearingCheck : bool
    frictionCoefficientPbolt : float
    crtCompCheckIS : int
    boltMaxGripLengthCoeff : float
    fatigueSectionOffset : float
    condensedElementLengthFactor : float
    gammaMu : float


class CodeSetup():
    def __init__(self, code_setup_json : CodeSetupJson):
        self.__dict__.update(code_setup_json)
    
    def to_json(self):
        return self.__dict__