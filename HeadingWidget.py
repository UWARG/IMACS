from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HeadingWidget(QVBoxLayout):

    def __init__(self, video):
        super(HeadingWidget, self).__init__()
        self.video = video
        self.circlepixmap = QPixmap('src/attitude controller.png')
        self.circlegraphic_pixmap = QGraphicsPixmapItem()
        self.circlegraphic_pixmap.setPixmap(self.circlepixmap)
        
        self.view = QGraphicsView()
        #self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.addWidget(self.view)

    def scaled(self):
    
        self.scene = QGraphicsScene()
        self.translateAttitude = QTransform()
        self.translateVideo = QTransform()
        self.circlegraphic_pixmap.setTransformOriginPoint(self.circlepixmap.width()/2, self.circlepixmap.height()/2)
        self.circlegraphic_pixmap.setRotation(30)
        self.scene.setBackgroundBrush(QBrush(Qt.GlobalColor.black))
        self.scene.addItem(self.video)
        self.scene.addItem(self.circlegraphic_pixmap)
        self.scene.setSceneRect(-(self.geometry().width() - self.video.boundingRect().width())/4, -(self.geometry().height() - self.video.boundingRect().height())/4, self.geometry().width(), self.geometry().height())
        self.view.setScene(self.scene)
    
        self.translateAttitude.translate((self.geometry().width()/2) - 350, 0)
        #self.translateVideo.translate((self.view.width() - self.video.boundingRect().width())/4, 0)
        self.circlegraphic_pixmap.setTransform(self.translateAttitude)
        self.video.setTransform(self.translateVideo)
        print(self.video.boundingRect().width())
        #print(self.view.width() - self.video.boundingRect().width())



