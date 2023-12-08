from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class SendNotificationView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/send_notification_view.ui', self)
