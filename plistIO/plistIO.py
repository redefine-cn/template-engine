# -*- coding=utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import codecs
from os.path import isfile
import json
from plistlib import *
f = file('../template-engine/settings.json')
data = json.load(f)

class PlistIO(QDialog):
    def __init__(self):
        super(PlistIO, self).__init__()
        self.setWindowTitle("update_plist")
        self.resize(200, 100)
        grid_layout = QGridLayout()
        button1 = QPushButton("update_plist_file")
        button2 = QPushButton("read_plist_file")
        grid_layout.addWidget(button1, 0, 0, 1, 1)
        grid_layout.addWidget(button2, 1, 0, 1, 1)
        self.setLayout(grid_layout)
        QObject.connect(button1, SIGNAL("clicked()"), self.update_plist)
        QObject.connect(button2, SIGNAL("clicked()"), self.read_plist)

    def update_plist(self):
        OK = "ok"
        writePlist(data, "c:/zhaolong/test.xml")
        message = QMessageBox(self)
        message.setText(QString.fromUtf8('ok,更新成功'))
        message.setWindowTitle(QString.fromUtf8('提示'))
        message.setIcon(QMessageBox.Warning)
        message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
        message.exec_()
        response = message.clickedButton().text()

    def read_plist(self):
        pl = readPlist("c:/zhaolong/test.xml")
        print pl
        json.dump(pl, open('../template-engine/settings.json', 'w'))
        message = QMessageBox(self)
        message.setText(QString.fromUtf8('ok,数据以Json数据存至json文件'))
        message.setWindowTitle(QString.fromUtf8('提示'))
        message.setIcon(QMessageBox.Warning)
        message.addButton(QString.fromUtf8("ok"), QMessageBox.AcceptRole)
        message.exec_()
        response = message.clickedButton().text()

app = QApplication(sys.argv)
my_window = PlistIO()
my_window.show()
# print data
app.exec_()
