from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class AdminView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/admin_view.ui', self)
    
