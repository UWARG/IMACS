from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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

        layout.addLayout(formLayout)
        layout.addLayout(mapLayout)

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