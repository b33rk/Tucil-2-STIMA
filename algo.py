def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def addListOfPoint(idx: int, listPoint: list[tuple[float, float]]):
    if(idx == len(listPoint)-1):
        # if (isDel or isEnd):
        #     listPoint = [x for x in listPoint if x != listPoint[idx - 1]]
        # print(isDel, idx, listPoint)
        return listPoint
    else:
        # if (isDel and idx > 1):
        #     listPoint = [x for x in listPoint if x != listPoint[idx - 1]]
        #     idx -= 1
        newPoint = findMiddlePoint(listPoint[idx], listPoint[idx + 1])
        listPoint.insert(idx+1,newPoint)
        # print(len(listPoint)-1, idx, listPoint)
        return addListOfPoint(idx + 2, listPoint)

def findListOfPoint(iterasi : int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
    print("a", iterasi)
    if(iterasi == 1):
        listPoint = addListOfPoint(0, listPoint)
        return listPoint
    else :
        listPoint = addListOfPoint(0, listPoint)
        return findListOfPoint(iterasi-1, listPoint)



point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


pairOfPoint = [(0, 0), (2,2), (0, 4)]

ans: list[tuple[float, float]] = findListOfPoint(2, pairOfPoint) 
print(ans)