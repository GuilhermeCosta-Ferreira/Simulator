# ================================================================
# 0. Section: IMPORTS
# ================================================================
from pathlib import Path
from dataclasses import dataclass

from simulator.domain.instantiation.simulation_blueprint import SimulationBlueprint
from simulator.service.simulation_run import SimulationRun

from .source import Source
from .repository import Repository
from .downloader import Downloader
from .config_loader import ConfigLoader


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class SimulationIO:
    source: Source

    _config_loader: ConfigLoader
    _downloader: Downloader
    _repository: Repository

    def init_simulation(self) -> Path:
        sim_folder = self._repository.init_simulation()

        return sim_folder

    def init_run(self) -> Path:
        run_folder = self._repository.init_run()

        return run_folder

    def load_config(self) -> SimulationBlueprint:
        blueprint = self._config_loader.load_config()
        return blueprint

    def download_run(
        self, simulation: SimulationRun, run_nr: int, out_file_type: str = "hdf5"
    ) -> Path:
        out_path = self._downloader.download_run(simulation, run_nr, out_file_type)
        return out_path
