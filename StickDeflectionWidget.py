from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StickDeflectionWidget(QWidget):
    
    def __init__(self, title: str, x_val: int, y_val: int):
        super(StickDeflectionWidget, self).__init__()

        layout = QVBoxLayout(self)

        self.label = QLabel()
        self.x_coordinate = x_val
        self.y_coordinate = y_val

        canvas = QPixmap(150, 150)
        canvas.fill( QColor("white") )
        self.label.setPixmap(canvas)

        self.draw_widget()

        layout.addWidget( QLabel(title) )
        layout.addWidget(self.label)

    def draw_widget(self):
        painter = QPainter(self.label.pixmap())
        pen = QPen()

        pen.setWidth(10)
        pen.setColor(QColor("red"))

        painter.setPen(pen)
        painter.drawPoint(self.x_coordinate, self.y_coordinate)
        painter.end()