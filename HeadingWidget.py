from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HeadingWidget(QVBoxLayout):

    def __init__(self, video):
        super(HeadingWidget, self).__init__()
        self.video = video
        videoWidget = QWidget()
        videoWidget.setLayout(self.video)
        self.circlepixmap = QPixmap('src/attitude controller.png')

        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.translate = QTransform()

        self.circlegraphic_pixmap = QGraphicsPixmapItem()
        self.circlegraphic_pixmap.setPixmap(self.circlepixmap)
        self.circlegraphic_pixmap.setTransformOriginPoint(self.circlepixmap.width()/2, self.circlepixmap.height()/2)
        
        self.scene.setBackgroundBrush(QBrush(Qt.GlobalColor.black))
        self.scene.addWidget(videoWidget)
        self.scene.addItem(self.circlegraphic_pixmap)
        
        self.heighty = self.geometry().height()  
        self.widthx = self.geometry().width()
        
        self.view.setSceneRect(0, 0, self.widthx, self.heighty)
        self.view.setScene(self.scene)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.addWidget(self.view)

    def scaled(self):
        self.heighty = self.view.height()  #try maybe it is view not self...
        self.widthx = self.view.width()
        self.scene.removeItem(self.circlegraphic_pixmap)
        self.scene.addItem(self.circlegraphic_pixmap)
        self.translate.translate(self.scene.width()/2, self.scene.height()/10)
        self.circlegraphic_pixmap.setTransform(self.translate)
        self.circlegraphic_pixmap.setRotation(15)
        #print(self.circlegraphic_pixmap.pos().x(), ' ', self.circlegraphic_pixmap.pos().y())
        #print('layout height: ', self.heighty)
        #print('layout width: ', self.widthx)


