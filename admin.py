import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtSql import *

DB_NAME = 'pharmacy.db'

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Dialog')
        self.line_edit_name = QLineEdit()
        self.line_edit_date = QLineEdit()
        self.line_edit_file = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow('Name:', self.line_edit_name)
        form_layout.addRow('Surname:', self.line_edit_date)
        form_layout.addRow('Email:', self.line_edit_file)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_pref()
        self.show_widgets()

    def window_pref(self):
        self.setWindowTitle('PyQt5 APP')
        self.def_width = 800
        self.def_height = 400
        self.def_size = self.setMinimumSize(self.def_width, self.def_height)

    def show_widgets(self):
        self.createConnection()
        self.setupMainWidgets()

    def createConnection(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(DB_NAME)

        if not db.open():
            QMessageBox.warning(self, 'PyQt5 APP',
                                'Error:{}'.format(db.lastError().text()))
            sys.exit(1)

    def setupMainWidgets(self):
        mw_widget = QWidget()
        main_panel = QHBoxLayout(mw_widget)

        # QSqlTableModel
        self.modelSql = QSqlTableModel()
        self.modelSql.setTable('users')
        self.modelSql.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelSql.select()

        self.modelSql.setHeaderData(0, Qt.Horizontal, 'Id')
        self.modelSql.setHeaderData(1, Qt.Horizontal, 'Name')
        self.modelSql.setHeaderData(2, Qt.Horizontal, 'Surname')
        self.modelSql.setHeaderData(3, Qt.Horizontal, 'Email')

        # QTableView()
        self.table_view = QTableView()
        self.table_view.setSelectionBehavior(1)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setModel(self.modelSql)

        self.table_view.setColumnHidden(0, True)

        self.table_view.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        main_panel.addWidget(self.table_view)

        # QVBoxLayout()
        right_panel = QVBoxLayout()
        line = QFrame()
        line.setFrameShape(QFrame.HLine)

        self.add_record = QPushButton('Add', self)
        self.add_record.clicked.connect(self.addRecord)

        self.change_record = QPushButton('Change', self)
        self.change_record.clicked.connect(self.changeRecord)

        self.delete_record = QPushButton('Delete', self)
        self.delete_record.clicked.connect(self.delRecord)

        right_panel.addSpacing(20)
        right_panel.addWidget(line)
        right_panel.addWidget(self.add_record)
        right_panel.addWidget(self.change_record)
        right_panel.addWidget(self.delete_record)
        right_panel.addStretch()

        main_panel.addLayout(right_panel)

        self.setCentralWidget(mw_widget)
        self.add_record.setFocus()

    def addRecord(self):
        inputDialog = Dialog()
        rez = inputDialog.exec()
        if not rez:
            msg = QMessageBox.information(self, 'Ошибка', 'Диалог сброшен.')
            return
        name = inputDialog.line_edit_name.text()
        date = inputDialog.line_edit_date.text()
        file = inputDialog.line_edit_file.text()
        if not name or not date or not file:
            msg = QMessageBox.information(self, 'Ошибка', 'Заполните пожалуйста все поля.')
            return

        r = self.modelSql.record()
        r.setValue("name", name)
        r.setValue("surname", date)
        r.setValue("email", file)
        self.modelSql.insertRecord(-1, r)
        self.modelSql.select()

    def delRecord(self):
        row = self.table_view.currentIndex().row()
        if row == -1:
            msg = QMessageBox.information(self, 'Ошибка', 'Выберите запись для удаления.')
            return

        name = self.modelSql.record(row).value(1)
        date = self.modelSql.record(row).value(2)
        file = self.modelSql.record(row).value(3)

        inputDialog = Dialog()
        inputDialog.setWindowTitle('Удалить запись?')
        inputDialog.line_edit_name.setText(name)
        inputDialog.line_edit_date.setText(date)
        inputDialog.line_edit_file.setText(file)
        rez = inputDialog.exec()
        if not rez:
            msg = QMessageBox.information(self, 'Ошибка', 'Диалог сброшен.')
            return

        self.modelSql.removeRow(self.table_view.currentIndex().row())
        self.modelSql.select()

        msg = QMessageBox.information(self, 'Успешно', 'Запись удалена.')

    def changeRecord(self):
        self.table_view.edit(self.table_view.currentIndex())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())