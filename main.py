import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from bruteforce import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bezier App")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 
        self.layout = QVBoxLayout(self.central_widget) 

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
    
        self.input_bezier = QLineEdit()
        self.input_bezier.setPlaceholderText("Masukkan point sebagai tuple, contoh: (x1, y1), (x2, y2)")
        self.layout.addWidget(self.input_bezier)

        self.button = QPushButton("Enter") 
        self.button.clicked.connect(self.plot_draw)
        self.layout.addWidget(self.button)

        box = QHBoxLayout()
        self.button_bruteforce = QPushButton("BruteForce") 
        self.button_dnc = QPushButton("Divide And Conquer")
        box.addWidget(self.button_bruteforce, 1)
        box.addWidget(self.button_dnc, 2)
        self.layout.addLayout(box) 

    def plot_draw(self): 
        input_bezier_text = self.input_bezier.text()
        try: 
            list_points: list[Point] = eval(input_bezier_text)
            result: list[Point] = bezierCurveNPoint(list_points, 0.05)

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
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())