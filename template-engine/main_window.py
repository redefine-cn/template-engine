#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import json
import os
from functools import partial
from settings import Settings
from central_window import CentralWindow
from uploader.uploader import Uploader
from autodock import autodock
from plistIO.plistIO import read_plist, save_plist

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        if os.path.exists('../tmp_data') == False:
            os.mkdir('../tmp_data')
        self.central = list()
        self.waitWindow = QDialog(self)
        self.waitWindow.setWindowTitle(QString.fromUtf8('正在加载，请等候...'))
        self.waitWindow.resize(250,50)
        self.loadData()
        self.initUI()
        self.resize(960, 540)

    def loadData(self):
        #load
        f = file('../data/settings.json')
        self.data = json.load(f)
        f.close()

        # add default value
        if self.data["path"] == "":
            self.data["path"] = os.path.abspath(sys.path[0])

        #leftTree
        self.model = None
        self.leftTree = None

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
        self.setWindowIcon(QIcon('../data/icon.png'))

    def createMenu(self):
        fileMenu = self.menuBar().addMenu(QString.fromUtf8("文件"))
        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileCreateAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self.exitAction)

        ActionMenu = self.menuBar().addMenu(QString.fromUtf8('动作'))
        ActionMenu.addAction(self.addNormalAction)
        ActionMenu.addAction(self.deleteAction)
        ActionMenu.addAction(self.addLayer)
        ActionMenu.addAction(self.addSubtitle)
        ActionMenu.addAction(self.addSegment)
        ActionMenu.addAction(self.animation)

        uploadMenu = self.menuBar().addMenu(QString.fromUtf8("上传"))
        uploadMenu.addAction(self.uploadAction)

        editMenu = self.menuBar().addMenu(QString.fromUtf8("设置"))
        editMenu.addAction(self.setting)

        helpMenu = self.menuBar().addMenu(QString.fromUtf8("关于"))
        helpMenu.addAction(self.aboutAction)

        # 右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.contextMenu = ActionMenu

    def showContextMenu(self, pos):
        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()

    def createAction(self):
        #打开文件
        self.fileOpenAction = QAction(QString.fromUtf8("打开"), self)
        self.fileOpenAction.setShortcut("Ctrl+O")
        self.fileOpenAction.setStatusTip(QString.fromUtf8("打开一个文件"))
        self.fileOpenAction.triggered.connect(self.slotOpenFile)

        #新建文件
        self.fileCreateAction = QAction(QString.fromUtf8("新建"), self)
        self.fileCreateAction.setShortcut("Ctrl+N")
        self.fileCreateAction.setStatusTip(QString.fromUtf8("创建一个文件"))
        self.fileCreateAction.triggered.connect(self.slotCreateFile)

        #保存文件
        self.fileSaveAction = QAction(QString.fromUtf8("保存"), self)
        self.fileSaveAction.setShortcut("Ctrl+S")
        self.fileSaveAction.setStatusTip(QString.fromUtf8("保存当前文件"))
        self.fileSaveAction.triggered.connect(self.slotSaveFile)

        #退出
        self.exitAction = QAction(QString.fromUtf8("退出"), self)
        self.exitAction.setShortcut("Ctrl+E")
        self.exitAction.setStatusTip(QString.fromUtf8("退出"))
        self.exitAction.triggered.connect(self.slotExit)

        #设置
        self.setting = QAction(QString.fromUtf8('设置'), self)
        self.setting.setShortcut('Ctrl+Q')
        self.setting.setStatusTip(QString.fromUtf8('设置'))
        self.setting.triggered.connect(self.slotSetting)

        # Action
        self.addNormalAction = QAction('&Add', self)
        self.addNormalAction.setShortcut('Ctrl+A')
        self.addNormalAction.setStatusTip(QString.fromUtf8('添加节点'))
        self.addNormalAction.triggered.connect(self.tab.currentWidget().addNormal)

        self.deleteAction = QAction('&Delete', self)
        self.deleteAction.setShortcut('Ctrl+D')
        self.deleteAction.setStatusTip(QString.fromUtf8('删除节点'))
        self.deleteAction.triggered.connect(self.tab.currentWidget().delete)

        self.addLayer = QAction('&AddLayer', self)
        self.addLayer.setShortcut('Ctrl+1')
        self.addLayer.setStatusTip(QString.fromUtf8('添加Layer'))
        self.addLayer.triggered.connect(partial(self.tab.currentWidget().addSomething, 'layer_layer.json'))

        self.addSubtitle = QAction('&AddSubtitle', self)
        self.addSubtitle.setShortcut('Ctrl+2')
        self.addSubtitle.setStatusTip(QString.fromUtf8('添加Subtitle'))
        self.addSubtitle.triggered.connect(partial(self.tab.currentWidget().addSomething, 'subtitle_subtitle.json'))

        self.addSegment = QAction('&AddSegment', self)
        self.addSegment.setShortcut('Ctrl+3')
        self.addSegment.setStatusTip(QString.fromUtf8('添加Segment'))
        self.addSegment.triggered.connect(partial(self.tab.currentWidget().addSomething, 'segment_segment.json'))

        self.addStraightLine = QAction('&AddStraightLine', self)
        # self.addStraightLine.setShortcut('Ctrl+4')
        self.addStraightLine.setStatusTip(QString.fromUtf8('添加StraightLine'))
        self.addStraightLine.triggered.connect(partial(self.tab.currentWidget().addSomething, 'animation_straightline.json'))

        self.addOpacity = QAction('&AddOpacity', self)
        # self.addOpacity.setShortcut('Ctrl+5')
        self.addOpacity.setStatusTip(QString.fromUtf8('添加Opacity'))
        self.addOpacity.triggered.connect(partial(self.tab.currentWidget().addSomething, 'animation_opacity.json'))

        self.addRotate = QAction('&AddRotate', self)
        # self.addRotate.setShortcut('Ctrl+3')
        self.addRotate.setStatusTip(QString.fromUtf8('添加Rotate'))
        self.addRotate.triggered.connect(partial(self.tab.currentWidget().addSomething, 'animation_rotate.json'))

        self.addScale = QAction('&AddScale', self)
        # self.addScale.setShortcut('Ctrl+3')
        self.addScale.setStatusTip(QString.fromUtf8('添加Scale'))
        self.addScale.triggered.connect(partial(self.tab.currentWidget().addSomething, 'animation_scale.json'))

        self.addStill = QAction('&AddStill', self)
        # self.addStill.setShortcut('Ctrl+3')
        self.addStill.setStatusTip(QString.fromUtf8('添加Still'))
        self.addStill.triggered.connect(partial(self.tab.currentWidget().addSomething, 'animation_still.json'))

        self.animation = QAction('&AddAnimation', self)
        self.animation.setStatusTip(QString.fromUtf8('添加Animation'))
        animationMenu = QMenu()
        animationMenu.addAction(self.addStill)
        animationMenu.addAction(self.addScale)
        animationMenu.addAction(self.addRotate)
        animationMenu.addAction(self.addOpacity)
        animationMenu.addAction(self.addStraightLine)
        self.animation.setMenu(animationMenu)

        #关于
        self.aboutAction = QAction(QString.fromUtf8("关于") ,self)
        self.aboutAction.setStatusTip(QString.fromUtf8("关于"))
        self.aboutAction.triggered.connect(self.slotAbout)

        # 上传文件
        self.uploadAction = QAction(QString.fromUtf8("上传模版") ,self)
        self.uploadAction.setShortcut('Ctrl+U')
        self.uploadAction.setStatusTip(QString.fromUtf8("上传模版文件"))
        self.uploadAction.triggered.connect(self.slotUpload)

    def createToolBars(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.setIconSize(QSize(100, 50))
        fileToolBar.addAction(self.fileOpenAction)
        fileToolBar.addAction(self.fileCreateAction)
        fileToolBar.addAction(self.fileSaveAction)

        addJsonToolBar = self.addToolBar(QString.fromUtf8("addJson"))
        addJsonToolBar.addAction(self.addNormalAction)
        addJsonToolBar.addAction(self.deleteAction)
        addJsonToolBar.addAction(self.addLayer)
        addJsonToolBar.addAction(self.addSubtitle)
        addJsonToolBar.addAction(self.addSegment)
        addJsonToolBar.addAction(self.animation)

    def createDockWidget(self):
        self.dock = autodock(self)
        self.dock.setMaximumSize(self.geometry().width()/3, self.geometry().height())
        self.dock.setMinimumSize(self.geometry().width()/4, self.geometry().height())
        self.dock.setFixedWidth(250)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

    def slotAbout(self):
        QMessageBox.about(self, QString.fromUtf8("About me"), QString.fromUtf8("欢迎使用本软件"))

    def slotUpload(self):
        self.uploadDialog = Uploader()
        # uploadDialog.show()

    def slotExit(self):
        self.close()

    def slotSaveFile(self):
        fileName = QFileDialog.getSaveFileName(self, QString.fromUtf8('另存为'), self.tr(''), self.tr('*.plist'))
        if len(fileName) != 0:
            save_plist(unicode(fileName), unicode(self.tab.currentWidget().path))

    def slotCreateFile(self):
        central = CentralWindow()
        self.central.append(central)
        self.tab.addTab(self.central[-1], 'Tab' + str(len(self.central)))
        self.tab.setCurrentWidget(self.central[-1])

    def slotOpenFile(self):
        fileName = unicode(QFileDialog.getOpenFileName(self, QString.fromUtf8('打开'), self.tr(''), self.tr('*.plist')))
        if len(fileName) == 0:
            return False
        file_json = read_plist(fileName)
        json_data = file(unicode('../tmp_data/') + file_json)
        if self.tab.currentWidget() == None:
            self.slotCreateFile()
        self.tab.currentWidget().path = unicode(file_json)
        data = json.load(json_data)
        # Check if window is not empty, create a new window
        if self.tab.currentWidget().root.childCount() != 0:
            self.slotCreateFile()
            self.tab.setCurrentWidget(self.central[-1])
        self.waitWindow.show()
        for k, v in data.items():
            self.tab.currentWidget().dfs(v, self.tab.currentWidget().root, k, type(v), v)
        self.waitWindow.close()

    def loadFile(self, fileName):
        file = QFile(fileName)
        if file.open(QIODevice.ReadOnly|QIODevice.Text):
            textStream = QTextStream(file)
            while not textStream.atEnd():
                self.text.append(textStream.readLine())

    def slotSetting(self):
        settings = Settings(self)
        settings.show()

    def setSplitter(self):
        mainSplitter = QSplitter(Qt.Horizontal, self)
        self.leftTree = QTreeView(mainSplitter)
        mainSplitter.setStretchFactor(0, 1)
        self.setLeftList()
        self.tab = QTabWidget(mainSplitter)
        central = CentralWindow()
        self.central.append(central)
        self.tab.addTab(self.central[-1], 'Tab' + str(len(self.central)))
        self.tab.setTabsClosable(True)
        self.tab.tabCloseRequested.connect(self.closeTab)
        mainSplitter.setStretchFactor(1, 3)
        mainSplitter.setWindowTitle(QString.fromUtf8("分割窗口"))
        self.setCentralWidget(mainSplitter)

    def closeTab(self):
        self.tab.removeTab(self.tab.currentIndex())

    def setLeftList(self):
        if not self.model:
            self.model = QDirModel()
            self.leftTree.setModel(self.model)
            self.leftTree.setRootIndex(self.model.index(self.data["path"]))
            self.leftTree.hideColumn(1)
            self.leftTree.hideColumn(2)
            self.leftTree.hideColumn(3)
            self.leftTree.doubleClicked.connect(self.slotList)
        else:
             self.leftTree.setRootIndex(self.model.index(self.data["path"]))

    def slotList(self, item):
        if not item.parent():
            return
        f = item.data().toString().split('.')
        if f[-1] != 'plist':
            return
        fileName = unicode(self.model.filePath(self.leftTree.selectedIndexes()[0]))
        file_json = unicode(read_plist(fileName))
        json_data = file(unicode('../tmp_data/') + file_json)
        # print file_json
        if self.tab.currentWidget() == None:
            self.slotCreateFile()
        self.tab.currentWidget().path = unicode(file_json)
        data = json.load(json_data)
        # Check if window is not empty, create a new window
        if self.tab.currentWidget().root.childCount() != 0:
            self.slotCreateFile()
            self.tab.setCurrentWidget(self.central[len(self.central) - 1])
        self.waitWindow.show()
        for k, v in data.items():
            self.tab.currentWidget().dfs(v, self.tab.currentWidget().root, k, type(v), v)
        self.waitWindow.close()

    def resizeEvent(self, *args, **kwargs):
        # self.dock.resize(self.geometry().width()/3, self.geometry().height())
        self.dock.setMaximumSize(self.geometry().width()/3, self.geometry().height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = main_window()
    mainWindow.show()
    sys.exit(app.exec_())



