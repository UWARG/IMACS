from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SetupPage(QWidget):
    def __init__(self, stack):
        super(SetupPage, self).__init__()

        self.stack = stack

        # Create the Setup page UI here
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Setup Page"))
        
        self.stack.setLayout(layout)