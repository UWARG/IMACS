#TO DO: Make entire GUI Full Screen and calculate where the indicators will go. 
# Make data thread for rotating indicator (might have to edit picture)

import sys
import folium
import io
from HomePage import HomePage
from MotorsPage import MotorsPage
from SetupPage import SetupPage
from LoggingPage import LoggingPage
from cameraThread import VideoFeedWorker
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class GroundStationGUI(QWidget):
    image_resize = pyqtSignal(float, float)
    def __init__(self):
        super(GroundStationGUI, self).__init__()

        # Constants for Window
        WINDOW_TITLE = "Integrated Monitoring and Command Station (IMACS)"
        HOME_PAGE = 0
        MOTORS_PAGE = 1
        SETUP_PAGE = 2
        LOGGING_PAGE = 3

        # Flag variable for switching video and map view
        self.switchFlag = True

        # Create the video stream
        self.videoFeedWorker = VideoFeedWorker()
        self.image_resize.connect(self.videoFeedWorker.scaled)
        self.videoFeedWorker.start()
        self.videoFeedLabel = QLabel() #emits the pictures
        self.videoFeedWorker.ImageUpdate.connect(self.imageUpdateSlot)
        self.video_layout = QGridLayout()
        self.video_layout.addWidget(self.videoFeedLabel, 0, 0, Qt.AlignCenter)

        # Create the map view for the homepage
        self.map_layout = QHBoxLayout()
        coordinate = (48.5107057, -71.6516848)
        map = folium.Map(
            # tiles='Stamen Terrain',
            tiles='http://localhost:8888/tiles/{z}/{x}/{y}.png',
            zoom_start=14,
            location=coordinate,
            attr="alma map"
        )
        data = io.BytesIO() 
        map.save(data, close_file=False)
        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())
        self.map_layout.addWidget(self.webView)

        # Set the window title
        self.setWindowTitle(WINDOW_TITLE)

        # Create the parent layout for the entire GUI
        parentLayout = QVBoxLayout()
       
        # Create horizontal box layout for header
        header = QHBoxLayout()

        # Create the header buttons for the different pages
        self.homeButton = QPushButton("Home")
        self.motorButton = QPushButton("Motors")
        self.setupButton = QPushButton("Setup")
        self.loggingButton = QPushButton("Logging")
       
        # Add push button widgets to the header layout
        header.addWidget(self.homeButton, 2)
        header.addWidget(self.motorButton, 2)
        header.addWidget(self.setupButton, 2)
        header.addWidget(self.loggingButton, 2)

        # Create the stacks for the different pages
        self.stackHomePage = HomePage(self.map_layout, self.video_layout, self.switchCameraAndMapView)
        self.stackMotorsPage = MotorsPage()
        self.stackSetupPage = SetupPage()
        self.stackLoggingPage = LoggingPage()

        # Add stack to StackedWidget
        stack = QStackedWidget(self)
        stack.addWidget(self.stackHomePage)
        stack.addWidget(self.stackMotorsPage)
        stack.addWidget(self.stackSetupPage)
        stack.addWidget(self.stackLoggingPage)

        # Set push button clicked methods to switch the page
        self.homeButton.clicked.connect(lambda: stack.setCurrentIndex(HOME_PAGE))
        self.motorButton.clicked.connect(lambda: stack.setCurrentIndex(MOTORS_PAGE))
        self.setupButton.clicked.connect(lambda: stack.setCurrentIndex(SETUP_PAGE))
        self.loggingButton.clicked.connect(lambda: stack.setCurrentIndex(LOGGING_PAGE))

        # Add header layout and body (Stacked Widget) to the parent layout
        parentLayout.addLayout(header)
        parentLayout.addWidget(stack)

        # Set the layout of the GUI to the parent layout
        self.setLayout(parentLayout)

        # Display the window
        self.showMaximized()

    def imageUpdateSlot(self, Image):
      self.videoFeedLabel.setPixmap(QPixmap.fromImage(Image))

    def switchCameraAndMapView(self):
      if(self.switchFlag):
        self.map_layout.addWidget(self.videoFeedLabel)
        self.video_layout.addWidget(self.webView)
        self.switchFlag = False
      else:
        self.map_layout.addWidget(self.webView)
        self.video_layout.addWidget(self.videoFeedLabel)
        self.switchFlag = True

    def resizeEvent(self, event):
      self.image_resize.emit(self.stackHomePage.getLayout().geometry().width(), self.stackHomePage.getLayout().geometry().height())


# Run the application
def main():
   app = QApplication(sys.argv)
   GUI = GroundStationGUI()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
  main()