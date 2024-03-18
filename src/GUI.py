import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from bruteforce import *
from dnc import *

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ani = None
        self.setUI()
        self.isPoint: bool = False
        self.cid = None
        self.list_point : list[Point] = []
    
    def setUI(self):
        self.clear_points()
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
        # self.setLayout(vertical_box)
        
    def clear_points(self):
        self.list_point = []

    def DNCUI(self): 
        self.menuBar().clear()
        self.setWindowTitle("Divide And Conquer Bezier")
    
        # setup window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 

        # back button
        self.button_back = QPushButton("Back")
        self.button_back.clicked.connect(self.setUI)
        self.button_back.setFixedSize(40, 20)


        # figure to show plt
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.initialize_plot()

        # toolbar
        toolbar = NavigationToolbar(self.canvas, self)

        # input point 
        self.input_bezier = QLineEdit()
        self.input_bezier.setPlaceholderText("Masukkan point sebagai tuple, contoh: (x1, y1), (x2, y2)")

        # iterasi 
        self.input_iterasi = QLineEdit() 
        self.input_iterasi.setPlaceholderText("Masukkan iterasi contoh: 2")

        # process
        self.button = QPushButton("Enter") 
        self.button.clicked.connect(self.plot_draw_dnc)

        #checkbox show all iteration 
        self.isAll: bool = False
        self.checkbox = QCheckBox("Tampilkan semua iterasi")
        self.checkbox.stateChanged.connect(self.updateIsAll)
        
        # animate
        self.button_animate = QPushButton("Animate") 
        self.button_animate.clicked.connect(self.plot_animate_dnc)

        self.time = QLabel("Execution time: ")
        self.point = QLabel("Jumlah titik akhir: ")

        self.layout = QVBoxLayout(self.central_widget) 
        self.layout.addWidget(self.button_back)
        self.layout.addWidget(toolbar)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.input_bezier)
        self.layout.addWidget(self.button_animate)
        self.intialize_box_dnc()
        self.layout.addLayout(self.box) 
        self.layout.addWidget(self.time)
        self.layout.addWidget(self.point)

    def intialize_box_dnc(self):
        self.box = QHBoxLayout()
        self.box.addWidget(self.input_iterasi, 1)
        self.box.addWidget(self.button, 2)
        self.box.addWidget(self.checkbox)
    
    def initialize_plot(self):
        # Customize the appearance of axes and grid
        self.axes = self.figure.add_subplot(111)
        self.axes.grid(True)  # Enable grid
        self.axes.set_xlim(0,10)
        self.axes.set_ylim(0,10)
        self.axes.set_autoscale_on(True)
        self.axes.set_title('Bezier Curve on Divide and Conquer')
        self.axes.set_xlabel('X')  # Set label for x-axis
        self.axes.set_ylabel('Y')  # Set label for y-axis

    def updateIsAll(self, state): 
        if state == 2: 
            self.isAll = True 
        else: 
            self.isAll = False
    
    def onclick(self, event):
        self.list_point.append([event.xdata, event.ydata])
        if len(self.input_bezier.text()) != 0 :
            self.input_bezier.insert(", ")
        self.input_bezier.insert(f"({event.xdata}, {event.ydata})")
        x, y = zip(*self.list_point)
        self.axes.plot(x, y, marker='o', linestyle='-')
        self.canvas.draw()

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
        self.button_back.setFixedSize(40, 20)

        # setup plot figure
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # input point 
        self.input_bezier = QLineEdit()
        self.input_bezier.setPlaceholderText("Masukkan point sebagai tuple, contoh: (x1, y1), (x2, y2)")

        # display input dan tombol sesuai jenis input yang dipilih
        if (self.isPoint):
            # tombol pengubah jenis input
            self.button_p = QPushButton("Input berupa iterasi")
            self.button_p.clicked.connect(self.updateIsPoint)
            self.button_p.clicked.connect(self.bruteforceUI)
            # input p
            self.input_p = QLineEdit() 
            self.input_p.setPlaceholderText("Masukkan jumlah titik akhir (bilangan bulat positif)")
        else :
            # tombol pengubah jenis input
            self.button_p = QPushButton("Input berupa jumlah titik akhir")
            self.button_p.clicked.connect(self.updateIsPoint)
            self.button_p.clicked.connect(self.bruteforceUI)
            # input t
            self.input_t = QLineEdit() 
            self.input_t.setPlaceholderText("Masukkan iterasi (bilangan bulat positif)")

        # button to process
        self.button = QPushButton("Enter") 
        self.button.clicked.connect(self.plot_draw_bruteforce)
        self.layout.addWidget(self.input_bezier)

        box = QHBoxLayout()
        if (self.isPoint):
            box.addWidget(self.input_p, 2)
        else:
            box.addWidget(self.input_t, 2)
        box.addWidget(self.button, 2)
        box.addWidget(self.button_p, 1)
        self.layout.addLayout(box) 
        self.time = QLabel("Execution time: ")
        self.layout.addWidget(self.time)
        self.point = QLabel("Jumlah titik akhir: ")
        self.layout.addWidget(self.point)
    
    def updateIsPoint(self):
        if (self.isPoint):
            self.isPoint = False
        else: 
            self.isPoint = True

    def plot_draw_bruteforce(self): 
        input_bezier_text = self.input_bezier.text()
        if (self.isPoint):
            input_p = self.input_p.text()
        else:
            input_t = self.input_t.text() 
        try: 
            list_points: list[Point] = eval(input_bezier_text)
            t : float
            if (self.isPoint):
                p: int = eval(input_p)
            else:
                t = eval(input_t)
            result: list[Point]
            start_time = time.time()
            if (self.isPoint):
                if (p > 0):
                    result = bezierCurveBruteForce_PointInput(list_points, p)
            else:
                if(t > 0):
                    result = bruteforceIterasi(list_points, t)
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
            self.point.setText("jumlah titik akhir: " + str(len(result)))
            ax.remove()
        except Exception as e:
            print("Error:", e)

    def plot_animate_dnc(self):
        input_bezier_text = self.input_bezier.text()
        input_iterasi = self.input_iterasi.text()
        try:
            list_points: list[Point] = eval(input_bezier_text)
            iterasi: float = eval(input_iterasi)

            self.ani = None
            self.axes.clear()
            self.figure.clear()

            self.initialize_plot()

            line, = self.axes.plot([], [], marker='o', linestyle='-', markersize=5)

            def init():
                line.set_data([], [])
                return line,

            def animate(iterasi):
                points = DnC_bezier_curve(iterasi,list_points)
                x, y = zip(*points)
                line.set_data(x, y)
                self.axes.set_xlim(min(x) - 1, max(x) + 1)
                self.axes.set_label(f"Iterasi ke-{iterasi}")
                self.axes.set_ylim(min(y) - 1, max(y) + 1)
                return line,

            # Create the animation
            self.ani = FuncAnimation(self.figure, animate, frames=iterasi + 1, init_func=init, interval = 1000, blit=True, repeat = False)

            self.canvas.draw()
        except Exception as e:
            print("Error:", e)

    def plot_draw_dnc(self): 
        input_bezier_text = self.input_bezier.text()
        input_iterasi = self.input_iterasi.text()
        try: 
            list_points: list[Point] = eval(input_bezier_text)
            iterasi: float = eval(input_iterasi)
            result: list[Point]

            self.ani = None
            self.figure.clear()

            self.initialize_plot()

            x_core, y_core = zip(*list_points)
            self.axes.plot(x_core, y_core, marker='x', linestyle='-', label='Initial Point')
            if(self.isAll == True):
                for i in range(1,iterasi+1):
                    if(i == iterasi): 
                        start_time = time.time()
                        result: list[Point] = DnC_bezier_curve(i, list_points)
                        end_time = time.time()
                        execution_time = (end_time-start_time)*1000
                        self.time.setText(f"execution time: {execution_time} miliseconds") 
                    else:
                        result: list[Point] = DnC_bezier_curve(i, list_points)
                    x_curve, y_curve = zip(*result)
                    self.axes.plot(x_curve, y_curve, marker='o', linestyle='-', label='Iterasi ke-' + str(i))    
            else:
                start_time = time.time()
                result: list[Point] = DnC_bezier_curve(iterasi, list_points)
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000
                self.time.setText(f"execution time: {execution_time} miliseconds") 
                x_curve, y_curve = zip(*result)
                self.axes.plot(x_curve, y_curve, marker='o', linestyle='-', label='Kurva Bezier')    

            self.axes.legend()

            self.point.setText("jumlah titik akhir: " + str((2**iterasi)+1))
            self.canvas.draw()
        except Exception as e:
            print("Error:", e)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.resize(800, 600)
#     window.show()
#     sys.exit(app.exec_())