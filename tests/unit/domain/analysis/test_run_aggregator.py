"""Contract tests for RunAggregator metadata propagation.

RunAggregator turns per-run histories into one MetricSeries. Beyond the mean/
std maths it must copy the metric's descriptive fields — name, title and unit
— onto the series, since downstream rendering labels plots from `title`.
"""

# ================================================================
# 0. Section: IMPORTS
# ================================================================
import numpy as np
import pytest

from simulator.domain.analysis import RunAggregator
from simulator.domain.analysis.metrics import AgeMetric

from tests.helpers.builders import build_engine, build_simulation


# ================================================================
# 1. Section: Unit Tests
# ================================================================
@pytest.mark.unit
def test_aggregate_copies_metric_metadata_onto_series() -> None:
    run = build_simulation(engine=build_engine())
    series = RunAggregator().aggregate([run], AgeMetric(unit="years"))

    assert series.name == "age_metric"
    assert series.title == "Age Metric"
    assert series.unit == "years"


@pytest.mark.unit
def test_aggregate_averages_metric_over_runs() -> None:
    run = build_simulation(engine=build_engine())
    series = RunAggregator().aggregate([run], AgeMetric(unit="years"))

    # The default engine's sole living HealthModule node is aged 25.
    np.testing.assert_array_equal(series.mean, np.array([25.0]))
    np.testing.assert_array_equal(series.std, np.array([0.0]))
