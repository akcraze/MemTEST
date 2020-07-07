import PyQt5
from PyQt5 import QtWidgets
import  matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Plotter(FigureCanvasQTAgg):

    def __init__(self):
        fig = Figure()
        
        self.axes = fig.add_subplot(111)
# code for main window
graph = Plotter()
score = data_pull()
graph.axes.plot(score)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Plotter()
    win.show()
    sys.exit(app.exec_())

