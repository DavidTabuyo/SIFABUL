import sqlite3
import bcrypt
import requests
import arrow


class __Controlador:
    def __init__(self, user_id: str):
        self._user_id = user_id
        
    def get_resumen_semanas(self, becario_id: str) -> list[int]:
        '''
        Devuelve una lista con las horas que el becario ha estado fichado en cada semana
        en n semanas
        '''
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT total_semana
                FROM semanas
                WHERE becario_id = ?
                ORDER BY lunes
                LIMIT 10
            ''', (self._user_id,))
            return [segundos // 3600 for (segundos,) in cursor.fetchall()]



class __ControladorBecario(__Controlador):
    def get_fichajes_hoy(self) -> list[tuple[str, bool]]:
        '''
        Devuelve todos los fichajes del dia en forma de [('HH:mm', True), ...]
        '''
        # Obtener fecha actual real
        timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
        fecha = timestamp.format('YYYY-MM-DD')
        
        # Obtener todos los fichajes de hoy 
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT hora, is_entrada
                FROM fichajes
                WHERE becario_id = ? and fecha = ?
                ORDER BY hora
            ''', (self._user_id, fecha))
            fichajes = cursor.fetchall() or ()
            
            # Formatear el resultado: [('HH:mm', True), ...]
            return [(hora[:-3], bool(is_entrada)) for (hora, is_entrada) in fichajes]
        
    def get_notificaciones(self) -> list[tuple[str, str, str, bool]]:
        '''
        Devuelve una lista con notificaciones(titulo, descripcion, fecha_hora, is_vista)
        '''
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT notificaciones.titulo, notificaciones.descripcion, notificaciones.fecha_hora, becarios_notificaciones.is_vista
                FROM notificaciones
                JOIN becarios_notificaciones ON becarios_notificaciones.notificacion_id = notificaciones.notificacion_id
                WHERE becario_id = ?
                ORDER BY fecha_hora
            ''', (self._user_id,))
            notificaiones = cursor.fetchall()
            
            # Cambio de 0, 1 a False, True
            return [(*rest, bool(is_vista)) for (*rest, is_vista) in notificaiones]
        
    def get_resumen_semanas(self) -> list[int]:
        '''
        Devuelve una lista con las horas que ha estado fichado en cada semana en n semanas
        '''
        return super().get_resumen_semanas(self._user_id)
 
    def add_fichaje(self):
        '''
        Añade un fichaje a la hora actual y actualiza la semana
        '''
        # Obtener hora actual real
        timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
        hora = timestamp.format('HH:mm:ss')
        fecha = timestamp.format('YYYY-MM-DD')
        
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            
            # Obtener el ultimo fichaje
            cursor.execute('''
                SELECT hora, is_entrada
                FROM fichajes
                WHERE becario_id = ? and fecha = ?
                ORDER BY hora DESC
            ''', (self._user_id, fecha))
            last_fichaje = cursor.fetchone()  # ((HH:mm:ss, 0) o None) o (HH:mm:ss, 1)
            
            # Comprobar si el ultimo fichaje es de salida o de entrada 
            new_fichaje_is_entrada = 1 if last_fichaje == None or last_fichaje[1] == 0 else 0

            # Añadir el nuevo fichaje
            cursor.execute('''
                INSERT INTO fichajes (becario_id, fecha, hora, is_entrada) VALUES
                    (?, ?, ?, ?);
            ''', (self._user_id, fecha, hora, new_fichaje_is_entrada))

            # Si es de entrada salir de la funcion
            if new_fichaje_is_entrada == 1:
                return
            
            
            # Obtener el total de la semana
            lunes = timestamp.floor('week').format("YYYY-MM-DD")
            cursor.execute('''
                SELECT total_semana FROM semanas WHERE becario_id = ? and lunes = ?
            ''', (self._user_id, lunes))
            total_semana = cursor.fetchone()
            total_semana = total_semana[0] if total_semana else 0
            
            # Calcular el timpo que ha estado fichado
            hora_entrada = arrow.get(last_fichaje[0], 'HH:mm:ss')
            hora_salida = arrow.get(hora, 'HH:mm:ss')
            segundos_fichado = (hora_salida - hora_entrada).total_seconds()
            
            # Actualizar la semana
            cursor.execute('''
                INSERT OR REPLACE INTO semanas (becario_id, lunes, total_semana) VALUES
                    (?, ?, ?);
            ''', (self._user_id, lunes, total_semana + segundos_fichado))

        
class __ControladorResponsable(__Controlador):
    def get_becarios(self) -> list[str, str]:
        '''
        Devuelve una lista de sus becarios
        '''
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT becarios.becario_id, users.nombre
                FROM becarios
                JOIN users ON users.user_id = becarios.becario_id
                WHERE becarios.responsable_id = ?
            ''', (self._user_id,))
            return list(cursor.fetchall())
        
    def get_notificaiones(self) -> list[tuple[str, str]]:
        '''
        Devuelve una lista de (titulo, descripcion) de todas las notificaciones
        '''
        with sqlite3.connect('db/db.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT DISTINCT notificaciones.titulo, notificaciones.descripcion
                FROM notificaciones
                JOIN becarios_notificaciones ON becarios_notificaciones.notificacion_id = notificaciones.notificacion_id
                JOIN becarios ON becarios.becario_id = becarios_notificaciones.becario_id
                WHERE becarios.responsable_id = ?
            ''', (self._user_id,))
            return cursor.fetchall()
    
    def add_user(self, new_user_email: str, new_user_password: str) -> bool:
        '''
        Devuelve false si ya existe ese usuario
        Dependiendo si es becario, lo añade con self como responsable
        '''
        ...
    
    def add_notificacion(self, titulo: str, descripcion: str, becario_ids: list[str]):
        '''
        Añade notificaciones a los becarios pasados en la lista
        '''
        

        
def login(user_id: str, password: str) -> __Controlador:
    salt = bcrypt.gensalt()
    with sqlite3.connect('db/db.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT salt, hash FROM users WHERE user_id = ?
        ''', (user_id,))

        # Comprueba si el usuario existe
        try:
            (salt, hash) = cursor.fetchone()
        except TypeError:
            raise LookupError('Usuario no encontrado')
        
        # Comprueba la contraseña
        if hash != bcrypt.hashpw(password.encode('utf-8'), salt):
            raise ValueError('Contraseña incorrecta')
        
        # Comprueba si es becario
        cursor.execute('''
            SELECT * FROM becarios WHERE becario_id = ?
        ''', (user_id,))
        if cursor.fetchone() != None:
            return __ControladorBecario(user_id)
        else:
            return __ControladorResponsable(user_id)
        
    




if __name__ == '__main__':
    controlador: __ControladorResponsable = login('emcuef', 'hola')
    print(controlador.get_becarios())
    
    