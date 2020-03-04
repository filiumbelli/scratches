import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow



class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow,self).__init__() #super yaptık modülü çektik
        #tüm verileri initte tanımlayıp fonksiyonu kendine döndürdük.
        self.initUI()
        self.setGeometry(700, 200, 500, 400)
        self.setWindowTitle("First Document")

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("First Layer")
        self.label.move(150, 200)


        self.b1 = QtWidgets.QPushButton(self) #selfe döndürdük
        self.b1.setText("Confirm!") #initte tanımladık
        self.b1.clicked.connect(self.clicked)

    def clicked(self): #butona özellik atar
        self.label.setText("You Pressed The Button")
        self.update()

    def update(self): # değişimleri update eder
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()