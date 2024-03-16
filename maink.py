import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bruteforce import *
from algo4 import *

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Bezier Curve Plotter")
        self.set_ui()

    def set_ui(self):
        self.label = tk.Label(self, text="Pilih Tipe Algoritma", font=("Helvetica", 20))
        self.label.pack(pady=20)

        self.bruteforce_button = tk.Button(self, text="BruteForce", command=self.bruteforce_ui, height=2, width=20)
        self.bruteforce_button.pack(pady=10)

        self.dnc_button = tk.Button(self, text="Divide And Conquer", command=self.dnc_ui, height=2, width=20)
        self.dnc_button.pack(pady=10)

    def dnc_ui(self):
        self.clear_ui()
        self.title("Divide And Conquer Bezier")

        self.button_back = tk.Button(self, text="Back", command=self.set_ui)
        self.button_back.pack()

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack()

        self.input_bezier = tk.Entry(self, width=50)
        self.input_bezier.pack()

        self.input_iterasi = tk.Entry(self, width=50)
        self.input_iterasi.pack()

        self.button = tk.Button(self, text="Enter", command=self.plot_draw_dnc)
        self.button.pack()

    def bruteforce_ui(self):
        self.clear_ui()
        self.title("Bruteforce Bezier")

        self.button_back = tk.Button(self, text="Back", command=self.set_ui)
        self.button_back.pack()

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack()

        self.input_bezier = tk.Entry(self, width=50)
        self.input_bezier.pack()

        self.input_t = tk.Entry(self, width=50)
        self.input_t.pack()

        self.button = tk.Button(self, text="Enter", command=self.plot_draw_bruteforce)
        self.button.pack()

    def clear_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

    def plot_draw_bruteforce(self):
        input_bezier_text = self.input_bezier.get()
        input_t = self.input_t.get()
        try:
            list_points = eval(input_bezier_text)
            t = eval(input_t)
            if 0 <= t <= 1:
                result = bezierCurveNPoint(list_points, t)

                x_core, y_core = zip(*list_points)
                x_curve, y_curve = zip(*result)

                self.ax.clear()
                self.ax.plot(x_core, y_core, marker='x', linestyle='-', label='Initial Point')
                self.ax.plot(x_curve, y_curve, marker='o', linestyle='-', label='Bezier Curve')
                self.ax.set_title('Bezier Curve on Brute force')
                self.ax.set_xlabel('X-axis')
                self.ax.set_ylabel('Y-axis')
                self.ax.legend()
                self.ax.grid(True)
                self.canvas.draw()
        except Exception as e:
            print("Error:", e)

    def plot_draw_dnc(self):
        input_bezier_text = self.input_bezier.get()
        input_iterasi = self.input_iterasi.get()
        try:
            list_points = eval(input_bezier_text)
            iterasi = eval(input_iterasi)
            if iterasi >= 0:
                result = addListOfPoint(True, iterasi, list_points)

                x_core, y_core = zip(*list_points)
                x_curve, y_curve = zip(*result)

                self.ax.clear()
                self.ax.plot(x_core, y_core, marker='x', linestyle='-', label='Initial Point')
                self.ax.plot(x_curve, y_curve, marker='o', linestyle='-', label='Bezier Curve')
                self.ax.set_title('Bezier Curve on Divide and Conquer')
                self.ax.set_xlabel('X-axis')
                self.ax.set_ylabel('Y-axis')
                self.ax.legend()
                self.ax.grid(True)
                self.canvas.draw()
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
