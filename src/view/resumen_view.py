from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
class ResumenView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/resumen_view.ui', self)
