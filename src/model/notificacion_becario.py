import arrow

class NotificacionBecario:
    def __init__(self, titulo: str, descripcion: str, fecha_hora: str, is_vista: bool) -> None:
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_hora = arrow.get(fecha_hora)
        self.is_vista = is_vista
