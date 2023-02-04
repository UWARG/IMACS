from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HeadingWidget(QVBoxLayout):

    def __init__(self, video):
        super(HeadingWidget, self).__init__()
        self.video = video
        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
        self.translateAttitude = QTransform()
        self.translateCenter = QTransform()
        self.translateCompass = QTransform()
        self.translateArrow = QTransform() 
        self.translateVideo = QTransform()
        
        self.circlepixmap = QPixmap('src/attitude controller.png')
        self.circlegraphic_pixmap = QGraphicsPixmapItem()
        self.circlegraphic_pixmap.setPixmap(self.circlepixmap)
        self.circlegraphic_pixmap.setScale(0.75)
        self.circlegraphic_pixmap.setTransformOriginPoint(self.circlegraphic_pixmap.boundingRect().width()/2, self.circlegraphic_pixmap.boundingRect().height()/2)
        self.circlegraphic_pixmap.setRotation(0)

        self.centerpixmap = QPixmap('src/center.png')
        self.centergraphic_pixmap = QGraphicsPixmapItem()
        self.centergraphic_pixmap.setPixmap(self.centerpixmap)

        self.compasspixmap = QPixmap('src/compass_wheel.png')
        self.compassgraphic_pixmap = QGraphicsPixmapItem()
        self.compassgraphic_pixmap.setPixmap(self.compasspixmap)
        self.compassgraphic_pixmap.setTransformOriginPoint(self.compassgraphic_pixmap.boundingRect().width()/2, self.compassgraphic_pixmap.boundingRect().height()/2)
        self.compassgraphic_pixmap.setScale(0.35)
        self.compassgraphic_pixmap.setRotation(180)

        self.arrowpixmap = QPixmap('src/arrow.png')
        self.arrowgraphic_pixmap = QGraphicsPixmapItem()
        self.arrowgraphic_pixmap.setPixmap(self.arrowpixmap)
        self.arrowgraphic_pixmap.setScale(0.10)
        self.arrowgraphic_pixmap.setRotation(180)

        self.scene.setBackgroundBrush(QBrush(Qt.GlobalColor.black))
        self.scene.setSceneRect(0, 0, self.geometry().width(), self.geometry().height())
        
        self.scene.addItem(self.video)
        self.scene.addItem(self.centergraphic_pixmap)
        self.scene.addItem(self.circlegraphic_pixmap)
        self.scene.addItem(self.compassgraphic_pixmap)
        self.scene.addItem(self.arrowgraphic_pixmap)
        
        self.translateAttitude.translate(312, -50)
        self.translateCompass.translate(837, -159)
        self.translateArrow.translate(1118, 115)
        self.translateVideo.translate(138, 0)

        self.video.setTransform(self.translateVideo)
        self.circlegraphic_pixmap.setTransform(self.translateAttitude)
        self.centergraphic_pixmap.setTransform(self.translateCenter)
        self.compassgraphic_pixmap.setTransform(self.translateCompass)
        self.arrowgraphic_pixmap.setTransform(self.translateArrow)

        self.view.setScene(self.scene)

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.addWidget(self.view)
        

    def scaled(self):
    
        print("changed")
        
        
        
        
        
        
    
        
        #self.translateVideo.translate((self.view.width() - self.video.boundingRect().width())/4, 0)
        #self.circlegraphic_pixmap.setTransform(self.translateAttitude)
        #print(self.view.width() - self.video.boundingRect().width())



