#coding=utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtNetwork
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
        self.http_progressBar = QProgressBar()
        self.btn_upload = QPushButton(QString.fromUtf8("上传"))
        self.btn_cancel = QPushButton(QString.fromUtf8("取消"))
        http_grid_layout = QGridLayout(self.tab_http)
        http_grid_layout.addWidget(self.ip, 0, 0)
        http_grid_layout.addWidget(self.ip_line, 0, 1)
        http_grid_layout.addWidget(self.file, 1, 0)
        http_grid_layout.addWidget(self.file_info, 1, 1)
        http_grid_layout.addWidget(self.file_select, 1, 5)
        http_grid_layout.addWidget(self.http_progressBar, 2, 0, 1, 5)
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
        self.connect(self.btn_upload, SIGNAL("clicked()"), self.link_url)
        self.connect(self.ftp_btn_upload, SIGNAL("clicked()"), self.ftp_upload)

    def http_fileSelect(self):
        select = QFileDialog.getOpenFileName(self, QString.fromUtf8("选择需要上传的文件"), self.tr("Image Files(*.png *.jpg *.bmp)"))
        select = QFileDialog.get
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

        self.http_progressBar.setMinimum(0)
        self.http_progressBar.setMaximum(20)
        for i in range(21):
            self.http_progressBar.setValue(i)
            QThread.msleep(200)

        self.thread = MyThread()
        self.thread.setIdentity("thread1")
        self.thread.sinOut.connect(self.outText)
        self.thread.setVal(100)
        print file_upload.http_upload(file_val, ip_val)

    def outText(self, text):
        print(text)

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

    def link_url(self):
        self.http = QtNetwork.QHttp(parent=self)
        # 绑定 done 信号
        self.http.done.connect(self.on_req_done)
        self.http.responseHeaderReceived.connect(self.on_response_header)
        self.url = QUrl("http://101.200.0.168/upload_videoScript")
        # 设置主机
        self.http.setHost(self.url.host(), self.url.port(80))
        self.data = QByteArray()

        self.data.append("username")
        self.data.append("password")
        print self.data
        self.getId = self.http.post(self.url.path(), self.data)
        self._cookiejar = QtNetwork.QNetworkCookieJar(parent=self)
        # self.configuration = QtNetwork.QNetworkConfiguration()
        # self._sessionjar = QtNetwork.QNetworkSession(self.configuration, parent=self)
        self.manager = QtNetwork.QNetworkAccessManager(parent=self)
        self.manager.setCookieJar(self._cookiejar)
        self.manager.finished.connect(self.on_reply)
        self.req = QtNetwork.QNetworkRequest(self.url)
        self.manager.get(self.req)

    def on_reply(self, reply):
        print reply, self._cookiejar.allCookies()
        print reply.rawHeaderList()[0]
        # print QByteArray('Server')
        # print reply.readAll()

    def on_response_header(self, response_header):
        print response_header.statusCode()
        if response_header.statusCode() in [301, 302]:
            location = response_header.value("Location")
            print "Redirect to: ", location
            self.getId = self.http.get(location)
            tmp = QUrl(location)
            if str(tmp.host()):
                self.url = tmp
                self.http.setHost(self.url.host(), self.url.port(80))
            else:
                self.url.setPath(location)
            self.http.get(self.url.path() or "/")
        elif response_header.statusCode() in [404, 500]:
            print "upload failure"
        elif response_header.statusCode() == 200:
            print "fine it is ok"

    def on_req_done(self, error):
        print error
        if not error:
            print "Success"
            print self.http.readAll()
        else:
            print "Error"

class MyThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
        self.identity = None

    def setIdentity(self, text):
        self.identity = text

    def setVal(self, val):
        self.times = int(val)
        ##执行线程的run方法
        self.start()

    def run(self):
        while self.times > 0 and self.identity:
            ##发射信号
            self.sinOut.emit(self.identity+" "+str(self.times))
            self.times -= 1
app = QApplication(sys.argv)
uploader = Uploader()
uploader.show()
app.exec_()