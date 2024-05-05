from abc import ABC, abstractmethod


class EntertainmentDevice:
    def connect_to_device_via_hdmi_cable(self, device): pass
    def connect_to_device_via_rca_cable(self, device): pass
    def connect_to_device_via_ethernet_cable(self, device): pass
    def connect_device_to_power_outlet(self, device): pass


class Cable(ABC):
    @abstractmethod
    def connect(self, device1, device2):
        ...


class HDMICable(Cable):
    def connect(self, device1, device2):
        return f'Connect {device1} to {device2} via HDMI'


class RCACable(Cable):
    def connect(self, device1, device2):
        return f'Connect {device1} to {device2} via RCA'


class EthernetCable(Cable):
    def connect(self, device1, device2):
        return f'Connect {device1} to {device2} via Ethernet'


class PowerOutlet(Cable):
    def connect(self, destination, _):
        return f'Connect device to power'


class Television(EntertainmentDevice):
    pass


class DVDPlayer(EntertainmentDevice):
    pass


class GameConsole(EntertainmentDevice):
    pass


class Router(EntertainmentDevice):
    pass


hdmi = HDMICable()
tv = Television
gc = GameConsole

hdmi.connect(tv, gc)
