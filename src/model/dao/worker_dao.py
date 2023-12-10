from model.check import Check
from model.notification import Notification


class WorkerDao:
    
    @staticmethod
    def get_notifications(worker_ID:str)->list[Notification]:
        ...
    
    
    @staticmethod
    def get_today_checks(worker_ID:str,date) ->list[Check]:
        ...
   
    @staticmethod        
    def get_last_check(worker_ID:str,date)->Check:
        ...
    
    @staticmethod
    def add_new_check(worker_ID:str,check:Check):
        ...
        
        