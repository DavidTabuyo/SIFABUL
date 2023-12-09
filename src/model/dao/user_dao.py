class User_dao:
    @staticmethod
    def is_worker(user_id:str)->bool:
        ...
    
    @staticmethod
    def is_admin(user_id:str)->bool:
        ...
        
    def get_weeks(worker_id:str):
        ...
