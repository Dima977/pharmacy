from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from item import Ui_item
from win_wiewing import windowViewing

class ItemWidget(QWidget):

    def __init__(self, id_widget: int, parent=None, image=None, name=None):
        super(ItemWidget, self).__init__(parent)
        self.ui = Ui_item()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.widget.setTitle(str(id_widget))
        self.ui.label_2.setText(name)
        self.image = QPixmap(image)
        self.ui.label.setPixmap(self.image)
        self.ui.btn_open.clicked.connect(lambda: self.press_open())

    def press_open(self):
        self.viewing = windowViewing(self.id_widget)
        self.viewing.show()



