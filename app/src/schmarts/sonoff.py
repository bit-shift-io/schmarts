import asyncio
import logging
from pysonofflan import (SonoffSwitch, Discover)
from .driver import Driver
from .device import Device

async def print_state_callback(device):
    if device.basic_info is not None:
        print("ON" if device.is_on else "OFF")
        device.shutdown_event_loop()

class SonoffDevice(Device):

    async def send_data(self, data: bytes) -> None:
        print("SonoffDevice.send_data called!")
        # for now turn on, with inching
        await self.device.turn_on()


class Sonoff(Driver):

    def create_device(self, config):
        print("create_device:")
        print(config)
        event_loop = asyncio.get_event_loop()
        print(event_loop)
        dev = SonoffSwitch(host=config["host"], loop=event_loop) #, callback_after_update=print_state_callback, inching_seconds=1)
        return SonoffDevice(self, dev)

    async def discover(self):
        found_devices = (await Discover.discover()).items()
        device_list = []
        for ip, found_device_id in found_devices:
            dev = self.create_device({"host": ip})
            device_list.append(SonoffDevice(self, dev))

        return device_list

    def __str__(self) -> str:
        return "Sonoff"
