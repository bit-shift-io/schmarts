from .broadlink import Broadlink
from .sonoff import Sonoff
from .tuya import Tuya

DRIVERS = {
    "Broadlink": Broadlink(),
    "Sonoff": Sonoff(),
    "Tuya": Tuya()
}

def get_driver_names():
    return DRIVERS.keys()

def get_drivers():
    return DRIVERS.values()

def get_driver(driver_name):
    return DRIVERS[driver_name]

def create_device(driver_name, device_config):
    if (driver_name not in DRIVERS):
        print("Driver %s not found. Failed to create device." % driver_name)
        return None

    return DRIVERS[driver_name].create_device(device_config)