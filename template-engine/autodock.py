#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json
import  sys



class autodock(QDockWidget):
    def __init__(self, parent):
        super(autodock, self).__init__(parent)
        self.fa = parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑"))
        self.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        self.row = 0
        self.labelCol = 0
        self.typeCol = 1
        self.contentCol = 2
        self.lv1 = 1
        self.lv2 = 2

        self.types = self.fa.data["Type"]

        self.gridLayout = QGridLayout()
        self.dialog = QDialog()
        data = None
        self.updateUI(data)

    def addValue(self, key, tp, value):
        label = QLabel(key)
        combobox = QComboBox()
        for i in range(len(self.types)):
            combobox.addItem(QString.fromUtf8(self.types[i]))
            if tp == self.types[i]:
                combobox.setCurrentIndex(i)

        self.gridLayout.addWidget(label, self.row, self.labelCol)
        self.gridLayout.addWidget(combobox, self.row, self.typeCol)


        if tp != "dict":
            edit = QLineEdit()
            edit.setText(value)
            self.gridLayout.addWidget(edit, self.row, self.contentCol)

        self.row += 1


    def updateUI(self, data):

        if not data:
            return

        if self.gridLayout :
            del self.gridLayout
            self.gridLayout = None

        if self.dialog :
            del self.dialog
            self.dialog = None

        self.gridLayout = QGridLayout()
        self.gridLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        self.row = 0

        if data.childCount() == 0:
            self.addValue(data.text(0), data.text(1), data.text(2))
        else:
            for i in range(data.childCount()):
                self.addValue(data.child(i).text(0), data.child(i).text(1), data.child(i).text(2))

        self.dialog = QDialog()
        self.dialog.setLayout(self.gridLayout)
        self.setWidget(self.dialog)




