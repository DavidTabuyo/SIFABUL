from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class SummaryView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/summary_view.ui', self)
