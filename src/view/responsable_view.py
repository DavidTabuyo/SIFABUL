from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class ResponsableView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/responsable_view.ui', self)
