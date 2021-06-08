from device import Device

class DeviceManager:

    def __init__(self):
        self.number_of_devices = 10
        self.list_of_devices = []
        self.dict_of_devices = {}

    def get_devices(self):
        return('[%s]' % ', '.join(map(str, self.list_of_devices)))

    def create_devices(self):
        for x in range(self.number_of_devices):
            self.list_of_devices.append(Device(x))
            self.dict_of_devices[x] = Device(str(x))
        
        for deviceID in self.dict_of_devices:
            device = self.dict_of_devices[deviceID]
            response = device.ping()
            print(response)

    def clear_devices(self):
        self.list_of_devices = []

    def setup_device(self, target, name, connections, ticks_until_update):
        self.dict_of_devices[target].setup(name, connections, ticks_until_update)

    def tick_devices(self):
        for deviceID in self.dict_of_devices:
            device = self.dict_of_devices[deviceID]
            device.tick()
            device.print_device_details()
            if(device.targetting()):
                target = device.get_target()
                print(self.dict_of_devices[target])
                targets_connections = self.dict_of_devices[target].get_connections()
                device.add_neighbour_connection(target, targets_connections)

    def neighbour_message(self, origin, destination):
        print("Neighbour Message")
        print(self.dict_of_devices)
        print(self.dict_of_devices[origin].get_connections())
        print(self.dict_of_devices[origin])
        message = self.dict_of_devices[origin].send_message(destination)
        print(message)
        self.dict_of_devices[destination].incoming_message(message)
