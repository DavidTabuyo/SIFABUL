# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5 import uic
esCorrecto=1 #0:no/1:si
esBecario=0 #0:no/1:si


#interfaz inicio de sesión

class InicioSesion(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui', self)
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
            #usuario correcto, vemos si es admin o user
            if esBecario:
                #mostramos la interfaz de usuario y ocultamos etsa
                self.close()
                nueva_ventana = interfazBecario()
                nueva_ventana.show()
                uic
            else:
                #mostramos la interfaz de responsable y ocultamos etsa
                self.close()
                print("kk")
                self.nueva_ventana = interfazResponsable()
                self.nueva_ventana.show()



        else:
            # Crear y mostrar un cuadro de mensaje de error
            mensaje_error = QMessageBox()
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.setWindowTitle('Error')
            mensaje_error.setText('Los datos introducidos no son correctos.')
            mensaje_error.setStandardButtons(QMessageBox.Ok)
            mensaje_error.exec_()


#interfaz de responsable

class interfazResponsable(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('interfazResponsable.ui', self)



#interfaz de becario

class interfazBecario(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('interfazBecario.ui', self)
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = InicioSesion()
    demo.show()
    sys.exit(app.exec_())

    

