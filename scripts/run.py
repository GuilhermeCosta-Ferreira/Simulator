# ================================================================
# 0. Section: IMPORTS
# ================================================================
from simulator import Simulation


# ================================================================
# 1. Section: INPUTS
# ================================================================



# ================================================================
# 2. Section: FUNCTIONS
# ================================================================



# ================================================================
# 3. Section: MAIN
# ================================================================
if __name__ == '__main__':
    sim = Simulation(
        simulation_name="test_simulation",
        simulation_description="the simulation to test",
    )

    sim.init_simulation()

    print(sim._source.folder)
    print(sim._source.config_path)
    print(sim._source.runs_folder)
    print(sim._source.base_folder)
    print(sim._source.simulation_name)
    print(sim._source.simulation_description)
