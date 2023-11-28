
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5 import uic
from becario import InterfazBecario
from responsable import InterfazResponsable
from controlador import *


esCorrecto=1 #0:no/1:si
esBecario=0 #0:no/1:si

class InicioSesion(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/inicio_sesion.ui', self)
        self.boton1.clicked.connect(self.button1_clicked)
        self.BotonOk.clicked.connect(self.BotonOk_clicked)
        self.nueva_ventana = None
        self.Password.setEchoMode(QLineEdit.Password)  # Configurar el modo de eco






    #boton borra
    def button1_clicked(self):
        #borra el contenido de los slots
        self.UserName.clear()
        self.Password.clear()

    #boton aceptar
    def BotonOk_clicked(self):
        #comprobamos si es correcto o n
        try:
            controlador = login(self.UserName.text(), self.Password.text())
        except LookupError as e:
            mensaje_error = QMessageBox()
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.setWindowTitle('Error')
            mensaje_error.setText(str(e))
            mensaje_error.setStandardButtons(QMessageBox.Ok)
            mensaje_error.exec_()
        except ValueError as e:
            mensaje_error = QMessageBox()
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.setWindowTitle('Error')
            mensaje_error.setText(str(e))
            mensaje_error.setStandardButtons(QMessageBox.Ok)
            mensaje_error.exec_()
        