import numpy as np

def create_grid(x_range, y_range, resolution):
    x_coords = np.linspace(x_range[0], x_range[1], resolution)
    y_coords = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x_coords, y_coords)

    dx = x_coords[1] - x_coords[0]
    dy = y_coords[1] - y_coords[0]

    return X, Y, dx, dy

def calculate_potential(X, Y, charges):
    k = 1
    epsilon = 0.1
    V = np.zeros_like(X)
    for charge in charges:
        r = np.sqrt((X - charge.x) ** 2 + (Y - charge.y) ** 2) + epsilon
        V += (k * charge.q) / r
    
    return V

def calculate_electric_field(V, dx, dy):
    grad_y, grad_x = np.gradient(V, dy, dx)
    Ex = -grad_x
    Ey = -grad_y
    return Ex, Ey