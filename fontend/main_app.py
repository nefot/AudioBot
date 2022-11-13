import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from AudioBot.fontend.build.gui import Ui_MainWindow


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.num_to_delete = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("Photoshop Bot")
        self.setWindowIcon(QIcon("build/assets/img/small_logo.png"))

    def set(self, num_to_delete: int):
        for i in range(10):
            self.num_to_delete = num_to_delete
            self.num_to_delete += i


def setMoveWindow(widget):
    """
    Позволяет перемещать окно ухватившись не только за заголовок, а за произвольный виджит (widget).
    """
    win = widget.window()
    cursorShape = widget.cursor().shape()
    moveSource = getattr(widget, "mouseMoveEvent")
    pressSource = getattr(widget, "mousePressEvent")
    releaseSource = getattr(widget, "mouseReleaseEvent")

    def move(event):
        if move.b_move:
            x = event.globalX() + move.x_korr - move.lastPoint.x()
            y = event.globalY() + move.y_korr - move.lastPoint.y()
            win.move(x, y)
            widget.setCursor(QtCore.Qt.SizeAllCursor)
        return moveSource(event)

    def press(event):
        if event.button() == QtCore.Qt.LeftButton:
            # Корекция геометрии окна: учитываем размеры рамки и заголовока
            x_korr = win.frameGeometry().x() - win.geometry().x()
            y_korr = win.frameGeometry().y() - win.geometry().y()
            # Корекция геометрии виджита: учитываем смещение относительно окна
            parent = widget
            while not parent == win:
                x_korr -= parent.x()
                y_korr -= parent.y()
                parent = parent.parent()
            move.func_dict.update({"lastPoint": event.pos(), "b_move": True, "x_korr": x_korr, "y_korr": y_korr})
        else:
            move.func_dict.update({"b_move": False})
            widget.setCursor(cursorShape)
        return pressSource(event)

    def release(event):
        move.func_dict.update({"b_move": False})
        widget.setCursor(cursorShape)
        return releaseSource(event)

    setattr(widget, "mouseMoveEvent", move)
    setattr(widget, "mousePressEvent", press)
    setattr(widget, "mouseReleaseEvent", release)
    move.func_dict.update({"b_move": False})
    return widget


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = App()
    application.set(1)
    application.set(1)
    application.show()
    sys.exit(app.exec_())
