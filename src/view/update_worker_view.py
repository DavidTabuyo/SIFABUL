from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class UpdateWorkerView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/update_worker_view.ui', self)
