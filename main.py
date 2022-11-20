import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QInputDialog, QPushButton, QTableWidget, \
    QTextEdit, QTableWidgetItem, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 11, 1271, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 24))
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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global obj
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute("""
                SELECT
                    *
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
            self.tableWidget.verticalHeader().resizeSection(i, 100)
        self.tableWidget.horizontalHeader().resizeSection(1, 150)
        self.tableWidget.horizontalHeader().resizeSection(3, 150)
        self.tableWidget.horizontalHeader().resizeSection(4, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
