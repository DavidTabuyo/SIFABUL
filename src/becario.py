from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from controlador import *


class InterfazBecario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/becario.ui', self)
        self.BtnFichar.clicked.connect(self.BtnFichar_clicked)



    def BtnFichar_clicked(self):
        #el becario ficha entrada o salida
        #login()
        ...





