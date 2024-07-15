from PyQt6 import QtWidgets


class CentralWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.settings = PortSetting()
        self.port = PortGroup()
        self.messanger = Messanger()

        l1 = QtWidgets.QHBoxLayout()
        l1.addWidget(self.port)
        l1.addWidget(self.settings)

        l2 = QtWidgets.QVBoxLayout(self)
        l2.addLayout(l1)
        l2.addWidget(self.messanger)


class PortSetting(QtWidgets.QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Настройки порта")
        l1 = QtWidgets.QHBoxLayout(self)

        self.port_speed = QtWidgets.QComboBox()
        self.port_speed.addItems([
            "9600",
            "115200",
        ])

        l1.addWidget(self.port_speed)


class PortGroup(QtWidgets.QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Настройки порта")
        l1 = QtWidgets.QVBoxLayout(self)

        self.port_list = QtWidgets.QComboBox()
        self.port_activate = QtWidgets.QPushButton("Открыть")

        l1.addWidget(self.port_list)
        l1.addWidget(self.port_activate)


class Messanger(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        l1 = QtWidgets.QVBoxLayout(self)
        l1.setContentsMargins(0, 0, 0, 0)

        self.send_line = QtWidgets.QLineEdit()
        self.send_line.setEnabled(False)

        self.send_message_area = QtWidgets.QTextEdit()
        self.send_message_area.setEnabled(False)

        self.receive_message_area = QtWidgets.QTextEdit()
        self.receive_message_area.setEnabled(False)

        l1.addWidget(self.send_line)
        l1.addWidget(self.send_message_area)
        l1.addWidget(self.receive_message_area)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = CentralWidget()
        self.setCentralWidget(self.widget)
