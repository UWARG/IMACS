from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import io
import folium  # pip install folium
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
"""
Folium in PyQt5
"""

class SetupPage(QWidget):
    coordinate=(48.5107057, -71.6516848)

    def newData(self, data):
        SetupPage.coordinate=(data.get('gps_data').get('alt'), data.get('gps_data').get('alt'))
        print(SetupPage.coordinate)

    def reloadMap():
        global count
        global webView
        webView.setParent(None)
        m = folium.Map(
            tiles='http://localhost:8888/tiles/{z}/{x}/{y}.png',
            zoom_start=14,
            location=SetupPage.coordinate,
            attr="alma map"
        )
        folium.Marker(
            SetupPage.coordinate, popup=SetupPage.coordinate,
            icon=folium.Icon(color='blue' , icon='plane' , icon_color='black', draggable=True)
        ).add_to(m)
        data = io.BytesIO()
        m.save(data, close_file=False)
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

    def newData(self, data):
        SetupPage.coordinate=(data.get('gps_data').get('alt'),data.get('gps_data').get('alt'))
        
    def __init__(self):
        super(SetupPage, self).__init__()
        global count
        global webView
        global layout
        count=0
        # Create the Setup page UI here
        layout = QHBoxLayout()
        lwaypoint_layout = QVBoxLayout()
        rwaypoint_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        waypoint_layout = QHBoxLayout()
        formLayout = QHBoxLayout()
        makeForm(formLayout)
        mapLayout = QHBoxLayout()
        coordinate = (48.5107057, -71.6516848)
        m = folium.Map(
            # tiles='Stamen Terrain',
            tiles='http://localhost:8888/tiles/{z}/{x}/{y}.png',
            zoom_start=14,
            location=coordinate,
            attr="alma map"
        )

        # save map data to data object
        dataMap = io.BytesIO()
        m.save(dataMap, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(dataMap.getvalue().decode())
        mapLayout.addWidget(webView)

        layout.addLayout(right_layout)

        right_layout.addLayout(formLayout)
        right_layout.addLayout(waypoint_layout)
        layout.addLayout(mapLayout)

        self.createWaypointGrid(formLayout)

        layout_1 = QHBoxLayout()
        layout_1.addWidget(QLabel("Alpha"))
        layout_1.addWidget(QLabel(f'{-71.6375025}'))
        layout_1.addWidget(QLabel(f'{48.5166707}'))
        layout_1.addWidget(QPushButton("Add"))
        layout_1.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_1)

        layout_2 = QHBoxLayout()
        layout_2.addWidget(QLabel("Bravo"))
        layout_2.addWidget(QLabel(f'{-71.6317518}'))
        layout_2.addWidget(QLabel(f'{48.5060947}'))
        layout_2.addWidget(QPushButton("Add"))
        layout_2.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_2)

        layout_3 = QHBoxLayout()
        layout_3.addWidget(QLabel("Charlie"))
        layout_3.addWidget(QLabel(f'{-71.6340069}'))
        layout_3.addWidget(QLabel(f'{48.4921159}'))
        layout_3.addWidget(QPushButton("Add"))
        layout_3.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_3)

        layout_4 = QHBoxLayout()
        layout_4.addWidget(QLabel("Delta"))
        layout_4.addWidget(QLabel(f'{-71.6404442}'))
        layout_4.addWidget(QLabel(f'{48.5150341}'))
        layout_4.addWidget(QPushButton("Add"))
        layout_4.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_4)

        layout_5 = QHBoxLayout()
        layout_5.addWidget(QLabel("Echo"))
        layout_5.addWidget(QLabel(f'{-71.6782955}'))
        layout_5.addWidget(QLabel(f'{48.5005337}'))
        layout_5.addWidget(QPushButton("Add"))
        layout_5.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_5)

        layout_6 = QHBoxLayout()
        layout_6.addWidget(QLabel("Foxtrot"))
        layout_6.addWidget(QLabel(f'{-71.6040591}'))
        layout_6.addWidget(QLabel(f'{48.5088395}'))
        layout_6.addWidget(QPushButton("Add"))
        layout_6.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_6)

        layout_7 = QHBoxLayout()
        layout_7.addWidget(QLabel("Golf"))
        layout_7.addWidget(QLabel(f'{-71.6522101}'))
        layout_7.addWidget(QLabel(f'{48.5101473}'))
        layout_7.addWidget(QPushButton("Add"))
        layout_7.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_7)

        layout_8 = QHBoxLayout()
        layout_8.addWidget(QLabel("Hotel"))
        layout_8.addWidget(QLabel(f'{-71.6426006}'))
        layout_8.addWidget(QLabel(f'{48.5129917}'))
        layout_8.addWidget(QPushButton("Add"))
        layout_8.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_8)

        layout_9 = QHBoxLayout()
        layout_9.addWidget(QLabel("India"))
        layout_9.addWidget(QLabel(f'{-71.6428152}'))
        layout_9.addWidget(QLabel(f'{48.5117408}'))
        layout_9.addWidget(QPushButton("Add"))
        layout_9.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_9)

        layout_10 = QHBoxLayout()
        layout_10.addWidget(QLabel("Juliette"))
        layout_10.addWidget(QLabel(f'{-71.6229056}'))
        layout_10.addWidget(QLabel(f'{48.5193311}'))
        layout_10.addWidget(QPushButton("Add"))
        layout_10.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_10)

        layout_11 = QHBoxLayout()
        layout_11.addWidget(QLabel("Kilo"))
        layout_11.addWidget(QLabel(f'{-71.6568088}'))
        layout_11.addWidget(QLabel(f'{48.4984623}'))
        layout_11.addWidget(QPushButton("Add"))
        layout_11.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_11)

        layout_12 = QHBoxLayout()
        layout_12.addWidget(QLabel("Lima"))
        layout_12.addWidget(QLabel(f'{-71.6253089}'))
        layout_12.addWidget(QLabel(f'{48.5019885}'))
        layout_12.addWidget(QPushButton("Add"))
        layout_12.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_12)

        layout_13 = QHBoxLayout()
        layout_13.addWidget(QLabel("Mike"))
        layout_13.addWidget(QLabel(f'{-71.6720008}'))
        layout_13.addWidget(QLabel(f'{48.520525}'))
        layout_13.addWidget(QPushButton("Add"))
        layout_13.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_13)

        layout_14 = QHBoxLayout()
        layout_14.addWidget(QLabel("November"))
        layout_14.addWidget(QLabel(f'{-71.6461702}'))
        layout_14.addWidget(QLabel(f'{48.5090567}'))
        layout_14.addWidget(QPushButton("Add"))
        layout_14.addWidget(QPushButton("Remove"))
        lwaypoint_layout.addLayout(layout_14)

        layout_15 = QHBoxLayout()
        layout_15.addWidget(QLabel("Oscar"))
        layout_15.addWidget(QLabel(f'{-71.6516848}'))
        layout_15.addWidget(QLabel(f'{48.5107057}'))
        layout_15.addWidget(QPushButton("Add"))
        layout_15.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_15)

        layout_16 = QHBoxLayout()
        layout_16.addWidget(QLabel("Papa"))
        layout_16.addWidget(QLabel(f'{-71.6298198}'))
        layout_16.addWidget(QLabel(f'{48.5039667}'))
        layout_16.addWidget(QPushButton("Add"))
        layout_16.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_16)

        layout_17 = QHBoxLayout()
        layout_17.addWidget(QLabel("Quebec"))
        layout_17.addWidget(QLabel(f'{-71.6345802}'))
        layout_17.addWidget(QLabel(f'{48.5262308}'))
        layout_17.addWidget(QPushButton("Add"))
        layout_17.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_17)

        layout_18 = QHBoxLayout()
        layout_18.addWidget(QLabel("Point 18"))
        layout_18.addWidget(QLabel(f'{-71.6804996}'))
        layout_18.addWidget(QLabel(f'{48.511563}'))
        layout_18.addWidget(QPushButton("Add"))
        layout_18.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_18)

        layout_19 = QHBoxLayout()
        layout_19.addWidget(QLabel("Romeo"))
        layout_19.addWidget(QLabel(f'{-71.6425625}'))
        layout_19.addWidget(QLabel(f'{48.4984266}'))
        layout_19.addWidget(QPushButton("Add"))
        layout_19.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_19)

        layout_20 = QHBoxLayout()
        layout_20.addWidget(QLabel("Sierra"))
        layout_20.addWidget(QLabel(f'{-71.6320911}'))
        layout_20.addWidget(QLabel(f'{48.5258329}'))
        layout_20.addWidget(QPushButton("Add"))
        layout_20.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_20)

        layout_21 = QHBoxLayout()
        layout_21.addWidget(QLabel("Tango"))
        layout_21.addWidget(QLabel(f'{-71.6758648}'))
        layout_21.addWidget(QLabel(f'{48.4996779}'))
        layout_21.addWidget(QPushButton("Add"))
        layout_21.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_21)

        layout_22 = QHBoxLayout()
        layout_22.addWidget(QLabel("Uniform"))
        layout_22.addWidget(QLabel(f'{-71.6290012}'))
        layout_22.addWidget(QLabel(f'{48.4937058}'))
        layout_22.addWidget(QPushButton("Add"))
        layout_22.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_22)

        layout_23 = QHBoxLayout()
        layout_23.addWidget(QLabel("Victor"))
        layout_23.addWidget(QLabel(f'{-71.6228085}'))
        layout_23.addWidget(QLabel(f'{48.510353}'))
        layout_23.addWidget(QPushButton("Add"))
        layout_23.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_23)

        layout_24 = QHBoxLayout()
        layout_24.addWidget(QLabel("Whiskey"))
        layout_24.addWidget(QLabel(f'{-71.6216069}'))
        layout_24.addWidget(QLabel(f'{48.5093153}'))
        layout_24.addWidget(QPushButton("Add"))
        layout_24.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_24)

        layout_25 = QHBoxLayout()
        layout_25.addWidget(QLabel("X-Ray"))
        layout_25.addWidget(QLabel(f'{-71.6034018}'))
        layout_25.addWidget(QLabel(f'{48.4969248}'))
        layout_25.addWidget(QPushButton("Add"))
        layout_25.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_25)

        layout_26 = QHBoxLayout()
        layout_26.addWidget(QLabel("Yankee"))
        layout_26.addWidget(QLabel(f'{-71.6312968}'))
        layout_26.addWidget(QLabel(f'{48.5112557}'))
        layout_26.addWidget(QPushButton("Add"))
        layout_26.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_26)

        layout_27 = QHBoxLayout()
        layout_27.addWidget(QLabel("Zulu"))
        layout_27.addWidget(QLabel(f'{-71.6664874}'))
        layout_27.addWidget(QLabel(f'{48.4932846}'))
        layout_27.addWidget(QPushButton("Add"))
        layout_27.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_27)

        layout_28 = QHBoxLayout()
        layout_28.addWidget(QLabel("Custom"))
        layout_28.addWidget(QLineEdit("Latitude"))
        layout_28.addWidget(QLineEdit("Longitude"))
        layout_28.addWidget(QPushButton("Add"))
        layout_28.addWidget(QPushButton("Remove"))
        rwaypoint_layout.addLayout(layout_28)

        waypoint_layout.addLayout(lwaypoint_layout)
        waypoint_layout.addLayout(rwaypoint_layout)

        self.setLayout(layout)

        # TO-DO: QFormLayout shell

    def createWaypointGrid(self, formLayout):
        gridLayout = QGridLayout()
        gridShell = QFormLayout()
        self.showWaypointButton = QPushButton("+")
        self.hideWaypointButton = QPushButton("-")
        gridLayout.addWidget(self.showWaypointButton, 0, 0)
        gridLayout.addWidget(self.hideWaypointButton, 0, 1)
        gridShell.addRow(gridLayout)
        formLayout.addLayout(gridShell)


def makeForm(formLayout):
    theFormLayout = QFormLayout()

    rcComboBox = QComboBox()

    rcComboBox.addItems(["1", "2", "3"])

    lineEdit = QLineEdit()

    theFormLayout.addRow(QLabel("Setup"))
    theFormLayout.addRow(QLabel("RC Link"), rcComboBox)
    theFormLayout.addRow(QLabel("Bidirectional data \n telemetry"), lineEdit)
    theFormLayout.addRow(QLabel("Waypoint"))

    theFormLayout.addWidget(QPushButton("Get marker on map"))
