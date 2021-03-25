"""
Open source cross-platform app to drive smart/IoT devices
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from functools import partial

from .drivers import DRIVERS

class Schmarts(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        devices_box = toga.Box(style=Pack(direction=ROW, padding=5))

        # discover devices
        for driver_name in DRIVERS:
            
            driver_class = DRIVERS[driver_name]
            driver_inst = driver_class()
            devices = driver_inst.discover()

            print("{} has discovered the following devices:".format(driver_name))
            for device in devices:
                print("\t{}".format(device))

                # https://stackoverflow.com/questions/41078154/adding-parameter-to-python-callback
                button = toga.Button(str(device), on_press=partial(self.on_device_press, device=device)) #self.on_device_press)
                devices_box.add(button)

        main_box.add(devices_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def on_device_press(self, button, device=None):
        # for now we send the command to toggle the BOSE power
        device.send_data(bytearray.fromhex('26004800000127941212123712121237123712371212123712371237121212371212121212371212121212121237123712121212123712121237123712121212123712371212123712000501'))



def main():
    return Schmarts()
