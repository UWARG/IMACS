from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HeadingWidget(QWidget):
    def __init__(self, widget):
        super(HeadingWidget, self).__init__()
        self.widget = widget
        pixmap = QPixmap('src/attitude controller.png')
        self.image = QLabel()
        self.image.setPixmap(pixmap)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.image, 0, Qt.AlignLeft | Qt.AlignTop)
        self.widget.setLayout(layout)

