import arrow
import requests
from controller.user_controller import UserController
from model.check import Check
from model.dao.worker_dao import WorkerDao
from model.notification_worker import NotificationWorker


class WorkerController(UserController):
    def __init__(self, worker_id: str):
        self.worker_id = worker_id

    def get_notifications(self) -> list[NotificationWorker]:
        #cuando llamemos a este metodo significa que el becario ya ha visto todas las notificaciones
        return WorkerDao.get_notifications(self.worker_id)

    def get_today_checks(self) -> list[Check]:
        return WorkerDao.get_today_checks(self.worker_id,self.get_date())
                     
    # def get_semanas(self, n: int) -> list[Week]:
    #     return super().get_semanas(self.user.user_id, n)

    def check(self) -> Check:
        new_check=Check(self.worker_id,self.get_date(),self.get_time(),self.get_next_check_status())
        if new_check.get_minutes()==WorkerDao.get_last_check(self.worker_id,self.get_date()).get_minutes():
            raise LookupError('Ya has fichado')
        WorkerDao.add_new_check(self.worker_id,new_check)
        return new_check            
    
    # def get_resumen(self):
    #     ...
    
    def get_date(self):
        # Obtener fecha actual real
        timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
        return timestamp.format('YYYY/MM/DD')
    
    def get_time(self):
        timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
        return timestamp.format('HH:mm:ss')    

    def get_next_check_status(self)->int:
        return  WorkerDao.get_last_check(self.worker_id,self.get_date()).get_next_status()
    
    
    


# class __ControladorBecario(__Controlador):
#     def add_fichaje(self):
#         '''
#         Añade un fichaje a la hora actual y actualiza la semana
#         '''
#         # Obtener hora actual real
#         timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
#         hora = timestamp.format('HH:mm:ss')
#         fecha = timestamp.format('YYYY-MM-DD')

#         with sqlite3.connect('db/db.sqlite') as connection:
#             cursor = connection.cursor()

#             # Obtener el ultimo fichaje
#             cursor.execute('''
#                 SELECT hora, is_entrada
#                 FROM fichajes
#                 WHERE becario_id = ? and fecha = ?
#                 ORDER BY hora DESC
#             ''', (self._user_id, fecha))
#             last_fichaje = cursor.fetchone()  # ((HH:mm:ss, 0) o None) o (HH:mm:ss, 1)

#             # Comprobar si el ultimo fichaje es de salida o de entrada
#             new_fichaje_is_entrada = 1 if last_fichaje == None or last_fichaje[1] == 0 else 0

#             # Añadir el nuevo fichaje
#             cursor.execute('''
#                 INSERT INTO fichajes (becario_id, fecha, hora, is_entrada) VALUES
#                     (?, ?, ?, ?);
#             ''', (self._user_id, fecha, hora, new_fichaje_is_entrada))

#             # Si es de entrada salir de la funcion
#             if new_fichaje_is_entrada == 1:
#                 return


#             # Obtener el total de la semana
#             lunes = timestamp.floor('week').format("YYYY-MM-DD")
#             cursor.execute('''
#                 SELECT total_semana FROM semanas WHERE becario_id = ? and lunes = ?
#             ''', (self._user_id, lunes))
#             total_semana = cursor.fetchone()
#             total_semana = total_semana[0] if total_semana else 0

#             # Calcular el timpo que ha estado fichado
#             hora_entrada = arrow.get(last_fichaje[0], 'HH:mm:ss')
#             hora_salida = arrow.get(hora, 'HH:mm:ss')
#             segundos_fichado = (hora_salida - hora_entrada).total_seconds()

#             # Actualizar la semana
#             cursor.execute('''
#                 INSERT OR REPLACE INTO semanas (becario_id, lunes, total_semana) VALUES
#                     (?, ?, ?);
#             ''', (self._user_id, lunes, total_semana + segundos_fichado))
