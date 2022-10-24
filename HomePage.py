from cameraThread import cameraThread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2 

class HomePage(QWidget):
    def __init__(self, stack, FeedLabel):
        super(HomePage, self).__init__()
        self.stack = stack
        self.FeedLabel = FeedLabel
        #self.CancelBTN = CancelBTN
        #self.clicked = False
        # Create the Home page UI here
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Home Page"))
        layout.addWidget(self.FeedLabel)
        #self.CancelBTN = QPushButton("Cancel")
        #self.CancelBTN.clicked.connect(self.clicked = True)
        #layout.addWidget(self.CancelBTN) #basic page layout
        self.stack.setLayout(layout)
    
        
    

