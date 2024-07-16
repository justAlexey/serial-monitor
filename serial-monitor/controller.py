from PyQt6.QtCore import QThread


class Worker(QThread):
    def __init__(self, method):
        super().__init__()
        self.method = method
        self.alive = False
        print("Created")

    def run(self):
        self.alive = True
        while self.alive:
            self.method()


class Controller:
    def __init__(self, gui, model):
        self.model = model
        self.gui = gui

        self.worker = Worker(self.update)

        self.create_signals()
        self.update_port_list()

    def update(self):
        message = self.model.read()
        self.gui.central_widget.messanger.add_receive_text(message)

    def create_signals(self):
        self.gui.central_widget.port.port_activate_button.clicked.connect(self.update_com_port)

    def update_port_list(self):
        ports = self.model.get_port_list()
        self.gui.central_widget.port.port_list.addItems(ports)

    def update_com_port(self):
        if self.model.port is None:
            self.connect_com_port()
            self.worker.start()
        else:
            self.worker.alive = False
            while self.worker.isRunning():
                pass
            self.disconnect_com_port()

    def connect_com_port(self):
        port = self.gui.central_widget.port.port_list.currentText()
        speed = self.gui.central_widget.settings.port_speed.currentText()

        status = self.model.connect(port, int(speed))
        if status == "busy":
            self.gui.statusBar().showMessage(f"port {port} is busy", 1000)
        if status == "connected":
            self.gui.statusBar().showMessage(f"port {port} connected")
            self.gui.central_widget.port.port_activate_button.setText("Закрыть")

    def disconnect_com_port(self):
        self.model.disconnect()
        self.gui.central_widget.port.port_activate_button.setText("Открыть")
        self.gui.statusBar().showMessage("port closed")
