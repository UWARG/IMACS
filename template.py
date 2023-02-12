from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# main class, inherits from pyqt QMainWindow

class MainWindow(QMainWindow):
    # define constructor
    def __init__(self):
        # make sure inherited class is initialized
        super(MainWindow, self).__init__()
        # set geometry of window
        self.setGeometry(1000, 900, 300, 300)
        # set title name
        self.setWindowTitle("WARG GUI")
        # initialize initializing method
        self.initUI()

    # everything in our main window
    def initUI(self):

        """
        
        main execution code for main window of GUI 
        
        """

        # define label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("WARG GUI") 
        self.label.move(50,50)

        # create a button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        """

        Currently for debugging

        """
        self.label.setText("clicked")
        self.update()

    def update(self):
        """
        
        ensures text does not run off page
        
        """
        self.label.adjustSize()

def window():

    """
    
    Command method for initialization/termination of application
    
    """


    app = QApplication(sys.argv) 
    win = MainWindow() 
    win.show()
    sys.exit(app.exec_())

window()