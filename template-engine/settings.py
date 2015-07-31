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

        baseLayout.addLayout(saveLayout, 1, buttonCol, Qt.AlignRight)

        self.setLayout(baseLayout)

    def slotChosePath(self):
        folder = QFileDialog.getExistingDirectory(self, QString.fromUtf8("选择项目文件夹"), "..")
        folder.replace("\\", '/')
        if folder and not folder.isEmpty():
            self.pathEdit.setText(folder)
            path = folder.toUtf8().data()

            self.data["path"] = path
            json.dump(self.data, open('../data/settings.json','w'))

    def closeEvent(self, QCloseEvent):
        self.fa.setLeftList()

    def slotSave(self):
        self.fa.setLeftList()
        self.close()

    def slotCancel(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Settings(None)
    mainWindow.show()
    sys.exit(app.exec_())