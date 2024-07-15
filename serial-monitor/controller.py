import model
from PyQt6.QtWidgets import QMainWindow


class Controller:
    def __init__(self, gui: QMainWindow, model: model.Port):
        self.model = model
        self.gui = gui

    def fill_gui(self):
        ports = list()
        for port in model.get_port_list():
            ports.append(port.name)
        self.gui.widget.port.port_list.addItems(ports)

