import arrow

class NotificacionResponsable:
    def __init__(self, titulo: str, descripcion: str, fecha_hora: str, is_all_vista: int) -> None:
        titulo = titulo
        descripcion = descripcion
        fecha_hora = arrow.get(fecha_hora)
        is_all_vista = bool(is_all_vista)