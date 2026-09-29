import numpy as np
import matplotlib.pyplot as plt

from newton import newton_interpolation
from lagrange import lagrange_interpolation
from hermite import hermite_interpolation


# ==========================================
# Original function
# ==========================================

def f(x):
    return x**2 + 2*x + 1


# Derivative
def df(x):
    return 2*x + 2


# ==========================================
# Data
# ==========================================

# Newton and Lagrange
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [f(xi) for xi in x]

# Hermite
x_h = [0 ,1, 2]
y_h = [f(xi) for xi in x_h]
dy_h = [df(xi) for xi in x_h]


# ==========================================
# Plot values
# ==========================================

x_plot = np.linspace(-1, 10, 200)

# Original function
y_original = [f(xi) for xi in x_plot]


# ==========================================
# Newton
# ==========================================

y_newton = [
    newton_interpolation(x, y, xi)[0]
    for xi in x_plot
]


# ==========================================
# Lagrange
# ==========================================

y_lagrange = [
    lagrange_interpolation(x, y, xi)
    for xi in x_plot
]


# ==========================================
# Hermite
# ==========================================

y_hermite = [
    hermite_interpolation(x_h, y_h, dy_h, xi)
    for xi in x_plot
]


# ==========================================
# Newton visualization
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    x_plot,
    y_original,
    label="Original f(x)"
)

plt.plot(
    x_plot,
    y_newton,
    "--",
    label="Newton interpolation"
)

plt.scatter(
    x,
    y,
    label="Interpolation points"
)

plt.title("Newton Interpolation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()


# ==========================================
# Lagrange visualization
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    x_plot,
    y_original,
    label="Original f(x)"
)

plt.plot(
    x_plot,
    y_lagrange,
    "--",
    label="Lagrange interpolation"
)

plt.scatter(
    x,
    y,
    label="Interpolation points"
)

plt.title("Lagrange Interpolation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()


# ==========================================
# Hermite visualization
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    x_plot,
    y_original,
    label="Original f(x)"
)

plt.plot(
    x_plot,
    y_hermite,
    "--",
    label="Hermite interpolation"
)

plt.scatter(
    x_h,
    y_h,
    label="Interpolation points"
)

plt.title("Hermite Interpolation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.show()