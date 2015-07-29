#coding=utf-8
__author__ = 'Administrator'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import json
from plistIO.plistIO import add, delete, new_tree

f = file('settings.json')
data = json.load(f)

# path = new_tree()

def checkInteger(text):
    text = str(text)
    for i in range(len(text)):
        if text[i] < '0' or text[i] > '9':
            return False
    return True

def findChild(parent):
    type = str(parent.text(1))
    if type == 'dict':
        ans = dict()
        for i in range(parent.childCount()):
            type1 = str(parent.child(i).text(1))
            if type1 == 'dict' or type1 == 'array':
                ans[str(parent.child(i).text(0))] = type1
            else:
                ans[str(parent.child(i).text(0))] = str(parent.child(i).text(2))
        print ans
    elif type == 'array':
        ans = list()
        for i in range(parent.childCount()):
            ans.append(str(parent.child(i).text(2)))
    return ans

def findFather(parent):
    fa = parent.fa
    falist = list()
    while str(fa.text(0)) != 'root':
        falist.append(str(fa.text(0)))
        if getattr(fa, 'parent', None) == None:
            break
        fa = fa.parent()
    return falist


def changeType(Type):
    if Type == type(1):
        return 'integer'
    elif Type == type('123'):
        return 'string'
    elif Type == type(1.1):
        return 'real'
    elif Type == type(True):
        return 'bool'
    else:
        return 'string'

