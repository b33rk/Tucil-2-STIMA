import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from bruteforce import *
from dnc import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ani = None
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

        #checkbox show all iteration 
        self.isAll: bool = False
        self.checkbox = QCheckBox("Tampilkan semua iterasi")
        self.checkbox.stateChanged.connect(self.updateIsAll)
        
        # animate
        self.button_animate = QPushButton("Animate") 
        self.button_animate.clicked.connect(self.plot_animate_dnc)
        self.layout.addWidget(self.button_animate)

        box = QHBoxLayout()
        box.addWidget(self.input_iterasi, 1)
        box.addWidget(self.button, 2)
        box.addWidget(self.checkbox)
        self.layout.addLayout(box) 
        self.layout.addLayout(box) 
        self.time = QLabel("Execution time: ")
        self.layout.addWidget(self.time)
    
    def updateIsAll(self, state): 
        if state == 2: 
            self.isAll = True 
        else: 
            self.isAll = False
    
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
        self.time = QLabel("Execution time: ")
        self.layout.addWidget(self.time)

    def plot_draw_bruteforce(self): 
        input_bezier_text = self.input_bezier.text()
        input_t = self.input_t.text() 
        try: 
            list_points: list[Point] = eval(input_bezier_text)
            t: float = eval(input_t)
            result: list[Point]
            start_time = time.time()
            if(t <= 1 and t >= 0):
                result = bezierCurveNPoint(list_points, t)

            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
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
            self.time.setText(f"execution time: {execution_time} miliseconds")
            ax.remove()
        except Exception as e:
            print("Error:", e)

    def plot_animate_dnc(self):
        input_bezier_text = self.input_bezier.text()
        input_iterasi = self.input_iterasi.text()
        try:
            list_points: list[Point] = eval(input_bezier_text)
            iterasi: float = eval(input_iterasi)

            self.figure.clear()

            ax = self.figure.add_subplot(111)
            ax.grid(True)
            ax.set_title('Bezier Curve on Divide and Conquer')
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')

            line, = ax.plot([], [], marker='o', linestyle='-', markersize=5)

            def init():
                line.set_data([], [])
                return line,

            def animate(iterasi):
                points = DnC_bezier_curve(iterasi,list_points)
                x, y = zip(*points)
                line.set_data(x, y)
                ax.set_xlim(min(x) - 1, max(x) + 1)
                ax.set_ylim(min(y) - 1, max(y) + 1)
                return line,

            # Create the animation
            self.ani = FuncAnimation(self.figure, animate, frames=iterasi, init_func=init, interval = 1000, blit=True, repeat = False)

            self.canvas.draw()
            self.show_animation()
        except Exception as e:
            print("Error:", e)

    def show_animation(self):
        # Create a new dialog to display the animation
        dialog = QDialog()
        dialog.setWindowTitle("Animation")
        layout = QVBoxLayout(dialog)
        
        # Embed the canvas in the dialog
        canvas = FigureCanvas(self.figure)
        layout.addWidget(canvas)
        
        # Add a button to close the dialog
        button_close = QPushButton("Close")
        button_close.clicked.connect(dialog.close)
        layout.addWidget(button_close)
        
        # Show the dialog
        dialog.exec_()

    def plot_draw_dnc(self): 
        input_bezier_text = self.input_bezier.text()
        input_iterasi = self.input_iterasi.text()
        try: 
            list_points: list[Point] = eval(input_bezier_text)
            iterasi: float = eval(input_iterasi)
            result: list[Point]
            ax = self.figure.add_subplot(111)
            ax.clear()

            x_core, y_core = zip(*list_points)
            ax.plot(x_core, y_core, marker='x', linestyle='-', label='Initial Point')
            if(self.isAll == True):
                for i in range(1,iterasi+1):
                    if(i == iterasi): 
                        start_time = time.time()
                        result: list[Point] = addListOfPoint(True, i, list_points)
                        end_time = time.time()
                        execution_time = (end_time-start_time)*1000
                        self.time.setText(f"execution time: {execution_time} miliseconds") 
                    else:
                        result: list[Point] = addListOfPoint(True, i, list_points)
                    x_curve, y_curve = zip(*result)
                    ax.plot(x_curve, y_curve, marker='o', linestyle='-', label='Iterasi ke-' + str(i))    
            else:
                start_time = time.time()
                result: list[Point] = addListOfPoint(True, iterasi, list_points) 
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000
                self.time.setText(f"execution time: {execution_time} miliseconds") 
                x_curve, y_curve = zip(*result)
                ax.plot(x_curve, y_curve, marker='o', linestyle='-', label='Kurva Bezier')    

            ax.set_title('Bezier Curve on Divide and Conquer')
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