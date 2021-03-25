import broadlink
from .driver import Driver
from .device import Device

class BroadlinkDevice(Device):
    
    def send_data(self, data: bytes) -> None:
        self.device.auth()
        self.device.send_data(data)


class Broadlink(Driver):

    def discover(self):
        # discover broadlink devices and wrap them in our own Device implementation
        devices = broadlink.discover(timeout=5)
        device_list = []
        for device in devices:
            device_list.append(BroadlinkDevice(self, device))

        return device_list

    def __str__(self) -> str:
        return "Broadlink"
