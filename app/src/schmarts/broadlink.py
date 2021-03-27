import broadlink
from .driver import Driver
from .device import Device

class BroadlinkDevice(Device):

    async def send_data(self, data: bytes) -> None:
        print("BroadlinkDevice.send_data with data:")
        print(data)
        self.device.auth()
        self.device.send_data(data)
        print("BroadlinkDevice.send_data done")


class Broadlink(Driver):

    async def discover(self):
        # discover broadlink devices and wrap them in our own Device implementation
        devices = broadlink.discover(timeout=1)
        device_list = []
        for device in devices:
            device_list.append(BroadlinkDevice(self, device))

        return device_list

    def __str__(self) -> str:
        return "Broadlink"
