from windows.start_window import StartWindow
from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
myapp = StartWindow()
myapp.show()
app.installEventFilter(myapp)
sys.exit(app.exec_())
