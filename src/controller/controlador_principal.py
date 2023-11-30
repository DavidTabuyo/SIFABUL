from controller.controlador import Controlador
from controller.controlador_becario import ControladorBecario
from controller.controlador_responsable import ControladorResponsable
from model.becario import Becario
from model.responsable import Responsable


def login(user_id: str, password: str) -> 'Controlador':
        # Comprueba si es becario
        if Becario.is_becario(user_id):
            becario = Becario.from_id(user_id)

            # Comprueba contraseña
            if not becario.check_password(password):
                raise ValueError('Contraseña incorrecta')
            
            return ControladorBecario(becario)
            
            
        # Comprueba si es responsable
        if Responsable.is_responsable(user_id):
            responsable = Responsable.from_id(user_id)
            
            # Comprueba contraseña
            if not responsable.check_password(password):
                raise ValueError('Contraseña incorrecta')
            
            return ControladorResponsable(responsable)
        
        
        # No existe
        raise LookupError('Usuario no encontrado')
        
        
        
        
        
        # with sqlite3.connect('db/db.sqlite') as connection:
        #     cursor = connection.cursor()
        #     cursor.execute('''
        #         SELECT salt, hash FROM users WHERE user_id = ?
        #     ''', (user_id,))

        #     # Comprueba si el usuario existe
        #     try:
        #         (salt, hash) = cursor.fetchone()
        #     except TypeError:
        #         raise LookupError('Usuario no encontrado')
            
        #     # Comprueba la contraseña
        #     if hash != bcrypt.hashpw(password.encode('utf-8'), salt):
        #         raise ValueError('Contraseña incorrecta')
            
        #     # Comprueba si es becario
        #     cursor.execute('''
        #         SELECT * FROM becarios WHERE becario_id = ?
        #     ''', (user_id,))
        #     if cursor.fetchone() != None:
        #         return __ControladorBecario(user_id)
        #     else:
        #         return __ControladorResponsable(user_id)
          