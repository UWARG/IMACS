from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HomePage(QWidget):
    def __init__(self, stack):
        super(HomePage, self).__init__()

        self.stack = stack

        # Create the Home page UI here
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Home Page"))
        
        self.stack.setLayout(layout)