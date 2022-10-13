import sys
from HomePage import HomePage
from MotorsPage import MotorsPage
from SetupPage import SetupPage
from LoggingPage import LoggingPage
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class GroundStationGUI(QWidget):
    def __init__(self):
        super(GroundStationGUI, self).__init__()

        # Constants for Window
        WINDOW_TITLE = "Integrated Monitoring and Command Station (IMACS)"
        HOME_PAGE = 0
        MOTORS_PAGE = 1
        SETUP_PAGE = 2
        LOGGING_PAGE = 3

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
        self.stackHomePage = QWidget()
        self.stackMotorsPage = QWidget()
        self.stackSetupPage = QWidget()
        self.stackLoggingPage = QWidget()

        # Assign each stack to a specific page in the application
        HomePage(self.stackHomePage)
        MotorsPage(self.stackMotorsPage)
        SetupPage(self.stackSetupPage)
        LoggingPage(self.stackLoggingPage)

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
        self.show()

# Run the application
def main():
   app = QApplication(sys.argv)
   GUI = GroundStationGUI()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
  main()