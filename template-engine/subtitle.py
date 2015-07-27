#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import  sys

class subtitle(QDockWidget):
    def __init__(self):
        super(subtitle, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑Subtitle"))
        self.setFeatures(QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        labelCol = 0
        contentCol = 1
        lv1 = 1
        lv2 = 2
        lv3 = 3

        textNameLabel = QLabel(QString.fromUtf8("textName"))
        textNameEdit = QLineEdit()
        fontNameLabel = QLabel(QString.fromUtf8("fontName"))
        fontNameEdit = QLineEdit()
        fontSizeLabel = QLabel(QString.fromUtf8("fontSize"))
        fontSizeEdit = QLineEdit()

        fontColorLabel = QLabel(QString.fromUtf8("fontColor"))
        fontColorRLable = QLabel(QString.fromUtf8("r"))
        fontColorREdit = QLineEdit()
        fontColorGLabel = QLabel(QString.fromUtf8("g"))
        fontColorGEdit = QLineEdit()
        fontColorBLabel = QLabel(QString.fromUtf8("b"))
        fontColorBEdit = QLineEdit()
        fontColorALabel = QLabel(QString.fromUtf8("a"))
        fontColorAEdit = QLineEdit()

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

        gridlayout = QGridLayout()
        gridlayout.addWidget(textNameLabel, 0, labelCol)
        gridlayout.addWidget(textNameEdit, 0, contentCol)
        gridlayout.addWidget(fontNameLabel, 1, labelCol)
        gridlayout.addWidget(fontNameEdit, 1, contentCol)
        gridlayout.addWidget(fontSizeLabel, 2, labelCol)
        gridlayout.addWidget(fontSizeEdit, 2, contentCol)
        gridlayout.addWidget(fontColorLabel, 3, labelCol)
        gridlayout.addWidget(fontColorRLable, 3, lv1)
        gridlayout.addWidget(fontColorREdit, 3, lv2)
        gridlayout.addWidget(fontColorGLabel, 4, lv1)
        gridlayout.addWidget(fontColorGEdit, 4, lv2)
        gridlayout.addWidget(fontColorBLabel, 5, lv1)
        gridlayout.addWidget(fontColorBEdit, 5, lv2)
        gridlayout.addWidget(fontColorALabel, 6, lv1)
        gridlayout.addWidget(fontColorAEdit, 6, lv2)
        gridlayout.addWidget(opacityLabel, 7, labelCol)
        gridlayout.addWidget(opacityEdit, 7, contentCol)
        gridlayout.addWidget(scaleLabel, 8, labelCol)
        gridlayout.addWidget(scaleXLable, 8, lv1)
        gridlayout.addWidget(scaleXEdit, 8, lv2)
        gridlayout.addWidget(scaleYLabel, 9, lv1)
        gridlayout.addWidget(scaleYEdit, 9, lv2)
        gridlayout.addWidget(anchorpointLabel, 10, labelCol)
        gridlayout.addWidget(anchorpointXLable, 10, lv1)
        gridlayout.addWidget(anchorpointXEdit, 10, lv2)
        gridlayout.addWidget(anchorpointYLabel, 11, lv1)
        gridlayout.addWidget(anchorpointYEdit, 11, lv2)
        gridlayout.addWidget(positionLabel, 12, labelCol)
        gridlayout.addWidget(positionXLable, 12, lv1)
        gridlayout.addWidget(positionXEdit, 12, lv2)
        gridlayout.addWidget(positionYLabel, 13, lv1)
        gridlayout.addWidget(positionYEdit, 13, lv2)
        gridlayout.addWidget(sizeLabel, 14, labelCol)
        gridlayout.addWidget(sizeWidthLable, 14, lv1)
        gridlayout.addWidget(sizeWidthEdit, 14, lv2)
        gridlayout.addWidget(sizeHeightLabel, 15, lv1)
        gridlayout.addWidget(sizeHeightEdit, 15, lv2)

        gridlayout.addWidget(animationsLabel, 16, labelCol)

        gridlayout.addWidget(starttimeLabel, 16, lv1)
        gridlayout.addWidget(secondLabel, 16, lv2)
        gridlayout.addWidget(secondEdit, 16, lv3)
        gridlayout.addWidget(frameLabel, 17, lv2)
        gridlayout.addWidget(framEdit, 17, lv3)

        gridlayout.addWidget(durationLabel, 18, lv1)
        gridlayout.addWidget(secondLabel2, 18, lv2)
        gridlayout.addWidget(secondEdit2, 18, lv3)
        gridlayout.addWidget(frameLabel2, 19, lv2)
        gridlayout.addWidget(framEdit2, 19, lv3)

        gridlayout.addWidget(animationLabel, 20, labelCol)
        self.gridLayout = gridlayout

        dialog = QDialog()
        dialog.setLayout(self.gridLayout)
        self.setWidget(dialog)