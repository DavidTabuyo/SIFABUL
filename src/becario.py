from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class InterfazBecario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interfazBecario.ui', self)