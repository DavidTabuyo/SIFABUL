# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class AppDemo(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui', self)
        self.boton1.clicked.connect(self.button1_clicked)



    def button1_clicked(self):
        print('hola')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closiing Window...')
