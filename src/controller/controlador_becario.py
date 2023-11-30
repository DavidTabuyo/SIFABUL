from controller.controlador_user import ControladorUser
from model.becario import Becario

class ControladorBecario(ControladorUser):
    def __init__(self, becario: Becario) -> None:
        super().__init__(becario)


        
        




# class __ControladorBecario(__Controlador):
#     def get_fichajes_hoy(self) -> list[Fichaje]:
#         '''
#         Devuelve todos los fichajes del dia en forma de [('HH:mm', True), ...]
#         '''
#         # Obtener fecha actual real
#         timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
#         fecha = timestamp.format('YYYY-MM-DD')
        
#         # Obtener todos los fichajes de hoy 
#         with sqlite3.connect('db/db.sqlite') as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT hora, is_entrada
#                 FROM fichajes
#                 WHERE becario_id = ? and fecha = ?
#                 ORDER BY hora DESC
#             ''', (self._user_id, fecha))
#             fichajes = cursor.fetchall() or ()
            
#             # Formatear el resultado: [('HH:mm', True), ...]
#             return [Fichaje(hora[:-3], bool(is_entrada)) for (hora, is_entrada) in fichajes]
        
#     def get_notificaciones(self) -> list[Notificacion]:
#         '''
#         Devuelve una lista con notificaciones(titulo, descripcion, fecha_hora, is_vista)
#         '''
#         with sqlite3.connect('db/db.sqlite') as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT notificaciones.titulo, notificaciones.descripcion, notificaciones.fecha_hora, becarios_notificaciones.is_vista
#                 FROM notificaciones
#                 JOIN becarios_notificaciones ON becarios_notificaciones.notificacion_id = notificaciones.notificacion_id
#                 WHERE becario_id = ?
#                 ORDER BY fecha_hora DESC
#             ''', (self._user_id,))
#             notificaiones = cursor.fetchall()
            
#             # Cambio de 0, 1 a False, True
#             return [Notificacion(*rest, bool(is_vista)) for (*rest, is_vista) in notificaiones]
        
#     def get_resumen_semanas(self) -> list[int]:
#         '''
#         Devuelve una lista con las horas que ha estado fichado en cada semana en n semanas
#         '''
#         return super().get_resumen_semanas(self._user_id)
 
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
