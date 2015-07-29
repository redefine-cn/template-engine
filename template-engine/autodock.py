#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json
import  sys
from functools import partial


class autodock(QDockWidget):
    def __init__(self, parent=None):
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
        self.index = {}
        self.gridLayout = QGridLayout()
        self.dialog = QDialog()
        self.updateUI(None)

    def addValue(self, key, tp, value, treeNode):

        labelEdit = QLineEdit()
        labelEdit.setText(key)

        combobox = QComboBox()
        for i in range(len(self.types)):
            combobox.addItem(QString.fromUtf8(self.types[i]))
            if tp == self.types[i]:
                combobox.setCurrentIndex(i)

        self.gridLayout.addWidget(labelEdit, self.row, self.labelCol)
        self.gridLayout.addWidget(combobox, self.row, self.typeCol)

        combobox.currentIndexChanged[int].connect(partial(self.slotCombobox, treeNode))

        if tp != "dict":
            edit = QLineEdit()
            edit.setText(value)
            self.gridLayout.addWidget(edit, self.row, self.contentCol)

        self.row += 1

    def slotCombobox(self, treeNode, index):
        treeNode.setText(1, QString.fromUtf8(self.types[index]))

    def updateUI(self, data):

        if not data:
            return

        if self.gridLayout :
            del self.gridLayout
            self.gridLayout = None

        if self.dialog :
            del self.dialog
            self.dialog = None

        if self.index :
            del self.index
            self.index = {}

        self.gridLayout = QGridLayout()
        self.gridLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        self.row = 0
        self.data = data
        if data.childCount() == 0:
            self.addValue(data.text(0), data.text(1), data.text(2), data)
        else:
            for i in range(data.childCount()):
                # self.index = i
                self.addValue(data.child(i).text(0), data.child(i).text(1), data.child(i).text(2), data.child(i))

        buttonLayout = QHBoxLayout()
        button = QPushButton(QString.fromUtf8("保存"))
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(button)
        buttonLayout.setAlignment(Qt.AlignCenter)

        self.gridLayout.addLayout(buttonLayout, self.row, self.labelCol, 1, 3)
        self.dialog = QDialog()
        self.dialog.setLayout(self.gridLayout)
        self.setWidget(self.dialog)




