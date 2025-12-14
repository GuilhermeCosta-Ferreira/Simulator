# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np
from copy import deepcopy

from ..logger import logger
from ..components import Citizen
from .utils import initiate_connectivity_matrix
from .engine_pieces import Properties, Run


class Simulation(Properties, Run):
    # ================================================================
    # 1. Section: Initializers
    # ================================================================
    def __init__(self, citizens: np.ndarray, connectivity_matrix: np.ndarray):
        self.citizens = citizens
        self.connectivity_matrix = connectivity_matrix
        
        self.iterations = 0

        self.citizens_history = [deepcopy(self.citizens)]
        self.connectivity_matrix_history = [deepcopy(self.connectivity_matrix)]

    @classmethod
    def random(cls, nr_of_citizens: int) -> "Simulation":
        citizens = np.array([Citizen.random(citizen_id=i) for i in range(nr_of_citizens)])
        connectivity = initiate_connectivity_matrix(nr_of_citizens)

        logger.info(f"Initialized random simulation with {nr_of_citizens} citizens.")
        logger.debug(f"Citizens:\n{citizens}")
        logger.debug(f"Connectivity Matrix:\n{connectivity}")

        return cls(citizens, connectivity)