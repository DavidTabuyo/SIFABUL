import arrow

class Fichaje:
    def __init__(self, becario_id: str, fecha: str, hora: str, is_entrada: int):
        self.becario_id = becario_id
        self.fecha = arrow.get(fecha, 'YYYY/MM/DD')
        self.hora = arrow.get(hora, 'HH:mm:ss')
        self.is_entrada = bool(is_entrada)

    def get_output(self) -> str:
        return self.hora.format("HH:mm:ss")
    
    def get_minutes(seld) ->str:
        return self.hora.minute