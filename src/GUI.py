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
        self.isClick: bool = False
        self.isPoint: bool = False
        self.setFixedSize(1000, 700)
        self.list_point : list[Point] = []
    
    def setUI(self):
        self.xlim : Point = (0,10)
        self.ylim : Point = (0,10)
        self.clear_plot()
        central_widget = QWidget()
        self.setCentralWidget(central_widget) 
        vertical_box = QVBoxLayout(central_widget)

        label = QLabel("Pilih Tipe Algoritma")
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(self.width(), 50)
        vertical_box.addWidget(label)

        font = QFont()
        font.setPointSize(20) 
        label.setFont(font)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.button_bruteforce = QPushButton("BruteForce")
        self.button_bruteforce.setFixedHeight(50)
        self.button_bruteforce.clicked.connect(self.bruteforceUI)
        self.button_dnc = QPushButton("Divide And Conquer")
        self.button_dnc.setFixedHeight(50)
        self.button_dnc.clicked.connect(self.DNCUI)

        vertical_box.addWidget(self.canvas)
        self.animateMainUI()
        vertical_box.addWidget(self.button_bruteforce)
        vertical_box.addWidget(self.button_dnc)
        # self.setLayout(vertical_box)

    def animateMainUI(self): 
        list_points: list[Point] = (6,-6),(3,-2),(-1, 3), (-2, 6), (0, 10), (3, 10), (5, 6) ,(5.5, 3), (6, -6), (6.5, 3), (7, 6) ,(9, 10), (12, 10), (14, 6), (13, 3), (9, -2), (6, -6)
        iterasi: float = 10

        self.ani = None
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.grid(True)
        ax.set_title('Bezier Curve')

        line, = ax.plot([], [], marker='o', linestyle='-', markersize=5, color = 'red')

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
        self.ani = FuncAnimation(self.figure, animate, frames=iterasi + 1, init_func=init, interval = 500, blit=True)

        self.canvas.draw() 
    
    def stopAnimation(self):
        if self.ani is not None:
            self.ani.event_source = None
        
    def clear_plot(self):
        self.list_point = []

    def clear_points(self):
        self.figure.clear()
        if (self.isDcui):
            self.initialize_plot("Bezier Curve on Divide and Conquer")
        else:
            self.initialize_plot("Bezier Curve on Bruteforce")
        self.canvas.draw()
        self.list_point = []
        self.input_bezier.setText("")

    def DNCUI(self): 
        self.isDcui: bool = True
        self.stopAnimation()
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
        self.initialize_plot("Bezier Curve on Divide and Conquer")

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

        # clear Plot
        self.button_clear = QPushButton("Clear Plot")
        self.button_clear.clicked.connect(self.clear_points)
        self.button_clear.setFixedSize(80, 20)

        # checkbox show all iteration 
        self.isAll: bool = False
        self.checkbox = QCheckBox("Tampilkan semua iterasi")
        self.checkbox.stateChanged.connect(self.updateIsAll)
        
        # checkbox click point
        self.checkbox_click = QCheckBox("Tambah point dengan klik")
        self.checkbox_click.stateChanged.connect(self.updateClick)

        # animate
        self.button_animate = QPushButton("Animate") 
        self.button_animate.clicked.connect(self.plot_animate_dnc)

        self.time = QLabel("Execution time: ")
        self.point = QLabel("Jumlah titik akhir: ")

        self.layout = QVBoxLayout(self.central_widget)
        self.top_box = QHBoxLayout()
        self.layout.addWidget(self.button_back)
        self.layout.addWidget(toolbar)
        self.top_box.addWidget(self.checkbox_click, 1)
        self.top_box.addWidget(self.button_clear)
        self.layout.addLayout(self.top_box) 
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
    
    def initialize_plot(self, plotTitle: str):
        # Customize the appearance of axes and grid
        self.axes = self.figure.add_subplot(111)
        self.axes.grid(True)  # Enable grid
        self.axes.set_xlim(self.xlim)
        self.axes.set_ylim(self.ylim)
        self.axes.set_title(plotTitle)
        self.axes.set_xlabel('X')  # Set label for x-axis
        self.axes.set_ylabel('Y')  # Set label for y-axis

    def updateIsAll(self, state): 
        if state == 2: 
            self.isAll = True 
        else: 
            self.isAll = False

    def updateClick(self, state): 
        if state == 2: 
            self.isClick = True 
        else: 
            self.isClick = False
    
    def onclick(self, event):
        if (event.xdata != None and event.ydata != None and self.isClick):
            self.list_point.append([event.xdata, event.ydata])
            if len(self.input_bezier.text()) != 0 :
                self.input_bezier.insert(", ")
            self.input_bezier.insert(f"({event.xdata}, {event.ydata})")
            x, y = zip(*self.list_point)
            xlim = self.axes.get_xlim()
            ylim = self.axes.get_ylim()
            self.axes.set_xlim(xlim)
            self.axes.set_ylim(ylim)
            self.axes.plot(x, y, marker='o', linestyle='-')
            self.canvas.draw()

    def bruteforceUI(self): 
        self.isDcui: bool = False
        # clear menu bar
        self.stopAnimation()
        self.menuBar().clear()
        self.setWindowTitle("Bruteforce Bezier")

        # setup window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 

        # button for back
        self.button_back = QPushButton("Back")
        self.button_back.clicked.connect(self.setUI)
        self.button_back.setFixedSize(40, 20)

        # setup plot figure
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.initialize_plot("Bezier Curve on Bruteforce")

        # Toolbar
        toolbar = NavigationToolbar(self.canvas, self)

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

        # clear Plot
        self.button_clear = QPushButton("Clear Plot")
        self.button_clear.clicked.connect(self.clear_points)
        self.button_clear.setFixedSize(80, 20)

        # checkbox click point
        self.checkbox_click = QCheckBox("Tambah point dengan klik")
        self.checkbox_click.stateChanged.connect(self.updateClick)

        box = QHBoxLayout()
        if (self.isPoint):
            box.addWidget(self.input_p, 2)
        else:
            box.addWidget(self.input_t, 2)
            
        box.addWidget(self.button, 2)
        box.addWidget(self.button_p, 1)
        self.time = QLabel("Execution time: ")
        self.point = QLabel("Jumlah titik akhir: ")

        self.layout = QVBoxLayout(self.central_widget) 
        self.top_box = QHBoxLayout()
        self.layout.addWidget(self.button_back)
        self.layout.addWidget(toolbar)
        self.top_box.addWidget(self.checkbox_click, 1)
        self.top_box.addWidget(self.button_clear)
        self.layout.addLayout(self.top_box)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.input_bezier)
        self.layout.addLayout(box) 
        self.layout.addWidget(self.time)
        self.layout.addWidget(self.point)
    
    def updateIsPoint(self):
        if (self.isPoint):
            self.isPoint = False
        else: 
            self.isPoint = True

    def plot_draw_bruteforce(self): 
        self.clear_plot()
        input_bezier_text = self.input_bezier.text()
        if (self.isPoint):
            input_p = self.input_p.text()
        else:
            input_t = self.input_t.text() 
        try: 
            list_points: list[Point] = eval(input_bezier_text)
            t : float
            result: list[Point]

            if (self.isPoint):
                p: int = eval(input_p)
            else:
                t = eval(input_t)
            
            start_time = time.time()
            if (self.isPoint):
                if (p > 0):
                    result = bezierCurveBruteForce_PointInput(list_points, p)
            else:
                if(t > 0):
                    result = bruteforceIterasi(list_points, t)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            
            self.figure.clear()
            self.initialize_plot("Bezier Curve on Bruteforce")

            x_core, y_core = zip(*list_points)
            xrange = (max(x_core) - min(x_core))/6
            yrange = (max(y_core) - min(y_core))/6
            self.axes.set_xlim(min(x_core) - xrange, max(x_core) + xrange)
            self.axes.set_ylim(min(y_core) - yrange, max(y_core) + yrange)
            x_curve, y_curve = zip(*result)

            self.axes.plot(x_core, y_core, marker='x', linestyle='-', label='Initial Point')
            self.axes.plot(x_curve, y_curve, marker='o', linestyle='-', label='Bezier Curve')

            self.axes.set_title('Bezier Curve on Brute force')
            self.axes.set_xlabel('X-axis')
            self.axes.set_ylabel('Y-axis')
            self.axes.legend()
            self.axes.grid(True)

            self.canvas.draw()
            self.time.setText(f"execution time: {execution_time} miliseconds")
            self.point.setText("jumlah titik akhir: " + str(len(result)))
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
            self.initialize_plot("Bezier Curve on Divide and Conquer")

            x_core, y_core = zip(*list_points)
            xrange = (max(x_core) - min(x_core))/6
            yrange = (max(y_core) - min(y_core))/6
            self.axes.set_xlim(min(x_core) - xrange, max(x_core) + xrange)
            self.axes.set_ylim(min(y_core) - yrange, max(y_core) + yrange)

            line, = self.axes.plot([], [], marker='o', linestyle='-', markersize=5)

            def init():
                line.set_data([], [])
                return line,

            def animate(iterasi):
                points = DnC_bezier_curve(iterasi,list_points)
                x, y = zip(*points)
                line.set_data(x, y)
                xrangeTemp = (max(x) - min(x))/6
                yrangeTemp = (max(y) - min(y))/6
                if (xrangeTemp < xrange):
                    self.axes.set_xlim(min(x) - xrangeTemp, max(x) + xrangeTemp)
                if (yrangeTemp < yrange):
                    self.axes.set_ylim(min(y) - yrangeTemp, max(y) + yrangeTemp)
                self.axes.set_label(f"Iterasi ke-{iterasi}")
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

            self.initialize_plot("Bezier Curve on Divide and Conquer")

            x_core, y_core = zip(*list_points)
            xrange = (max(x_core) - min(x_core))/6
            yrange = (max(y_core) - min(y_core))/6
            self.axes.set_xlim(min(x_core) - xrange, max(x_core) + xrange)
            self.axes.set_ylim(min(y_core) - yrange, max(y_core) + yrange)
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

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Yakin Bro-ku?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def DisplayGUI():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())