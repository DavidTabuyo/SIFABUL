from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class InterfazResponsable(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/responsable.ui', self)
