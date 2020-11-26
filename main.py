import sys
from random import choice
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow


class Sec(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.let_paint)
        self.can_paint = False

    def let_paint(self):
        self.can_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.can_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        diameter = choice(range(20, 60)) * 2
        qp.drawEllipse(60, 60, diameter, diameter)


app = QApplication(sys.argv)
ex = Sec()
ex.show()
sys.exit(app.exec())
