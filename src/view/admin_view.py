from PyQt5.QtWidgets import QMainWindow, QLabel,QSizePolicy,QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import uic
from controller.admin_controller import AdminController
from view.change_password_view import ChangePasswordView
from view.edit_worker_list_view import EditWorkerListView
from view.send_notification_view import SendNotificationView
from view.update_worker_view import UpdateWorkerView

class AdminView(QMainWindow):
    def __init__(self,admin:AdminController):
        super().__init__()
        self.admin=admin
        self.nueva_ventana=None
        uic.loadUi('src/view/ui/admin_view.ui', self)
        
        self.change_password_btn.clicked.connect(self.change_password_btn_clicked)
        self.edit_list_btn.clicked.connect(self.edit_list_btn_clicked)
        self.send_notification_btn.clicked.connect(self.send_notification_btn_clicked)
        self.update_btn.clicked.connect(self.update_btn_clicked)

        
        #update notifications
        self.update_notifications()
        
        #update worker list
        self.update_worker_list()
        
        
        
    def update_notifications(self):
        #update notificacions list
        self.clear_layout(self.notifications_layout)
        notList= self.admin.get_notifications()
        for i in notList:
            label = QLabel(i.get_output())
            self.notifications_layout.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            #if all workers has seen the notificarion
            if i.is_seen:
                label.setStyleSheet('background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet('background-color: red;font-size: 20px;border-radius: 10px;')

        
        
    def update_worker_list(self):
        self.clear_layout(self.list_layout)
        workerList= self.admin.get_workers()
        for worker in workerList:
            boton = QPushButton(worker.get_output_for_list(), self)
            self.list_layout.addWidget(boton)
            boton.setAlignment(Qt.AlignCenter)
            boton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            boton.setStyleSheet('background-color: blue;font-size: 20px;border-radius: 10px;')
            self.boton.clicked.connect(self.worker_btn_clicked(worker.worker_id))
            
        
    def worker_btn_clicked(self,worker_id:str):
        self.nueva_ventana= UpdateWorkerView()
        self.nueva_ventana.show()
    
    def send_notification_btn_clicked(self):
        self.nueva_ventana= SendNotificationView()
        self.nueva_ventana.show()
    
    def edit_list_btn_clicked(self):
        self.nueva_ventana= EditWorkerListView()
        self.nueva_ventana.show()
        
    def change_password_btn_clicked(self):
        self.nueva_ventana= ChangePasswordView()
        self.nueva_ventana.show()
    
    def update_btn_clicked(self):
        self.update_notifications()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
