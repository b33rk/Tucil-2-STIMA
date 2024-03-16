import matplotlib.pyplot as plt
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
                temp =  [item for item in ans if item not in (list_listPoint[idx])]
                temp = findListOfPoint(temp)
                temp.insert(0, initialPoint)
                temp.insert(len(temp), lastPoint) 
                list_listPoint.append(temp)
                idx += 1
            else: 
                list_listPoint.append(ans)

    return list_listPoint

def cleanListPoint(listPoint: list[list[Point]], itr: int) -> list[Point]:
    ans: list[Point] = []
    temp: list[list[Point]] = listPoint[itr-1]
    for i in range(1, len(temp) - 1, 2):
        temp[i] = findMiddlePoint(temp[i-1], temp[i+1])

    garbage: list[Point] = []
    if(itr >= 3): 
        for i in range(0, len(listPoint)):
            garbage.extend(listPoint[i])
        garbage = list(set(garbage))
        print(temp)
        temp = [item for item in temp if item not in garbage]

    ans.append(temp[0])
    for i in range(1, len(temp)):
        ans.append(temp[i]) 
    ans.append(temp[len(temp) - 1])
    return ans

arr = [(0, 0), (2, 2), (4, 0)] 
arrNew = process(arr, 2)
# cleanArr = cleanListPoint(arrNew, )
for elmt in arrNew:
    print(elmt)

x, y = zip(*arr)
# x, y = zip(*cleanArr)
for i in range(len(arrNew)): 
    x, y = zip(*arrNew[i])
    plt.plot(x, y, marker='o', linestyle='-', label = i + 1)

plt.title('Modified Points on Cartesian Diagram')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
