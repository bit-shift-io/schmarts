
class Device():

    def __init__(self, driver, device):
        self.driver = driver
        self.device = device

    def __str__(self) -> str:
        """Return a readable representation of the device."""
        return "%s %s" % (str(self.driver), str(self.device))

    def send_data(self, data: bytes) -> None:
        print("TODO: implement device.send_data")