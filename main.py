from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QScrollArea, QPushButton)
from PyQt5.QtCore import *
from mainwindow import Ui_MainWindow
from widget import ItemWidget
from database import a, b, c
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cart = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0
        self.add_widget()

    def add_widget(self):
        while self.counter_id != a[0][0]:
            self.counter_id += 1
            widget = ItemWidget(self.counter_id, image=c[self.counter_id-1][0], name=b[self.counter_id-1][0])
            self.ui.layout.addWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())