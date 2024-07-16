import serial
from serial.tools import list_ports


class Model:
    def __init__(self):
        self.connected = False
        self.port: serial.Serial | None = None

    def get_port_list(self):
        ports = list()
        for port in list_ports.comports():
            ports.append(port.name)
        return ports

    def connect(self, port, speed):
        try:
            self.port = serial.Serial(port, speed)
        except Exception as e:
            print(e)
            return "busy"
        if self.port.isOpen():
            return "connected"

    def disconnect(self):
        if self.port is not None:
            self.port.close()
        self.port = None

    def write(self, message: str):
        if self.port is None:
            return
        self.port.write(message.encode())

    def read(self):
        message = b""
        while self.port.in_waiting == 0:
            pass
        if self.port.isOpen() and self.port.readable():
            message += self.port.read_all()
        return message.decode()
