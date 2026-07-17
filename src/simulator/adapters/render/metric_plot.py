# ================================================================
# 0. Section: IMPORTS
# ================================================================
from matplotlib import pyplot as plt

from dataclasses import dataclass
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from ...domain.analysis import Axis, MetricSeries
from .metric_renders import MetricRenderer, renderer_for


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class MetricPlot:
    """Draw one MetricSeries, delegating the marks to a MetricRenderer.

    The renderer defaults to the one registered for the series' `plot_kind`;
    pass one explicitly to override that choice.
    """

    series: MetricSeries
    renderer: MetricRenderer | None = None

    def __post_init__(self) -> None:
        if self.renderer is None:
            self.renderer = renderer_for(self.series.plot_kind)

    def render(self) -> Figure:
        figure, axes = plt.subplots()
        self.draw(axes)
        return figure

    def draw(
        self, axes: Axes, show_xlabel: bool = True, show_ylabel: bool = True
    ) -> None:
        """Draw the series onto an existing Axes (used by grids too)."""
        self.renderer.draw(axes, self.series)

        axes.set_title(self.series.title)
        if show_xlabel:
            axes.set_xlabel(_axis_label(self.series.x))
        if show_ylabel:
            axes.set_ylabel(_axis_label(self.series.y))


# ================================================================
# 2. Section: Functions — labelling
# ================================================================
def _axis_label(axis: Axis) -> str:
    return f"{axis.label} ({axis.unit})"
