# PYDEA.StatiCa - IDEA.StatiCa Python Wrapper
# IDEA.StatiCa Plugin API - Connection Loading Data Structures
__all__ = ['LoadingCase']


from typing import TypedDict


class SegmentForce(TypedDict):
    beamSegmentId : int
    position : int
    n : float
    qy : float
    qz : float
    mx : float
    my : float
    mz : float
    absPosition : float
    forceIn : int

class LoadCaseJson(TypedDict):
    id : int
    name : str
    checkEquilibrium : bool
    percentageLoad : bool
    forcesOnSegments : list[SegmentForce]
    forcesPercentageOnSegments : list[SegmentForce]


class LoadingCase():
    def __init__(self, id : int, name : str,
                 segment_forces : list[SegmentForce],
                 percentage_segment_forces : list[SegmentForce],
                 check_equilibrium : bool = True,
                 percentage_load : bool = False):
        self.id = id
        self.name = name
        self.check_equilibrium = check_equilibrium
        self.percentage_load = percentage_load
        self.segment_forces = segment_forces
        self.percentage_segment_forces = percentage_segment_forces
    
    @classmethod
    def from_json(cls, load_case_json : LoadCaseJson):
        return cls(load_case_json['id'],
                   load_case_json['name'],
                   load_case_json['forcesOnSegments'],
                   load_case_json['forcesPercentageOnSegments'],
                   load_case_json['checkEquilibrium'],
                   load_case_json['percentageLoad'])

    def to_json(self) -> LoadCaseJson:
        return {'id': self.id,
                'name': self.name,
                'checkEquilibrium': self.check_equilibrium,
                'percentageLoad': self.percentage_load,
                'forcesOnSegments': self.segment_forces,
                'forcesPercentageOnSegments': self.percentage_segment_forces}