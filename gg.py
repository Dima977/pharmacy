from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from G import Ui_Form

class GG(QWidget):
    def __init__(self):
        super(GG, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)