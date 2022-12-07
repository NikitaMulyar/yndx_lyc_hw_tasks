import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QInputDialog, QPushButton, QTableWidget, \
    QTextEdit, QTableWidgetItem, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets

obj = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1285, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 1271, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 0, 551, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Изменить запись"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить запись"))


class Ui_ExtraWindow(object):
    def setupUi(self, ExtraWindow):
        ExtraWindow.setObjectName("ExtraWindow")
        ExtraWindow.resize(800, 597)
        self.centralwidget = QtWidgets.QWidget(ExtraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setMinimumSize(QtCore.QSize(0, 40))
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.view = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.view.setMinimumSize(QtCore.QSize(0, 40))
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 1, 1, 1, 1)
        self.cost = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cost.setMinimumSize(QtCore.QSize(0, 40))
        self.cost.setObjectName("cost")
        self.gridLayout.addWidget(self.cost, 4, 1, 1, 1)
        self.volume = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.volume.setMinimumSize(QtCore.QSize(0, 40))
        self.volume.setObjectName("volume")
        self.gridLayout.addWidget(self.volume, 5, 1, 1, 1)
        self.roast = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.roast.setMinimumSize(QtCore.QSize(0, 40))
        self.roast.setObjectName("roast")
        self.gridLayout.addWidget(self.roast, 2, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 500, 261, 41))
        self.pushButton.setObjectName("pushButton")
        ExtraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExtraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        ExtraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExtraWindow)
        self.statusbar.setObjectName("statusbar")
        ExtraWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ExtraWindow)
        QtCore.QMetaObject.connectSlotsByName(ExtraWindow)

    def retranslateUi(self, ExtraWindow):
        _translate = QtCore.QCoreApplication.translate
        ExtraWindow.setWindowTitle(_translate("ExtraWindow", "MainWindow"))
        self.label_2.setText(_translate("ExtraWindow", "Вид"))
        self.label_5.setText(_translate("ExtraWindow", "Цена за порцию"))
        self.label_3.setText(_translate("ExtraWindow", "Обжарка зерен"))
        self.label_4.setText(_translate("ExtraWindow", "Описание"))
        self.label.setText(_translate("ExtraWindow", "Имя"))
        self.label_6.setText(_translate("ExtraWindow", "Объем порции"))
        self.pushButton.setText(_translate("ExtraWindow", "Сохранить"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global obj
        super().__init__()
        self.setupUi(self)
        self.upd()
        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.new)
        obj = self

    def upd(self):
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        res = cur.execute("""
                        SELECT
                            cofees.id,
                            cofees.name,
                            roasts.name,
                            cofees.view,
                            cofees.description,
                            cofees.price,
                            cofees.volume
                        FROM
                            cofees
                        INNER JOIN roasts
                            ON roasts.id = cofees.roast""").fetchall()
        con.close()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Обжарка', 'Вид',
                                                    'Описание', 'Цена', 'Объем'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
            self.tableWidget.verticalHeader().resizeSection(i, 150)
        self.tableWidget.horizontalHeader().resizeSection(1, 150)
        self.tableWidget.horizontalHeader().resizeSection(3, 150)
        self.tableWidget.horizontalHeader().resizeSection(4, 500)

    def edit(self):
        if not len(self.tableWidget.selectedIndexes()):
            self.msg = QMessageBox(self)
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.setText('Вы не выбрали строку с кофе!')
            self.msg.setWindowTitle("Ошибка")
            self.msg.exec()
            return
        row = self.tableWidget.selectedIndexes()[0].row()
        self.id = int(self.tableWidget.item(row, 0).text())
        name = self.tableWidget.item(row, 1).text()
        view = self.tableWidget.item(row, 3).text()
        roast = self.tableWidget.item(row, 2).text()
        descr = self.tableWidget.item(row, 4).text()
        price = self.tableWidget.item(row, 5).text()
        volume = self.tableWidget.item(row, 6).text()
        self.flag = 'E'  # E - editing
        self.ed = ExtraWindow(name=name, view=view, roast=roast, descr=descr, price=price,
                              vol=volume)
        self.ed.show()

    def new(self):
        self.flag = 'C'  # C - creating
        self.ed = ExtraWindow()
        self.ed.show()


class ExtraWindow(QMainWindow, Ui_ExtraWindow):
    def __init__(self, name=None, view=None, roast=None, descr=None, price=None, vol=None):
        global obj
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        res = cur.execute("""SELECT name FROM roasts""").fetchall()
        con.close()
        for i in res:
            self.roast.addItem(i[0])
        if name is not None:
            self.name.setText(name)
            self.view.setText(view)
            self.roast.setCurrentText(roast)
            self.textEdit.setText(descr)
            self.cost.setText(price)
            self.volume.setText(vol)

    def run(self):
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        if self.name.text() == '' or self.textEdit.toPlainText() == '' or self.cost == '' or \
                self.view == '' or self.volume == '':
            self.msg = QMessageBox(self)
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.setText('Неправильно заполнена форма')
            self.msg.setWindowTitle("Ошибка")
            self.msg.exec()
            return
        res = cur.execute(f"""SELECT id FROM roasts WHERE name = '{self.roast.currentText()}'
                            """).fetchall()[0][0]
        if obj.flag == 'E':
            id = obj.id
            cur.execute(f"""UPDATE cofees
                            SET name = '{self.name.text()}', roast = {res},
                            view = '{self.view.text()}',
                            description = '{self.textEdit.toPlainText()}',
                            price = {int(self.cost.text())}, volume = {int(self.volume.text())}
                            WHERE id = {id}""")
        else:
            cur.execute(f"""INSERT INTO cofees(name, roast, view, description, price, volume)
                            VALUES ('{self.name.text()}', {res}, 
                            '{self.view.text()}', '{self.textEdit.toPlainText()}',
                            {int(self.cost.text())}, {int(self.volume.text())})""")
        con.commit()
        con.close()
        obj.upd()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
