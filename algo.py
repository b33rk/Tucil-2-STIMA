def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def findListOfPoint(listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
    ans: list[tuple[float, float]] = []
    if(len(listPoint) == 2):
        return findMiddlePoint(listPoint[0], listPoint[1])

    for point1, point2 in zip(listPoint[:-1], listPoint[1:]):
        ans.append(findMiddlePoint(point1, point2))
    ans = (findListOfPoint(ans))
    return ans



point1: tuple[float, float] = (1, 0)
point2: tuple[float, float] = (2, 0)
middlePoint12: tuple[float, float] = findMiddlePoint(point1, point2)


pairOfPoint = [(0, 0), (2, 4), (4, 0), (4, 3), (9, 1)]

# brute force 

ans: list[tuple[float, float]] = findListOfPoint(pairOfPoint) 
print(ans)