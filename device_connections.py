class Connection:
    
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        print("Im Alive")
        
    def check_connection(self, origin, destination):
        if(self.origin == origin and self.destination == destination):
            return True
        else:
            return False
