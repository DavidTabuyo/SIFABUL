from PyQt5.QtWidgets import QMainWindow, QLabel, QSizePolicy, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
from controller.worker_controller import WorkerController
from view.change_password_view import ChangePasswordView
from view.summary_view import SummaryView


class WorkerView(QMainWindow):
    def __init__(self, becario: WorkerController):
        self.worker = becario
        self.nueva_ventana = None
        super().__init__()
        uic.loadUi('src/view/ui/worker_view.ui', self)

        self.BtnFichar.clicked.connect(self.BtnFichar_clicked)
        self.btnResumen.clicked.connect(self.btnResumen_clicked)
        self.btnChangePassword.clicked.connect(self.btnChangePassword_clicked)
        self.refresh_btn.clicked.connect(self.refresh_btn_clicked)


        # actualizamos la lista de fichajes
        self.update_fichajes()

        # llamamos a get notificaciones y obtenemos lista de notificaciones
        #self.update_notifications()

    def BtnFichar_clicked(self):
        # el becario ficha entrada o salida
        try:
            check = self.worker.check()
            self.clear_layout(self.layoutFichajes)
            self.update_fichajes()
        except LookupError as e:
            # pulsamos el boton dos veces seguidas(mismo minuto)
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle('Error')
            error_message.setText(str(e))
            error_message.setStandardButtons(QMessageBox.Ok)
            error_message.exec_()
            
    def refresh_btn_clicked(self):
        self.update_notifications()

    def btnResumen_clicked(self):
        # el becario quiere ver su resumen
        self.nueva_ventana = SummaryView()
        self.nueva_ventana.show()

    def btnChangePassword_clicked(self):
        # bbecario quiere cambiar su contraseña
        self.nueva_ventana = ChangePasswordView()
        self.nueva_ventana.show()

    def update_fichajes(self):
        self.clear_layout(self.layoutFichajes)
        fichajes = self.worker.get_today_checks()
        for object in fichajes:
            label = QLabel(object.get_output())
            self.layoutFichajes.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if object.is_entry:
                label.setStyleSheet(
                    'background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet(
                    'background-color: red;font-size: 20px;border-radius: 10px;')

    def update_notifications(self):
        self.clear_layout(self.notifications_layout)
        notList = self.worker.get_notifications()
        for i in notList:
            label = QLabel(i.get_output())
            self.notifications_layout.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if i.is_seen:
                label.setStyleSheet(
                    'background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet(
                    'background-color: red;font-size: 20px;border-radius: 10px;')
    
    def clear_layout(self, layout):
        # Borrar todos los widgets en el layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        if layout==self.layoutFichajes:    
            check_label = QLabel('Fichajes', self)
            check_label.setAlignment(Qt.AlignCenter)
            check_label.setStyleSheet(
                "QLabel {"
                "   font-family: Decorative;"
                "   font-size: 20px;"
                "   color: black;"
                "   background-color: #FFB6C1;" 
                "}"
            )     
            layout.addWidget(check_label)
   
                
    
