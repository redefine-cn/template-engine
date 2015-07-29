#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import json
import os
from settings import Settings
from central_window import CentralWindow
from SettingDialog import SettingDialog
from uploader.uploader import Uploader
from animation import animation
from layer import layer
from subtitle import subtitle
from root import root
from part import part
from autodock import autodock
from plistIO.plistIO import read_plist, save_plist

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.central = list()
        self.loadData()
        self.initUI()
        self.resize(960, 540)

    def loadData(self):
        #load
        f = file('settings.json')
        self.data = json.load(f)
        f.close()

        # add default value
        if self.data["path"] == "":
            self.data["path"] = os.path.abspath(sys.path[0])

    def initUI(self):
        self.text = QTextEdit()
        #name
        self.setWindowTitle(QString.fromUtf8('Template-Engine'))
        #Splitter
        self.setSplitter()
        #Action
        self.createAction()
        #menu
        self.createMenu()
        #toolBar
        self.createToolBars()
        #statusBar
        self.statusBar()
        #DockWidget
        self.createDockWidget()
        #set Icon
        self.setWindowIcon(QIcon('../image/icon.png'))

    def createMenu(self):
        fileMenu = self.menuBar().addMenu(QString.fromUtf8("File"))
        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileCreateAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self.exitAction)

        editMenu = self.menuBar().addMenu(QString.fromUtf8("Settings"))
        editMenu.addAction(self.setting)

        # editMenu = self.menuBar().addMenu(QString.fromUtf8("Setting"))
        # editMenu.addAction(self.settingAction)

        ActionMenu = self.menuBar().addMenu('Action')
        ActionMenu.addAction(self.addNormalAction)
        ActionMenu.addAction(self.deleteAction)
        # editMenu.addAction(self.setting)
        # editMenu.addAction(self.cutAction)
        # editMenu.addAction(self.copyAction)
        # editMenu.addAction(self.pasteAction)

        helpMenu = self.menuBar().addMenu(QString.fromUtf8("About"))
        helpMenu.addAction(self.aboutAction)

        uploadMenu = self.menuBar().addMenu(QString.fromUtf8("Upload"))
        uploadMenu.addAction(self.uploadAction)

    def createAction(self):
        #打开文件
        self.fileOpenAction = QAction(QIcon("../image/icon.png"), QString.fromUtf8("Open"), self)
        self.fileOpenAction.setShortcut("Ctrl+O")
        self.fileOpenAction.setStatusTip(QString.fromUtf8("打开一个文件"))
        self.fileOpenAction.triggered.connect(self.slotOpenFile)

        #新建文件
        self.fileCreateAction = QAction(QString.fromUtf8("New"), self)
        self.fileCreateAction.setShortcut("Ctrl+N")
        self.fileCreateAction.setStatusTip(QString.fromUtf8("创建一个文件"))
        self.fileCreateAction.triggered.connect(self.slotCreateFile)

        #保存文件
        self.fileSaveAction = QAction(QString.fromUtf8("Save"), self)
        self.fileSaveAction.setShortcut("Ctrl+S")
        self.fileSaveAction.setStatusTip(QString.fromUtf8("保存当前文件"))
        self.fileSaveAction.triggered.connect(self.slotSaveFile)

        #退出
        self.exitAction = QAction(QString.fromUtf8("Exit"), self)
        self.exitAction.setShortcut("Ctrl+E")
        self.exitAction.setStatusTip(QString.fromUtf8("退出"))
        self.exitAction.triggered.connect(self.slotExit)



        #打开配置文件
        # self.settingAction = QAction(QString.fromUtf8("setting"), self)
        # # self.settingAction.setShortcut("Ctrl+O")
        # self.settingAction.setStatusTip(QString.fromUtf8("配置"))
        # self.settingAction.triggered.connect(self.slotSetting)

        #设置
        self.setting = QAction(QString.fromUtf8('设置'), self)
        self.setting.setShortcut('Ctrl+Alt+S')
        self.setting.setStatusTip(QString.fromUtf8('设置'))
        self.setting.triggered.connect(self.slotSetting)

        # Action
        self.addNormalAction = QAction('&add', self)
        self.addNormalAction.setShortcut('Ctrl+A')
        self.addNormalAction.triggered.connect(self.tab.currentWidget().addNormal)
        self.deleteAction = QAction('&delete', self)
        self.deleteAction.setShortcut('Ctrl+D')
        self.deleteAction.triggered.connect(self.tab.currentWidget().delete)

        #关于
        self.aboutAction = QAction(QString.fromUtf8("关于") ,self)
        self.aboutAction.setStatusTip(QString.fromUtf8("关于"))
        self.aboutAction.triggered.connect(self.slotAbout)

        self.uploadAction = QAction(QString.fromUtf8("上传模版") ,self)
        self.uploadAction.setStatusTip(QString.fromUtf8("上传模版文件"))
        self.uploadAction.triggered.connect(self.slotUpload)


    def createToolBars(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.fileOpenAction)
        fileToolBar.addAction(self.fileCreateAction)
        fileToolBar.addAction(self.fileSaveAction)

        editToolBar = self.addToolBar(QString.fromUtf8("Edit"))

    def createDockWidget(self):
        self.dock = autodock(self)
        self.dock.setMaximumSize(self.geometry().width()/3, self.geometry().height())
        self.dock.setMinimumSize(self.geometry().width()/4, self.geometry().height())
        self.dock.setFixedWidth(200)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

    def slotAbout(self):
        QMessageBox.about(self, QString.fromUtf8("About me"), QString.fromUtf8("欢迎使用本软件"))

    def slotUpload(self):
        self.uploadDialog = Uploader()
        # uploadDialog.show()

    def slotExit(self):
        self.close()

    def slotSaveFile(self):
        fileName = QFileDialog.getSaveFileName(self)
        if len(fileName) != 0:
            save_plist(unicode(fileName) + unicode('.plist'), str(self.tab.currentWidget().path))

    def slotCreateFile(self):
        central = CentralWindow()
        self.central.append(central)
        self.tab.addTab(self.central[len(self.central) - 1], 'Tab' + str(len(self.central)))

    def slotOpenFile(self):
        fileName = unicode(QFileDialog.getOpenFileName(self))
        data = {}
        file_json = read_plist(fileName)
        json_data = file(unicode('../tmp_data/') + file_json)
        # print file_json
        self.tab.currentWidget().path = unicode(file_json)
        data = json.load(json_data)
        # Check if window is not empty, create a new window
        if self.tab.currentWidget().root.childCount() != 0:
            self.slotCreateFile()
            self.tab.setCurrentWidget(self.central[len(self.central) - 1])
        for k, v in data.items():
            self.tab.currentWidget().dfs(v, self.tab.currentWidget().root, k, type(v), v)

    def loadFile(self, fileName):
        file = QFile(fileName)
        if file.open(QIODevice.ReadOnly|QIODevice.Text):
            textStream = QTextStream(file)
            while not textStream.atEnd():
                self.text.append(textStream.readLine())

    def slotSetting(self):
        settingDialog = SettingDialog(self)
        settingDialog.show()

    def setSplitter(self):
        mainSplitter = QSplitter(Qt.Horizontal, self)

        self.leftList = QListWidget(mainSplitter)
        mainSplitter.setStretchFactor(0, 1)
        self.setLeftList()
        self.tab = QTabWidget(mainSplitter)
        central = CentralWindow()
        self.central.append(central)
        self.tab.addTab(self.central[len(self.central) - 1], 'Tab' + str(len(self.central)))
        mainSplitter.setStretchFactor(1, 3)
        mainSplitter.setWindowTitle(QString.fromUtf8("分割窗口"))
        self.setCentralWidget(mainSplitter)

    def setLeftList(self):
        dir = QDir(self.data["path"])
        dir.setFilter(QDir.Dirs|QDir.NoDot|QDir.NoDotDot)
        list = dir.entryList()
        self.leftList.clear()
        for i in xrange(len(list)):
            self.leftList.addItem(QListWidgetItem(list[i]))

        self.leftList.itemDoubleClicked.connect(self.slotList)

    def slotList(self, item):
        
        # name = item.text()
        # fileName = unicode(self.data["path"]) + unicode("/") + unicode(name) + unicode("/") + unicode(name) + unicode('.plist')
        # data = {}
        # file_json = unicode(read_plist(fileName))
        # json_data = file(unicode('../tmp_data/') + file_json)
        # # print file_json
        # self.tab.currentWidget().path = unicode(file_json)
        # data = json.load(json_data)
        # # Check if window is not empty, create a new window
        # if self.tab.currentWidget().root.childCount() != 0:
        #     self.slotCreateFile()
        #     self.tab.setCurrentWidget(self.central[len(self.central) - 1])
        # for k, v in data.items():
        #     self.tab.currentWidget().dfs(v, self.tab.currentWidget().root, k, type(v), v)

    def resizeEvent(self, *args, **kwargs):
        # self.dock.setMinimumSize(self.geometry().width()/4, self.geometry().height())
        self.dock.setMaximumSize(self.geometry().width()/3, self.geometry().height())

if __name__ == '__main__':
    dic11 = {"dict": {"backgroundImage": "run01bg0001.png", "animation1": {"values": [{"y": 1.1, "x": 105}, {"y": 105, "x": 105}, {"y": 100, "x": 100}], "name": "scale", "starttime": {"second": 0, "frame": 0}}, "starttime": {"second": 0, "frame": 0}}}
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())



