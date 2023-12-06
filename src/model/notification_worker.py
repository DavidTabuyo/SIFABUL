class NotificationWorker:
    def __init__(self, title: str, description: str, datetime: str, is_seen: bool):
        self.title = title
        self.description = description
        self.datetime = datetime
        self.is_seen = is_seen
        
    def get_output(self) -> str:
        fecha_hora_formateada = f"{self.datetime}"

        # Construir el string formateado
        return  f"Título: {self.title}\nFecha y Hora: {fecha_hora_formateada}\n\nDescripción: {self.description}"
        
