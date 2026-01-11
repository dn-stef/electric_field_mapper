import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import numpy as np

class Visualizer:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
    
    def update_plot(self, X, Y, V, Ex, Ey, charges):
        self.ax.clear()
        self.ax.streamplot(X, Y, Ex, Ey, density=2, color='black', linewidth=1, zorder=1)
        V_clipped = np.clip(V, -100, 100)
        self.ax.contour(X, Y, V_clipped, levels=20, colors='magenta', linewidths=0.5, zorder=2)

        for charge in charges:
            color='blue' if charge.q > 0 else 'red'
            self.ax.scatter(charge.x, charge.y, color=color, s=200, zorder=3)

            text = '+' if charge.q > 0 else '-'
            self.ax.text(charge.x, charge.y, text, fontsize=16, fontweight='bold', color='black',
                         ha='center', va='center', zorder=4)
        title = "Electric Field Lines & Equipotentials"
        self.ax.set_title(title)

        self.ax.set_xlim(X.min(), X.max())
        self.ax.set_ylim(Y.min(), Y.max())
        self.fig.canvas.draw()

    def setup_ui_controls(self, callback):
        left, bottom, width, height = 0.01, 0.4, 0.15, 0.16
        ax_radio = plt.axes([left, bottom, width, height])

        labels = ("Positive", "Negative")
        radio = RadioButtons(ax_radio, labels)
        radio.on_clicked(callback)

        return radio