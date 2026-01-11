import matplotlib.pyplot as plt
from charges import ChargeManager
from field_calculator import create_grid, calculate_potential, calculate_electric_field
from visualizer import Visualizer
from interactive_handler import InteractiveHandler

x_range = (-10, 10)
y_range = (-10, 10)
resolution = 200
grid_data = create_grid(x_range, y_range, resolution)

fig, ax = plt.subplots(figsize=(8, 6))
fig.canvas.manager.set_window_title("Point Charge Electric Field Simulator")
fig.subplots_adjust(left=0.22)

charge_manager = ChargeManager()
visualizer = Visualizer(fig, ax)
interactive_handler = InteractiveHandler(charge_manager, visualizer, grid_data)

interactive_handler.connect_events(fig)

X, Y, dx, dy = grid_data
initial_V = calculate_potential(X, Y, charge_manager.get_all_charges())
initial_e_field = calculate_electric_field(initial_V, dx, dy)
visualizer.update_plot(X, Y, initial_V, initial_e_field[0], initial_e_field[1], 
                       charge_manager.get_all_charges())

plt.show()