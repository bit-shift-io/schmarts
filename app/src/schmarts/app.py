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



        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(devices_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.main_window.info_dialog(
            'Hi there!',
            "Hello, {}".format(self.name_input.value)
        )

    def on_device_press(self, button, device=None):
        self.main_window.info_dialog(
            'Device pressed',
            "{}".format(str(device))
        )



def main():
    return Schmarts()
