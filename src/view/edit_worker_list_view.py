from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class EditWorkerListView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/edit_worker_list_view.ui', self)
