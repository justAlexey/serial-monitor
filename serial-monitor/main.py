from PyQt6.QtWidgets import QApplication
from view import MainWindow
from controller import Controller
from model import Model


def main():
    app = QApplication([])
    window = MainWindow()
    port = Model()
    controller = Controller(window, port)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
