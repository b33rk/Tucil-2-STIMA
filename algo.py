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
