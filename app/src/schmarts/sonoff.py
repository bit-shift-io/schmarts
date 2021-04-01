import asyncio
import logging
from pysonofflan import (SonoffSwitch, Discover)
from .driver import Driver
from .device import Device

#from .sonoffLAN import async_setup
from .sonoffLAN.switch import EWeLinkToggle
#from homeassistant.helpers.typing import HomeAssistantType
from .sonoffLAN.sonoff_main import EWeLinkRegistry

from zeroconf import Zeroconf

async def print_state_callback(device):
    if device.basic_info is not None:
        print("ON" if device.is_on else "OFF")
        device.shutdown_event_loop()

class SonoffDevice(Device):

    async def send_data(self, data: bytes) -> None:
        print("SonoffDevice.send_data called!")

        # start the registry in "LAN mode"
        if (not self.driver.registry.local.started):
            await self.driver.registry.local_start([], Zeroconf()) #[add_device], zeroconf)
        

        # TODO: we are crashing here, because the deviceid we put in create_device is not legit, 
        # then we need to hacks the registry to include the device
        await self.device.async_turn_on()
        print("send_data done")


class Sonoff(Driver):

    def __init__(self):
        print("init sonoff driver")
        #async_setup(hass: HomeAssistantType, {})
        #self.session = async_get_clientsession(hass)
        self.registry = EWeLinkRegistry(None)

        print("init done")

    def create_device(self, config):
        print("create_device:")
        print(config)
        #event_loop = asyncio.get_event_loop()
        #print(event_loop)
        #dev = SonoffSwitch(host=config["host"], loop=event_loop) #, callback_after_update=print_state_callback, inching_seconds=1)

        # start the registry in "LAN mode"
        #if (not self.registry.local.started):
        #    await self.registry.local_start() #[add_device], zeroconf)
        
        # how to get device id?
        self.registry.concat_devices({
            "f9765c85-463a-4623-9cbe-8d59266cb2e4": {
                "device_class": "switch",
                "uiid": "f9765c85-463a-4623-9cbe-8d59266cb2e4",
                "name": "Sonoff Basic",
                "host": config["host"]
            }
        })
        dev = EWeLinkToggle(self.registry, "f9765c85-463a-4623-9cbe-8d59266cb2e4", channels=None)
        return SonoffDevice(self, dev)

    async def discover(self):
        found_devices = (await Discover.discover()).items()
        device_list = []
        for ip, found_device_id in found_devices:
            dev = self.create_device({"host": ip})
            device_list.append(dev)

        return device_list

    def __str__(self) -> str:
        return "Sonoff"
