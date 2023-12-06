class Check:
    def __init__(self, worker_id: str, date: str, time: str, is_entry: int):
        self.worker_id = worker_id
        self.date = date
        self.time = time
        self.is_entry = is_entry

    def get_output(self) -> str:
        return self.time

    def get_minutes(self) -> str:
        return self.time[3:5]
