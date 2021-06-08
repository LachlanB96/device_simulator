class Device:

    # name = "Default"
    # connections = []
    # neighbours_connections = []
    from device_states import seeking, targetting


    def __init__(self, name):
        self.name = name
        self.connections = []
        self.neighbours_connections = {}
        self.state = "online"
        self.ticks_until_update = 10
        self.target = 5

    def __repr__(self):
        return f"ID: {self.name}"


    def setup(self, name, connections, ticks_until_update):
        self.name = name
        self.connections = connections
        self.ticks_until_update = ticks_until_update

    def ping(self):
        return (str(self.name) + ": pong")

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_name(self):
        return self.name

    def get_connections(self):
        return self.connections

    def get_target(self):
        return self.target

    def add_neighbour_connection(self, target, targets_connections):
        self.neighbours_connections[target] = targets_connections

    def can_reach(self, target):
        print("---")
        print("Connections")
        print('[%s]' % ', '.join(map(str, self.connections)))
        print("---")
        for neighbour in self.neighbours_connections:
            print(neighbour)
        if (target in self.connections):
            return True
        else:
            print("no")
            self.check_if_neightbour_knows(target)
            return False

    #This function checks to see if the target we need is in the neighbours connection list
    def check_if_neightbour_knows(self, target):
        for neighbours_connection in self.neighbours_connections:
            print(self.neighbours_connections)

    def print_connections(self):
        return('[%s]' % ', '.join(map(str, self.connections)))

    def print_name(self):
        return(self.name)

    def print_device_details(self):
        print("==="*20)
        print("Device: " + str(self.name))
        print("TTU: " + str(self.ticks_until_update) + " || State: " + str(self.state))
        print("---")
        print("Connections")
        print('[%s]' % ', '.join(map(str, self.connections)))
        print("---")

    def tick(self):
        self.ticks_until_update -= 1
        if(self.ticks_until_update == 0):
            
            self.state = "seeking"
            if(len(self.connections) > len(self.neighbours_connections)):
                self.state = "targetting"
                self.target = self.connections[0]
        
        
