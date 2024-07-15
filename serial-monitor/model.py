import serial
from serial.tools import list_ports


def get_port_list():
    return list_ports.comports()


class Port:
    def __init__(self):
        self.port_number = None
        self.port_speed = None
        self.connected = False
        self.port: serial.Serial | None = None

    def connect(self):
        self.port = serial.Serial(self.port_number, self.port_speed)
        self.port.open()

    def disconnect(self):
        if self.port:
            self.port.close()
        self.port = None

    def write(self, message: str):
        if self.port is None:
            return
        self.port.write(message.encode())
