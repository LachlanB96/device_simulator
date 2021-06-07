from device_manager import DeviceManager

running = True

device_manager = DeviceManager()
device_manager.create_devices()
device_manager.setup_device(0, "0", [1, 2], 1)
device_manager.setup_device(1, "1", [3], 5)
device_manager.tick_devices()

while running:
    
    val = input("(? for help) >> ")
    if(val == "1"):
        device_manager.tick_devices()
    elif(val == "2"):
        print(device_manager.get_devices())
    elif(val == "?"):
        print("1. Tick")
        print("2. Select Device")
        print("3. Print All Device Info")
        print("q. Quit Program")
        print("?. Shows All Commands")
    elif(val == "q"):
        running = False

# list_of_devices[0].add_connection(1)
# list_of_devices[0].add_connection(2)
# list_of_devices[1].add_connection(3)
# list_of_devices[1].add_connection(4)
# list_of_devices[1].add_connection(0)
# list_of_devices[1].add_connection(7)


# list_of_devices[0].setup("0", [1, 2], 2)

# print(response)
# print(list_of_devices[0].ping())
# print(list_of_devices[0].can_reach(1))
# print(list_of_devices[0].can_reach(3))
# print(list_of_devices[0].can_reach(5))
# print(list_of_devices[0].print_connections())
# print(list_of_devices[1].print_connections())
# print(list_of_devices[7].print_connections())

# print(list_of_devices[0].print_name())
# print(list_of_devices[1].print_name())


# list_of_devices[0].tick()
# print(list_of_devices[0].print_device_details())
# list_of_devices[0].tick()
# print(list_of_devices[0].print_device_details())




#list_of_devices[0].set