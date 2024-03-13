import matplotlib.pyplot as plt
import numpy as np

def quadratic_bezier_curve(points, t):
    p0, p1, p2 = points
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y

def plot_quadratic_bezier_curve(points, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    curve_points = [quadratic_bezier_curve(points, t) for t in t_values]
    x, y = zip(*curve_points)
    plt.plot(x, y, label='Quadratic Bézier Curve')
    for point in points:
        plt.scatter(*point, color='red', zorder=5)
    plt.title('Quadratic Bézier Curve')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
control_points = [(1, 1), (2, 5), (4, 3)]  # Define control points as tuples (x, y)
plot_quadratic_bezier_curve(control_points)