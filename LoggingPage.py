from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LoggingPage(QWidget):
    def __init__(self, stack):
        super(LoggingPage, self).__init__()

        self.stack = stack

        # Create the Logging page UI here
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Logging Page"))
        
        self.stack.setLayout(layout)