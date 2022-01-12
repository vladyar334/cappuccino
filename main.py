import sys
from random import randint

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_yellow_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_yellow_circle(self, qp):
        rand_size = randint(50, 100)
        qp.setBrush(QColor(QtCore.Qt.yellow))
        qp.setPen(QtGui.QPen(QtCore.Qt.yellow, 1, QtCore.Qt.SolidLine))
        qp.drawEllipse(randint(1, 800), randint(1, 600), rand_size, rand_size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
