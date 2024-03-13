def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def addListOfPoint(iterasi: int, listPoint: list[tuple[float, float]], x: int) -> list[tuple[float, float]]:
    if(iterasi == 0):
        return listPoint
    else:
        end = len(listPoint)
        start = 0
        isDel = (iterasi*2) % 2 == 0
        if (iterasi == 0.5):
            isDel = True
            start = 1
            end = len(listPoint) - 1
        for idx in range (start, end, 2):
            # print("b", idx)
            newPoint = findMiddlePoint(listPoint[idx], listPoint[idx + 1])
            listPoint.insert(idx+1,newPoint)
            end = len(listPoint)
            print(iterasi, end, listPoint)
        tempPoint = [listPoint[i] for i in range(len(listPoint)) if i not in [0, end-1, end//2]]
        if (isDel):
            listPoint = [x for x in listPoint if x not in tempPoint]
            print("a",iterasi, tempPoint)
            
        return addListOfPoint(iterasi - 0.5, listPoint, x)

# def findListOfPoint(iterasi : int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
#     print("a", iterasi)
#     if(iterasi == 1):
#         listPoint = addListOfPoint(0, listPoint)
#         return listPoint
#     else :
#         listPoint = addListOfPoint(0, listPoint)
#         return findListOfPoint(iterasi-1, listPoint)



point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


pairOfPoint = [(0, 0), (2,2), (4, 0)]

ans: list[tuple[float, float]] = addListOfPoint(2, pairOfPoint, 2) 
print(ans)