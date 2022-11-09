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
        MainWindow.setStyleSheet("background-color: rgba(231, 231, 231, 1)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 220, 111, 31))
        self.pushButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.534091, y1:1, x2:0.437, y2:0.00568182, stop:0 rgba(0, 93, 255, 255), stop:1 rgba(0, 158, 255, 255));\n"
            "border-radius:10px;\n"
            " font-family: \"YouTube Sans\",\"Roboto\",sans-serif;\n"
            "    font-size: 12px;\n"
            "    line-height: 2.8rem;\n"
            "    font-weight: 600;\n"
            "color:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 220, 91, 31))
        self.pushButton_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.534091, y1:1, x2:0.437, y2:0.00568182, stop:0 rgba(0, 93, 255, 255), stop:1 rgba(0, 158, 255, 255));\n"
            "border-radius:10px;\n"
            " font-family: \"YouTube Sans\",\"Roboto\",sans-serif;\n"
            "    font-size: 12px;\n"
            "    line-height: 2.8rem;\n"
            "    font-weight: 600;\n"
            "color:rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 20, 521, 21))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "\n"
                                 "word-break: break-word;\n"
                                 "\n"
                                 "    font-size: 16px;\n"
                                 "    line-height: 2.8rem;\n"
                                 "    font-weight: 600;\n"
                                 "color:rgb(0, 0, 0)")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 451, 21))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(37)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                   "word-break: break-word;\n"
                                   "font-family: \'JetBrains Mono\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 300;\n"
                                   "font-size: 12px;\n"
                                   "line-height: 12px;\n"
                                   "color:rgb(0, 0, 0)\n"
                                   "")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 451, 21))
        self.label_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(37)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 8pt \"Consolas\";\n"
                                   "word-break: break-word;\n"
                                   "font-family: \'JetBrains Mono\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 300;\n"
                                   "font-size: 12px;\n"
                                   "line-height: 12px;\n"
                                   "color:rgb(0, 0, 0)")
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setLineWidth(1)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(310, 80, 31, 19))
        self.toolButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "background: #D9D9D9;\n"
                                      "box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.25);\n"
                                      "border-radius: 4px;")
        self.toolButton.setObjectName("toolButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 140, 311, 21))
        self.comboBox.setStyleSheet("\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "background: #D9D9D9;\n"
                                    "box-shadow: 12px 4px 6px rgba(0, 0, 0, 0.25);\n"
                                    "border-radius: 4px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 271, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "background: #D9D9D9;\n"
                                    "box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.25);\n"
                                    "border-radius: 4px;")
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
        self.label.setText(_translate("MainWindow", "Добро пожаловать в голосового помошника фотошоп"))
        self.label_3.setText(_translate("MainWindow", "Выберете модель для озвучивания"))
        self.label_4.setText(_translate("MainWindow", "Выберете директорию фотошоп"))
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
