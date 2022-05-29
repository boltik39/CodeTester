from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from utils.ConfigManager import ConfigManager


class ErrorMessage(QtWidgets.QErrorMessage):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Упс.. Ошибка")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setStyleSheet(
            f"font-size : "
            f"{ConfigManager().get_from_error_msg_config('font-size')}")

    def show_error(self, message):
        self.showMessage(message)
        self.exec_()
