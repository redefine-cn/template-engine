#coding=utf-8
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import json
from os import sep
import zipfile

class ZipUpload(QWidget):
    def __init__(self):
        super(ZipUpload, self).__init__()
        self.setWindowTitle(QString.fromUtf8("压缩并上传文件"))
        self.setWindowIcon(QIcon("../image/icon.png"))
        self.resize(600, 200)
        self.file_path = QLabel(QString.fromUtf8("压缩路径"))
        self.file_path_info = QLabel()
        self.file_path_choose = QPushButton(QString.fromUtf8("点击选择压缩路径"))
        grid_layout = QGridLayout(self)
        grid_layout.addWidget(self.file_path, 0, 0)
        grid_layout.addWidget(self.file_path_info, 0, 1, 1, 3)
        grid_layout.addWidget(self.file_path_choose, 0, 4)

        self.connect(self.file_path_choose, SIGNAL("clicked()"), self.zip_dir)

    def zip_dir(self):
        file_path = QFileDialog.getExistingDirectory(self, QString.fromUtf8("选择路径"),  "C:" + sep + "Users" +
                                sep + "Administrator" + sep + "Desktop" + sep + "models")
        print unicode(file_path)
        self.file_path_info.setText(file_path)
        z = zipfile.ZipFile(unicode(file_path) + unicode('/test_zip.zip'), 'w')
        filelist = []
        if os.path.isfile(file_path):
            filelist.append(file_path)
        else:
            for root, dirs, files in os.walk(unicode(file_path)):
                for name in files:
                    filelist.append(os.path.join(root, name))
        for tar in filelist:
            arcname = tar[len(file_path):]
            z.write(tar, arcname)
        z.close()
        print unicode(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    zip_upload = ZipUpload()
    zip_upload.show()
    app.exec_()