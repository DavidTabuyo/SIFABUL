from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class BecarioView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/becario_view.ui', self)
        self.BtnFichar.clicked.connect(self.BtnFichar_clicked)



    def BtnFichar_clicked(self):
        #el becario ficha entrada o salida
        #login()
        ...





