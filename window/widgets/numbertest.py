
from PyQt5 import QtWidgets
from widgets.TestGenerators.NumberGenerator import NumGen
from PyQt5 import QtGui
from PyQt5 import QtCore
import time


class numtest(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #main ui function to make the ui 
        
        self.ScoreDisplay = QtWidgets.QLabel()
        self.NumberDisplay  = QtWidgets.QLabel()
        self.SubmitButton =  QtWidgets.QPushButton()
        self.AnswerBox =  QtWidgets.QTextEdit()
       
        self.timer = QtWidgets.QProgressBar()
        self.prog_bar_color = QtGui.QPalette(self.palette())
        self.prog_bar_color.setColor(QtGui.QPalette.Highlight, QtCore.Qt.green)
        self.timer.setPalette(self.prog_bar_color)
    
        

        
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.addWidget(self.ScoreDisplay,0,0)
        self.grid.addWidget(self.NumberDisplay,1,0)
        self.grid.addWidget(self.timer,2,0)
        self.grid.addWidget(self.AnswerBox,3,0,2,0)
        self.grid.addWidget(self.SubmitButton,5,0)
        self.grid.setSpacing(10)
        self.setLayout(self.grid)
        s = '''
        QWidget{
            font-family:consolas;
        }
        QLabel {
            font-size:24px;
        }
        QTextEdit {
            border:solid;
            border-width:2px;
            border-color:blue;
            font-size:20px;

        }
        QPushButton {
            border:solid;
            border-width:4px;
            border-color:orange;
            background-color:rgb(28, 183, 240);
            font-size:20px;
            width:100px;
            height:40px;
            border-radius:20px;
            
        }
    
         '''
        self.setStyleSheet(s)
        
        self.main()
        
#FIXME move these functions to a seperate file
    def main(self):
    
        self.ScoreDisplay.setText("SCORE:0")
        self.score = 0
        self.diffculty = 4
        
        self.timer.setValue(0)
        
        self.NumberDisplay.setText(" ***RULES*** \n you will get 10 seconds to remember \n the number  which would disappear \n after 10 seconds after that\n then enter the number and click submit")
        self.NumberDisplay.adjustSize()
        
        self.SubmitButton.setText("START")
        self.SubmitButton.clicked.connect(self.submit)
        
        self.start = True
#FIXME the shortcut doesn't work because of QTextedit as EOL get inserted when we press Enter  it can work if QLineEdit is used but QLineEdit shrinks the Box size
        self.SubmitButton.setShortcut("Enter")

    def submit(self):
        #this conditional statement is used to change the text of the pushbutton
        if self.start == True:
            self.SubmitButton.setText("SUBMIT")
            self.AnswerBox.setText("")#this is used to clear the final result text from the last game 
            self.num()
            self.Time()
            self.start = False
        else:
            self.compare()
    def compare(self):
         #this function compares the input of user to the generated number so answer can be verified
        answer = self.AnswerBox.toPlainText()#this takes answer from QTextedit and it is str format so it should be converted to int before usage
        
        if answer  == str(self.number):
            self.TextToScore()
            self.num()
            self.diffculty += 1
        
            self.Time()
            #this used to clear previous input from the user
            self.AnswerBox.setText("")
        else:
            self.AnswerBox.setText(f"incorrect answer!! \n the correct answer is {self.number} and your answer was {answer}")
            self.SubmitButton.setText("RESTART")
            self.start = True
            
#FIXME this function makes the whole program to freeze so need to work around it  
    def Time(self):
        #this function makes the progress bar fill in 10 seconds so the user can see the time left
        #and changes the color of statusbar depending upon the time left
        for i in range(1,101):
            time.sleep(0.1)
            self.timer.setValue(i)
            if i == 20: 
                self.prog_bar_color.setColor(QtGui.QPalette.Highlight, QtCore.Qt.green)
            elif i == 60:
                self.prog_bar_color.setColor(QtGui.QPalette.Highlight, QtCore.Qt.yellow)
            elif i == 90:
                self.prog_bar_color.setColor(QtGui.QPalette.Highlight, QtCore.Qt.red)
                           
            self.timer.setPalette(self.prog_bar_color)

        self.NumberDisplay.setText("Enter the number below")
    def num(self):
        #this function generates the random number for the user to remember
            self.number = NumGen(self.diffculty)
            self.NumberDisplay.setText(str(self.number))
    def TextToScore(self):
        #this function adds +1 to the total score of user and displays the text
        self.score += 1
        temp = str(self.score)
        self.ScoreDisplay.setText("SCORE:"+temp)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win  = numtest()
    win.show()
    sys.exit(app.exec_())   

     
 
