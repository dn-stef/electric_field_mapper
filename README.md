# Electric Field Mapper

An interactive 2D electric field and equipotential visualizer built with Python, NumPy, and Matplotlib. Click to place positive and negative charges and see the resulting electric field lines and equipotential surfaces in real-time.

![Electric Field Simulator](screenshot.png)
*Example visualization showing field lines (black arrows) and equipotential lines (purple contours)*

---

## Table of Contents

- [Features](#features)
- [Physics Background](#physics-background)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Requirements](#requirements)

---

## Features

- **Interactive charge placement**: Click anywhere on the plot to add point charges
- **Real-time visualization**: Electric field lines and equipotential surfaces update instantly
- **Toggle charge type**: Switch between positive and negative charges using radio buttons
- **Color-coded display**: 
  - Blue circles with `+` symbols for positive charges
  - Red circles with `−` symbols for negative charges
  - Black arrows showing electric field direction
  - Purple contour lines for equipotential surfaces
- **Physics-accurate**: Based on Coulomb's Law and the gradient relationship between field and potential

---

## Physics Background

### Electric Potential

The electric potential at any point is the sum of contributions from all charges:

$$V(\vec{r}) = k \sum_{i} \frac{q_i}{r_i}$$

Where:
- $V$ = electric potential (volts)
- $k$ = Coulomb's constant (set to 1 for simplicity)
- $q_i$ = magnitude of charge $i$
- $r_i$ = distance from charge $i$ to the point

### Electric Field

The electric field is derived from the potential gradient:

$$\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}, \frac{\partial V}{\partial y}\right)$$

### Key Relationship

**Electric field lines are always perpendicular to equipotential lines.** This fundamental relationship arises because the field points in the direction of steepest potential decrease.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/dn-stef/electric_field_mapper.git
cd electric_field_mapper
```

2. Install required packages:
```bash
pip install numpy matplotlib
```

Or using requirements.txt (if provided):
```bash
pip install -r requirements.txt
```

---

## Usage

Run the simulator:
```bash
python main.py
```

### Controls

1. **Select charge type**: Use the radio buttons on the left to choose "Positive" or "Negative"
2. **Place charges**: Click anywhere on the plot to add a charge
3. **Observe**: Watch the electric field lines (black arrows) and equipotential contours (purple lines) update in real-time

### Tips

- Start with a single charge to see the radial field pattern
- Place opposite charges to see field lines connecting them
- Place same-sign charges to see how fields repel and combine
- Equipotential lines show regions of equal voltage (like topographic elevation lines)

---

## Project Structure
```
electric_field_mapper/
│
├── main.py                    # Entry point - initializes and runs the application
├── charges.py                 # Charge and ChargeManager classes
├── field_calculator.py        # Physics calculations (potential, E-field)
├── visualizer.py              # Matplotlib plotting and rendering
├── interactive_handler.py     # Mouse clicks, button callbacks, event handling
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

### Module Descriptions

- **`charges.py`**: Defines the `Charge` class (stores position and magnitude) and `ChargeManager` class (manages the collection of charges and current placement mode)

- **`field_calculator.py`**: Contains pure physics calculations:
  - `create_grid()`: Generates the 2D coordinate grid
  - `calculate_potential()`: Computes electric potential at all grid points
  - `calculate_electric_field()`: Derives field from potential using gradient

- **`visualizer.py`**: Handles all matplotlib visualization:
  - Draws streamplot for field lines
  - Draws contour plot for equipotentials
  - Renders charge markers with +/− symbols
  - Creates radio button UI controls

- **`interactive_handler.py`**: Connects user interactions to physics:
  - Handles mouse clicks to place charges
  - Manages mode switching (positive/negative)
  - Triggers recalculation and redrawing

- **`main.py`**: Ties everything together and launches the application

---

## How It Works

### Computational Approach

1. **Grid Creation**: A 2D meshgrid of 200×200 points is created using `np.meshgrid`

2. **Potential Calculation**: For each charge, the contribution $kq/r$ is calculated at every grid point and summed

3. **Field Calculation**: The electric field is computed using `np.gradient` to find $\vec{E} = -\nabla V$

4. **Visualization**: 
   - `matplotlib.pyplot.streamplot` traces field lines by following the vector field
   - `matplotlib.pyplot.contour` finds and draws curves of constant potential
   - Charge markers are plotted with `scatter` and annotated with `text`

### Singularity Handling

Since potential approaches infinity at charge locations ($r \to 0$), a small epsilon value (0.1) is added to distances to prevent division by zero:
```python
r = np.sqrt((X - charge.x)**2 + (Y - charge.y)**2) + epsilon
```

### Vectorization

NumPy's array broadcasting is used extensively for efficiency. Instead of looping over individual grid points, operations are performed on entire arrays simultaneously:
```python
r = np.sqrt((X - charge.x)**2 + (Y - charge.y)**2)  # Vectorized distance calculation
```

---

## Requirements

- **Python**: 3.7+
- **NumPy**: 1.19+ (for array operations and gradient calculations)
- **Matplotlib**: 3.3+ (for visualization and interactive widgets)

Create a `requirements.txt`:
```
numpy>=1.19.0
matplotlib>=3.3.0
```

---

## About the Author 🃏

I'm a physics graduate specializing in computational physics and Python development. 

This project demonstrates the application of numerical methods and scientific visualization to classical electromagnetism, translating Coulomb's Law and field theory into an interactive educational tool.


---

Built with Python.

<p align="center">
  <img src="https://images.icon-icons.com/2699/PNG/512/python_logo_icon_168886.png" alt="Python" width="80" height="80"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo. svg.png" alt="Matplotlib" width="80" height="80"/>
  <img src="https://img.icons8.com/color/512/numpy.png" alt="NumPy" width="80" height="80"/>
</p>
