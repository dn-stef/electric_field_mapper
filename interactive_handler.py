from charges import Charge
from field_calculator import calculate_potential, calculate_electric_field


class InteractiveHandler:
    def __init__(self, charge_manager, visualizer, grid_data):
        self.charge_manager = charge_manager
        self.visualizer = visualizer
        self.grid_data = grid_data

    def on_click(self, event):
        if event.inaxes == self.visualizer.ax:
            charge = Charge(event.xdata, event.ydata, self.charge_manager.current_mode)
            self.charge_manager.add_charge(charge)
            V = calculate_potential(self.grid_data[0], self.grid_data[1], self.charge_manager.get_all_charges())
            e_field = calculate_electric_field(V, self.grid_data[2], self.grid_data[3])
            self.visualizer.update_plot(self.grid_data[0], self.grid_data[1], V, e_field[0], e_field[1], 
                                   self.charge_manager.get_all_charges())
            

    def on_mode_change(self, label):
        mode = 1 if label == "Positive" else -1
        self.charge_manager.set_mode(mode)

    def connect_events(self, fig):
        self.cid = fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.radio = self.visualizer.setup_ui_controls(self.on_mode_change)