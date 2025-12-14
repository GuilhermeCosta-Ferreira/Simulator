from copy import deepcopy

from .Summary import Summary
from ..utils import age_citizens

class Run(Summary):
    def run_step(self):
        age_citizens(self.citizens)
        self.iterations += 1
        self.citizens_history.append(deepcopy(self.citizens))

    def run(self):
        while any(citizen.state == "alive" for citizen in self.citizens): 
            self.run_step()

        self.summary()