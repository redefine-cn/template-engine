#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import  sys

class root(QDockWidget):
    def __init__(self):
        super(root, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑root"))
        self.setFeatures(QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        labelCol = 0
        contentCol = 1
        lv1 = 1
        lv2 = 2
        lv3 = 3

        frameTimeLabel = QLabel(QString.fromUtf8("frameTime"))
        frameTimeSecondLable = QLabel(QString.fromUtf8("second"))
        frameTimeSecondEdit = QLineEdit()
        frameTimeFrameLabel = QLabel(QString.fromUtf8("frame"))
        frameTimeFrameEdit = QLineEdit()

        partLabel = QLabel(QString.fromUtf8("part"))

        gridlayout = QGridLayout()
        gridlayout.addWidget(frameTimeLabel, 0, labelCol)
        gridlayout.addWidget(frameTimeSecondLable, 0, lv1)
        gridlayout.addWidget(frameTimeSecondEdit, 0, lv2)
        gridlayout.addWidget(frameTimeFrameLabel, 1, lv1)
        gridlayout.addWidget(frameTimeFrameEdit, 1, lv2)

        gridlayout.addWidget(partLabel, 2, labelCol)

        self.gridLayout = gridlayout

        dialog = QDialog()
        dialog.setLayout(self.gridLayout)
        self.setWidget(dialog)