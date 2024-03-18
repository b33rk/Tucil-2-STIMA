

def toIntRange(input_str: str, range1: int, range2: int) -> int: 
    while True:
        try:
            choice = int(input_str)
            if range1 <= choice <= range2:
                return choice
            else:
                print(f"Input out of range. Masukkan sesuai range antara {range1} dan {range2}")
        except ValueError:
            print("Invalid input. Masukkan sebuah integer")

        input_str = input("Masukkan ulang input: ")

def toPoints(input_str: str) -> list[tuple[float, float]]:
    ans: list[tuple[float, float]] = []
    while True:
        ans = []
        try:
            points = input_str.replace(' ', '').split('),(')
            points[0] = points[0].replace('(', '')
            points[-1] = points[-1].replace(')', '')

            for point in points:
                x, y = point.split(',')
                ans.append((float(x), float(y)))

            break

        except ValueError:
            print("Invalid input. Masukkan input seperti contoh: (1, 2), (4, 5)")

        input_str = input("Masukkan input lagi: ")

    return ans

def toInt(input_str: str) -> int: 
    while True:
        try:
            choice = int(input_str)
            return choice
        except ValueError:
            print("Invalid input. Masukkan sebuah integer")

        input_str = input("Masukkan ulang input: ") 

    
def toFloat(input_str: str) -> float: 
    while True:
        try:
            choice = float(input_str)
            if(choice < 0 and choice > 1): 
                print("nilai tidak diantaranya 0 dan 1, masukkan ulang" )
            else: 
                return choice
        except ValueError:
            print("Invalid input. Masukkan sebuah integer")

        input_str = input("Masukkan ulang input: ") 

    