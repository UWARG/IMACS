from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from test import GroundReceive

class HomePageDataAccessor(QThread):
    def __init__(self):
        self.dataStream = GroundReceive()
        self.dataStream.start()
        self.dataStream.new_data.connect(self.getNewData)



