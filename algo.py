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

def DnC_MiddlePoint(Point1: tuple[float, float], Point2: tuple[float, float], Point3: tuple[float, float], middlePoint : list[tuple[float, float]]):
    point1 = findMiddlePoint(Point3, Point1)
    point2 = findMiddlePoint(Point3, Point2)
    point = findMiddlePoint(point1,point2)
    middlePoint.append(point1)
    middlePoint.append(point2)
    return point

def addListOfPoint(iterasi: int, listPoint: list[tuple[float, float]], middlePoint:  list[tuple[float, float]], x: int) -> list[tuple[float, float]]:
    tempPoint : list[tuple[float, float]] = []
    if(iterasi == 0):
        return listPoint
    else:
        if (x == iterasi):
            tempList = listPoint
            while (len(middlePoint) != 1):
                tempPoint = middlePoint
                middlePoint = makeMiddlePoint(tempList)
                tempList = middlePoint
            # print(tempPoint)
            listPoint = [listPoint[0], middlePoint[0], listPoint[len(listPoint) - 1]]
        else:
            end = len(listPoint)*2 - 1
            # print(end)
            idx = 0
            for i in range(0,end - 1,2):
                # print(listPoint,middlePoint)
                point = DnC_MiddlePoint(listPoint[i],listPoint[i+1], middlePoint[idx], tempPoint)
                listPoint.insert(i + 1, point)
                idx += 1
        return addListOfPoint(iterasi - 1, listPoint, tempPoint,x)

point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3)]
pairOfPoint = [(1, 2), (3,1), (3, 3), (0,1)]
# pairOfPoint = [(1, 1), (3,1), (1, 2), (2,3), (2,5), (9,0), (10,8), (7,3), (0,0), (4,5)]

ans: list[tuple[float, float]] = addListOfPoint(10, pairOfPoint, [], 10)
# print(ans)
x, y = zip(*ans)
plt.plot(x, y, marker='o', linestyle='-', markersize=0.5) 
x, y = zip(*pairOfPoint)
plt.plot(x, y, marker='o', linestyle='-', markersize=5) 
plt.title('Plot of Lists of Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()