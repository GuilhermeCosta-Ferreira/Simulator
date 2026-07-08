# ================================================================
# 0. Section: IMPORTS
# ================================================================
from numpy.typing import NDArray
from dataclasses import dataclass


# ================================================================
# 1. Section: Functions
# ================================================================
@dataclass
class ConnectivityMatrix:
    data: NDArray

    def get_most_connected(self):
        pass
