from PyQt5 import QtWidgets
from ui.gui import Ui_MainWindow
from app.logic import *
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = ExternalUi()
    window.show()
    sys.exit(app.exec_())