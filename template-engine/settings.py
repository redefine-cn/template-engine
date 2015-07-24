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
        self.label=QLabel("Settings")

        self.pathLabel = QLabel('Path')
        self.pathLabelText = QLabel(data['path'])
        self.pathButton = QPushButton('Change Path')

        self.actionLable = QLabel('Action')
        self.actionList = QComboBox()
        for action in data['actionList']:
            self.actionList.addItem(action)
        self.actionButton = QPushButton('Add Action')

        gridLayout=QGridLayout(self)
        gridLayout.addWidget(self.label,0,0,1,3)

        gridLayout.addWidget(self.pathLabel, 1, 0)
        gridLayout.addWidget(self.pathLabelText, 1, 1)
        gridLayout.addWidget(self.pathButton, 1, 2)

        gridLayout.addWidget(self.actionLable, 2, 0)
        gridLayout.addWidget(self.actionList, 2, 1)
        gridLayout.addWidget(self.actionButton, 2, 2)

        self.connect(self.pathButton, SIGNAL('clicked()'), self.changePath)
        self.connect(self.actionButton, SIGNAL('clicked()'), self.addActionRewrite)

    def changePath(self):
        fname = QFileDialog.getOpenFileName(self , 'open file')
        self.pathLabelText.setText(fname)
        #TODO write fname to json file

    def addActionRewrite(self):
        text, ok = QInputDialog().getText(self, 'Add Action', 'Action')
        if ok:
            # TODO write text to json file (actionList)
            self.actionList.addItem(text)
            # self.actionList.destroy()
