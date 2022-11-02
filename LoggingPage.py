from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class LoggingPage(QWidget):
    def __init__(self, stack):
        super(LoggingPage, self).__init__()

        self.stack = stack
        layout = QVBoxLayout()

        # Create the Logging page UI here
        
        self.textbox = QTextEdit(self)

        #setting to read-only, does not take in keyboard input
        self.textbox.setReadOnly(True)
        layout.addWidget(self.textbox)
        
        layout.addWidget(QLabel("Logging Page"))
        self.stack.setLayout(layout)






    
    
        

        