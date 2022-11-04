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
    def __init__(self, stack):
        super(SetupPage, self).__init__()

        self.stack = stack

        # Create the Setup page UI here
        layout = QHBoxLayout()

        formLayout = QHBoxLayout()
        makeForm(formLayout)


        mapLayout = QHBoxLayout()
        mapLayout.addWidget(QLabel("Map"))
        coordinate = (-71.6516848, 48.5107057)
        m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=13,
            location=coordinate
        )

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        mapLayout.addWidget(webView)
        
        layout.addLayout(mapLayout)
        layout.addLayout(formLayout)
        self.createWaypointGrid(formLayout)
        
        self.stack.setLayout(layout)
        

        

        # TO-DO: QFormLayout shell

    def createWaypointGrid(self,formLayout):
        gridLayout = QGridLayout()
        gridShell = QFormLayout()
        self.showWaypointButton = QPushButton("+")
        self.hideWaypointButton = QPushButton("-")
        gridLayout.addWidget(self.showWaypointButton,0,0)
        gridLayout.addWidget(self.hideWaypointButton,0,1)
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

    formLayout.addLayout(theFormLayout) 