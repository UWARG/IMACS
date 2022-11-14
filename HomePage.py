from CameraThread import VideoFeedWorker
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import io
import folium  # pip install folium
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
"""
Folium in PyQt5
"""


class HomePage(QWidget):
    
    def __init__(self, stack, map_layout, video_layout, switchViewsFunction):
        super(HomePage, self).__init__()
        self.stack = stack
        self.videoLayout = video_layout
        self.mapLayout = map_layout

        # Create the Home page UI here
        body_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        information_layout=QVBoxLayout()
        altitude=10
        ground_speed=20
        battery=30
        flight_time=40
        vertical_speed=50

        # Layout for the left side of the screen
        information_layout.addWidget(QLabel("Drone Information"))
        information_layout.addWidget(QLabel(f"Altitude: {altitude}"))
        information_layout.addWidget(QLabel(f"Ground Speed: {ground_speed}" ))
        information_layout.addWidget(QLabel(f"Battery(V): {battery}"))
        information_layout.addWidget(QLabel(f"Fight Time: {flight_time}"))
        information_layout.addWidget(QLabel(f"Vertical Speed: {vertical_speed}"))
        
        self.switchButton = QPushButton("Switch Camera and Map View")   
        self.switchButton.clicked.connect(switchViewsFunction)
        information_layout.addWidget(self.switchButton)

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
        left_layout.addLayout(information_layout)
        left_layout.addLayout(self.videoLayout)

        body_layout.addLayout(left_layout)
        body_layout.addLayout(self.mapLayout)
        self.stack.setLayout(body_layout)
