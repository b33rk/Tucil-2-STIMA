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

def findListOfPointDepth(listPoint: list[Point], itr: int) -> list[Point]:
    ans: list[Point] = []
    if(itr == 0):
        if(len(listPoint) > 2):
            return []
        elif(len(listPoint) == 2):
            temp = findMiddlePoint(listPoint[0], listPoint[1])
            listPoint.insert(1, temp)
            return listPoint
        else:
            return []
    itr -= 1 
    mid: int = len(listPoint) // 2
    left = findListOfPointDepth(listPoint[:mid + 1], itr)
    right = findListOfPointDepth(listPoint[mid:], itr)
    ans.extend(left + right)

    return sorted(list(set(ans)))

arr = [(0, 0), (2, 2), (4, 0)] 
arrNew = findListOfPointDepth(arr, 2)
print(arrNew)