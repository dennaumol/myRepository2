import sys
from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from UI import Ui_MainWindow

SCREEN_SIZE = [700, 700]


class Example(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.drawCircle)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.circles = list()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawCircle(self, qp):
        try:
            red = randrange(0, 255)
            green = randrange(0, 255)
            blue = randrange(0, 255)
            r = randrange(0, 300)
            x = randrange(0, 700)
            y = randrange(0, 700)
            self.circles.append((x, y, r, red, green, blue))
            for circle in self.circles:
                qp.setBrush(QColor(circle[3], circle[4], circle[5]))
                qp.drawEllipse(circle[0], circle[1], circle[2], circle[2])
        except Exception:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
