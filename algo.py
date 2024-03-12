def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def addListOfPoint(idx: int, listPoint: list[tuple[float, float]]):
    if(idx == len(listPoint) - 2):
        return listPoint
    else:
        newPoint = findMiddlePoint(listPoint[idx], listPoint[idx + 1])
        listPoint.insert(idx+1,newPoint)
        return addListOfPoint(idx + 2, listPoint)



def findListOfPoint(iterasi : int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if(iterasi == 0.5):
        listPoint = addListOfPoint(0, listPoint)
        return [x for x in listPoint if x != listPoint[len(listPoint)//2 + 1]]
    else :
        listPoint = addListOfPoint(0, listPoint)
        return findListOfPoint(iterasi-0.5, [x for x in listPoint if x != listPoint[len(listPoint)//2 + 1]])



point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


pairOfPoint = [(0, 0), (0, 1), (0, 4)]

ans: list[tuple[float, float]] = findListOfPoint(1, pairOfPoint) 
print(ans)