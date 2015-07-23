# coding=utf8
from PyQt4 import QtGui, QtCore
import sys
class TemplateEngine(QtGui.QMainWindow):
    def __init__(self):
        super(TemplateEngine, self).__init__()

        self.MainWidget = QtGui.QWidget()
        self.initWidget()
        self.MainWidgetLayout = QtGui.QVBoxLayout()
        self.initMenuBar()
        self.resize(960,540)
        self.setWindowTitle('Template-Engine')
        self.show()

    def initWidget(self):
        sub_layout = QtGui.QHBoxLayout()
        Q1 = QtGui.QLabel('segment')
        Q2 = QtGui.QLabel('string')
        Q3 = QtGui.QLabel('dict')
        sub_layout.addWidget(Q1)
        sub_layout.addWidget(Q2)
        sub_layout.addWidget(Q3)

        self.setCentralWidget(self.MainWidget)
        layout = QtGui.QVBoxLayout()
        layout.addChildLayout(sub_layout)
        self.MainWidgetLayout = layout
        self.MainWidget.setLayout(layout)
        # self.layout()
        # self.MainWidget.layout()

    def initMenuBar(self):
        # Exit Action
        exitAction = QtGui.QAction('&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close)
        # Open File Action
        openFileAction = QtGui.QAction('&open', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.setStatusTip('Open File')
        openFileAction.triggered.connect(self.openFile)

        # Add Widget Action
        addSeg = QtGui.QAction('&addSeg', self)
        addSeg.triggered.connect(self.addSeg)

        # Add Menu
        menu = self.menuBar()
        filemenu = menu.addMenu('&File')
        actionMenu = menu.addMenu('&Action')
        settingsmenu = menu.addMenu('&Setings')
        aboutmenu = menu.addMenu('&About')

        # Add Action
        filemenu.addAction(exitAction)
        filemenu.addAction(openFileAction)
        actionMenu.addAction(addSeg)
        # self.toolbar = self.addToolBar('Exit')
        # self.toolbar.addAction(exitAction)
        self.statusBar()
    def addSeg(self):
        sub_layout = QtGui.QHBoxLayout()
        Q1 = QtGui.QLabel('segment')
        Q2 = QtGui.QLabel('string')
        Q3 = QtGui.QLabel('dict')
        sub_layout.addWidget(Q1)
        sub_layout.addWidget(Q2)
        sub_layout.addWidget(Q3)

        # self.setCentralWidget(self.MainWidget)
        # self.MainWidgetLayout.addChildLayout(sub_layout)
        # self.MainWidget.layout(self.MainWidgetLayout)
        # self.MainWidgetLayout.addWidget(sub_layout)

    def openFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self , 'open file', '/c')
        # f = open(fname, 'r')
        # with f:
        #     data = f.read()
        #     self.textEdit.setText(data)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    x = TemplateEngine()
    app.exec_()