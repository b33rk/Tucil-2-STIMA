import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def makeMiddlePoint(listPoint: list[tuple[float, float]]):
    middlePoint : list[tuple[float, float]] = []
    for i in range(0,len(listPoint) - 1,1):
        middlePoint.append(findMiddlePoint(listPoint[i], listPoint[i+1]))
    return middlePoint

def addListOfPoint(isLeft: bool, iterasi: int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
    tempPoint : list[tuple[float, float]] = []
    leftSide: list[tuple[float, float]] = []
    rightSide: list[tuple[float, float]] = []
    if(iterasi == 0):
        if (isLeft):
            return [listPoint[0]] + [listPoint[-1]]
        else:
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
        return addListOfPoint(True, iterasi - 1, leftSide) + addListOfPoint(False, iterasi - 1, rightSide)
    

def DnC_bezier_curve(iterasi: int, listPoint: list[tuple[float, float]]):
    if (iterasi == 0):
        return listPoint
    else:
        return addListOfPoint(True, iterasi, pairOfPoint)

point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


# pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3)]
# pairOfPoint = [(1, 2), (3,1), (3, 3), (0,1)]
pairOfPoint = [(3, 1), (1,3), (3, 3), (1,1)]
# pairOfPoint = [(1, 1), (3,2), (1, 2), (3,3)]
# pairOfPoint = [(2, 0), (0,2), (5, 2), (7,0), (10, 10)]
# pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3), (2,5), (9,0), (10,8), (7,3), (0,0), (4,5)]

a : list[list[tuple[float, float]]] = []
ans: list[tuple[float, float]] = addListOfPoint(True, 20, pairOfPoint)
# x, y = zip(*ans)
# plt.plot(x, y, marker='o', linestyle='-', markersize=2)
# # for i in range(1,3):
# #     x, y = zip(*addListOfPoint(True, i, pairOfPoint))
# #     plt.plot(x, y ,marker='o', linestyle='-', markersize=5, label = i + 1) 
# x, y = zip(*pairOfPoint)
# print(len(ans))
# plt.plot(x, y, marker='o', linestyle='-', markersize=5) 
# plt.title('Plot of Lists of Points')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.show()
fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', linestyle='-', markersize=5)
ax.grid(True)
ax.set_title('Plot of Lists of Points')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
def init():
    line.set_data([], [])
    return line,

def animate(iteration):
    points = DnC_bezier_curve(iteration,pairOfPoint)
    x, y = zip(*points)
    line.set_data(x, y)
    ax.set_xlim(min(x) - 1, max(x) + 1)
    ax.set_ylim(min(y) - 1, max(y) + 1)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, frames=5, init_func=init, interval = 1000, blit=True, repeat = False)

# plt.show()