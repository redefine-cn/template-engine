#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import  sys

class layer(QDockWidget):
    def __init__(self):
        super(layer, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑Layer"))
        self.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        labelCol = 0
        contentCol = 1
        lv1 = 1
        lv2 = 2
        lv3 = 3

        opacityLabel = QLabel(QString.fromUtf8("opacity"))
        opacityEdit = QLineEdit()

        scaleLabel = QLabel(QString.fromUtf8("scale"))
        scaleXLable = QLabel(QString.fromUtf8("X"))
        scaleXEdit = QLineEdit()
        scaleYLabel = QLabel(QString.fromUtf8("Y"))
        scaleYEdit = QLineEdit()

        anchorpointLabel = QLabel(QString.fromUtf8("anchorpoint"))
        anchorpointXLable = QLabel(QString.fromUtf8("X"))
        anchorpointXEdit = QLineEdit()
        anchorpointYLabel = QLabel(QString.fromUtf8("Y"))
        anchorpointYEdit = QLineEdit()

        imageNameLabel = QLabel(QString.fromUtf8("imageName"))
        imageNameEdit = QLineEdit()

        positionLabel = QLabel(QString.fromUtf8("position"))
        positionXLable = QLabel(QString.fromUtf8("X"))
        positionXEdit = QLineEdit()
        positionYLabel = QLabel(QString.fromUtf8("Y"))
        positionYEdit = QLineEdit()

        sizeLabel = QLabel(QString.fromUtf8("size"))
        sizeWidthLable = QLabel(QString.fromUtf8("width"))
        sizeWidthEdit = QLineEdit()
        sizeHeightLabel = QLabel(QString.fromUtf8("height"))
        sizeHeightEdit = QLineEdit()

        animationsLabel = QLabel(QString.fromUtf8("animations"))

        starttimeLabel = QLabel(QString.fromUtf8("starttime"))
        secondLabel = QLabel(QString.fromUtf8("second"))
        secondEdit = QLineEdit()
        frameLabel = QLabel(QString.fromUtf8("frame"))
        framEdit = QLineEdit()

        durationLabel = QLabel(QString.fromUtf8("duration"))
        secondLabel2 = QLabel(QString.fromUtf8("second"))
        secondEdit2 = QLineEdit()
        frameLabel2 = QLabel(QString.fromUtf8("frame"))
        framEdit2 = QLineEdit()

        animationLabel = QLabel(QString.fromUtf8("animation"))

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(opacityLabel, 0, labelCol)
        self.gridLayout.addWidget(opacityEdit, 0, contentCol)
        self.gridLayout.addWidget(scaleLabel, 1, labelCol)
        self.gridLayout.addWidget(scaleXLable, 1, lv1)
        self.gridLayout.addWidget(scaleXEdit, 1, lv2)
        self.gridLayout.addWidget(scaleYLabel, 2, lv1)
        self.gridLayout.addWidget(scaleYEdit, 2, lv2)
        self.gridLayout.addWidget(anchorpointLabel, 3, labelCol)
        self.gridLayout.addWidget(anchorpointXLable, 3, lv1)
        self.gridLayout.addWidget(anchorpointXEdit, 3, lv2)
        self.gridLayout.addWidget(anchorpointYLabel, 4, lv1)
        self.gridLayout.addWidget(anchorpointYEdit, 4, lv2)
        self.gridLayout.addWidget(imageNameLabel, 5, labelCol)
        self.gridLayout.addWidget(imageNameEdit, 5, contentCol)
        self.gridLayout.addWidget(positionLabel, 6, labelCol)
        self.gridLayout.addWidget(positionXLable, 6, lv1)
        self.gridLayout.addWidget(positionXEdit, 6, lv2)
        self.gridLayout.addWidget(positionYLabel, 7, lv1)
        self.gridLayout.addWidget(positionYEdit, 7, lv2)
        self.gridLayout.addWidget(sizeLabel, 8, labelCol)
        self.gridLayout.addWidget(sizeWidthLable, 8, lv1)
        self.gridLayout.addWidget(sizeWidthEdit, 8, lv2)
        self.gridLayout.addWidget(sizeHeightLabel, 9, lv1)
        self.gridLayout.addWidget(sizeHeightEdit, 9, lv2)

        self.gridLayout.addWidget(animationsLabel, 10, labelCol)

        self.gridLayout.addWidget(starttimeLabel, 10, lv1)
        self.gridLayout.addWidget(secondLabel, 10, lv2)
        self.gridLayout.addWidget(secondEdit, 10, lv3)
        self.gridLayout.addWidget(frameLabel, 11, lv2)
        self.gridLayout.addWidget(framEdit, 11, lv3)

        self.gridLayout.addWidget(durationLabel, 12, lv1)
        self.gridLayout.addWidget(secondLabel2, 12, lv2)
        self.gridLayout.addWidget(secondEdit2, 12, lv3)
        self.gridLayout.addWidget(frameLabel2, 13, lv2)
        self.gridLayout.addWidget(framEdit2, 13, lv3)

        self.gridLayout.addWidget(animationLabel, 14, labelCol)

        self.gridLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        dialog = QDialog()
        dialog.setLayout(self.gridLayout)
        self.setWidget(dialog)