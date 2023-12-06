from PyQt5.QtWidgets import QMainWindow, QLabel,QSizePolicy,QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
from controller.controlador_becario import ControladorBecario
from view.summary_view import SummaryView
from model.fichaje import Fichaje

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
        fichajes = becario.get_fichajes_hoy()
        for object in fichajes:           
            etiqueta = QLabel(str(object.getOutput))
            self.layoutFichajes.addWidget(etiqueta)
            etiqueta.setAlignment(Qt.AlignCenter)
            etiqueta.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if object.is_entrada:
                etiqueta.setStyleSheet('background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                etiqueta.setStyleSheet('background-color: red;font-size: 20px;border-radius: 10px;')
                
        #llamamos a get notificaciones y obtenemos lista de notificaciones
        listaNot= becario.get_notificaciones()
        '''
                for texto in listaNot:
            item = QListWidgetItem(texto)
            self.list_view.addItem(item)
        
        '''



    def BtnFichar_clicked(self):
        #el becario ficha entrada o salida
        try:
            self.worker.fichar
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

    def btnChangePassword_clicked(seld):
        #bbecario quiere cambiar su contraseña
        ...





