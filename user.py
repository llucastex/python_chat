from datetime import datetime

class User():
    def __init__(self, name) -> None:
        self.name = name
        self.connection_time = datetime.now()
    
    def get_name(self):
        return self.name
    