# ================================================================
# 0. Section: IMPORTS
# ================================================================
from numpy.typing import NDArray
from dataclasses import dataclass

from .axis import Axis


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class MetricSeries:
    name: str
    title: str
    x: Axis
    y: Axis
    std: NDArray
    plot_kind: str
