import matplotlib.pyplot as plt
import time

Point = tuple[float, float] 

def bezierCurveNPoint(list_point: list[Point], smoother: float = 0.1) -> list[Point]:
    n: int = len(list_point) - 1
    result: list[Point] = []
    t: float = 0
    while(t <= 1):
        x: float = 0
        y: float = 0
        for k, (point_x, point_y) in enumerate(list_point): 
            x += bezierPointCalc(point_x, n, k, t)
            y += bezierPointCalc(point_y, n, k, t)
        result.append((x, y)) 
        t += smoother
    return result

def bezierPointCalc(point_x_or_y: float, n: int, k: int, t: float) -> float:
    return binomialCoeff(n, k) * point_x_or_y * pow((1-t), (n-k)) * pow(t, k)

def binomialCoeff(n: int, k: int) -> float: 
    return fact(n) / (fact(k) * fact(n-k))

def fact(n: int) -> int: 
    ans: int = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

def bruteforceIterasi(list_point: list[Point], iterasi: int):
    temp_list = list(set(list_point))
    if (len(temp_list) < 3):
        return []
    else :
        point_count = pow(2, iterasi) + 1
        return bezierCurveBruteForce_PointInput(list_point, point_count)

def bezierCurveBruteForce_PointInput(list_point: list[Point], result_point_count: int) -> list[Point]:
    t : int = 1/result_point_count
    if (1 % t != 0):
        result_point_count -= 1
    if (1 % t == 0 and t <= 20):
        result_point_count -= 1
    t = 1/result_point_count
    return bezierCurveNPoint(list_point, t)

def plotBezier(core_point: list[Point], curve_point: list[Point]):
    x_core, y_core = zip(*core_point)
    x_curve, y_curve = zip(*curve_point)
    plt.plot(x_core, y_core, marker = 'x', linestyle = '-', label = 'Initial Point')
    plt.plot(x_curve, y_curve, marker='o', linestyle='-', label = 'Bezier Curve')

    plt.title('Bezier Curve on Cartesian Diagram')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

list_point = [(0, 0), (2, 2), (4, 0), (3, 4), (5, 6), (6,-5), (7, 10), (8, -10), (10, 10), (11, -50), (50, -100)]
# list_point = [(2, 0), (0,2), (5, 2), (7,0), (10, 10)]
# start_time = time.time()
points = bezierCurveBruteForce_PointInput(list_point, 25)
# points = bruteforceIterasi(list_point, 10)
# points = bezierCurveNPoint(list_point, 0.105)
print(len(points))
# end_time = time.time()
# execution_time = end_time - start_time
# print(len(points))
# print("Execution time:", execution_time, "seconds")
# plotBezier(list_point1, points)