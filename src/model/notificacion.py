class Notificacion:
    def __init__(self, titulo: str, descripcion: str, fecha_hora: str, is_vista: int) -> None:
        titulo: str = titulo
        descripcion: str = descripcion
        fecha_hora: str = fecha_hora
        is_vista: bool = bool(is_vista)