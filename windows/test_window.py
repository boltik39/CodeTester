from PyQt5 import QtWidgets, QtGui
from py_designes.test_page import Ui_MainWindow
import os
import shutil
import subprocess


class TestWindow(QtWidgets.QMainWindow):
    __STUDENT_NAME = ""
    __DIRECTORY_FOR_PROGRAM = "student_work"
    __NAME_OF_PROGRAM = "test.py"

    def __init__(self, student_name, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.__STUDENT_NAME = student_name
        self.ui.setupUi(self)
        self.showMaximized()
        self.init_win()

    def init_win(self):
        self.ui.runButton.clicked.connect(self.__check_code)

    def __check_code(self):
        program = self.ui.textEdit.text()
        if program != "":
            self.__create_dir_and_py_file(program)
            output, error = self.__run_code()
            self.ui.textBrowser.setTextColor(QtGui.QColor("#ffffff"))
            self.ui.textBrowser.setText(output)
            self.ui.textBrowser.setTextColor(QtGui.QColor("#dc143c"))
            self.ui.textBrowser.append(error)

    def __create_dir_and_py_file(self, program):
        os.mkdir(self.__DIRECTORY_FOR_PROGRAM)
        python_file = open(
            f"{self.__DIRECTORY_FOR_PROGRAM}/{self.__NAME_OF_PROGRAM}", "w+")
        python_file.write(program)
        python_file.close()

    def __run_code(self):
        command = \
            f'python {self.__DIRECTORY_FOR_PROGRAM}/{self.__NAME_OF_PROGRAM}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        try:
            output, error = process.communicate(timeout=5)
            shutil.rmtree(f"{self.__DIRECTORY_FOR_PROGRAM}")
            return output.decode('utf-8'), error.decode('utf-8')
        except subprocess.TimeoutExpired:
            process.kill()
            shutil.rmtree(f"{self.__DIRECTORY_FOR_PROGRAM}")
            return "", "Timeout error"
