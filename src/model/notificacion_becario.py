import arrow

class NotificacionBecario:
    def __init__(self, titulo: str, descripcion: str, fecha_hora: str, is_vista: str) -> None:
        titulo: str = titulo
        descripcion: str = descripcion
        fecha_hora: str = arrow.get(fecha_hora)
        is_vista: bool = arrow.get(is_vista)