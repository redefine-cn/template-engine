#coding=utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import file_upload
import codecs
from os.path import isfile
from plistIO import plistIO

class Uploader(QWidget):
    def __init__(self, parent=None):
        super(Uploader, self).__init__(parent)
        self.setWindowTitle(QString.fromUtf8("上传文件"))
        # self.resize(500, 200)
        self.tab_upload = QTabWidget(self)

        self.tab_http = QWidget()
        self.tab_ftp = QWidget()
        # self.tab_http.resize(500, 500)

        self.ip = QLabel(QString.fromUtf8("IP地址"))
        self.ip_line = QLineEdit()
        self.file = QLabel(QString.fromUtf8("文件"))
        self.file_info = QLabel(QString.fromUtf8("file_info"))
        self.file_select = QPushButton(QString.fromUtf8("选择文件"))
        self.btn_upload = QPushButton(QString.fromUtf8("上传"))
        self.btn_cancel = QPushButton(QString.fromUtf8("取消"))
        http_grid_layout = QGridLayout(self.tab_http)
        http_grid_layout.addWidget(self.ip, 0, 0)
        http_grid_layout.addWidget(self.ip_line, 0, 1)
        http_grid_layout.addWidget(self.file, 1, 0)
        http_grid_layout.addWidget(self.file_info, 1, 1)
        http_grid_layout.addWidget(self.file_select, 1, 5)
        http_grid_layout.addWidget(self.btn_upload, 3, 4)
        http_grid_layout.addWidget(self.btn_cancel, 3, 5)

        self.ftp_ip = QLabel(QString.fromUtf8("IP地址"))
        self.ftp_ip_line = QLineEdit()
        self.ftp_file = QLabel(QString.fromUtf8("文件"))
        self.ftp_file_info = QLabel(QString.fromUtf8(""))
        self.ftp_file_select = QPushButton(QString.fromUtf8("选择文件"))
        self.ftp_username = QLabel(QString.fromUtf8("用户名"))
        self.ftp_username_line = QLineEdit(QString.fromUtf8(""))
        self.ftp_password = QLabel(QString.fromUtf8("密码"))
        self.ftp_password_line = QLineEdit()
        self.ftp_btn_upload = QPushButton(QString.fromUtf8("上传"))
        self.ftp_btn_cancel = QPushButton(QString.fromUtf8("取消"))
        ftp_grid_layout = QGridLayout(self.tab_ftp)
        ftp_grid_layout.addWidget(self.ftp_ip, 0, 0)
        ftp_grid_layout.addWidget(self.ftp_ip_line, 0, 1)
        ftp_grid_layout.addWidget(self.ftp_file, 1, 0)
        ftp_grid_layout.addWidget(self.ftp_file_info, 1, 1)
        ftp_grid_layout.addWidget(self.ftp_file_select, 1, 5)
        ftp_grid_layout.addWidget(self.ftp_username, 2, 0)
        ftp_grid_layout.addWidget(self.ftp_username_line, 2, 1)
        ftp_grid_layout.addWidget(self.ftp_password, 3, 0)
        ftp_grid_layout.addWidget(self.ftp_password_line, 3, 1)
        ftp_grid_layout.addWidget(self.ftp_btn_upload, 4, 4)
        ftp_grid_layout.addWidget(self.ftp_btn_cancel, 4, 5)

        self.tab_upload.addTab(self.tab_http, "http")
        self.tab_upload.addTab(self.tab_ftp, "FTP")
        layout = QHBoxLayout(self)
        layout.addWidget(self.tab_upload)

        self.connect(self.file_select, SIGNAL("clicked()"), self.http_fileSelect)
        self.connect(self.ftp_file_select, SIGNAL("clicked()"), self.ftp_fileSelect)
        self.connect(self.btn_cancel, SIGNAL("clicked()"), self.close)
        self.connect(self.ftp_btn_cancel, SIGNAL("clicked()"), self.close)
        self.connect(self.btn_upload, SIGNAL("clicked()"), self.http_upload)
        self.connect(self.ftp_btn_upload, SIGNAL("clicked()"), self.ftp_upload)

    def http_fileSelect(self):
        select = QFileDialog.getOpenFileName(self, "select file")
        self.file_info.setText(select)

    def ftp_fileSelect(self):
        select = QFileDialog.getOpenFileName(self, "select file")
        self.ftp_file_info.setText(select)

    def http_upload(self):
        OK = '确定'
        ip_val = self.ip_line.text()
        file_val = self.file_info.text()
        if ip_val == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('IP为空，请填写IP地址'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            print unicode(ip_val)
            return
        if file_val == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('请选择文件'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            print unicode(file_val)
            return
        file_upload.http_upload(file_val, ip_val)

    def ftp_upload(self):
        OK = '确定'
        ip_val = self.ftp_ip_line.text()
        file_val = self.ftp_file_info.text()
        if ip_val == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('IP为空，请填写IP地址'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            print unicode(ip_val)
            return
        if file_val == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('请选择文件'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            print unicode(file_val)
            return
        username = self.ftp_username_line.text()
        password = self.ftp_password_line.text()
        if username == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('用户名不能为空'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8("ok"), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            return
        if password == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('密码不能为空'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8("ok"), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            return
        result = plistIO.ftp_login(username, password)
        if result == "success":
            file_upload.ftp_upload(file_val, ip_val, username, password)
        else:
            print "failure"
app = QApplication(sys.argv)
uploader = Uploader()
uploader.show()
app.exec_()