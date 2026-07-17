# ================================================================
# 0. Section: IMPORTS
# ================================================================
from matplotlib.axes import Axes
from dataclasses import dataclass
from abc import ABC, abstractmethod


from ....domain.analysis import MetricSeries



# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class MetricRenderer(ABC):
    @abstractmethod
    def draw(self, axes: Axes, series: MetricSeries) -> None:
        ...
