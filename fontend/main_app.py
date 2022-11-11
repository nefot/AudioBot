import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from gui import Ui_MainWindow


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.pushButton.clicked.connect(self.set)
    def init_UI(self):
        self.setWindowTitle("Photoshop Bot")
        self.setWindowIcon(QIcon("build/assets/img/small_logo.png"))
        self.ui.label_hello.setText("PyScripts")

    def set(self, varr: int):
        for i in range(10):
            self.varr = varr
            self.varr +=i
            self.ui.progressBar.setProperty("value",self.varr+1)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    application = App()
    application.set(1)
    application.set(1)
    application.show()

    sys.exit(app.exec_())
