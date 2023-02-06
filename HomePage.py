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
    def __init__(self, map_layout, video_layout, data):
        super(HomePage, self).__init__()
        self.videoLayout = video_layout
        self.mapLayout = map_layout
        self.data = data 
        self.headingIndicator = HeadingWidget(self.videoLayout, self.data)
        # Create the Home page UI here
        body_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        information_layout= QVBoxLayout()
        altitude = self.data.get('gps_data').get('alt')
        ground_speed = self.data.get('ground_speed')
        battery = self.data.get('batery_voltages')
        flight_time = 0 
        vertical_speed = 0 

        # Layout for the left side of the screen
        information_layout.addWidget(QLabel("Drone Information"))
        information_layout.addWidget(QLabel(f"Altitude: {altitude}"))
        information_layout.addWidget(QLabel(f"Ground Speed: {ground_speed}" ))
        information_layout.addWidget(QLabel(f"Battery(V): {battery}"))
        information_layout.addWidget(QLabel(f"Fight Time: {flight_time}"))
        information_layout.addWidget(QLabel(f"Vertical Speed: {vertical_speed}"))
        
        # self.mapLayout = map_layout
        # coordinate = (48.5107057, -71.6516848)
        # m = folium.Map(
        #     tiles='Stamen Terrain',
        #     zoom_start=13,
        #     location=coordinate
        # )

        # # save map data to data object
        # data = io.BytesIO()
        # m.save(data, close_file=False)

        # webView = QWebEngineView()
        # webView.setHtml(data.getvalue().decode())
        # self.mapLayout.addWidget(webView)
        

        # Layout for the body of the page
        self.left_layout.addLayout(information_layout)
        self.left_layout.addLayout(self.headingIndicator)

        body_layout.addLayout(self.left_layout)
        body_layout.addLayout(self.mapLayout)
        self.setLayout(body_layout)

    def getLayout(self):
        return self.headingIndicator
    
