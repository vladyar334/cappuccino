import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtWidgets import *


class Ui_SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.save_results)
        self.pushButton_3.clicked.connect(self.add_coffee)

    def search(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        if self.lineEdit.text():
            conor = sqlite3.connect('coffee.sqlite')
            cur = conor.cursor()
            result = cur.execute(f'''SELECT * FROM coffee where id = {self.lineEdit.text()}''').fetchall()
            self.titles = [description[0] for description in cur.description]
            conor.close()
            if result:
                result = result[0]
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(result[0])))
                self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(result[1])))
                self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(result[2])))
                self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(result[3])))
                self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(result[4])))
                self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(str(result[5])))
                self.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(str(result[6])))
                self.modified = {}
                self.tableWidget.itemChanged.connect(self.item_changed)
            else:
                self.label_2.setText(
                    "ID не найден, если хотите добавить, введите в пустую строку значнеия и нажмите соотвествующую кнопку")
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(self.lineEdit.text())))

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            conor = sqlite3.connect('coffee.sqlite')
            cur = conor.cursor()
            que = "UPDATE coffee SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            que += f" WHERE id = {self.lineEdit.text()}"
            cur.execute(que)
            conor.commit()
            self.modified.clear()

    def add_coffee(self):
        result = []
        for i in range(self.tableWidget.columnCount()):
            if self.tableWidget.item(0, i):
                result.append(self.tableWidget.item(0, i).text())
            else:
                result.append('')
        conor = sqlite3.connect('coffee.sqlite')
        cur = conor.cursor()
        if not cur.execute(f'''SELECT * FROM coffee where id = {result[0]}''').fetchall():
            cur.execute(f"""INSERT INTO coffee VALUES {tuple(result)}""")
            conor.commit()
        else:
            self.label_2.setText(
                "ID уже существует, попробуйте отредактировать его!")
        cur.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.resize(1500, 1000)
        self.pushButton.clicked.connect(self.show_dialog)
        self.pushButton_2.clicked.connect(self.refresh)
        self.refresh()

    def show_dialog(self):
        self.w2 = Ui_SecondWindow()
        self.w2.show()

    def refresh(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
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
