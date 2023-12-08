from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class ChangePasswordView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/change_password_view.ui', self)

