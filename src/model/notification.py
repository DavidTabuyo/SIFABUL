class Notification:
    def __init__(self, notifiaction_id:str, title: str, description: str, datetime: str):
        self.notification_id = notifiaction_id
        self.title = title
        self.description = description
        self.datetime = datetime