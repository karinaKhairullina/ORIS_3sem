import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QCheckBox, QStatusBar, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Как настроение")
        self.setFixedSize(QSize(500, 400))

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addWidget(QLabel("Карина лучшая"))
        toolbar.addWidget(QCheckBox())
        self.setStatusBar(QStatusBar(self))

        button_action = QAction("Сюда",self)
        button_action.triggered.connect(self.first_button_clicked)
        toolbar.addAction(button_action)

        button_action2 = QAction("Туда", self)
        button_action2.triggered.connect(self.second_button_clicked)
        toolbar.addAction(button_action2)

        widget = QComboBox()
        widget.addItems(["Супер", "Класс", "Норм","Нияз поставь фулл балл"])

        # отправляет текущий индекс выбранного элемента
        widget.currentIndexChanged.connect(self.index_changed)

        # альтернативный сигнал отправки текста
        widget.editTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i — это int
        print(i)

    def text_changed(self, s):  # s — это str
        print(s)


    def first_button_clicked(self):
        print("клик")

    def second_button_clicked(self):
        print("не тыкай")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
