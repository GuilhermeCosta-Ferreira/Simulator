"""Shared fixtures for adapter integration tests.

Every adapter reads or writes through a Source. These fixtures pin the Source to
tmp_path so the real data/ tree is never touched, and provide a ready-built
Simulation for the (de)serialization adapters.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from simulator.adapters.source import Source
from simulator.service.simulation import Simulation
from tests.helpers import builders


@pytest.fixture
def source(tmp_path: Path) -> Source:
    return Source("sim", "a test simulation", base_folder=tmp_path)


@pytest.fixture
def simulation() -> Simulation:
    return builders.build_simulation(current_step=1)
