from controller.controlador import Controlador
from model.responsable import Responsable

class ControladorResponsable(Controlador):
    def __init__(self, responsable: Responsable) -> None:
        super().__init__(responsable)
        
        
        
# class __ControladorResponsable(__Controlador):
#     def get_becarios(self) -> list[Becario]:
#         '''
#         Devuelve una lista de sus becarios
#         '''
#         with sqlite3.connect('db/db.sqlite') as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT becarios.becario_id, users.nombre
#                 FROM becarios
#                 JOIN users ON users.user_id = becarios.becario_id
#                 WHERE becarios.responsable_id = ?
#             ''', (self._user_id,))
#             return [Becario(*becario) for becario in cursor.fetchall()]
        
#     def get_notificaiones(self) -> list[Notificacion]:
#         '''
#         Devuelve una lista de (titulo, descripcion) de todas las notificaciones
#         '''
#         with sqlite3.connect('db/db.sqlite') as connection:
#             cursor = connection.cursor()
#             cursor.execute('''
#                 SELECT DISTINCT *
#                 FROM notificaciones
#                 JOIN becarios_notificaciones ON becarios_notificaciones.notificacion_id = notificaciones.notificacion_id
#                 JOIN becarios ON becarios.becario_id = becarios_notificaciones.becario_id
#                 WHERE becarios.responsable_id = ?
#                 ORDER BY notificaciones.fecha_hora DESC
#             ''', (self._user_id,))
#             return [Notificacion(*rest, is_all_vista or self._get_is_all_vista(id)) for (id, *rest, is_all_vista) in cursor.fetchall()]
    
#     def _get_is_all_vista(self, notificacion_id: str) -> bool:
#         '''
#         Devuelve si una notificacion ha sido vista
#         '''
    
#     def add_user(self, new_user_email: str, new_user_password: str) -> bool:
#         '''
#         Devuelve false si ya existe ese usuario
#         Dependiendo si es becario, lo añade con self como responsable
#         '''
#         ...
    
#     def add_notificacion(self, titulo: str, descripcion: str, becario_ids: list[str]):
#         '''
#         Añade notificaciones a los becarios pasados en la lista
#         '''
        