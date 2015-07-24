# -*- coding: utf-8 -*-   
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
import json

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  

f = file('settings.json')
data = json.load(f)

class Settings(QDialog):
    def __init__(self,parent=None):  
        super(Settings,self).__init__(parent)
        self.setWindowTitle("Settings")
        self.resize(300,300)

        self.pathLabel = QLabel('Path')
        self.pathLabelText = QLabel(data['path'])
        self.pathButton = QPushButton('Change Path')

        self.actionLable = QLabel('Action')
        self.actionList = QComboBox()
        for action in data['actionList']:
            self.actionList.addItem(action)
        self.actionButton = QPushButton('Add/Delete Action')

        self.saveButton = QPushButton('Save')

        gridLayout=QGridLayout(self)

        gridLayout.addWidget(self.pathLabel, 1, 0)
        gridLayout.addWidget(self.pathLabelText, 1, 1)
        gridLayout.addWidget(self.pathButton, 1, 2)

        gridLayout.addWidget(self.actionLable, 2, 0)
        gridLayout.addWidget(self.actionList, 2, 1)
        gridLayout.addWidget(self.actionButton, 2, 2)

        gridLayout.addWidget(self.saveButton, 3, 2)

        self.connect(self.pathButton, SIGNAL('clicked()'), self.changePath)
        self.connect(self.actionButton, SIGNAL('clicked()'), self.addActionRewrite)
        self.connect(self.saveButton, SIGNAL('clicked()'), self.saveAll)

    def changePath(self):
        fname = QFileDialog.getExistingDirectory(self, 'open file')
        self.pathLabelText.setText(fname)

    def addActionRewrite(self):
        text, ok = QInputDialog().getText(self, 'Add/Delete Action', QString.fromUtf8('插入相同的动作即删除'))
        if ok:
            index = self.actionList.findText(text)
            if int(index) == -1:
                data['actionList'].append(str(text))
                self.actionList.addItem(text)
            else :
                data['actionList'].remove(str(text))
                self.actionList.removeItem(index)

    def saveAll(self):
        data['path'] = str(self.pathLabelText.text())
        json.dump(data, open('settings.json', 'w'))