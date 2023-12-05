import arrow

class NotificacionBecario:
    def __init__(self, titulo: str, descripcion: str, fecha_hora: str, is_vista: bool) -> None:
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_hora = arrow.get(fecha_hora)  # Convierte la cadena a un objeto de fecha y hora usando Arrow
        self._is_vista = is_vista

    # Getters
    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def fecha_hora(self) -> arrow.arrow.Arrow:
        return self._fecha_hora

    @property
    def is_vista(self) -> bool:
        return self._is_vista

    # Setters
    @titulo.setter
    def titulo(self, nuevo_titulo: str) -> None:
        self._titulo = nuevo_titulo

    @descripcion.setter
    def descripcion(self, nueva_descripcion: str) -> None:
        self._descripcion = nueva_descripcion

    @fecha_hora.setter
    def fecha_hora(self, nueva_fecha_hora: str) -> None:
        self._fecha_hora = arrow.get(nueva_fecha_hora)

    @is_vista.setter
    def is_vista(self, nuevo_valor: bool) -> None:
        self._is_vista = nuevo_valor
