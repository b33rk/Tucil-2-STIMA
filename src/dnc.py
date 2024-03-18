import matplotlib.pyplot as plt
import numpy as np
import time

def findMiddlePoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    return ((0.5) * point1[0] + 0.5 * point2[0], (0.5) * point1[1] + 0.5*point2[1])

def makeMiddlePoint(listPoint: list[tuple[float, float]]):
    middlePoint : list[tuple[float, float]] = []
    for i in range(0,len(listPoint) - 1,1):
        middlePoint.append(findMiddlePoint(listPoint[i], listPoint[i+1]))
    return middlePoint

def addListOfPoint(iterasi: int, listPoint: list[tuple[float, float]]) -> list[tuple[float, float]]:
    tempPoint : list[tuple[float, float]] = []
    leftSide: list[tuple[float, float]] = []
    rightSide: list[tuple[float, float]] = []
    if(iterasi == 0):
        return [listPoint[-1]]
    else:
        tempList = listPoint
        leftSide = [listPoint[0]]
        while (len(tempList) != 1):
            tempPoint = makeMiddlePoint(tempList)
            leftSide.append(tempPoint[0])
            rightSide.append(tempPoint[-1])
            tempList = tempPoint
        rightSide.reverse()
        rightSide.append(listPoint[-1])
        return addListOfPoint(iterasi - 1, leftSide) + addListOfPoint(iterasi - 1, rightSide)

def DnC_bezier_curve(iterasi: int, listPoint: list[tuple[float, float]]):
    if iterasi == 0:
        return listPoint
    else:
        return [listPoint[0]] + addListOfPoint(iterasi, listPoint)