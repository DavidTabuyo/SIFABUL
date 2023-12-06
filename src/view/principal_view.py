from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5 import uic
from controller.controlador_becario import ControladorBecario
from view.worker_view import WorkerView
from view.admin_view import AdminView
from controller.controlador_principal import login



class PrincipalView(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/principal_view.ui', self)
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
            
            #dependiendo del tipo de controlador que sea, llamamos a una vista
            if type(controlador) == ControladorBecario:
                self.nueva_ventana = WorkerView(controlador)
            else:
                self.nueva_ventana = AdminView(controlador)

            self.close()
            self.nueva_ventana.show()
            

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
        