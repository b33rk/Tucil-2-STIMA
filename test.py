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

def findListOfPointD(listPoint: list[Point], itr: int, ctr: int) -> list[Point]:
    ans: list[Point] = []
    if(itr >= 1):
        mid: int = len(listPoint) // 2
        left = findListOfPoint(listPoint[:mid + 1])
        right = findListOfPoint(listPoint[mid:])
        ans.extend(left + right)
        if(ctr == 1):
            ans = sorted(list(set(ans)))
            ans[len(ans)//2] = findMiddlePoint(ans[1], ans[3])
    else: 
        return listPoint 
    return sorted(list(set(findListOfPointD(ans, itr - 1, ctr + 1))))

def process(listPoint: list[Point], itr: int) -> list[list[Point]]:
    initialPoint: Point = listPoint[0]
    lastPoint: Point = listPoint[2]
    ctr: int = 1
    list_listPoint: list[list[Point]] = []
    idx: int = 0
    for i in range(1, itr+1): 
            ans: list[Point] = findListOfPointD(listPoint, i, ctr)
            if i > 1:
                temp: list[Point] = [item for item in ans if item not in list_listPoint[idx]]
                temp = findListOfPoint(temp)
                temp.insert(0, initialPoint)
                temp.insert(len(temp), lastPoint) 
                list_listPoint.append(temp)
                idx += 1
            else: 
                list_listPoint.append(ans)

    return list_listPoint

arr = [(0, 0), (2, 2), (4, 0)] 
arrNew = process(arr, 3)
print(arrNew[1])

