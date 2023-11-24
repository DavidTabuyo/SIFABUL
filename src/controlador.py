import sqlite3


class __Controlador:
    def __init__(self, user_id: str):
        self.__user_id = user_id



class __ControladorBecario(__Controlador):
    def add_fichaje(self):
        '''
        Añade un fichaje a la hora actual
        '''
        ...
        
        
        
class __ControladorResponsable(__Controlador):
    def get_becario_ids(self) -> list[str]:
        '''
        Devuelve una lista de ids de sus becarios
        '''
        ...
        
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
            ''', (self.__user_id,))
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
    if user_id == 'emcuef' and password == 'hola':
        return __ControladorResponsable(user_id)
    
    




if __name__ == '__main__':
    controlador: __ControladorResponsable = login('emcuef', 'hola')
    for line in controlador.get_notificaiones():
        print(line)