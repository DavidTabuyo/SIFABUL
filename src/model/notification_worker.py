class NotificationWorker:
    def __init__(self, title: str, description: str, datetime: str, seen: str):
        self.title = title
        self.description = description
        self.datetime = datetime
        self.seen = seen
        
    def get_output(self) -> str:
        # Construir el string formateado
        return  f"Título: {self.title}\nFecha y Hora: {self.datetime}\n\nDescripción: {self.description}"
        
