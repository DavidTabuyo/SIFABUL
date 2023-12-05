from PyQt5.QtWidgets import QMainWindow, QLabel,QSizePolicy,QListWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
from controller.controlador_becario import ControladorBecario

class BecarioView(QMainWindow):
    def __init__(self,becario:ControladorBecario):
        self.becario=becario
        super().__init__()
        uic.loadUi('src/view/ui/becario_view.ui', self)
        self.BtnFichar.clicked.connect(self.BtnFichar_clicked)
        self.btnResumen.clicked.connect(self.btnResumen_clicked)
        
        #ejemplo **llamamos a get fichajes**
        fichajes = ['kk:05', 'kk:04', 'kk:03', 'kk:02', 'kk:01']
        for index, objeto in enumerate(fichajes):           
            etiqueta = QLabel(str(objeto))
            self.layoutFichajes.addWidget(etiqueta)
            etiqueta.setAlignment(Qt.AlignCenter)
            etiqueta.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if index%2==0:
                etiqueta.setStyleSheet('background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                etiqueta.setStyleSheet('background-color: red;font-size: 20px;border-radius: 10px;')


        #llamamos a get notificaciones y obtenemos lista de notificaciones
        listaNot= becario.get_notificaciones
        '''
                for texto in listaNot:
            item = QListWidgetItem(texto)
            self.list_view.addItem(item)
        
        '''



    def BtnFichar_clicked(self):
        #el becario ficha entrada o salida
        ...
    
    def btnResumen_clicked(self):
        #el becario quiere ver su resumen
        ...






