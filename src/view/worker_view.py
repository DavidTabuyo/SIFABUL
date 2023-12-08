from PyQt5.QtWidgets import QMainWindow, QLabel,QSizePolicy,QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
from controller.controlador_becario import ControladorBecario
from view.change_password_view import ChangePasswordView
from view.summary_view import SummaryView

class WorkerView(QMainWindow):
    def __init__(self,becario:ControladorBecario):
        self.worker=becario
        self.nueva_ventana = None
        super().__init__()
        uic.loadUi('src/view/ui/worker_view.ui', self)

        self.BtnFichar.clicked.connect(self.BtnFichar_clicked)
        self.btnResumen.clicked.connect(self.btnResumen_clicked)
        self.btnChangePassword.clicked.connect(self.btnChangePassword_clicked)

        #actualizamos la lista de fichajes
        self.update_fichajes()

        #llamamos a get notificaciones y obtenemos lista de notificaciones
        self.update_notifications()



    def BtnFichar_clicked(self):
        #el becario ficha entrada o salida
        try:
            check=self.worker.check()
            label = QLabel(check.get_output())
            self.layoutFichajes.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if check.is_entry:
                label.setStyleSheet('background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet('background-color: red;font-size: 20px;border-radius: 10px;')
                
        except LookupError as e:
            #pulsamos el boton dos veces seguidas(mismo minuto)
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle('Error')
            error_message.setText(str(e))
            error_message.setStandardButtons(QMessageBox.Ok)
            error_message.exec_()

    
    def btnResumen_clicked(self):
        #el becario quiere ver su resumen
        self.nueva_ventana= SummaryView()
        self.nueva_ventana.show()

    def btnChangePassword_clicked(self):
        #bbecario quiere cambiar su contraseña
        self.nueva_ventana= ChangePasswordView()
        self.nueva_ventana.show()
        
    def update_fichajes(self):
        fichajes = self.worker.get_fichajes_hoy()
        for object in fichajes:           
            label = QLabel(object.get_output())
            self.layoutFichajes.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if object.is_entry:
                label.setStyleSheet('background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet('background-color: red;font-size: 20px;border-radius: 10px;')
                
    def update_notifications(self):
        notList= self.worker.get_notificaciones()
        for i in notList:
            label = QLabel(i.get_output())
            self.notifications_layout.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if i.is_seen:
                label.setStyleSheet('background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet('background-color: red;font-size: 20px;border-radius: 10px;')

        

        






