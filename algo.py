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
import matplotlib.pyplot as plt
Point = tuple[float, float]

def findMiddlePoint(point1: Point, point2: Point) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0],  (0.5) * point1[1] + 0.5*point2[1])
    return middlePoint

def findPeakPoint(point1: Point, point2: Point, point3: Point) -> Point: 
    x: float = pow((1-0.5), 2)*point1[0] + (1-0.5)*0.5*point2[0] + pow((0.5), 2) * point3[0]
    y: float = pow((1-0.5), 2)*point1[1] + (1-0.5)*0.5*point2[1] + pow((0.5), 2) * point3[1]
    return (x, y)

def findListOfPoint(listPoint: list[Point]) -> list[Point]:
    ans: list[Point] = []
    if(len(listPoint) == 2):
        return findMiddlePoint(listPoint[0], listPoint[1])

    for point1, point2 in zip(listPoint[:-1], listPoint[1:]):
        ans.append(findMiddlePoint(point1, point2))
    ans.append(findListOfPoint(ans))
    return ans

def findListOfPointNew(listPoint: list[Point], itr: int) -> list[Point]:
    ans: list[Point] = []
    if(itr >= 1):
        itr -= 1
        if(len(listPoint) == 3):
            ans = firstIteration(listPoint)
        else: 
            for point1, point2 in zip(listPoint[:-1], listPoint[1:]):
                ans.append(findMiddlePoint(point1, point2))
        ans.extend(findListOfPointNew(ans, itr))
        ans.sort(key=lambda point: point[0])
    return ans

def firstIteration(listPoint: list[Point]) -> list[Point]: 
    ans: list[Point] = []
    for point in listPoint: 
        ans.append(point)

    ans.append(findMiddlePoint(listPoint[0], listPoint[1]))
    ans.append(findMiddlePoint(listPoint[1], listPoint[2]))
    middle: Point = findPeakPoint(listPoint[0], listPoint[1], listPoint[2])
    ans.sort(key=lambda point: point[0])
    ans[len(listPoint)//2 + 1] = middle

    return ans

pairOfPoint = [(0, 0), (2, 2), (4, 0)]
# brute force 
ans: list[Point] = findListOfPointNew(pairOfPoint, 1) 
# Plot the points
print(ans)
