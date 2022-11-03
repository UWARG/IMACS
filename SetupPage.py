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
        gridShell.addRow(gridLayout)
        formLayout.addLayout(gridShell)

def makeForm(formLayout):
    theFormLayout = QFormLayout()

    rcComboBox = QComboBox()

    rcComboBox.addItems(["1", "2", "3"])

    lineEdit = QLineEdit()

    verticalWaypoint =  QHBoxLayout()
    verticalWaypoint.addWidget(QLabel("Waypoint"))
    verticalWaypoint.addWidget(QPushButton("+"))
    verticalWaypoint.addWidget(QPushButton("-"))

    theFormLayout.addRow(QLabel("Setup"))
    theFormLayout.addRow(QLabel("RC Link"), rcComboBox)
    theFormLayout.addRow(QLabel("Bidirectional data \n telemetry"), lineEdit)
    theFormLayout.addRow(verticalWaypoint)

    # createTable(theFormLayout)

    formLayout.addLayout(theFormLayout) 

# def createTable(theFormLayout):
#     theTable = QTableWidget()

#     theFormLayout.addRow(theTable)