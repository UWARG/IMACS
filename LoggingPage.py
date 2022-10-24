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
        
        self.textbox = QPlainTextEdit()
        layout.addWidget(self.textbox)
        
        layout.addWidget(QLabel("Logging Page"))
        self.stack.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }

    ''')

    loggingpage = LoggingPage()
    loggingpage.show()




    
    
        

        