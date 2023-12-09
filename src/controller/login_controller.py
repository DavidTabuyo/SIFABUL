import bcrypt
from controller.admin_controller import AdminController
from controller.worker_controller import WorkerController
from model.dao.user_dao import UserDao


def login(user_id: str, password: str) -> WorkerController | AdminController:
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
    # Comprueba si es becario o responsable o no existe
    if UserDao.is_worker(user_id):
        controller = WorkerController(user_id)
    elif UserDao.is_admin(user_id):
        controller = AdminController(user_id)
    else:
        raise LookupError('Usuario no encontrado')

    # Comprueba contraseña
    if not check_password(user_id, password):
        raise ValueError('Contraseña incorrecta')

    return controller


def check_password(user_id: str, password: str) -> bool:
    user = UserDao.get_user(user_id)
    return user.hash == bcrypt.hashpw(password.encode('utf-8'), user.salt)
