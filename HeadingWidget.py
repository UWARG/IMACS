from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HeadingWidget(QVBoxLayout):

    def __init__(self, video):
        super(HeadingWidget, self).__init__()
        self.video = video
        videoWidget = QWidget()
        videoWidget.setLayout(self.video)
        circlepixmap = QPixmap('src/attitude controller.png')
        self.view = QGraphicsView()
        scene = QGraphicsScene()
        translate = QTransform()
        circlegraphic_pixmap = QGraphicsPixmapItem()
        circlegraphic_pixmap.setPixmap(circlepixmap)
        scene.setBackgroundBrush(QBrush(Qt.GlobalColor.black))
        scene.addWidget(videoWidget)
        scene.addItem(circlegraphic_pixmap)
        self.heighty = self.geometry().height()  
        self.widthx = self.geometry().width()
        self.view.setSceneRect(0, 0, self.widthx, self.heighty)
        self.view.setScene(scene)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        print('layout height: ', self.heighty)
        print('layout width: ', self.widthx)
        translate.translate(self.widthx/2, self.heighty/4)
        circlegraphic_pixmap.setTransform(translate)
        self.addWidget(self.view)

    def scaled(self):
        self.heighty = self.geometry().height()  
        self.widthx = self.geometry().width()
        print('layout height: ', self.heighty)
        print('layout width: ', self.widthx)


