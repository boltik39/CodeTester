from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from creatures.GoogleSheet import GoogleSheet
from py_designes.start_page import Ui_Dialog
from windows.error_message import ErrorMessage
from windows.test_window import TestWindow


class StartWindow(QtWidgets.QDialog):
    __STUDENTS = []
    __CURRENT_STUDENT_NAME = ""
    __TEST_WINDOW = None

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.ui.setupUi(self)
        self.init_win()

    def init_win(self):
        self.ui.startButton.clicked.connect(self.run_exam)
        self.__get_all_students()
        self.__add_students_to_combobox()

    def __get_all_students(self):
        self.__STUDENTS = GoogleSheet().get_values_from_table("Students!A2:A50")

    def __add_students_to_combobox(self):
        for student_lst in self.__STUDENTS:
            for student in student_lst:
                self.ui.comboBox.addItem(student)

    def run_exam(self):
        if self.ui.comboBox.currentText() == "":
            error = ErrorMessage()
            error.show_error("Для начала выбери себя из списка! "
                             "Если тебя там нет, то обратись к преподавателю")
        else:
            self.__CURRENT_STUDENT_NAME = self.ui.comboBox.currentText()
            self.close()
            self.__TEST_WINDOW = TestWindow(self.__CURRENT_STUDENT_NAME)
            self.__TEST_WINDOW.show()
            self.close()

