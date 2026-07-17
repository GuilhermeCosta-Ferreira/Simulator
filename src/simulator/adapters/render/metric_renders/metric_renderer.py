# ================================================================
# 0. Section: IMPORTS
# ================================================================
from matplotlib.axes import Axes
from dataclasses import dataclass
from abc import ABC, abstractmethod


from ....domain.analysis import MetricField, MetricSeries


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class MetricRenderer(ABC):
    """Draws the marks for one aggregated metric onto an Axes.

    Implementations accept the container their plot kind produces: a
    MetricSeries for line-like kinds, a MetricField for gridded ones. Titles
    and axis labels are MetricPlot's job, not the renderer's.
    """

    @abstractmethod
    def draw(self, axes: Axes, series: MetricSeries | MetricField) -> None: ...
