from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QScrollArea, QPushButton, QMessageBox)
from PyQt5.QtCore import *
from payment import Ui_MainWindow
from gg import GG
import sqlite3
import re

class windowPayment(QMainWindow):
    def __init__(self, id_widget: int):
        super(windowPayment, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buyed = False
        self.id_widget = id_widget
        self.ui.btn_buy.clicked.connect(lambda: self.purchase())
        self.ui.btn_buy.clicked.connect(lambda: self.cl())

    def purchase(self):
        spin = self.ui.spinBox.value()
        name = self.ui.lineEdit.text()
        surname = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()
        valid_pattern = re.compile(r'^([a-z0-9]([\-\_\.]*[a-z0-9])*)+@([a-z0-9]([\-]*[a-z0-9])*\.)+[a-z]{2,6}$', re.I)

        def validate(name: str) -> bool:
            return bool(valid_pattern.match(name))
        with sqlite3.connect("pharmacy.db") as db:
            cur = db.cursor()
            if validate(email):
                cur.execute(f"""UPDATE medicines SET quantity = quantity - {spin} WHERE id_medicines = {self.id_widget} """)
                try:
                    cur.execute(f"""INSERT INTO users (name, surname, email) VALUES ('{name}','{surname}','{email}') """)
                except:
                    pass
                finally:
                    self.buyed = True
                    self.qqq = GG()
                    self.qqq.show()
            else:
                QMessageBox.information(self, 'Ошибка', 'В поле email допущена ошибка')


    def cl(self):
        if self.buyed:
            self.close()









