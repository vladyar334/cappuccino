import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.resize(1500, 1000)
        conor = sqlite3.connect('coffee.sqlite')
        nor = conor.cursor()
        result = nor.execute(f'''SELECT * FROM coffee''').fetchall()
        conor.close()
        for coffee in result:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(coffee[0])))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(coffee[1])))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(coffee[2])))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(coffee[3])))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(coffee[4])))
            self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(str(coffee[5])))
            self.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(str(coffee[6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
