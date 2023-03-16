#TO DO: Make entire GUI Full Screen and calculate where the indicators will go. 
# Make data thread for rotating indicator (might have to edit picture)

import sys
import io
from HomePage import HomePage
from MotorsPage import MotorsPage
from SetupPage import SetupPage
from LoggingPage import LoggingPage
from cameraThread import VideoFeedWorker
from MockGroundReceive import MockGroundReceiveWorker, ThrottleInfo, BatteryVoltages, RotationInfo, IMUData, DroneInfo, Coordinates, MotorInfo
import folium
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class GroundStationGUI(QWidget):
    image_resize = pyqtSignal(float, float)
    drone_signal = pyqtSignal(dict)
    throttle_signal = pyqtSignal(dict)
    coordinate_signal = pyqtSignal(dict)
    battery_signal = pyqtSignal(dict)
    rotation_signal = pyqtSignal(dict)
    imu_signal = pyqtSignal(dict)
    motor_signal = pyqtSignal(dict)
    
    def __init__(self):
        super(GroundStationGUI, self).__init__()
        
        #self.data.payload is the dictionary,it may require use of a QThread
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
        self.videoFeedLabel = QGraphicsPixmapItem() 
        self.videoFeedWorker.ImageUpdate.connect(self.imageUpdateSlot)

        ground_worker = MockGroundReceiveWorker()
        
        self.drone_info = DroneInfo(ground_worker)
        #self.throttle_info = ThrottleInfo(ground_worker)
        self.coordinate_info = Coordinates(ground_worker)
        self.battery_voltages_info = BatteryVoltages(ground_worker)
        self.rotation_info = RotationInfo(ground_worker)
        self.imu_info = IMUData(ground_worker)
        self.motor_info = MotorInfo(ground_worker) 

        self.drone_info.start()
        #self.throttle_info.start()
        self.coordinate_info.start()
        self.battery_voltages_info.start()
        self.rotation_info.start()
        self.imu_info.start() 
        self.motor_info.start()

        # Create the map view for the homepage
        self.map_layout = QVBoxLayout()
        coordinate = (48.5107057, -71.6516848)
        map = folium.Map(
            # tiles='Stamen Terrain',
            tiles='http://localhost:8888/tiles/{z}/{x}/{y}.png',
            zoom_start=14,
            location=coordinate,
            attr="alma map"
        )
        data = io.BytesIO() 

        # map.save(data, close_file=False)
        # folium.Marker(
        #     location = [48.6107077, -71.6516848], 
        #     popup='drone2',
        #     # tooltip=tooltip,
        #     icon=folium.Icon(color='green' , icon='plane' , icon_color='black', draggable=True)
        # ).add_to(map)
        map.save(data, close_file=False)
        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())
        self.map_layout.addWidget(self.webView)
        
        # folium.Marker(
        #     location = [48.5107057, -71.6516848], 
        #     popup='drone',
        #     # tooltip=tooltip,
        #     icon=folium.Icon(color='blue' , icon='plane' , icon_color='black', draggable=True)
        # ).add_to(map)


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
        self.stackHomePage = HomePage(self.map_layout, self.videoFeedLabel)
        self.stackMotorsPage = MotorsPage()
        self.stackSetupPage = SetupPage()
        self.stackLoggingPage = LoggingPage()

        self.drone_info.new_data.connect(self.emitDrone)
        #self.throttle_info.new_data.connect(self.emitThrottle)
        self.coordinate_info.new_data.connect(self.emitCoordinates)
        self.battery_voltages_info.new_data.connect(self.emitBattery)
        self.rotation_info.new_data.connect(self.emitRotation)
        self.imu_info.new_data.connect(self.emitIMU)
        self.motor_info.new_data.connect(self.emitMotor)

        self.drone_signal.connect(self.stackHomePage.newDroneInfo)
        #self.throttle_signal.connect(self.stackMotorsPage.newThrottleInfo)
        self.coordinate_signal.connect(self.stackHomePage.newCoordinateInfo)
        self.battery_signal.connect(self.stackHomePage.newBatteryInfo)
        self.rotation_signal.connect(self.stackHomePage.newRotationInfo)
      #   self.imu_signal.connect(self.stackMotorsPage.newIMUInfo)
      #   self.motor_signal.connect(self.stackMotorsPage.newMotorInfo)

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

    def resizeEvent(self, event):
      self.image_resize.emit(self.stackHomePage.getLayout().geometry().width(), self.stackHomePage.getLayout().geometry().height())

      #call these functions at whatever rate  
    
    def emitDrone(self, data):
       self.drone_signal.emit(data)
       
    def emitCoordinates(self, data):
       self.coordinate_signal.emit(data)
      
    def emitIMU(self, data):
       self.imu_signal.emit(data)

    def emitThrottle(self, data):
       self.throttle_signal.emit(data)

    def emitBattery(self, data):
       self.battery_signal.emit(data)

    def emitRotation(self, data):
       self.rotation_signal.emit(data)

    def emitMotor(self, data): 
       self.motor_signal.emit(data) 

# Run the application
def main():
    app = QApplication(sys.argv)
    GUI = GroundStationGUI()
    timer = QTimer()
    timer.timeout.connect(SetupPage.reloadMap)  # execute `display_time`
    timer.setInterval(5000)  # 1000ms = 1s
    timer.start()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
  main()