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
        # cuando llamemos a este metodo significa que el becario ya ha visto todas las notificaciones
        return WorkerDao.get_notifications(self.worker_id)

    def get_today_checks(self) -> list[Check]:
        return WorkerDao.get_today_checks(self.worker_id, self.get_current_time()[1])

    # def get_semanas(self, n: int) -> list[Week]:
    #     return super().get_semanas(self.user.user_id, n)

    def check(self):
        # Obtener fecha actual real
        monday, date, time = self.get_current_time()

        # Obtener el ultimo fichaje del dia
        last_check = WorkerDao.get_last_today_check(self.worker_id, date)
        if last_check and time[3:5] == last_check.time[3:5]:
            raise LookupError('Ya has fichado')

        # Añadir nuevo fichaje
        is_new_check_entry = not last_check.is_entry if last_check else True
        WorkerDao.add_new_check(self.worker_id, date, time, is_new_check_entry)

        # Salir de la funcion si es fichaje de salida
        if is_new_check_entry:
            return

        # Calculo de tiempo fichado y actualizar semana
        week = WorkerDao.get_week(monday)
        week_total = week.total if week else 0

        entry = arrow.get(last_check.time, 'HH:mm:ss')
        exit = arrow.get(time, 'HH:mm:ss')
        total_seconds_check_in = (entry - exit).total_seconds()

        WorkerDao.update_or_create_week(
            self.worker_id, monday, week_total + total_seconds_check_in)

    # def get_resumen(self):
    #     ...

    def get_current_time(self) -> tuple[str, str, str]:
        timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
        monday = timestamp.floor('week').format('YYYY-MM-DD')
        date = timestamp.format('YYYY/MM/DD')
        time = timestamp.format('HH:mm:ss')
        return (monday, date, time)


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
