from cameraThread import cameraThread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2 

class HomePage(QWidget, cameraThread):
    
    def __init__(self, stack, cvstream):
        super(HomePage, self).__init__()
        self.stack = stack
        # Create the Home page UI here
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Home Page"))
        self.FeedLabel = QLabel()
        layout.addWidget(self.FeedLabel)
        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        layout.addWidget(self.CancelBTN) #basic page layout
        self.cvstream = cvstream
        self.cvstream.ImageUpdate.connect(self.ImageUpdateSlot) 
        self.stack.setLayout(layout)
        
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.cvstream.stop()

