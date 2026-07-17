"""Unit tests for MetricPlot labelling.

MetricPlot draws one MetricSeries onto an Axes. The labels come from the
series' human-readable `title` (not its machine `name`): the axes title is the
title, and the y-label is "title (unit)". Matplotlib runs headless (Agg).
"""

# ================================================================
# 0. Section: IMPORTS
# ================================================================
import matplotlib

matplotlib.use("Agg")

import numpy as np
import pytest
from matplotlib import pyplot as plt

from simulator.domain.analysis import MetricSeries
from simulator.adapters.render import MetricPlot


# ================================================================
# 1. Section: Builders
# ================================================================
def _series() -> MetricSeries:
    timepoints = np.arange(5, dtype=float)
    return MetricSeries(
        name="age_metric",
        title="Age Metric",
        unit="years",
        timepoints=timepoints,
        mean=timepoints,
        std=np.zeros(5),
        time_unit="days",
    )


# ================================================================
# 2. Section: Unit Tests
# ================================================================
@pytest.mark.unit
def test_draw_titles_the_axes_with_the_series_title() -> None:
    _, axes = plt.subplots()

    MetricPlot(_series()).draw(axes)

    assert axes.get_title() == "Age Metric"
    plt.close("all")


@pytest.mark.unit
def test_draw_labels_axes_from_title_not_name() -> None:
    _, axes = plt.subplots()

    MetricPlot(_series()).draw(axes)

    assert axes.get_xlabel() == "Time (days)"
    assert axes.get_ylabel() == "Age Metric (years)"
    plt.close("all")
