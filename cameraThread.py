from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2 

class VideoFeedWorker(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.heighty = 1080
        self.widthx = 1920
        self.ThreadActive = True
        # defines video capture
        Capture = cv2.VideoCapture(0) # We will need to edit this line so that it eventually goes to the drone camera
        while self.ThreadActive: #while it can read
            ret, frame = Capture.read()
            if ret: #if it can read
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert to color pic but pyqt cannot read still
                FlippedImage = cv2.flip(Image, 1) #flip on vertical axis
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1241, 767, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    
    def scaled(self, width, height):
        self.heighty = height
        self.widthx = width
        

    

    # def stop(self):
    #     self.ThreadActive = False
    #     self.quit() 