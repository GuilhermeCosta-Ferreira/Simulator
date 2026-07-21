# ================================================================
# 0. Section: IMPORTS
# ================================================================
from typing import Generic, TypeVar
from matplotlib.axes import Axes
from dataclasses import dataclass
from abc import ABC, abstractmethod

from ....domain.analysis import BaseAggregator

# Aggregator variant each concrete renderer draws (line, field, ...).
AggregatorT = TypeVar("AggregatorT", bound=BaseAggregator)


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class MetricRenderer(ABC, Generic[AggregatorT]):
    @abstractmethod
    def draw(self, axes: Axes, series: AggregatorT) -> None: ...
