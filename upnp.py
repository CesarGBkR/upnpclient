import upnpy


# Variables Globales
upnp = upnpy.UPnP()
services = []
actions = []


# Descubre los Dispositivos en la red
devices = upnp.discover()

print("Devices:\n")
print(devices)
print("********************************")

# Descubre los Servicios disponibles para cada Dispocitivo y sus Acciones

for device in devices:
    servicesToActions = []
    print(f"{device}")
    print("Services:")
    print(device.get_services())

    for service in device.get_services():
        splited = service.id.split(":")
        serviceClean =  splited[3]
        services.append(serviceClean)
        servicesToActions.append(serviceClean)

    print("Actions:")
    actionToIP = ""
    for dictService in servicesToActions:
        service = device[dictService]
        for action in service.get_actions():
            if action.name == "GetExternalIPAddress":
                actionToIP = action.name
            print(action.name)
        if actionToIP != "":
            print("External IP:")
            print(service.GetExternalIPAddress())
    print("\n=========================\n")
