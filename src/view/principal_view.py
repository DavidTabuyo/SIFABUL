from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5 import uic
from controller.worker_controller import WorkerController
from view.worker_view import WorkerView
from view.admin_view import AdminView
from controller.login_controller import login


class PrincipalView(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('src/view/ui/principal_view.ui', self)
        self.boton1.clicked.connect(self.button1_clicked)
        self.BotonOk.clicked.connect(self.BotonOk_clicked)
        self.nueva_ventana = None
        # Configurar el modo de eco
        self.Password.setEchoMode(QLineEdit.Password)

    # boton borra
    def button1_clicked(self):
        # borra el contenido de los slots
        self.UserName.clear()
        self.Password.clear()

    # boton aceptar
    def BotonOk_clicked(self):
        # comprobamos si es correcto o n
        try:
            controller = login(self.UserName.text(), self.Password.text())

            # dependiendo del tipo de controlador que sea, llamamos a una vista
            if type(controller) == WorkerController:
                self.nueva_ventana = WorkerView(controller)
            else:
                self.nueva_ventana = AdminView(controller)

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
