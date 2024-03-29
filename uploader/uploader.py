#coding=utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtNetwork
import file_upload
import json
from plistIO import plistIO
f = file('../data/settings.json')
data = json.load(f)
class Uploader(QDialog):
    def __init__(self, parent=None):
        super(Uploader, self).__init__()
        self.setWindowTitle(QString.fromUtf8("上传文件"))
        self.setWindowIcon(QIcon('../data/icon.png'))
        self.resize(600, 200)
        self.tab_upload = QTabWidget(self)
        # self.tab_upload.setTabsClosable(True)
        self.tab_http = QWidget()
        self.tab_ftp = QWidget()
        # self.tab_http.resize(500, 500)

        self.ip = QLabel(QString.fromUtf8("IP地址"))
        self.ip_line = QLineEdit("http://123.57.206.52/upload_videoScript/")
        self.file = QLabel(QString.fromUtf8("文件"))
        self.file_info = QLabel()
        self.file_select = QPushButton(QString.fromUtf8("上传本地文件"))
        self.file_select_current = QPushButton(QString.fromUtf8("上传当前模版"))
        self.file_cover = QLabel(QString.fromUtf8("封面"))
        self.file_cover_info = QLabel()
        self.file_cover_select = QPushButton(QString.fromUtf8("选择封面"))
        self.check_cover_btn = QCheckBox(QString.fromUtf8("是否上传封面"))
        self.file_name = QLabel(QString.fromUtf8("文件名称"))
        self.file_name_line = QLineEdit()
        self.btn_upload = QPushButton(QString.fromUtf8("上传"))
        self.btn_success = QPushButton(QString.fromUtf8("完成"))
        self.btn_cancel = QPushButton(QString.fromUtf8("取消"))
        # self.http_choice = QComboBox()
        # self.http_choice.addItem(QString.fromUtf8("直接上传"))
        # self.http_choice.addItem(QString.fromUtf8("登录系统并上传"))
        self.http_login = QPushButton(QString.fromUtf8("登录服务器"))
        self.http_choice_server = QComboBox()
        for k, v in data["server"].items():
            if k != 'choice':
                self.http_choice_server.addItem(k)
        # self.http_choice_server.addItem(QString.fromUtf8("developer"))
        # self.http_choice_server.addItem(QString.fromUtf8("production"))
        # self.http_choice_server.addItem(QString.fromUtf8("production"))
        self.http_progressBar = QProgressBar()
        self.http_upload_tip = QLabel()
        http_grid_layout = QGridLayout(self.tab_http)
        http_grid_layout.addWidget(self.ip, 0, 0)
        http_grid_layout.addWidget(self.ip_line, 0, 1)
        # http_grid_layout.addWidget(self.http_choice, 0, 4)
        http_grid_layout.addWidget(self.http_login, 0, 4)
        http_grid_layout.addWidget(self.http_choice_server, 0, 5)
        http_grid_layout.addWidget(self.file, 2, 0)
        http_grid_layout.addWidget(self.file_info, 2, 1)
        http_grid_layout.addWidget(self.file_select_current, 2, 4)
        http_grid_layout.addWidget(self.file_select, 2, 5)
        http_grid_layout.addWidget(self.file_name, 3, 0)
        http_grid_layout.addWidget(self.file_name_line, 3, 1)
        http_grid_layout.addWidget(self.check_cover_btn, 3, 4)
        http_grid_layout.addWidget(self.file_cover, 4, 0)
        http_grid_layout.addWidget(self.file_cover_info, 4, 1)
        http_grid_layout.addWidget(self.file_cover_select, 4, 5)
        http_grid_layout.addWidget(self.http_progressBar, 5, 0, 1, 5)
        http_grid_layout.addWidget(self.http_upload_tip, 5, 1)
        http_grid_layout.addWidget(self.btn_upload, 6, 4)
        http_grid_layout.addWidget(self.btn_success, 6, 4)
        http_grid_layout.addWidget(self.btn_cancel, 6, 5)

        self.ftp_ip = QLabel(QString.fromUtf8("IP地址"))
        self.ftp_ip_line = QLineEdit()
        self.ftp_file = QLabel(QString.fromUtf8("文件"))
        self.ftp_file_info = QLabel(QString.fromUtf8(""))
        self.ftp_file_select = QPushButton(QString.fromUtf8("选择文件"))
        self.ftp_username = QLabel(QString.fromUtf8("用户名"))
        self.ftp_username_line = QLineEdit(QString.fromUtf8(""))
        self.ftp_password = QLabel(QString.fromUtf8("密码"))
        self.ftp_password_line = QLineEdit()
        self.ftp_password_line.setEchoMode(QLineEdit.Password)
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
        self.file_cover.hide()
        self.file_cover_info.hide()
        self.file_cover_select.hide()
        self.btn_success.hide()
        self.tab_upload.addTab(self.tab_http, "http")
        self.tab_upload.addTab(self.tab_ftp, "FTP")
        layout = QHBoxLayout(self)
        layout.addWidget(self.tab_upload)

        self.connect(self.file_select, SIGNAL("clicked()"), self.http_fileSelect)
        self.connect(self.file_select_current, SIGNAL("clicked()"), self.http_fileSelect_current)
        self.connect(self.file_cover_select, SIGNAL("clicked()"), self.http_fileCoverSelect)
        self.connect(self.ftp_file_select, SIGNAL("clicked()"), self.ftp_fileSelect)
        self.connect(self.btn_cancel, SIGNAL("clicked()"), self.close)
        self.connect(self.ftp_btn_cancel, SIGNAL("clicked()"), self.close)
        self.connect(self.btn_upload, SIGNAL("clicked()"), self.http_upload)
        self.connect(self.ftp_btn_upload, SIGNAL("clicked()"), self.ftp_upload)
        # self.http_choice.currentIndexChanged.connect(self.choose_style)
        self.connect(self.http_login, SIGNAL("clicked()"), self.htpp_login_action)
        self.http_choice_server.currentIndexChanged.connect(self.choose_server)
        self.connect(self.tab_upload, SIGNAL("tabCloseRequested(int)"), self.closeTab)
        self.connect(self.check_cover_btn, SIGNAL("stateChanged(int)"), self.choose_cover)
        self.connect(self.btn_success, SIGNAL("clicked()"), self.close)
        self.show()

    def http_fileSelect_current(self):
        file_path = "C:\Users\Administrator\Desktop\models\蔚蓝之境"
        path = file_upload.get_file_directory(file_path)
        data["current_directory_path"] = unicode(path)
        self.zip_file = ZipFile(self)

    def http_fileCoverSelect(self):
        select = QFileDialog.getOpenFileName(self, QString.fromUtf8("选择需要上传的封面文件"), self.tr("*.png"))
        self.file_cover_info.setText(select)

    def choose_cover(self):
        if self.check_cover_btn.isChecked():
            self.file_cover.show()
            self.file_cover_info.show()
            self.file_cover_select.show()
        else:
            self.file_cover.hide()
            self.file_cover_info.hide()
            self.file_cover_select.hide()

    def closeTab(self):
        #关闭标签
        i = self.tab_upload.currentIndex()  #获取当前处于激活状态的标签
        self.tab_upload.removeTab(i)

    def choose_style(self):
        current_index = (self.http_choice.currentIndex())
        print current_index
        if current_index == 1:
            self.login_window = Login()
            # self.Window = Login()
        else:
            pass

    def htpp_login_action(self):
        self.login_window = Login()

    def choose_server(self):
        # current_index = self.http_choice_server.currentIndex()
        current_server = unicode(self.http_choice_server.currentText())
        print current_server
        if current_server == u"developer":
            data["server"]["choice"] = unicode(current_server)
            self.ip_line.setText(data["server"][data["server"]["choice"]]["upload_ip"])
        else:
            data["server"]["choice"] = unicode(current_server)
            self.ip_line.setText(data["server"][data["server"]["choice"]]["upload_ip"])

    def http_fileSelect(self):
        select = QFileDialog.getOpenFileName(self, QString.fromUtf8("选择需要上传的文件"), self.tr("*.zip"))
        select_len = len(str(QString.fromUtf8(select)).split('/'))
        self.file_info.setText(select)
        self.file_name_line.setText(QString.fromUtf8("请输入文件名"))

    def ftp_fileSelect(self):
        select = QFileDialog.getOpenFileName(self, "select file")
        self.ftp_file_info.setText(select)

    def http_upload(self):
        OK = '确定'
        ip_val = self.ip_line.text()
        file_val = self.file_info.text()
        file_name = self.file_name_line.text()
        cover_val = self.file_cover_info.text()
        if ip_val == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('IP为空，请填写IP地址'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            return
        if file_val == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('请选择文件'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            return
        if self.check_cover_btn.isChecked() and cover_val == "":
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('请选择封面文件'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8(OK), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            return
        # self.thread = MyThread()
        # self.thread.setIdentity("thread1")
        # self.thread.sinOut.connect(self.outText)
        # self.thread.setVal(100)
        try:
            if self.login_window.login_status == "success":
                pass
            else:
                self.login_window = Login()
                return
        except:
            self.login_window = Login()
            return
        # return
        self.http_progressBar.setMinimum(0)
        self.http_progressBar.setMaximum(20)
        for i in range(4):
            self.http_progressBar.setValue(i)
            QThread.msleep(200)
        # QThread.msleep(2000)
        # self.http_upload_tip.setText(u"正在上传...")
        # QThread.sleep(2000)
        result = file_upload.http_upload(str(QString.fromUtf8(ip_val)), unicode(file_val),  unicode(file_name))
        return_id = 0
        try:
            return_id = int(result)
            if self.check_cover_btn.isChecked():
                ip_val = data["server"][data["server"]["choice"]]["cover_ip"]
                result = file_upload.http_upload(ip_val, unicode(file_val), unicode(file_name), unicode(cover_val),
                                                 return_id)
            for i in range(4, 21):
                self.http_progressBar.setValue(i)
                QThread.msleep(200)
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('上传成功'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8("ok"), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            self.btn_upload.hide()
            self.btn_success.show()
        except:
            message = QMessageBox(self)
            message.setText(result)
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8("ok"), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            self.http_progressBar.setValue(0)

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
        ip_val = self.ip_line.text()
        file_val = self.file_info.text()
        self.http = QtNetwork.QHttp(parent=self)
        # 绑定 done 信号
        self.http.done.connect(self.on_req_done)
        self.http.responseHeaderReceived.connect(self.on_response_header)
        # http://101.200.0.168/upload_videoScript
        self.url = QUrl(ip_val)
        # 设置主机
        self.http.setHost(self.url.host(), self.url.port(80))
        # self.data = dict()
        # self.data['username'] = "test"
        # self.data['pwd'] = "pwdtest"
        self.data = QByteArray()
        self.data.append("uusername")

        print self.data
        self.getId = self.http.post(self.url.path(), self.data)
        self.manager = QtNetwork.QNetworkAccessManager(parent=self)
        # self.getId = self.manager.post(self.url.path(), self.data)
        self.req = QtNetwork.QNetworkRequest(self.url)
        self.manager.get(self.req)

    def on_response_header(self, response_header):
        print response_header.statusCode()
        if response_header.statusCode() in [301, 302]:
            location = response_header.value("Location")
            print "Redirect to: ", location
            self.getId = self.http.get(location)
            print self.getId
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
            # print self.http.readAll()
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

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle(QString.fromUtf8("用户登录"))
        self.resize(500, 200)
        self.setWindowIcon(QIcon('../data/icon.png'))
        self.init()

    def init(self):
        self.login_status = "error"
        self.ip_addr = QLabel(QString.fromUtf8("IP地址"))
        self.ip_addr_line = QLineEdit()
        self.username = QLabel(QString.fromUtf8("用户名"))
        self.password = QLabel(QString.fromUtf8("密码"))
        self.username_line = QLineEdit()
        self.password_line = QLineEdit()
        self.password_line.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(QString.fromUtf8("登录"))
        self.cancel_btn = QPushButton(QString.fromUtf8("取消"))
        grid_layout = QGridLayout(self)
        grid_layout.addWidget(self.ip_addr, 0, 0)
        grid_layout.addWidget(self.ip_addr_line, 0, 1)
        grid_layout.addWidget(self.username, 1, 0)
        grid_layout.addWidget(self.username_line, 1, 1)
        grid_layout.addWidget(self.password, 2, 0)
        grid_layout.addWidget(self.password_line, 2, 1)
        grid_layout.addWidget(self.login_btn, 5, 3)
        grid_layout.addWidget(self.cancel_btn, 5, 4)
        self.connect(self.login_btn, SIGNAL("clicked()"), self.login)
        self.connect(self.cancel_btn, SIGNAL("clicked()"), self.close)
        self.show()
        self.ip_addr_line.setText(data["server"][data["server"]["choice"]]["login_ip"])

    def login(self):
        ip = str(self.ip_addr_line.text())
        username = str(self.username_line.text())
        password = self.password_line.text()
        print username, password, ip
        result = file_upload.login_session(username, password, ip)
        if result == "success":
            self.login_status = "success"
            message = QMessageBox(self)
            message.setText(QString.fromUtf8('登陆成功'))
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8("ok"), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()
            if response == "ok":
                self.window().close()
                # self.window = Uploader()
        else:
            self.login_status = "failure"
            message = QMessageBox(self)
            message.setText(result)
            message.setWindowTitle(QString.fromUtf8('提示'))
            message.setIcon(QMessageBox.Warning)
            message.addButton(QString.fromUtf8("ok"), QMessageBox.AcceptRole)
            message.exec_()
            response = message.clickedButton().text()

class ZipFile(QDialog):
    def __init__(self, father):
        super(ZipFile, self).__init__()
        self.father = father
        self.setWindowTitle(QString.fromUtf8("正在压缩..."))
        self.setWindowIcon(QIcon("../data/icon.png"))
        self.resize(300, 50)
        self.zip_title = QLabel(QString.fromUtf8("正在压缩"))
        self.progress_bar = QProgressBar()
        self.path = ""
        grid_layout = QGridLayout(self)
        grid_layout.addWidget(self.zip_title, 0, 0)
        grid_layout.addWidget(self.progress_bar, 0, 1)
        self.show()
        self.ziping()

    def ziping(self):
        print "ziping...", data["current_directory_path"]
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(10)
        for i in range(4):
            self.progress_bar.setValue(i)
            QThread.msleep(200)
        zip_file_path = file_upload.zip_directory(data["current_directory_path"])
        for i in range(4, 11):
            self.progress_bar.setValue(i)
            QThread.msleep(200)
        self.father.file_info.setText(zip_file_path)
        self.father.file_name_line.setText(QString.fromUtf8("请输入文件名"))
        self.window().close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uploader = Uploader()
    uploader.show()
    app.exec_()