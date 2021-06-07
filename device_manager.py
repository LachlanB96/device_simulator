from device import Device

class DeviceManager:

    def __init__(self):
        self.number_of_devices = 10
        self.list_of_devices = []

    def get_devices(self):
        device_names = []
        for device in self.list_of_devices:
            device_names.append(device.get_name())
        return(device_names)

    def create_devices(self):
        for x in range(self.number_of_devices):
            self.list_of_devices.append(Device(x))
        
        for device in self.list_of_devices:
            response = device.ping()
            print(response)

    def clear_devices(self):
        self.list_of_devices = []

    def setup_device(self, target, name, connections, ticks_until_update):
        self.list_of_devices[target].setup(name, connections, ticks_until_update)
        #self.list_of_devices[target].print_device_details()

    def tick_devices(self):
        for device in self.list_of_devices:
            device.tick()
            device.print_device_details()
            if(device.targetting()):
                target = device.get_target()
                targets_connections = self.list_of_devices[target].get_connections()
                device.add_neighbour_connection(target, targets_connections)