import arrow

class NotificacionResponsable:
    def __init__(self, titulo: str, descripcion: str, fecha_hora: str, is_all_vista: int) -> None:
        titulo: str = titulo
        descripcion: str = descripcion
        fecha_hora: str = arrow.get(fecha_hora)
        is_all_vista: bool = bool(is_all_vista)