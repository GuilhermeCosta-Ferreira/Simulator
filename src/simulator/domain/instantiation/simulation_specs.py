# ================================================================
# 0. Section: IMPORTS
# ================================================================
from dataclasses import dataclass

from .step_type import StepType


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class SimulationSpecs:
    step_size: StepType
    max_duration: int
    re_connection: bool
    seed: int
