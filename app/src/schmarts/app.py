"""
Open source cross-platform app to drive smart/IoT devices
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import asyncio
from functools import partial

from .drivers import get_drivers, create_device

class Schmarts(toga.App):

    async def add_known_devices(self, widget, **kwargs):
        # manually create a device
        device = create_device("Sonoff", {"host": "192.168.1.106"})
        button = toga.Button(str(device), on_press=self.on_device_press)
        button.device = device
        self.devices_box.add(button)
        print("add known devices finished")


    async def discover_devices(self, widget, **kwargs):

        # discover devices
        print(get_drivers())
        for driver in get_drivers():
            devices = await driver.discover()

            print("{} has discovered the following devices:".format(driver))
            for device in devices:
                print("\t{}".format(device))
                button = toga.Button(str(device), on_press=self.on_device_press)
                button.device = device
                self.devices_box.add(button)

        print("discovery finished")


    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.devices_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        main_box.add(self.devices_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


        self.add_background_task(self.discover_devices)
        self.add_background_task(self.add_known_devices)


    async def on_device_press(self, button):
        print("device pressed: %s" % button.device)
        # for now we send the command to toggle the BOSE power
        #device.send_data(bytearray.fromhex('26004800000127941212123712121237123712371212123712371237121212371212121212371212121212121237123712121212123712121237123712121212123712371212123712000501'))



def main():
    return Schmarts()
