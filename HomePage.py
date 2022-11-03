from CameraThread import VideoFeedWorker
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2 

class HomePage(QWidget):
    def __init__(self, stack, videoFeedLabel):
        super(HomePage, self).__init__()
        self.stack = stack
        self.videoFeedLabel = videoFeedLabel
        
        # Create the Home page UI here
        body_layout = QHBoxLayout()
        left_layout = QVBoxLayout()

        # Layout for the left side of the screen
        left_layout.addWidget(self.videoFeedLabel)

        # Layout for the body of the page
        body_layout.addLayout(left_layout)

        self.stack.setLayout(body_layout)
    
        
    

