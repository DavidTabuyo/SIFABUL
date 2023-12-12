from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5 import uic

from controller.user_controller import UserController

class ChangePasswordView(QMainWindow):
    def __init__(self,user:UserController):
        super().__init__()
        uic.loadUi('src/view/ui/change_password_view.ui', self)
        self.user=user
        self.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        self.accept_btn.clicked.connect(self.accept_btn_clicked)
        
    def accept_btn_clicked(self):
        try:
            self.user.change_password(self.old_password_imp.text(),self.new_password_imp.text())
        except LookupError as e:
            #error if passwords if old password equal new password or old pasword not the same
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle('Error')
            error_message.setText(str(e))
            error_message.setStandardButtons(QMessageBox.Ok)
            error_message.exec_()
            
    
    def cancel_btn_clicked(self):
        self.close()
    


    
    
        
    
    
    

