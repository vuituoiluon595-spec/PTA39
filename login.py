from PyQt6.QtWidgets import   QMainWindow , QMessageBox
import sys
from PyQt6 import uic
import os
import re

#mock data
account = {"fullname":"Hai Nam","email":"abc@gamail.com","password":"123123"}


class LoginPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()  # ke thua cac code init cua lop cha
        self.main_window = main_window  # luu tham so
        self.root_dir = root_dir
                
        # load file ui
        ui_path = self.root_dir + "/GUI/login.ui"
        uic.loadUi(ui_path, self)
        self.login.clicked.connect(self.handle_login)
        self.nav_register.clicked.conect (self.goto_register)
        self.show()

    #--------------------------xu ly su kien -------------------------
    def handle_login(self):
        email_imput = self.email.text().strip()
        prassword_input = self.prassword.text()
        #vaildate du lieu 
        if(self.__validate_imput(email_imput,prassword_input)is not None):
            self.show_message(self.__validate_imput)(email_imput,prassword_input)
            return
        else:
            self.__goto_home()

    def goto_register(self):
        from pages.register import HomePage
        home_page = HomePage(main_window=self.main_window, root_dir =self.root_dỉr)

    def __validate_imput(self,emai,password):
        #kiem tra email 
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(regex, emai) is None: 
            return "email khong hop le!"
        if len(password)< 6 :
            return"prassword phai tu 6 chu so to len !"
    def show_message(self):
        # Khởi tạo hộp thoại thông báo
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText("Đây là nội dung thông báo của bạn!")
        msg.setIcon(QMessageBox.Icon.Information) # Các icon mặc định: Information, Warning, Critical, Question
        msg.setStandardButtons(QMessageBox.StandardButton.Ok) # Nút bấm OK
        
        # Hiển thị hộp thoại
        msg.exec()