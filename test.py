Point = tuple[float, float]


def findMiddlePoint(point1: Point, point2: Point) -> Point:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0],  (0.5) * point1[1] + 0.5*point2[1])
    return middlePoint

def findListOfPoint(listPoint: list[Point]) -> list[Point]:
    ans: list[Point] = []
    if(len(listPoint) < 2):
        return []

    if(len(listPoint) == 2):
        temp = findMiddlePoint(listPoint[0], listPoint[1])
        listPoint.insert(1, temp)
        return listPoint
    else: 
        mid: int = len(listPoint) // 2
        left = findListOfPoint(listPoint[:mid + 1])
        right = findListOfPoint(listPoint[mid:])

    ans.extend(left + right)
    return sorted(list(set(ans)))

def findListOfPointD(listPoint: list[Point], itr: int) -> list[Point]:
    ans: list[Point] = []
    if(itr >= 1):
        itr -= 1      
        mid: int = len(listPoint) // 2
        left = findListOfPoint(listPoint[:mid + 1])
        right = findListOfPoint(listPoint[mid:])
        ans.extend(left + right)
    else: 
        return listPoint
        
    return sorted(list(set(findListOfPointD(ans, itr))))

def findPeakPoint(point1: Point, point2: Point, point3: Point) -> Point: 
    x: float = pow((1-0.5), 2)*point1[0] + (1-0.5)*0.5*point2[0] + pow((0.5), 2) * point3[0]
    y: float = pow((1-0.5), 2)*point1[1] + (1-0.5)*0.5*point2[1] + pow((0.5), 2) * point3[1]
    return (x, y)

def firstIteration(listPoint: list[Point]) -> list[Point]: 
    ans: list[Point] = []
    for point in listPoint: 
        ans.append(point)

    ans.append(findMiddlePoint(listPoint[0], listPoint[1]))
    ans.append(findMiddlePoint(listPoint[1], listPoint[2]))
    middle: Point = findPeakPoint(listPoint[0], listPoint[1], listPoint[2])
    ans.sort(key=lambda point: point[0])
    ans[len(listPoint)//2 + 1] = middle

arr = [(0, 0), (2, 2), (4, 0)] 
arrNew = findListOfPointD(arr, 10)
print(arrNew)

# def findListOfPointDepth(listPoint: list[Point], itr: int) -> list[Point]:
#     ans: list[Point] = []
#     if(itr > 1):
#         if(len(listPoint) > 2):
#             return []
#         elif(len(listPoint) == 2):
#             temp = findMiddlePoint(listPoint[0], listPoint[1])
#             listPoint.insert(1, temp)
#             return listPoint
#         else:
#             return []
#     itr -= 1 
#     mid: int = len(listPoint) // 2
#     left = findListOfPoint(listPoint[:mid + 1])
#     right = findListOfPoint(listPoint[mid:])
#     ans.extend(left + right)
#     return sorted(list(set(ans)))