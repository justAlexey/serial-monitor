from PyQt6.QtWidgets import QApplication
from gui import MainWindow
import controller as cntrl
import model as mdl


def main():
    app = QApplication([])
    window = MainWindow()
    port = mdl.Port()
    controller = cntrl.Controller(window, port)
    controller.fill_gui()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
