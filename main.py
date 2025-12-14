from src import Simulation, show_style

# Inspect the Portugal style
#show_style(style_label="portugal_style")

sim = Simulation.random(10)

sim.run()