from PyQt5.QtWidgets import QMainWindow, QLabel,QSizePolicy,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import uic
from controller.admin_controller import AdminController
from view.change_password_view import ChangePasswordView
from view.edit_worker_list_view import EditWorkerListView
from view.send_notification_view import SendNotificationView

class AdminView(QMainWindow):
    def __init__(self,admin:AdminController):
        super().__init__()
        self.admin=admin
        self.nueva_ventana=None
        uic.loadUi('src/view/ui/admin_view.ui', self)
        self.change_password_btn.clicked.connect(self.change_password_btn_clicked)
        self.edit_list_btn.clicked.connect(self.edit_list_btn_clicked)
        self.send_notification_btn.clicked.connect(self.send_notification_btn_clicked)

        
        #update notifications
        self.update_notifications()
        
        #update worker list
        self.update_worker_list()
        
        
        
    def update_notifications(self):
        #update notificacions list
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
        workerList= self.admin.get_workers()
        for worker in workerList:
            label = QLabel(worker.get_output_for_list())
            self.list_layout.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            label.setStyleSheet('background-color: blue;font-size: 20px;border-radius: 10px;')
            
            
        
    
    def send_notification_btn_clicked(self):
        self.nueva_ventana= SendNotificationView()
        self.nueva_ventana.show()
    
    def edit_list_btn_clicked(self):
        self.nueva_ventana= EditWorkerListView()
        self.nueva_ventana.show()
        
    def change_password_btn_clicked(self):
        self.nueva_ventana= ChangePasswordView()
        self.nueva_ventana.show()
    
