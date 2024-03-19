from bruteforce import * 
from dnc import * 
from util import * 


def CLI(): 
    while(True):
        print("pilih tipe algoritma: ")
        print("1. Bruteforce")
        print("2. Divide and Conquer") 
        print("3. exit")
        choice = toIntRange(input(), 1, 3)
        if(choice == 1): 
            Bruteforce()
        elif(choice == 2):
            DnC()
        else: 
            break

def Bruteforce(): 
    print("Masukkan titik")
    listTitik: list[tuple[float, float]] = toPoints(input())
    print("Masukkan nilai iterasi contoh 2")
    iterasi: float = toInt(input())
    result_bezier: list[tuple[float, float]] = bruteforceIterasi(listTitik, iterasi)
    start_time = time.time()
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    print(f"Execution time: {execution_time} ms ")
    plotBezier(listTitik, result_bezier)

def DnC(): 
    print("Masukkan titik")
    listTitik: list[tuple[float, float]] = toPoints(input())
    print("Masukkan nilai iterasi contoh 2")
    iterasi: int = toInt(input())
    start_time = time.time()
    result_bezier: list[tuple[float, float]] = addListOfPoint(iterasi, listTitik)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    print(f"Execution time: {execution_time} ms ")
    plotBezier(listTitik, result_bezier)