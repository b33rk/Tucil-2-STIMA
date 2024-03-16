import matplotlib.pyplot as plt

def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    middlePoint: tuple[float, float]
    middlePoint = ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

    return middlePoint

def addListOfPoint(iterasi: int, tempPoint: list[tuple[float, float]], listPoint: list[tuple[float, float]], answer : list[list[tuple[float, float]]]) -> list[tuple[float, float]]:
    if(iterasi == 0):
        return listPoint
    else:
        end = len(listPoint)*2 - 1
        temp : list[tuple[float,float]] = []
        for idx in range (0, end - 1, 2):
            # print("b", idx)
            newPoint = findMiddlePoint(listPoint[idx], listPoint[idx + 1])
            temp.append(newPoint)
            listPoint.insert(idx+1,newPoint)
        # print(listPoint)
        listPoint = [x for x in listPoint if x not in tempPoint]
        answer.append(listPoint)
        # print(iterasi, listPoint, tempPoint)
            
        return addListOfPoint(iterasi - 1, temp, listPoint, answer)

# def findListOfPoint(iterasi : int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
#     print("a", iterasi)
#     if(iterasi == 1):
#         listPoint = addListOfPoint(0, listPoint)
#         return listPoint
#     else :
#         listPoint = addListOfPoint(0, listPoint)
#         return findListOfPoint(iterasi-1, listPoint)


pairOfPoint = [(0, 0), (2,2), (4, 0)]
answer : list[list[tuple[float,float]]] = []

ans: list[tuple[float, float]] = addListOfPoint(20,[pairOfPoint[len(pairOfPoint)//2]],pairOfPoint, answer) 
x, y = zip(*pairOfPoint)
plt.plot(x, y, marker='o', linestyle='-', markersize=5) 
for i in answer:
    x, y = zip(*i)
    plt.plot(x, y, marker='o', linestyle='-', markersize=5)  # Plot each list of points
plt.title('Plot of Lists of Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()