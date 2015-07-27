#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import  sys

class autodock(QDockWidget):
    def __init__(self):
        super(autodock, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑"))
        self.setFeatures(QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        self.row = 0
        self.labelCol = 0
        self.contentCol = 1
        self.lv1 = 1
        self.lv2 = 2

        self.gridLayout = QGridLayout()
        self.dialog = QDialog()
        data = {}
        self.updateUI(data)

    def addValue(self, key, value):
        label = QLabel(QString.fromUtf8(key))
        edit = QLineEdit()
        edit.setText(QString.fromUtf8(str(value)))
        self.gridLayout.addWidget(label, self.row, self.labelCol)
        self.gridLayout.addWidget(edit, self.row, self.contentCol)
        self.row += 1

    def updateUI(self, data):

        if self.gridLayout :
            del self.gridLayout
            self.gridLayout = None

        if self.dialog :
            del self.dialog
            self.dialog = None

        gridLayout = QGridLayout()
        self.gridLayout = gridLayout
        self.gridLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        self.row = 0
        for item in data:
            if type(data[item]) == dict:
                label = QLabel(QString.fromUtf8(item))
                gridLayout.addWidget(label, self.row, self.labelCol)
                self.row += 1
                itemDict = data[item]
                for i in itemDict:
                    self.addValue(i, itemDict[i])
            else:
                self.addValue(item, data[item])
        self.dialog = QDialog()
        self.dialog.setLayout(self.gridLayout)
        self.setWidget(self.dialog)




