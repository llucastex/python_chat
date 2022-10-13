from datetime import datetime
import threading

# class User(threading.Thread):
class User():
    def __init__(self, name) -> None:
        # threading.Thread.__init__(self, target = target, args = args)
        self.name = name
        self.connection_time = datetime.now()
    
    def get_name(self):
        return self.name
    