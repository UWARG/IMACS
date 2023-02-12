from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from HeadingWidget import HeadingWidget
import cv2
import io
import folium  # pip install folium
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
"""
Folium in PyQt5
"""


class HomePage(QWidget):
    new_heading_data = pyqtSignal(dict)
    def __init__(self, map_layout, video_layout):
        super(HomePage, self).__init__()
        self.videoLayout = video_layout
        self.mapLayout = map_layout
        self.headingIndicator = HeadingWidget(self.videoLayout)
        self.new_heading_data.connect(self.headingIndicator.newData)
        # Create the Home page UI here
        body_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.information_layout= QVBoxLayout()
        self.altitude = 0
        self.ground_speed = 0
        self.battery = 0
        self.flight_time = 0 
        self.airspeed = 0 

        self.altitude_label = QLabel(self.tr(f"Altitude: {self.altitude}"))
        self.ground_speed_label = QLabel(f"Ground Speed: {self.ground_speed}")
        self.battery_label = QLabel(f"Battery(V): {self.battery}")
        self.flight_label = QLabel(f"Flight Time: {self.flight_time}")
        self.airspeed_label = QLabel(f"Airspeed: {self.airspeed}")

        # Layout for the left side of the screen
        self.information_layout.addWidget(QLabel("Drone Information"))
        self.information_layout.addWidget(self.altitude_label)
        self.information_layout.addWidget(self.ground_speed_label)
        self.information_layout.addWidget(self.battery_label)
        self.information_layout.addWidget(self.flight_label)
        self.information_layout.addWidget(self.airspeed_label)
        
        # Layout for the body of the page
        self.left_layout.addLayout(self.information_layout)
        self.left_layout.addLayout(self.headingIndicator)

        body_layout.addLayout(self.left_layout)
        body_layout.addLayout(self.mapLayout)
        self.setLayout(body_layout)

    def getLayout(self):
        return self.headingIndicator

    def newData(self, data):
        self.altitude_label.setText(f"Altitude: {round(data.get('gps_data').get('alt'), 3)}")
        self.ground_speed_label.setText(f"Ground Speed: {round(data.get('ground_speed'), 3)}")
        self.battery_label.setText(f"Battery(V): {round(data.get('battery_voltages')[0], 3)}")
        #self.flight_label.setText(f"Flight Time: {round(data.get(''))}")
        self.airspeed_label.setText(f"Airspeed: {round(data.get('air_speed'), 3)}")
        self.new_heading_data.emit(data)
    
