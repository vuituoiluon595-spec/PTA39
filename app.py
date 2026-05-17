from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
import os


from pages.login import LoginPage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QMainWindow):
     def __int__ (self):
        super().__int__()
        #dat ten app
        self .setWindowTitle("apdoption pet app - login")

        #load trang login tu loginpage
        self.login_page = LoginPage(  
            main_window=self, root_dir = BASE_DIR
        )
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
