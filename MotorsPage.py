from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MotorsPage(QWidget):
    def __init__(self, stack):
        super(MotorsPage, self).__init__()

        self.stack = stack

        # Create the Motor page UI here
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Motors Page"))
        
        self.stack.setLayout(layout)