from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(False, False)
        MainWindow.resize(571, 275)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(571, 275))
        MainWindow.setMaximumSize(QtCore.QSize(571, 275))
        MainWindow.setBaseSize(QtCore.QSize(111, 111))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 220, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 220, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_hello = QtWidgets.QLabel(self.centralwidget)
        self.label_hello.setEnabled(True)
        self.label_hello.setGeometry(QtCore.QRect(20, 20, 521, 21))
        self.label_hello.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)

        self.label_hello.setFont(font)
        self.label_hello.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_hello.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_hello.setLineWidth(1)
        self.label_hello.setTextFormat(QtCore.Qt.AutoText)
        self.label_hello.setScaledContents(False)
        self.label_hello.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hello.setWordWrap(False)
        self.label_hello.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_hello.setObjectName("label")


        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setEnabled(True)
        self.label_model.setGeometry(QtCore.QRect(30, 110, 451, 21))
        self.label_model.setBaseSize(QtCore.QSize(0, 0))
        self.label_model.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_model.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_model.setLineWidth(1)
        self.label_model.setTextFormat(QtCore.Qt.AutoText)
        self.label_model.setScaledContents(False)
        self.label_model.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_model.setWordWrap(False)
        self.label_model.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_model.setObjectName("label_3")


        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setEnabled(True)
        self.label_dir.setGeometry(QtCore.QRect(30, 50, 451, 21))
        self.label_dir.setBaseSize(QtCore.QSize(0, 0))
        self.label_dir.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_dir.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_dir.setLineWidth(1)
        self.label_dir.setTextFormat(QtCore.Qt.AutoText)
        self.label_dir.setScaledContents(False)
        self.label_dir.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_dir.setWordWrap(False)
        self.label_dir.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_dir.setObjectName("label_4")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(310, 80, 31, 19))

        self.toolButton.setObjectName("toolButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 140, 311, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 271, 20))

        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 220, 281, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "Генерировать"))
        self.pushButton_2.setText(_translate("MainWindow", "отмена"))

        self.label_hello.setText(_translate("MainWindow", f"Добро пожаловать в голосового помошника фотошоп версии"))
        self.label_model.setText(_translate("MainWindow", "Выберете модель для озвучивания"))
        self.label_dir.setText(_translate("MainWindow", "Выберете директорию фотошоп"))

        self.toolButton.setText(_translate("MainWindow", "..."))

        self.comboBox.setItemText(0, _translate("MainWindow", "kseniya"))
        self.comboBox.setItemText(1, _translate("MainWindow", "xenia"))
        self.comboBox.setItemText(2, _translate("MainWindow", "aidar"))
        self.comboBox.setItemText(3, _translate("MainWindow", "baya"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
