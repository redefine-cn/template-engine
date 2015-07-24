# *-* coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import json

class SettingDialog(QDialog):
    def __init__(self, parent):
        super(SettingDialog, self).__init__(parent)
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


        choseLabel1 = QLabel(QString.fromUtf8("选项1："))
        choseBox1 = QComboBox()
        choseBox1.addItem(QString.fromUtf8("男"))
        choseBox1.addItem(QString.fromUtf8("女"))


        choseLabel2 = QLabel(QString.fromUtf8("选项2："))
        choseEdit2 = QLineEdit()

        choseLabel3 = QLabel(QString.fromUtf8("选项3："))
        choseEdit3 = QLineEdit()

        baseLayout.addWidget(pathLabel, 0, labelCol)
        baseLayout.addWidget(self.pathEdit, 0, contentCol)
        baseLayout.addWidget(choseButton, 0, buttonCol)

        baseLayout.addWidget(choseLabel1, 1, labelCol)
        baseLayout.addWidget(choseBox1, 1, contentCol)

        baseLayout.addWidget(choseLabel2, 2, labelCol)
        baseLayout.addWidget(choseEdit2, 2, contentCol)

        baseLayout.addWidget(choseLabel3, 3, labelCol)
        baseLayout.addWidget(choseEdit3, 3, contentCol)

        self.setLayout(baseLayout)

    def slotChosePath(self):
        folder = QFileDialog.getExistingDirectory(self, QString.fromUtf8("选择项目文件夹"), "..")
        # path = QFileDialog.getOpenFileName(self, QString.fromUtf8("选择路径"), "..", " ", None, QFileDialog.ShowDirsOnly)
        if folder and not folder.isEmpty():
            self.pathEdit.setText(folder)
            self.data["path"] = folder.toUtf8().data()
            json.dump(self.data, open('settings.json','w'))

    def closeEvent(self, QCloseEvent):
        self.fa.setLeftList()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = SettingDialog(None)
    mainWindow.show()
    sys.exit(app.exec_())