
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from becario import InterfazBecario
from responsable import InterfazResponsable


esCorrecto=1 #0:no/1:si
esBecario=0 #0:no/1:si

class InicioSesion(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/inicio_sesion.ui', self)
        self.boton1.clicked.connect(self.button1_clicked)
        self.BotonOk.clicked.connect(self.BotonOk_clicked)
        self.nueva_ventana = None





    #boton borra
    def button1_clicked(self):
        #borra el contenido de los slots
        self.UserName.clear()
        self.Password.clear()

    #boton aceptar
    def BotonOk_clicked(self):
        #comprobamos si es correcto o no
        if esCorrecto:
            self.close()
            #usuario correcto, vemos si es admin o user
            if esBecario:
                #mostramos la interfaz de becario
                self.nueva_ventana = InterfazBecario()
            else:
                #mostramos la interfaz de responsable
                self.nueva_ventana = InterfazResponsable()
            self.nueva_ventana.show()
            
        else:
            # Crear y mostrar un cuadro de mensaje de error
            mensaje_error = QMessageBox()
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.setWindowTitle('Error')
            mensaje_error.setText('Los datos introducidos no son correctos.')
            mensaje_error.setStandardButtons(QMessageBox.Ok)
            mensaje_error.exec_()
