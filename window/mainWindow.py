from PyQt5.QtWidgets import(QMainWindow,QApplication,QPushButton)

from widgets.numbertest import numtest

from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        width = 400
        height = 400
        title = "MEM TEST !!"
        icon = QIcon("icon.png")
        
        self.setGeometry(300, 300, width,height)
        self.setWindowTitle(title)
        self.setWindowIcon(icon)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win  = MainWindow()
    win.show()
    sys.exit(app.exec_())
