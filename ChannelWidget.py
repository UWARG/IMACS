from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ChannelWidget(QWidget):

    def __init__(self, title, value):
        super(ChannelWidget, self).__init__()

        layout = QHBoxLayout(self)

        self.label = QLabel()

        canvas = QPixmap(400, 25)
        canvas.fill( QColor("white") )
        self.label.setPixmap(canvas)

        self.draw_widget()

        layout.addWidget( QLabel(title) )
        layout.addSpacing(5)
        layout.addWidget( QLabel(value) )
        layout.addSpacing(10)
        layout.addWidget(self.label)

    def draw_widget(self):
        painter = QPainter(self.label.pixmap())
        
        pen_1 = QPen()
        pen_1.setColor( QColor("red") )

        painter.setPen(pen_1)
        painter.setBrush( QBrush(Qt.red, Qt.SolidPattern) )
        painter.drawRect(200, 0, 50, 25)

        pen_2 = QPen()
        pen_2.setColor( QColor("black") )
        pen_2.setWidth(4)
        
        painter.setPen(pen_2)
        painter.drawLine(200, 0, 200, 100)



        