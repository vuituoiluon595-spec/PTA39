from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow 
import sys
from PyQt6 import uic

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("B4/home.ui", self)
        self.show()



app = QApplication(sys.argv)
Home = Home()
sys.exit(app.exec())