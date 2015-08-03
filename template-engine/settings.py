# *-* coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import json

class Settings(QDialog):
    def __init__(self, parent):
        super(Settings, self).__init__(parent)
        self.data = parent.data
        self.InitUI()
        self.fa = parent

    def InitUI(self):
        self.setWindowTitle(QString.fromUtf8("设置"))
        self.resize(500, 200)
        labelCol = 0
        contentCol = 1
        buttonCol = 2

        baseLayout = QGridLayout()
        pathLabel = QLabel(QString.fromUtf8("路径："))
        self.pathEdit = QLineEdit()
        self.pathEdit.setText(QString.fromUtf8(self.data["path"]))
        choseButton = QPushButton(QString.fromUtf8("选择"))
        choseButton.clicked.connect(self.slotChosePath)
        chooseLabel = QLabel(QString.fromUtf8("动画："))
        self.choosebox = QComboBox()
        for itm in self.data["actionList"]:
            self.choosebox.addItem(QString.fromUtf8(itm))
        self.chooseAdd = QPushButton(QString.fromUtf8("添加"))
        self.chooseAdd.clicked.connect(self.slotchooseAdd)
        # TODO Here to Change settings.json

        saveButton = QPushButton(QString.fromUtf8("保存"))
        saveButton.clicked.connect(self.slotSave)

        cancelButton = QPushButton(QString.fromUtf8("取消"))
        cancelButton.clicked.connect(self.slotCancel)

        saveLayout = QHBoxLayout()
        saveLayout.addWidget(saveButton)
        saveLayout.addWidget(cancelButton)
        saveLayout.setAlignment(Qt.AlignRight)

        baseLayout.addWidget(pathLabel, 0, labelCol)
        baseLayout.addWidget(self.pathEdit, 0, contentCol)
        baseLayout.addWidget(choseButton, 0, buttonCol)
        baseLayout.addWidget(chooseLabel, 1, labelCol)
        baseLayout.addWidget(self.choosebox, 1, contentCol)
        baseLayout.addWidget(self.chooseAdd, 1, buttonCol)
        baseLayout.addLayout(saveLayout, 2, buttonCol, Qt.AlignRight)
        self.setLayout(baseLayout)

    def slotChosePath(self):
        folder = QFileDialog.getExistingDirectory(self, QString.fromUtf8("选择项目文件夹"), "..")
        folder.replace("\\", '/')
        if folder and not folder.isEmpty():
            self.pathEdit.setText(folder)
            path = folder.toUtf8().data()

            self.data["path"] = path
            json.dump(self.data, open('../data/settings.json','w'))

    def slotchooseAdd(self):
        choose_add = ChooseAddDialog(self)
        choose_add.show()
        json.dump(self.data, open('../data/settings.json','w'))

    def closeEvent(self, QCloseEvent):
        self.fa.setLeftList()

    def slotSave(self):
        self.fa.setLeftList()
        self.close()

    def slotCancel(self):
        self.close()

class ChooseAddDialog(QDialog):
    def __init__(self, parent):
        super(ChooseAddDialog, self).__init__(parent)
        self.data = parent.data
        self.setWindowTitle(QString.fromUtf8("添加新的动画"))

        self.addLabel = QLabel(QString.fromUtf8("请输入新的动画名称："))
        self.addText = QLineEdit()

        saveButton = QPushButton(QString.fromUtf8("保存"))
        saveButton.clicked.connect(self.slotSave)

        cancelButton = QPushButton(QString.fromUtf8("取消"))
        cancelButton.clicked.connect(self.slotCancel)

        saveLayout = QHBoxLayout()
        saveLayout.addWidget(saveButton)
        saveLayout.addWidget(cancelButton)
        saveLayout.setAlignment(Qt.AlignRight)

        baseLayout = QGridLayout()
        baseLayout.addWidget(self.addLabel, 0, 0)
        baseLayout.addWidget(self.addText, 0, 1)
        baseLayout.addLayout(saveLayout, 1, 2, Qt.AlignRight)
        self.setLayout(baseLayout)

    def slotSave(self):
        choose = unicode(self.addText.text())
        if choose == "":
            return
        self.parent().data["actionList"].append(choose)
        json.dump(self.data, open('../data/settings.json', 'w'))
        self.parent().choosebox.addItem(QString.fromUtf8(choose))
        self.close()

    def slotCancel(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Settings(None)
    mainWindow.show()
    sys.exit(app.exec_())