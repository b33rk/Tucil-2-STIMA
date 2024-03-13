import matplotlib.pyplot as plt

def quadratic_bezier_curve(control_points, iterations):
    for _ in range(iterations):
        new_control_points = []
        for i in range(len(control_points) - 1):
            p0 = control_points[i]
            p1 = control_points[i + 1]
            midpoint = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
            new_control_points.append(p0)
            new_control_points.append(midpoint)
        new_control_points.append(control_points[-1])
        control_points = new_control_points
    return control_points

def plot_quadratic_bezier_curve(control_points):
    x, y = zip(*control_points)
    plt.plot(x, y, 'ro-', label='Control Points')
    plt.title('Quadratic Bézier Curve')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
control_points = [(1, 1), (2, 5), (4, 3)]  # Define control points as tuples (x, y)
iterations = 3  # Number of iterations
final_control_points = quadratic_bezier_curve(control_points, iterations)
plot_quadratic_bezier_curve(final_control_points)