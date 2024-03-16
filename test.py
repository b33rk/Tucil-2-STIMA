import pygame
import sys
from pygame.locals import *
import numpy as np
from bruteForc import *

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bezier Curve Simulator")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Control points
control_points = [(100, 300), (200, 100), (400, 500), (600, 200), (700, 400)]
selected_point = None
dragging = False

# Function to draw the control points and lines
def draw():
    screen.fill(WHITE)
    for point in control_points:
        pygame.draw.circle(screen, RED, point, 5)
    if len(control_points) > 1:
        pygame.draw.lines(screen, BLUE, False, control_points, 2)
    pygame.display.flip()

# Function to calculate Bezier curve points
def calculate_bezier(t):
    n = len(control_points) - 1
    result = np.zeros(2)
    for i, point in enumerate(control_points):
        result += point * np.math.comb(n, i) * ((1 - t) ** (n - i)) * (t ** i)
    return result

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for i, point in enumerate(control_points):
                    if pygame.Rect(point[0] - 5, point[1] - 5, 10, 10).collidepoint(event.pos):
                        selected_point = i
                        dragging = True
                        break
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                dragging = False
                selected_point = None
        elif event.type == MOUSEMOTION:
            if dragging and selected_point is not None:
                control_points[selected_point] = event.pos

    draw()
    pairOfPoint = [(2, 0), (0,2), (5, 2), (7,0), (10, 10)]
    ans: list[tuple[float, float]] = bezierCurveNPoint(pairOfPoint,0.1)
    # Draw the Bezier curve
    for i in range(len(ans)):
        pygame.draw.circle(screen, BLACK, ans[i], 1)

    pygame.display.update()