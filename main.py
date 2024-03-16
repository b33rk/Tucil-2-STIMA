import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from bruteforce import *
from algo4 import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget) 
        vertical_box = QVBoxLayout(central_widget)

        label = QLabel("Pilih Tipe Algoritma")
        label.setAlignment(Qt.AlignCenter)
        vertical_box.addWidget(label)

        font = QFont()
        font.setPointSize(20) 
        label.setFont(font)


        self.button_bruteforce = QPushButton("BruteForce")
        self.button_bruteforce.setFixedHeight(50)
        self.button_bruteforce.clicked.connect(self.bruteforceUI)
        self.button_dnc = QPushButton("Divide And Conquer")
        self.button_dnc.setFixedHeight(50)
        self.button_dnc.clicked.connect(self.DNCUI)

        vertical_box.addStretch(0)
        vertical_box.addWidget(self.button_bruteforce)
        vertical_box.addWidget(self.button_dnc)
        self.setLayout(vertical_box)
        
    def DNCUI(self): 
        self.menuBar().clear()
        self.setWindowTitle("Divide And Conquer Bezier")
    
        # setup window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 
        self.layout = QVBoxLayout(self.central_widget) 

        # back button
        self.button_back = QPushButton("Back")
        self.button_back.clicked.connect(self.setUI)
        self.layout.addWidget(self.button_back)
        self.button_back.setFixedSize(30, 20)

        # figure to show plt
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # input point 
        self.input_bezier = QLineEdit()
        self.input_bezier.setPlaceholderText("Masukkan point sebagai tuple, contoh: (x1, y1), (x2, y2)")

        # iterasi 
        self.input_iterasi = QLineEdit() 
        self.input_iterasi.setPlaceholderText("Masukkan iterasi contoh: 2")

        # process
        self.button = QPushButton("Enter") 
        self.button.clicked.connect(self.plot_draw_dnc)
        self.layout.addWidget(self.input_bezier)

        box = QHBoxLayout()
        box.addWidget(self.input_iterasi, 1)
        box.addWidget(self.button, 2)
        self.layout.addLayout(box) 
    
    def bruteforceUI(self): 
        # clear menu bar
        self.menuBar().clear()
        self.setWindowTitle("Bruteforce Bezier")

        # setup window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 
        self.layout = QVBoxLayout(self.central_widget) 

        # button for back
        self.button_back = QPushButton("Back")
        self.button_back.clicked.connect(self.setUI)
        self.layout.addWidget(self.button_back)
        self.button_back.setFixedSize(30, 20)

        # setup plot figure
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # input point 
        self.input_bezier = QLineEdit()
        self.input_bezier.setPlaceholderText("Masukkan point sebagai tuple, contoh: (x1, y1), (x2, y2)")

        # input t
        self.input_t = QLineEdit() 
        self.input_t.setPlaceholderText("Masukkan nilai t antara 0 - 1")

        # button to process
        self.button = QPushButton("Enter") 
        self.button.clicked.connect(self.plot_draw_bruteforce)
        self.layout.addWidget(self.input_bezier)

        box = QHBoxLayout()
        box.addWidget(self.input_t, 1)
        box.addWidget(self.button, 2)
        self.layout.addLayout(box) 

    def plot_draw_bruteforce(self): 
        input_bezier_text = self.input_bezier.text()
        input_t = self.input_t.text() 
        try: 
            list_points: list[Points] = eval(input_bezier_text)
            t: float = eval(input_t)
            result: list[Points]
            if(t <= 1 and t >= 0):
                result = bezierCurveNPoint(list_points, t)

            ax = self.figure.add_subplot(111)
            ax.clear()

            x_core, y_core = zip(*list_points)
            x_curve, y_curve = zip(*result)

            ax.plot(x_core, y_core, marker='x', linestyle='-', label='Initial Point')
            ax.plot(x_curve, y_curve, marker='o', linestyle='-', label='Bezier Curve')

            ax.set_title('Bezier Curve on Brute force')
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.legend()
            ax.grid(True)

            self.canvas.draw()
            ax.remove()
        except Exception as e:
            print("Error:", e)

    def plot_draw_dnc(self): 
        input_bezier_text = self.input_bezier.text()
        input_iterasi = self.input_iterasi.text() 
        try: 
            list_points: list[Points] = eval(input_bezier_text)
            iterasi: float = eval(input_iterasi)
            result: list[Points]
            if(iterasi >= 0):
                result: list[Points] = addListOfPoint(True, iterasi, list_points)

            ax = self.figure.add_subplot(111)
            ax.clear()

            x_core, y_core = zip(*list_points)
            x_curve, y_curve = zip(*result)

            ax.plot(x_core, y_core, marker='x', linestyle='-', label='Initial Point')
            ax.plot(x_curve, y_curve, marker='o', linestyle='-', label='Bezier Curve')

            ax.set_title('Bezier Curve on Brute force')
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.legend()
            ax.grid(True)

            self.canvas.draw()
            ax.remove()
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())