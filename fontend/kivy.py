import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from gui import Ui_MainWindow


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle("Photoshop Bot")
        self.setWindowIcon(QIcon("build/assets/img/small_logo.png"))




app = QtWidgets.QApplication([])
application = App()

application.show()

sys.exit(app.exec_())