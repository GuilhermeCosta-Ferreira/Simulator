"""Contract tests for SimulationIO.

SimulationIO is a thin facade: it owns a Source and delegates each operation to
an injected collaborator (ConfigLoader, Downloader, Repository) and returns that
collaborator's result unchanged. These tests use recording fakes to prove the
delegation and argument forwarding, without touching the filesystem — the real
I/O is covered by the individual adapter integration tests.
"""

# ================================================================
# 0. Section: IMPORTS
# ================================================================
from pathlib import Path

import pytest

from simulator.adapters.simulation_io import SimulationIO
from simulator.adapters.source import Source


# ================================================================
# 1. Section: Fakes
# ================================================================
class FakeConfigLoader:
    def __init__(self, blueprint: object) -> None:
        self.blueprint = blueprint
        self.calls = 0

    def load_config(self) -> object:
        self.calls += 1
        return self.blueprint


class FakeDownloader:
    def __init__(self, out_path: Path) -> None:
        self.out_path = out_path
        self.calls: list[tuple] = []

    def download_run(
        self, simulation: object, run_nr: int, out_file_type: str = "hdf5"
    ) -> Path:
        self.calls.append((simulation, run_nr, out_file_type))
        return self.out_path


class FakeRepository:
    def __init__(self, sim_folder: Path, run_folder: Path) -> None:
        self.sim_folder = sim_folder
        self.run_folder = run_folder
        self.init_simulation_calls = 0
        self.init_run_calls = 0

    def init_simulation(self) -> Path:
        self.init_simulation_calls += 1
        return self.sim_folder

    def init_run(self) -> Path:
        self.init_run_calls += 1
        return self.run_folder


# ================================================================
# 2. Section: Fixtures
# ================================================================
@pytest.fixture
def source(tmp_path: Path) -> Source:
    return Source("sim", "desc", base_folder=tmp_path)


# ================================================================
# 3. Section: Unit Tests
# ================================================================
@pytest.mark.unit
def test_init_simulation_delegates_to_repository(source: Source) -> None:
    repository = FakeRepository(sim_folder=Path("sim"), run_folder=Path("run"))
    io = SimulationIO(
        source, FakeConfigLoader(None), FakeDownloader(Path()), repository
    )

    result = io.init_simulation()

    assert repository.init_simulation_calls == 1
    assert result == Path("sim")


@pytest.mark.unit
def test_init_run_delegates_to_repository(source: Source) -> None:
    repository = FakeRepository(sim_folder=Path("sim"), run_folder=Path("run"))
    io = SimulationIO(
        source, FakeConfigLoader(None), FakeDownloader(Path()), repository
    )

    result = io.init_run()

    assert repository.init_run_calls == 1
    assert result == Path("run")


@pytest.mark.unit
def test_load_config_returns_blueprint_from_config_loader(source: Source) -> None:
    sentinel_blueprint = object()
    config_loader = FakeConfigLoader(sentinel_blueprint)
    io = SimulationIO(
        source,
        config_loader,
        FakeDownloader(Path()),
        FakeRepository(Path(), Path()),
    )

    result = io.load_config()

    assert config_loader.calls == 1
    assert result is sentinel_blueprint


@pytest.mark.unit
def test_download_run_forwards_arguments_to_downloader(source: Source) -> None:
    out_path = Path("out/simulation.hdf5")
    downloader = FakeDownloader(out_path)
    io = SimulationIO(
        source,
        FakeConfigLoader(None),
        downloader,
        FakeRepository(Path(), Path()),
    )
    simulation = object()

    result = io.download_run(simulation, run_nr=7, out_file_type="hdf5")

    assert downloader.calls == [(simulation, 7, "hdf5")]
    assert result == out_path
