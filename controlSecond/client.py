import socket
from PyQt6 import QtCore, QtWidgets

class UiWindow(object):
    def setupUi(self,Window):
        Window.setObjectName("Window")
        Window.resize(500, 500)

        self.widget = QtWidgets.QWidget(Window)
        self.widget.setObjectName("widget")

        self.line = QtWidgets.QLineEdit(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.line.setObjectName("line")

        self.list = QtWidgets.QListWidget(self.widget)
        self.list.setGeometry(QtCore.QRect(10, 90, 300, 231))
        self.list.setObjectName("list")

        Window.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))

        self.bar = QtWidgets.QStatusBar(Window)
        self.bar.setObjectName("bar")
        Window.setStatusBar(self.bar)

        self.add = QtWidgets.QPushButton(self.widget, clicked= lambda: self.adds())
        self.add.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.add.setObjectName("add")

        self.delete = QtWidgets.QPushButton(self.widget, clicked= lambda: self.deletes())
        self.delete.setGeometry(QtCore.QRect(140, 50, 141, 31))
        self.delete.setObjectName("delete")

        self.clear = QtWidgets.QPushButton(self.widget, clicked= lambda: self.clears())
        self.clear.setGeometry(QtCore.QRect(290, 50, 101, 31))
        self.clear.setObjectName("clear")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def adds(self):
        item = self.line.text()
        sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockets.connect(('localhost', 55000))
        sockets.send(f''.encode())
        self.list.addItem(item)
        self.line.setText("")

    def deletes(self):
        clicked = self.list.currentRow()
        sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockets.connect(('localhost', 55000))
        sockets.send(f'{clicked} + delete'.encode())
        self.list.takeItem(clicked)

    def clears(self):
        sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockets.connect(('localhost', 55000))
        sockets.send(f'clear'.encode())
        self.list.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Window", "To Do"))
        self.add.setText(_translate("Window", "Add"))
        self.delete.setText(_translate("Window", "Delete"))
        self.clear.setText(_translate("Window", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    ui = UiWindow()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec())
