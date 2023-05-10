from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QScrollArea, QPushButton)
from PyQt5.QtCore import *
from viewing import Ui_MainWindow
from PyQt5.QtGui import *
from database import *
from windowPayment import windowPayment
from database import a, b, c, e
import sys

class windowViewing(QMainWindow):
    def __init__(self, id_widget: int):
        super(windowViewing, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.btn_back.clicked.connect(lambda: self.close())
        self.ui.label_2.setText(b[id_widget-1][0])
        self.image = QPixmap(c[id_widget-1][0])
        self.ui.label.setPixmap(self.image)
        self.ui.label_3.setText(d[id_widget-1][0])
        self.ui.label_4.setText(f'{price[id_widget-1][0]} ₽')
        self.ui.btn_buy.clicked.connect(lambda: self.pay())
        self.ui.btn_buy.clicked.connect(lambda: self.close())

    def pay(self):
        self.payme = windowPayment(self.id_widget)
        self.payme.show()




