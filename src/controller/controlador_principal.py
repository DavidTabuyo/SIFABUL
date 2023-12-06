from controller.controlador_becario import ControladorBecario
from controller.controlador_responsable import ControladorResponsable
from model.user import User
from model.worker import Worker
from model.admin import Admin


def login(user_id: str, password: str) -> ControladorBecario | ControladorResponsable:
    """
    Realiza el proceso de inicio de sesión para un usuario.

    Args:
        user_id (str): El ID del usuario que intenta iniciar sesión.
        password (str): La contraseña proporcionada por el usuario.

    Returns:
        ControladorBecario | ControladorResponsable: 
            - Un ControladorBecario si el usuario es un becario y la contraseña es correcta.
            - Un ControladorResponsable si el usuario es un responsable y la contraseña es correcta.

    Raises:
        ValueError: Se lanza si la contraseña proporcionada es incorrecta.
        LookupError: Se lanza si el usuario no se encuentra en el sistema.
    """
    # Comprueba si es becario
    if User.is_becario(user_id):
        becario = Worker.from_id(user_id)
        controlador_becario = ControladorBecario(becario)

        # Comprueba contraseña
        if not controlador_becario.check_password(password):
            raise ValueError('Contraseña incorrecta')
        
        return controlador_becario
        
        
    # Comprueba si es responsable
    if User.is_responsable(user_id):
        responsable = Admin.from_id(user_id)
        controlador_responsable = ControladorResponsable(responsable)

        # Comprueba contraseña
        if not controlador_responsable.check_password(password):
            raise ValueError('Contraseña incorrecta')
        
        return controlador_responsable
    
    
    # No existe
    raise LookupError('Usuario no encontrado')