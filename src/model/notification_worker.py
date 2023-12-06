class NotificationWorker:
    def __init__(self, title: str, description: str, datetime: str, is_seen: bool):
        self.title = title
        self.description = description
        self.datetime = datetime
        self.is_seen = is_seen
