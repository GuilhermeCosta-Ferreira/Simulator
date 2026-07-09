# ================================================================
# 0. Section: IMPORTS
# ================================================================
import re

from pathlib import Path
from dataclasses import dataclass

from simulator.adapters.source import Source
from simulator.adapters.simulation_io import SimulationIO


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class Simulation:
    simulation_name: str
    simulation_description: str
    base_folder: Path = Path("data")

    @property
    def _source(self):
        return Source(
            simulation_name=self.simulation_name,
            simulation_description=self.simulation_description,
            base_folder=self.base_folder,
        )

    @_source.setter
    def _source(self, value: Source):
        self.simulation_name = value.simulation_name
        self.simulation_description = value.simulation_description
        self.base_folder = value.base_folder

    @property
    def _io(self):
        return SimulationIO(self._source)

    # ================================================================
    # 2. Section: Methods
    # ================================================================
    def init_simulation(self) -> Path:
        self._source = _updated_simulation_name(self._source)
        self._io.source = self._source

        run_folder = SimulationIO(self._source).init_simulation()
        return run_folder


# ──────────────────────────────────────────────────────
# 1.1 Subsection: Helper Functions
# ──────────────────────────────────────────────────────
def _updated_simulation_name(source: Source) -> Source:
    simulation_name = source.simulation_name

    if not source.base_folder.exists():
        return source

    pattern = re.compile(rf"{re.escape(simulation_name)}(_\d+)?$")
    nr_copies = len(
        [
            p
            for p in source.base_folder.iterdir()
            if p.is_dir() and pattern.fullmatch(p.name)
        ]
    )

    if nr_copies > 0:
        simulation_name = source.simulation_name + "_" + str(nr_copies + 1)

    source.simulation_name = simulation_name

    return source
