#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import  sys

class part(QDockWidget):
    def __init__(self):
        super(part, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑part"))
        self.setFeatures(QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        labelCol = 0
        contentCol = 1
        lv1 = 1
        lv2 = 2
        lv3 = 3

        partNameLabel = QLabel(QString.fromUtf8("partName"))
        partNameEdit = QLineEdit()

        minTimeLabel = QLabel(QString.fromUtf8("minTime"))
        minTimeSecondLable = QLabel(QString.fromUtf8("second"))
        minTimeSecondEdit = QLineEdit()
        minTimeFrameLabel = QLabel(QString.fromUtf8("frame"))
        minTimeFrameEdit = QLineEdit()

        maxTimeLabel = QLabel(QString.fromUtf8("maxTime"))
        maxTimeSecondLable = QLabel(QString.fromUtf8("second"))
        maxTimeSecondEdit = QLineEdit()
        maxTimeFrameLabel = QLabel(QString.fromUtf8("frame"))
        maxTimeFrameEdit = QLineEdit()

        previewImageLabel = QLabel(QString.fromUtf8("previewImage"))
        previewImageEdit = QLineEdit()

        overlayImageLabel = QLabel(QString.fromUtf8("overlayImage"))
        overlayImageEdit = QLineEdit()

        previewVideoLabel = QLabel(QString.fromUtf8("previewVideo"))
        previewVideoEdit = QLineEdit()

        subtitlesLabel = QLabel(QString.fromUtf8("subtitles"))

        gridLayout = QGridLayout()
        gridLayout.addWidget(partNameLabel, 0, labelCol)
        gridLayout.addWidget(partNameEdit, 0, contentCol)

        gridLayout.addWidget(minTimeLabel, 1, labelCol)
        gridLayout.addWidget(minTimeSecondLable, 1, lv1)
        gridLayout.addWidget(minTimeSecondEdit, 1, lv2)
        gridLayout.addWidget(minTimeFrameLabel, 2, lv1)
        gridLayout.addWidget(minTimeFrameEdit, 2, lv2)

        gridLayout.addWidget(maxTimeLabel, 3, labelCol)
        gridLayout.addWidget(maxTimeSecondLable, 3, lv1)
        gridLayout.addWidget(maxTimeSecondEdit, 3, lv2)
        gridLayout.addWidget(maxTimeFrameLabel, 4, lv1)
        gridLayout.addWidget(maxTimeFrameEdit, 4, lv2)

        gridLayout.addWidget(previewImageLabel, 5, labelCol)
        gridLayout.addWidget(previewImageEdit, 5, contentCol)
        gridLayout.addWidget(overlayImageLabel, 6, labelCol)
        gridLayout.addWidget(overlayImageEdit, 6, contentCol)
        gridLayout.addWidget(previewVideoLabel, 7, labelCol)
        gridLayout.addWidget(previewVideoEdit, 7, contentCol)

        gridLayout.addWidget(subtitlesLabel, 8, labelCol)
        self.gridLayout = gridLayout
        self.gridLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        dialog = QDialog()
        dialog.setLayout(self.gridLayout)
        self.setWidget(dialog)
