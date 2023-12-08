class Worker:
    def __init__(self, worker_id: str, name: str, salt: bytes, hash: bytes, admin_id: str):
        self.worker_id = worker_id
        self.name = name
        self.salt = salt
        self.hash = hash
        self.admin_id = admin_id

    def get_output_for_list(self) ->str:
        return self.worker_id

    # def get_notificaciones(self) -> list[NotificacionBecario]:
    #     '''
    #     Obtiene una lista de las notificaiones de un becario.

    #     Returns:
    #         list[Fichaje]: Una lista de objetos NotificacionBecario que representan las notificaiones.
    #     '''
    #     connection = sqlite3.connect('db/db.sqlite')
    #     notificaciones = connection.execute('''
    #         SELECT notificaciones.titulo, notificaciones.descripcion, notificaciones.fecha_hora, becarios_notificaciones.is_vista
    #         FROM notificaciones
    #         JOIN becarios_notificaciones ON becarios_notificaciones.notificacion_id = notificaciones.notificacion_id
    #         WHERE becario_id = ?
    #         ORDER BY fecha_hora DESC
    #     ''', (self.user_id,)).fetchall()
    #     connection.close()

    #     return [NotificacionBecario(*notificacion) for notificacion in notificaciones]

    # def get_fichajes_hoy(self, fecha: str) -> list[Fichaje]:
    #     '''
    #     Obtiene una lista de fichajes realizados en una fecha específica.

    #     Args:
    #         fecha (str): La fecha para la cual se desean obtener los fichajes en formato YYYY-MM-DD.

    #     Returns:
    #         list[Fichaje]: Una lista de objetos Fichaje que representan los fichajes realizados en la fecha dada.
    #     '''
    #     connection = sqlite3.connect('db/db.sqlite')
    #     fichajes = connection.execute('''
    #         SELECT becario_id, fecha, hora, is_entrada
    #         FROM fichajes
    #         WHERE becario_id = ? and fecha = ?
    #         ORDER BY hora DESC
    #     ''', (self.user_id, fecha)).fetchall()
    #     connection.close()
    #     print(fichajes)
    #     return [Fichaje(*fichaje) for fichaje in fichajes]
    
    # def get_last_fichaje(self,fecha_str):
    #     ...

    # def get_semanas(self) -> list[Semana]:
    #     return super().get_semanas(self.user_id)

    # @staticmethod
    # def from_id(becario_id: str) -> 'Becario':
    #     '''
    #     Crea una instancia de la clase Becario utilizando el ID del becario.

    #     Args:
    #         becario_id (str): ID del becario.

    #     Returns:
    #         Becario: Instancia de la clase Becario.
    #     '''
    #     connection = sqlite3.connect('db/db.sqlite')
    #     becario = connection.execute('''
    #         SELECT users.user_id, users.nombre, users.salt, users.hash, becarios.responsable_id
    #         FROM users
    #         JOIN becarios ON users.user_id = becarios.becario_id
    #         WHERE user_id = ?
    #     ''', (becario_id,)).fetchone()
    #     connection.close()

    #     return Becario(*becario)
