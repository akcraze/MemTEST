from PyQt5 import QtWidgets

from widgets.numbertest import numtest


from PyQt5  import QtGui

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        width = 400
        height = 400
        title = "MEM TEST !!"
        icon = QtGui.QIcon("window/icon.png")
        
        self.setGeometry(300, 300, width,height)
        self.setWindowTitle(title)
        self.setWindowIcon(icon)
     
        self.number_game =  QtWidgets.QPushButton(self)
        self.number_game.clicked.connect(self.game1)
    
    def game1(self):
        self.setCentralWidget(numtest())
        self.number_game.setGeometry(0,0,0,0)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win  = MainWindow()
    win.show()
    sys.exit(app.exec_())


    