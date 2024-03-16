import matplotlib.pyplot as plt

def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def makeMiddlePoint(listPoint: list[tuple[float, float]]):
    middlePoint : list[tuple[float, float]] = []
    for i in range(0,len(listPoint) - 1,1):
        middlePoint.append(findMiddlePoint(listPoint[i], listPoint[i+1]))
    return middlePoint

def DnC_MiddlePoint(Point1: tuple[float, float], Point2: tuple[float, float], Point3: tuple[float, float]):
    point1 = findMiddlePoint(Point3, Point1)
    point2 = findMiddlePoint(Point3, Point2)
    point = findMiddlePoint(point1,point2)
    return point

def addListOfPoint(isLeft: bool, iterasi: int, listPoint: list[tuple[float, float]], middlePoint:  list[list[tuple[float, float]]], x: int) -> list[tuple[float, float]]:
    tempPoint : list[list[tuple[float, float]]] = []
    point: list[tuple[float, float]] = []
    if(iterasi == 0):
        if (isLeft):
            listPoint.pop()
        return listPoint
    else:
        
        if (x == iterasi):
            tempList = listPoint
        else:
            # print(len(middlePoint[0]))
            if (isLeft):
                medList = [x[0] for x in middlePoint]
            else:
                middlePoint.reverse()
                medList = [x[-1] for x in middlePoint]

            tempList = [listPoint[0]] + medList + [listPoint[-1]]
        index = 0
        while (len(tempList) != 1):
            tempPoint.append(makeMiddlePoint(tempList))
            tempList = tempPoint[index]
            index += 1
        point.append(DnC_MiddlePoint(listPoint[0],listPoint[1], tempPoint[-1][0]))
        listPoint = [listPoint[0]] + point + [listPoint[-1]]
        leftSide = listPoint[:len(listPoint)//2 + 1]
        rightSide = listPoint[len(listPoint)//2:]
        return addListOfPoint(True, iterasi - 1, leftSide, tempPoint,x) + addListOfPoint(False, iterasi - 1, rightSide, tempPoint,x,)
point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3)]
pairOfPoint = [(1, 2), (3,1), (3, 3), (0,1)]
# pairOfPoint = [(2, 0), (0,2), (5, 2), (7,0), (10, 10)]
# pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3), (2,5), (9,0), (10,8), (7,3), (0,0), (4,5)]

a : list[list[tuple[float, float]]] = []
ans: list[tuple[float, float]] = addListOfPoint(True, 3, pairOfPoint, a, 3)
x, y = zip(*ans)
plt.plot(x, y, marker='o', linestyle='-', markersize=4)
# for i in range(1,3):
#     x, y = zip(*addListOfPoint(True, i, pairOfPoint, [], i))
#     plt.plot(x, y ,marker='o', linestyle='-', markersize=5, label = i + 1) 
x, y = zip(*pairOfPoint)
plt.plot(x, y, marker='o', linestyle='-', markersize=5) 
plt.title('Plot of Lists of Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# def DnC_Point(middlePoint:  list[list[tuple[float, float]]], Point1: tuple[float, float], Point2: tuple[float, float], tempPoint : list[list[tuple[float, float]]]):
#     medList = [x[0] for x in middlePoint]
#     tempList = [Point1] + medList + [Point2]
#     index = 0
#     while (len(tempPoint) != len(tempList) - 1):
#         tempPoint.append(makeMiddlePoint(tempList))
#         tempList = tempPoint[index]
#         index += 1
#     point = DnC_MiddlePoint(Point1, Point2, tempPoint[-1][0])
#     return [Point1] + [point] + [Point2]