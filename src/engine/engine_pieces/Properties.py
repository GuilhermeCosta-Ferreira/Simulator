# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np



# ================================================================
# 1. Section: Properties Class
# ================================================================
class Properties:
    @property
    def nr_of_citizens(self) -> int: return self._nr_of_citizens

    @property
    def connectivity_matrix(self) -> np.ndarray: return self._connectivity_matrix

    @property
    def citizens(self): return self._citizens



    # ================================================================
    # 2. Section: Setters
    # ================================================================
    @nr_of_citizens.setter
    def nr_of_citizens(self, value: int):
        if value <= 0: raise ValueError("Number of citizens must be positive.")

        self._nr_of_citizens = value

    @connectivity_matrix.setter
    def connectivity_matrix(self, value: np.ndarray): self._connectivity_matrix = value

    @citizens.setter
    def citizens(self, value: np.ndarray): self._citizens = value