#import tinytuya # not great!
from tuyapy import TuyaApi

from .driver import Driver
from .device import Device



class TuyaDevice(Device):

    async def send_data(self, data: bytes) -> None:
        print("TuyaDevice.send_data called!")

        #data = self.device.status() 
        #print('set_status() result %r' % data)

        print("send_data done")


class Tuya(Driver):

    def __init__(self):
        print("init Tuya driver")

        print("init done")

    def create_device(self, config):
        print("create_device:")
        print(config)

        dev = tinytuya.OutletDevice(config['gwId'], config['ip'], config['productKey'])
        #dev.set_version(3.1)

        return TuyaDevice(self, dev)

    async def discover(self):
        print("tuya scan...")
        device_list = []

        # https://github.com/dev-est/tuya_tray/blob/master/tuya-tray.py
        api = TuyaApi()
        api.init("USER_NAME", "PASSWORD", "61", "smart_life")
        devices2 = api.discover_devices()
        print(devices2)

        #devices = tinytuya.deviceScan(True, 1)
        #for ip in devices:
        #    dev_conf = devices[ip]
        #    print(devices[ip])
        #    dev = self.create_device(dev_conf)
        #    print("we found a tuya device!")
        #    device_list.append(dev)

        print("tuya scan done")
        return device_list

    def __str__(self) -> str:
        return "Tuya"
