import matplotlib.pyplot as plt
import numpy as np
import time

def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    return ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

def makeMiddlePoint(listPoint: list[tuple[float, float]]):
    middlePoint : list[tuple[float, float]] = []
    for i in range(0,len(listPoint) - 1,1):
        middlePoint.append(findMiddlePoint(listPoint[i], listPoint[i+1]))
    return middlePoint

def addListOfPoint(iterasi: int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
    tempPoint : list[tuple[float, float]] = []
    leftSide: list[tuple[float, float]] = []
    rightSide: list[tuple[float, float]] = []
    if(iterasi == 0):
        return [listPoint[-1]]
    else:
        tempList = listPoint
        leftSide = [listPoint[0]]
        while (len(tempList) != 1):
            tempPoint = makeMiddlePoint(tempList)
            leftSide.append(tempPoint[0])
            rightSide.append(tempPoint[-1])
            tempList = tempPoint
        rightSide.reverse()
        rightSide.append(listPoint[-1])
        return addListOfPoint(iterasi - 1, leftSide) + addListOfPoint(iterasi - 1, rightSide)

def DnC_bezier_curve(iterasi: int, listPoint: list[tuple[float, float]]):
    if iterasi == 0:
        return listPoint
    else:
        return [listPoint[0]] + addListOfPoint(iterasi, listPoint)

# pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3)]
# pairOfPoint = [(1, 2), (3,1), (3, 3), (0,1)]
# pairOfPoint = [(3, 1), (1,3), (3, 3), (1,1)]
# pairOfPoint = [(1, 1), (3,2), (1, 2), (3,3)]
# pairOfPoint = [(1, 1), (1,3), (0, 0), (3,1)]
# pairOfPoint = [(6,-6),(3,-2),(-1, 3), (-2, 6), (0, 10), (3, 10), (5, 6) ,(5.5, 3), (6, -6), (6.5, 3), (7, 6) ,(9, 10), (12, 10), (14, 6), (13, 3), (9, -2), (6, -6)]
pairOfPoint = [(2, 0), (0,2), (5, 2), (7,0), (10, 10)]
# pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3), (2,5), (9,0), (10,8), (7,3), (0,0), (4,5)]

# a : list[list[tuple[float, float]]] = []
# start_time = time.time()
# ans: list[tuple[float, float]] = DnC_bezier_curve(5, pairOfPoint)
# end_time = time.time()
# execution_time = end_time - start_time
# print(len(ans))
# print("Execution time:", execution_time, "seconds")
# x, y = zip(*ans)
# plt.plot(x, y, marker='o', linestyle='-', markersize=2)
# # for i in range(1,5):
# #     x, y = zip(*addListOfPoint(True, i, pairOfPoint))
# #     plt.plot(x, y ,marker='o', linestyle='-', markersize=5, label = i + 1) 
# x, y = zip(*pairOfPoint)
# plt.plot(x, y, marker='o', linestyle='-', markersize=5) 
# plt.title('Plot of Lists of Points')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.show()