def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def addListOfPoint(idx: int, end : int, listPoint: list[tuple[float, float]], isDel : bool):
    if(idx == end):
        if (isDel and idx > 2):
            listPoint = [x for x in listPoint if x != listPoint[idx - 2]]
        print(isDel, idx, listPoint)
        return listPoint
    else:
        if (isDel and idx > 2):
            listPoint = [x for x in listPoint if x != listPoint[idx - 1]]
            idx -= 1
        newPoint = findMiddlePoint(listPoint[idx], listPoint[idx + 1])
        listPoint.insert(idx+1,newPoint)
        print(isDel, end, idx, listPoint)
        isDel = not isDel
        return addListOfPoint(idx + 2, end, listPoint, isDel)



def findListOfPoint(iterasi : int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
    print("a")
    if(iterasi == 0.5):
        listPoint = addListOfPoint(1, len(listPoint) - 1, listPoint, True)
        return listPoint
    else :
        listPoint = addListOfPoint(0, len(listPoint) - 1, listPoint, True)
        return findListOfPoint(iterasi-0.5, listPoint)



point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


pairOfPoint = [(0, 0), (2,2), (0, 4)]

ans: list[tuple[float, float]] = findListOfPoint(1, pairOfPoint) 
print(ans)