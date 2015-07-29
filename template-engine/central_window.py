#coding=utf-8
__author__ = 'Administrator'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import json
from plistIO.plistIO import add, delete, new_tree

f = file('settings.json')
data = json.load(f)

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

def changeTypeInDFS(Type):
    if Type == type({}):
        return 'dict'
    elif Type == type([]):
        return 'array'
    elif Type == type('ad'):
        return 'string'
    elif Type == type(1):
        return 'integer'
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
        if fatext == 'integer' or fatext == 'string' or fatext == 'real' or fatext == 'bool':
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

        self.E3bool = QComboBox()
        self.E3bool.addItem('True')
        self.E3bool.addItem('False')

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
            layout.addWidget(self.E3bool, 1, 1)
            layout.addWidget(self.E3, 1, 1)
            layout.addWidget(self.butsavearray, 2, 1)
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
            layout.addWidget(self.E3bool, 2, 1)
            layout.addWidget(self.E3, 2, 1)
            layout.addWidget(self.butsave, 3, 1)

        self.setLayout(layout)
    def arrayBoxChange(self):
        currentText = str(self.E2.currentText())
        if currentText == 'dict':
            self.E3bool.hide()
            self.E3.hide()
            self.L3.hide()
        elif currentText == 'bool':
            self.L3.show()
            self.E3.hide()
            self.E3bool.show()
        else:
            self.E3bool.hide()
            self.L3.show()
            self.E3.show()

    def boxChange(self):
        currentText = str(self.E2.currentText())
        if currentText == 'dict' or currentText == 'array':
            self.E3bool.hide()
            self.E3.hide()
            self.L3.hide()
        elif currentText == 'bool':
            self.L3.show()
            self.E3.hide()
            self.E3bool.show()
        else:
            self.E3bool.hide()
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
        Type = str(self.E2.currentText())
        if len(self.E3.text()) == 0 and Type != 'dict' and Type != 'bool':
            QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
            return False
        if Type == 'integer' and checkInteger(self.E3.text()) == False:
            QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
            return False
        child = QTreeWidgetItem(self.fa)
        child.setText(1, self.E2.currentText())
        if Type == 'bool':
            Value = self.E3bool.currentText()
        else:
            Value = self.E3.text()
        if Type == 'integer' or Type == 'string' or Type == 'bool' or Type == 'string':
            Value = str(Value)
        child.setText(2, QString.fromUtf8(Value))
        child.setExpanded(True)
        self.dic['Key'] = 'ARRAY'
        self.dic['Type'] = Type
        self.dic['Value'] = Value

        self.dic['parent'] = findFather(self)
        add(self.fa, child, self.dic, self.father.path)
        self.close()

    def save(self):
        self.dic['Value'] = ''
        Type = str(self.E2.currentText())
        if Type == 'dict' or Type == 'array':
            if len(self.E1.text()) == 0:
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, QString.fromUtf8(unicode(self.E1.text())))
            child.setText(1, self.E2.currentText())
            child.setExpanded(True)
            self.dic['Key'] = unicode(self.E1.text())
            self.dic['Type'] = Type
            add(self.fa, child, self.dic, self.father.path)
        elif Type == 'integer':
            if len(self.E1.text()) == 0 or len(self.E3.text()) == 0:
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            if checkInteger(self.E3.text()) == False:
                QMessageBox.critical(self, 'error', self.tr('Type Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, QString.fromUtf8(unicode(self.E1.text())))
            child.setText(1, self.E2.currentText())
            Value = self.E3.text()
            if Type == 'integer' or Type == 'real' or Type == 'bool' or Type == 'string':
                Value = str(Value)
            child.setText(2, QString.fromUtf8(Value))
            child.setExpanded(True)
            self.dic['Key'] = unicode(self.E1.text())
            self.dic['Type'] = str(self.E2.currentText())
            self.dic['Value'] = Value
            add(self.fa, child, self.dic, self.father.path)
        else :
            if len(self.E1.text()) == 0 or (len(self.E3.text()) == 0 and Type != 'bool'):
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, QString.fromUtf8(unicode(self.E1.text())))
            child.setText(1, self.E2.currentText())
            if Type == 'bool':
                Value = self.E3bool.currentText()
            else:
                Value = self.E3.text()

            if Type == 'integer' or Type == 'real' or Type == 'bool' or Type == 'string':
                Value = str(Value)
            # print Value
            child.setText(2, QString.fromUtf8(Value))
            child.setExpanded(True)
            self.dic['Key'] = unicode(self.E1.text())
            self.dic['Type'] = Type
            self.dic['Value'] = Value
            add(self.fa, child, self.dic, self.father.path)
        self.close()


class CentralWindow(QTreeWidget):

    def __init__(self, parent=None):
        super(CentralWindow, self).__init__(parent)
        self.init()
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
            Type = changeTypeInDFS(Type)
            child = QTreeWidgetItem(fa)
            child.setText(0, QString.fromUtf8(unicode(Key)))
            child.setText(1, Type)
            if Type == 'integer' or Type == 'real' or Type == 'bool':
                Value = str(Value)
            child.setText(2, QString.fromUtf8((Value)))
            child.setExpanded(True)
            add(fa, child, {'Key':(Key),'Type':Type,'Value':Value}, self.path)

    def mouseDoubleClickEvent(self, QmouseEvent):
        if QmouseEvent.button() == Qt.LeftButton:
            if self.parent().parent().parent().parent().dock.isHidden():
                self.parent().parent().parent().parent().dock.show()
            self.parent().parent().parent().parent().dock.updateUI(self.currentItem())

    def addNormal(self):
        self.Window = AddWidget(self.currentItem(), self)

    def delete(self):
        if self.currentItem().text(0) != 'root':
            Node = {}
            Node['Key'] = unicode(self.currentItem().text(0))
            delete(self.currentItem().parent(), self.currentItem(), Node, self.path)
            self.currentItem().parent().removeChild(self.currentItem())
        else:
            return False


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
    app = QApplication(sys.argv)
    mainWindow = Example()
    mainWindow.show()
    app.exec_()