class AddWidget(QWidget):

    def __init__(self, fa, father):

        if hasattr(fa, 'text'):
            fatext = str(fa.text(1))
        else:
            QMessageBox.critical(fa, 'error', QString.fromUtf8('Please Select Node'), QMessageBox.Ok)
            return
        if fatext == 'integer' or fatext == 'string' or fatext == 'real':
            QMessageBox.critical(None, 'error', QString.fromUtf8('Can Not Add'), QMessageBox.Ok)
            return
        super(AddWidget, self).__init__()
        self.father = father
        self.fa = fa
        self.col = 3
        self.dic = dict()
        self.arrayDic = dict()
        self.arrayE = list()
        self.init()
        self.setWindowTitle('Add Widget')
        self.show()

    def init(self):
        fatext = str(self.fa.text(1))
        self.L1 = QLabel('Key')
        self.L2 = QLabel('Type')
        self.L3 = QLabel('Value')

        if fatext == 'array':
            self.E2 = QComboBox()
            self.E2.addItem('string')
            self.E2.addItem('integer')
            self.E2.addItem('real')
            self.E2.addItem('bool')
            self.E2.addItem('dict')
            self.E3 = QLineEdit()
            self.E2.currentIndexChanged.connect(self.arrayBoxChange)
            self.butsavearray = QPushButton('Save')
            self.butsavearray.clicked.connect(self.saveArray)

            layout = QGridLayout()
            layout.addWidget(self.L2, 0, 0)
            layout.addWidget(self.E2, 0, 1)
            layout.addWidget(self.L3, 1, 0)
            layout.addWidget(self.E3, 1, 1)
            layout.addWidget(self.butsavearray, 2, 1)
        # self.col = 3
        else :
            self.E1 = QLineEdit()
            self.E2 = QComboBox()
            for type in data['Type']:
                self.E2.addItem(type)
            self.E2.currentIndexChanged.connect(self.boxChange)
            self.E3 = QLineEdit()

            self.butsave = QPushButton('Save')
            self.butsave.clicked.connect(self.save)

            layout = QGridLayout()
            layout.addWidget(self.L1, 0, 0)
            layout.addWidget(self.E1, 0, 1)
            layout.addWidget(self.L2, 1, 0)
            layout.addWidget(self.E2, 1, 1)
            layout.addWidget(self.L3, 2, 0)
            layout.addWidget(self.E3, 2, 1)
            layout.addWidget(self.butsave, 3, 1)

        self.setLayout(layout)
    def arrayBoxChange(self):
        # self.col = 3
        currentText = str(self.E2.currentText())
        if currentText == 'dict':
            self.E3.hide()
            self.L3.hide()
            # self.butadd = QPushButton('Add')
            # self.layout().addWidget(self.butadd, self.col, 0)
            # self.butadd.clicked.connect(self.addCol)
            # self.layout().addWidget(self.butsavearray, self.col, 1)
            # pass
        else:
            self.L3.show()
            self.E3.show()

    def boxChange(self):
        currentText = str(self.E2.currentText())
        if currentText == 'dict' or currentText == 'array':
            self.E3.hide()
            self.L3.hide()
        else:
            self.E3.show()
            self.L3.show()

    # def addCol(self):
    #     L1 = QLabel('Key')
    #     L2 = QLabel('Type')
    #     L3 = QLabel('Value')
    #     self.arrayE.append(QLineEdit())
    #     self.arrayE.append(QComboBox())
    #     self.arrayE.append(QLineEdit())
    #     l = len(self.arrayE)
    #     self.arrayE[l - 2].addItem('integer')
    #     self.arrayE[l - 2].addItem('real')
    #     self.arrayE[l - 2].addItem('string')
    #
    #     self.layout().addWidget(L1, self.col, 0)
    #     self.layout().addWidget(L2, self.col + 1, 0)
    #     self.layout().addWidget(L3, self.col + 2, 0)
    #     self.layout().addWidget(self.arrayE[l - 3], self.col, 1)
    #     self.layout().addWidget(self.arrayE[l - 2], self.col + 1, 1)
    #     self.layout().addWidget(self.arrayE[l - 1], self.col + 2, 1)
    #     self.layout().addWidget(self.butadd, self.col + 3, 0)
    #     self.butsavearraydic = QPushButton('Save')
    #     self.butsavearraydic.clicked.connect(self.saveArrayDic)
    #     self.layout().addWidget(self.butsavearraydic, self.col + 3, 1)
    #     self.col += 3

    # def saveArrayDic(self):
    #     l = len(self.arrayE)
    #     print l
    #     child = QTreeWidgetItem(self.fa)
    #     child.setText(1, 'dict')
    #     pos = 0
    #     while pos < l:
    #         if str(self.arrayE[pos + 1].currentText()) == 'integer':
    #             val = int(self.arrayE[pos + 2].text())
    #         elif str(self.arrayE[pos + 1].currentText()) == 'string':
    #             val = str(self.arrayE[pos + 2].text())
    #         else:
    #             val = float(self.arrayE[pos + 2].text())
    #         self.arrayDic[str(self.arrayE[pos].text())] = val
    #         childnext = QTreeWidgetItem(child)
    #         childnext.setText(0, self.arrayE[pos].text())
    #         childnext.setText(1, self.arrayE[pos + 1].currentText())
    #         childnext.setText(2, self.arrayE[pos + 2].text())
    #         pos += 3
    #     self.dic['Type'] = 'dict'
    #     self.dic['Key'] = 'ARRAY'
    #     self.dic['Value'] = self.arrayDic
    #     self.close()

    def saveArray(self):
        self.dic['Type'] = ''
        type = str(self.E2.currentText())
        if len(self.E3.text()) == 0 and type != 'dict':
            QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
            return False
        if type == 'integer' and checkInteger(self.E3.text()) == False:
            QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
            return False
        child = QTreeWidgetItem(self.fa)
        child.setText(1, self.E2.currentText())
        Value = self.E3.text()
        Type = self.E2.currentText()
        if changeType(Type) == 'integer' or changeType(Type) == 'string' or changeType(Type) == 'bool':
            Value = str(Value)
        child.setText(2, QString.fromUtf8(Value))
        child.setExpanded(True)
        self.dic['Key'] = 'ARRAY'
        self.dic['Type'] = str(self.E2.currentText())
        self.dic['Value'] = Value

        self.dic['parent'] = findFather(self)
        add(self.fa, child, self.dic, self.father.path)
        # add_node(self.dic, path)
        self.close()

    def save(self):
        self.dic['Value'] = ''
        type = str(self.E2.currentText())
        if type == 'dict' or type == 'array':
            if len(self.E1.text()) == 0:
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, QString.fromUtf8(unicode(self.E1.text())))
            child.setText(1, self.E2.currentText())
            child.setExpanded(True)
            self.dic['Key'] = unicode(self.E1.text())
            self.dic['Type'] = str(self.E2.currentText())
            add(self.fa, child, self.dic, self.father.path)
        elif type == 'integer':
            # print len(self.E1.text())
            if len(self.E1.text()) == 0 or len(self.E3.text()) == 0:
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            if checkInteger(self.E3.text()) == False:
                QMessageBox.critical(self, 'error', self.tr('Type Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            # print QString.fromUtf8(self.E1.text())
            child.setText(0, QString.fromUtf8(unicode(self.E1.text())))
            child.setText(1, self.E2.currentText())
            Value = self.E3.text()
            Type = self.E2.currentText()
            if changeType(Type) == 'integer' or changeType(Type) == 'real' or changeType(Type) == 'bool':
                Value = str(Value)
            # print(Value)
            # print unicode(self.E1.text())
            child.setText(2, QString.fromUtf8(Value))
            child.setExpanded(True)
            self.dic['Key'] = unicode(self.E1.text())
            self.dic['Type'] = str(self.E2.currentText())
            self.dic['Value'] = Value
            # print self.father.path
            add(self.fa, child, self.dic, self.father.path)
        else :
            if len(self.E1.text()) == 0 or len(self.E3.text()) == 0:
                # print 222
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, QString.fromUtf8(unicode(self.E1.text())))
            child.setText(1, self.E2.currentText())
            Value = self.E3.text()
            Type = self.E2.currentText()
            if changeType(Type) == 'integer' or changeType(Type) == 'real' or changeType(Type) == 'bool':
                Value = str(Value)
            child.setText(2, QString.fromUtf8(Value))
            child.setExpanded(True)
            self.dic['Key'] = unicode(self.E1.text())
            self.dic['Type'] = str(self.E2.currentText())
            self.dic['Value'] = Value
            add(self.fa, child, self.dic, self.father.path)
        self.close()


class CentralWindow(QTreeWidget):

    def __init__(self, parent=None):
        super(CentralWindow, self).__init__(parent)
        self.init()
        # self.path = 'asd'
        self.path = new_tree()

    def init(self):
        self.setColumnCount(3)
        self.setHeaderLabels(['Key', 'Type', 'Value'])
        self.header().resizeSection(0, 200)
        self.header().resizeSection(1, 200)
        self.header().resizeSection(2, 200)
        self.root = QTreeWidgetItem(self)
        self.root.setText(0, 'root')

    def dfs(self, dic, fa, Key, Type, Value):
        # print findFatherObject(fa)
        if Type == type({}) or Type == type([]):
            child = QTreeWidgetItem(fa)
            child.setText(0, QString.fromUtf8(unicode(Key)))
            if Type == type({}):
                child.setText(1, 'dict')
                child.setExpanded(True)
                add(fa, child, {'Key':(Key),'Type':'dict'}, self.path)
                for k, v in dic.items():
                    self.dfs(v, child, k, type(v), v)
            else:
                child.setText(1, 'array')
                child.setExpanded(True)
                add(fa, child, {'Key':(Key),'Type':'array'}, self.path)
                for i in range(len(dic)):
                    self.dfs(dic[i], child, 'item'+ str(i), type(dic[i]), dic[i])
        else:
            child = QTreeWidgetItem(fa)
            child.setText(0, QString.fromUtf8(unicode(Key)))
            child.setText(1, changeType(Type))
            if changeType(Type) == 'integer' or changeType(Type) == 'real' or changeType(Type) == 'bool':
                Value = str(Value)
            # print Type
            child.setText(2, QString.fromUtf8((Value)))
            child.setExpanded(True)
            add(fa, child, {'Key':(Key),'Type':changeType(Type),'Value':Value}, self.path)

    def mouseDoubleClickEvent(self, QmouseEvent):
        if QmouseEvent.button() == Qt.LeftButton:
            self.parent().parent().dock.updateUI(self.currentItem())
            # pass
            # TODO show information in right window
            # dic = dict()
            # if int(self.currentItem().childCount()) > 0:
            #     for i in range(int(self.currentItem().childCount())):
            #         if str(self.currentItem().child(i).text(1)) == 'dict':
            #             dic1 = dict()
            #             for j in range(int(self.currentItem().child(i).childCount())):
            #                 if str(self.currentItem().child(i).child(j).text(1)) == 'array' \
            #                         or str(self.currentItem().child(i).child(j).text(1)) == 'dict':
            #                     # dic1[str(self.currentItem().child(i).child(j).text(0))] = findChild(self.currentItem().child(i).child(j))
            #                     dic1[str(self.currentItem().child(i).child(j).text(0))] = str(self.currentItem().child(i).child(j).text(1))
            #                 else:
            #                     dic1[str(self.currentItem().child(i).child(j).text(0))] = str(self.currentItem().child(i).child(j).text(2))
            #             dic[str(self.currentItem().child(i).text(0))] = dic1
            #         elif str(self.currentItem().child(i).text(1)) == 'array':
            #             lis = list()
            #             for j in range(int(self.currentItem().child(i).childCount())):
            #                 lis.append(str(self.currentItem().child(i).child(j).text(2)))
            #             dic[str(self.currentItem().child(i).text(0))] = lis
            #         else:
            #             dic[str(self.currentItem().child(i).text(0))] = str(self.currentItem().child(i).text(2))
            # else:
            #     dic[str(self.currentItem().text(0))] = str(self.currentItem().text(2))
            # dic['title'] = str(self.currentItem().text(0))
            # print dic
            # for k, v in dic11.items():
            #     self.dfs(v, mainWindow.central.root, k, type(v), v)
            # self.parent().parent().dock.updateUI(dic)


    def addNormal(self):
        self.Window = AddWidget(self.currentItem(), self)
        # self.Window.show()

    def delete(self):
        if self.currentItem().text(0) != 'root':
            Node = {}
            Node['Key'] = unicode(self.currentItem().text(0))
            delete(self.currentItem().parent(), self.currentItem(), Node, self.path)
            self.currentItem().parent().removeChild(self.currentItem())
        else:
            return False


class TabCenter(QWidget):
    def __init__(self, parent = None):
        super(TabCenter, self).__init__(parent)
        self.init()

    def init(self):
        self.center = CentralWindow(self)
        self.tab = QTabWidget()
        self.tab.addTab(self.center, '1')
        layout = QGridLayout()
        layout.addWidget(self.center)
        self.setLayout(layout)


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init()

    def init(self):
        menu = self.menuBar()
        action = menu.addMenu('&Action')
        self.central = CentralWindow()
        self.setCentralWidget(self.central)

        self.test_action = QAction('&add', self)
        self.test_action.setShortcut('Ctrl+a')
        self.test_action1 = QAction('&delete', self)
        self.test_action1.setShortcut('Ctrl+d')
        self.test_action.triggered.connect(self.central.addNormal)
        self.test_action1.triggered.connect(self.central.delete)

        action.addAction(self.test_action)
        action.addAction(self.test_action1)

        self.resize(960,540)


if __name__ == '__main__':
    dic11 = {"dict": {"backgroundImage": "run01bg0001.png", "animation1": {"values": [{"y": 1.1, "x": 105}, {"y": 105, "x": 105}, {"y": 100, "x": 100}], "name": "scale", "starttime": {"second": 0, "frame": 0}}, "starttime": {"second": 0, "frame": 0}}}
    app = QApplication(sys.argv)
    mainWindow = Example()
    mainWindow.show()
    app.exec_()
