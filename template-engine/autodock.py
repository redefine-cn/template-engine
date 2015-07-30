#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json
import  sys
sys.path.append('../')
from plistIO.plistIO import modify
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

        self.row = -1
        self.labelCol = 0
        self.typeCol = 1
        self.contentCol = 2
        self.lv1 = 1
        self.lv2 = 2

        self.types = self.fa.data["Type"]
        self.gridLayout = QGridLayout()
        self.dialog = QDialog()
        self.updateUI(None)

    def addValue(self, key, tp, value, treeNode):
        self.row += 1
        labelEdit = QLineEdit()
        labelEdit.setText(key)
        key = unicode(key)
        tp = str(tp)
        value = unicode(value)

        combobox = QComboBox()

        if treeNode.childCount() != 0 or treeNode.parent() == None:
            combobox.addItem(tp)
        else:
            for i in range(len(self.types)):
                combobox.addItem(str(self.types[i]))
                if tp == str(self.types[i]):
                    combobox.setCurrentIndex(i)

        if treeNode.parent() == None:
            x = QLabel(key)
            self.gridLayout.addWidget(x, self.row, self.labelCol)
        else:
            self.gridLayout.addWidget(labelEdit, self.row, self.labelCol)
        self.gridLayout.addWidget(combobox, self.row, self.typeCol)

        labelEdit.textChanged[QString].connect(partial(self.slotlabelEdit, treeNode))
        combobox.currentIndexChanged[int].connect(partial(self.slotCombobox, treeNode))

        if tp != 'dict' and tp != 'array' and treeNode.parent() != None:
            if tp != 'bool':
                edit = QLineEdit()
                edit.setText(value)
                edit.textChanged[QString].connect(partial(self.slotValueEdit, treeNode))
                self.gridLayout.addWidget(edit, self.row, self.contentCol)
            else:
                box = QComboBox()
                box.addItem('True')
                box.addItem('False')
                if str(value) == 'True':
                    box.setCurrentIndex(0)
                else:
                    box.setCurrentIndex(1)
                box.currentIndexChanged[QString].connect(partial(self.slotValueEdit, treeNode))
                self.gridLayout.addWidget(box, self.row, self.contentCol)

    def slotlabelEdit(self, treeNode, text):
        node = {}
        node['PreKey'] = unicode(treeNode.text(0))
        treeNode.setText(0, text)
        node['Key'] = unicode(text)
        node['Type'] = str(treeNode.text(1))
        node['Value'] = unicode(treeNode.text(2))
        modify(treeNode.parent(), treeNode, node, self.parent().tab.currentWidget().path, self.parent().tab.currentWidget().root, 0)
        # self.updateUI(treeNode.parent())

    def slotCombobox(self, treeNode, index):
        treeNode.setText(1, QString.fromUtf8(self.types[index]))
        node = {}
        node['Key'] = unicode(treeNode.text(0))
        node['Type'] = str(self.types[index])
        if node['Type'] == 'dict' or node['Type'] == 'array':
            treeNode.setText(2, QString.fromUtf8(''))
        if node['Type'] == 'integer':
            try:
                node['Value'] = int(treeNode.text(2))
            except:
                node['Value'] = '1'
        elif node['Type'] == 'real':
            try:
                node['Value'] = float(treeNode.text(2))
            except:
                node['Value'] = '1.0'
        elif node['Type'] == 'bool':
            try:
                node['Value'] = str(treeNode.text(2))
            except:
                node['Value'] = 'True'
            if node['Value'] != 'True' and node['Value'] != 'False':
                node['Value'] = 'True'
        else:
            node['Value'] = unicode(treeNode.text(2))

        if treeNode.text(2) == QString.fromUtf8(''):
            treeNode.setText(2, unicode(node['Value']))
            edit = QLineEdit(treeNode.text(2))
            self.gridLayout.addWidget(edit, self.row, self.contentCol)
        treeNode.setText(2, unicode(node['Value']))
        modify(treeNode.parent(), treeNode, node, self.parent().tab.currentWidget().path, self.parent().tab.currentWidget().root, 1)
        # self.updateUI(treeNode.parent())

    def slotValueEdit(self, treeNode, text):
        treeNode.setText(2, text)
        node = {}
        node['Key'] = unicode(treeNode.text(0))
        node['Type'] = str(treeNode.text(1))
        node['Value'] = unicode(text)
        modify(treeNode.parent(), treeNode, node, self.parent().tab.currentWidget().path, self.parent().tab.currentWidget().root, 1)
        # self.updateUI(treeNode.parent())

    def updateUI(self, data):

        if self.gridLayout :
            del self.gridLayout
            self.gridLayout = None

        if self.dialog :
            del self.dialog
            self.dialog = None

        self.gridLayout = QGridLayout()
        self.gridLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        if data:
            self.row = 0
            self.data = data
            self.addValue(data.text(0), data.text(1), data.text(2), data)
            if data.childCount() != 0:
                for i in range(data.childCount()):
                    self.addValue(data.child(i).text(0), data.child(i).text(1), data.child(i).text(2), data.child(i))

        self.dialog = QDialog()
        self.dialog.setLayout(self.gridLayout)
        self.setWidget(self.dialog)

if __name__ == '__main__':
    print float('123')
