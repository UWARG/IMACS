from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class LoggingPage(QWidget):
    def __init__(self, stack):
        super(LoggingPage, self).__init__()

        self.stack = stack
        body_layout = QVBoxLayout()

        # Create the Logging page UI here
    
        self.textbox = QTextEdit(self)

        #setting to read-only, does not take in keyboard input
        self.textbox.setReadOnly(True)

        # Add textbox to logging page
        body_layout.addWidget(self.textbox)
        
        self.stack.setLayout(body_layout)






    
    
        

        