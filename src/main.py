from GUI import *
from CLI import * 
from util import * 
from PyQt5.QtWidgets import QApplication


def main(): 
    while(True): 
        print("Silahkan memilih tipe tampilan")
        print("1. CLI")
        print("2. GUI")
        print("3. Exit")
        choice = toIntRange(input(), 1, 3)
        if(choice == 1): 
            CLI()
        elif(choice == 2): 
            DisplayGUI()
        else: quit()


main()