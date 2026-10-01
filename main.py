import numpy as np
import matplotlib.pyplot as plt

from newton import newton_interpolation
from lagrange import lagrange_interpolation


# Runge's function used across the whole file
def f(x):
    return 1 / (1 + 25 * x**2)


# Dense grid for plotting the original function and evaluations
x_plot = np.linspace(-1, 1, 500)
y_original = [f(xi) for xi in x_plot]


# ==============================================================================
# 1. BEFORE: Low degree polynomial (5 points) -> Smooth approximation
# ==============================================================================
x_5 = np.linspace(-1, 1, 5)
y_5 = [f(xi) for xi in x_5]

y_newton_5 = [newton_interpolation(x_5, y_5, xi)[0] for xi in x_plot]
y_lagrange_5 = [lagrange_interpolation(x_5, y_5, xi) for xi in x_plot]

plt.figure(figsize=(9, 5))
plt.plot(x_plot, y_original, "k-", label="Original f(x)", linewidth=2)
plt.plot(x_plot, y_newton_5, "r--", label="Newton (5 points)")
plt.plot(x_plot, y_lagrange_5, "b:", label="Lagrange (5 points)")
plt.scatter(x_5, y_5, color="black", label="Nodes (N=5)", zorder=5)

plt.title("BEFORE: 5 Interpolation Points (Smooth, low error)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.legend()
plt.show()


# ==============================================================================
# 2. AFTER: High degree polynomial (11 points) -> Runge's Phenomenon
# ==============================================================================
x_11 = np.linspace(-1, 1, 11)
y_11 = [f(xi) for xi in x_11]

y_newton_11 = [newton_interpolation(x_11, y_11, xi)[0] for xi in x_plot]
y_lagrange_11 = [lagrange_interpolation(x_11, y_11, xi) for xi in x_plot]

plt.figure(figsize=(9, 5))
plt.plot(x_plot, y_original, "k-", label="Original f(x)", linewidth=2)
plt.plot(x_plot, y_newton_11, "r--", label="Newton (11 points)")
plt.plot(x_plot, y_lagrange_11, "b:", label="Lagrange (11 points)")
plt.scatter(x_11, y_11, color="red", label="Nodes (N=11)", zorder=5)

plt.title("AFTER: 11 Interpolation Points (Runge Phenomenon Edge Oscillations)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-0.5, 1.5)  # Constrained to see the blowup at boundaries
plt.grid(True)
plt.legend()
plt.show()
