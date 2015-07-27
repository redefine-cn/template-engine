#coding=utf-8
__author__ = 'Administrator'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import json
from plistIO.plistIO import add_node, delete_node
f = file('settings.json')
data = json.load(f)

def checkInteger(text):
    text = str(text)
    for i in range(len(text)):
        if text[i] < '0' or text[i] > '9':
            return False
    return True

def checkNone(text):
    text = str(text)
    if text == '':
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


class AddWidget(QWidget):

    def __init__(self, fa):

        if hasattr(fa, 'text'):
            fatext = str(fa.text(1))
        else:
            QMessageBox.critical(fa, 'error', QString.fromUtf8('Please Select Node'), QMessageBox.Ok)
            return
        if fatext == 'integer' or fatext == 'string' or fatext == 'real':
            QMessageBox.critical(None, 'error', QString.fromUtf8('Can Not Add'), QMessageBox.Ok)
            return
        super(AddWidget, self).__init__()
        self.fa = fa
        self.init()
        self.setWindowTitle('Add Widget')
        self.show()

    def init(self):
        self.dic = dict()

        fatext = str(self.fa.text(1))
        if fatext == 'array':
            self.L2 = QLabel('Type')
            self.L3 = QLabel('Value')

            self.E2 = QComboBox()
            self.E2.addItem('string')
            self.E2.addItem('integer')
            self.E2.addItem('real')
            self.E3 = QLineEdit()

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
            self.L1 = QLabel('Key')
            self.L2 = QLabel('Type')
            self.L3 = QLabel('Value')

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

    def boxChange(self):
        currentText = str(self.E2.currentText())
        # self.col = 3
        if currentText == 'dict' or currentText == 'array':
            self.E3.hide()
            self.L3.hide()
        # elif currentText == 'array':
        #     self.L3.hide()
        #     self.E3.hide()
        #     self.butadd = QPushButton('Add')
        #
        #     self.layout().addWidget(self.butadd, self.col, 0)
        #     self.butadd.clicked.connect(self.addCol)
        #
        #     self.layout().addWidget(self.butsave, self.col, 1)
        else:
            self.E3.show()
            self.L3.show()

    # def addCol(self):
    #     sbox = QComboBox()
    #     sbox.addItem('integer')
    #     sbox.addItem('string')
    #     sbox.addItem('real')
    #
    #     slin = QLineEdit()
    #
    #     self.layout().addWidget(sbox, self.col, 0)
    #     self.layout().addWidget(slin, self.col, 1)
    #
    #     self.layout().addWidget(self.butadd, self.col + 1, 0)
    #     self.layout().addWidget(self.butsave, self.col + 1, 1)
    #     self.col += 1

    def saveArray(self):
        self.dic['Type'] = ''
        type = str(self.E2.currentText())
        if checkNone(self.E3.text()) == False:
            QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
            return False
        if type == 'integer' and checkInteger(self.E3.text()) == False:
            QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
            return False
        child = QTreeWidgetItem(self.fa)
        child.setText(1, self.E2.currentText())
        child.setText(2, self.E3.text())
        self.dic['Key'] = 'ARRAY'
        self.dic['Type'] = str(self.E2.currentText())
        self.dic['Value'] = str(self.E3.text())
        fa = self.fa
        falist = list()
        while str(fa.text(0)) != 'root':
            falist.append(str(fa.text(0)))
            if getattr(fa, 'parent', None) == None:
                break
            fa = fa.parent()
        self.dic['parent'] = falist
        print self.dic
        add_node(self.dic)
        self.close()

    def save(self):
        self.dic['Value'] = ''
        type = str(self.E2.currentText())
        if type == 'dict' or type == 'array':
            if checkNone(self.E1.text()) == False:
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, self.E1.text())
            child.setText(1, self.E2.currentText())
            self.dic['Key'] = str(self.E1.text())
            self.dic['Type'] = str(self.E2.currentText())
        elif type == 'integer':
            if checkNone(self.E1.text()) == False or checkNone(self.E3.text()) == False:
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            if checkInteger(self.E3.text()) == False:
                QMessageBox.critical(self, 'error', self.tr('Type Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, self.E1.text())
            child.setText(1, self.E2.currentText())
            child.setText(2, self.E3.text())
            self.dic['Key'] = str(self.E1.text())
            self.dic['Type'] = str(self.E2.currentText())
            self.dic['Value'] = str(self.E3.text())
        else :
            if checkNone(self.E1.text()) == False or checkNone(self.E3.text()) == False:
                QMessageBox.critical(self, 'error', self.tr('Value Error'), QMessageBox.Ok)
                return False
            child = QTreeWidgetItem(self.fa)
            child.setText(0, self.E1.text())
            child.setText(1, self.E2.currentText())
            child.setText(2, self.E3.text())
            self.dic['Key'] = str(self.E1.text())
            self.dic['Type'] = str(self.E2.currentText())
            self.dic['Value'] = str(self.E3.text())

        fa = self.fa
        falist = list()
        while str(fa.text(0)) != 'root':
            falist.append(str(fa.text(0)))
            if getattr(fa, 'parent', None) == None:
                break
            fa = fa.parent()
        self.dic['parent'] = falist
        print self.dic
        add_node(self.dic)
        self.close()


class CentralWindow(QTreeWidget):

    def __init__(self, parent=None):
        super(CentralWindow, self).__init__(parent)
        self.init()

    def init(self):
        self.setColumnCount(3)
        self.setHeaderLabels(['Key', 'Type', 'Value'])
        self.header().resizeSection(0, 200)
        self.header().resizeSection(1, 200)
        self.header().resizeSection(2, 200)
        self.root = QTreeWidgetItem(self)
        self.root.childCount()
        self.root.setText(0, 'root')

    def mouseDoubleClickEvent(self, QmouseEvent):
        if QmouseEvent.button() == Qt.LeftButton:
            dic = dict()
            if int(self.currentItem().childCount()) > 0:
                for i in range(int(self.currentItem().childCount())):
                    if str(self.currentItem().child(i).text(1)) == 'dict':
                        dic1 = dict()
                        for j in range(int(self.currentItem().child(i).childCount())):
                            if str(self.currentItem().child(i).child(j).text(1)) == 'array' \
                                    or str(self.currentItem().child(i).child(j).text(1)) == 'dict':
                                # dic1[str(self.currentItem().child(i).child(j).text(0))] = findChild(self.currentItem().child(i).child(j))
                                dic1[str(self.currentItem().child(i).child(j).text(0))] = str(self.currentItem().child(i).child(j).text(1))
                            else:
                                dic1[str(self.currentItem().child(i).child(j).text(0))] = str(self.currentItem().child(i).child(j).text(2))
                        dic[str(self.currentItem().child(i).text(0))] = dic1
                    elif str(self.currentItem().child(i).text(1)) == 'array':
                        lis = list()
                        for j in range(int(self.currentItem().child(i).childCount())):
                            lis.append(str(self.currentItem().child(i).child(j).text(2)))
                        dic[str(self.currentItem().child(i).text(0))] = lis
                    else:
                        dic[str(self.currentItem().child(i).text(0))] = str(self.currentItem().child(i).text(2))
            else:
                dic[str(self.currentItem().text(0))] = str(self.currentItem().text(2))
            dic['title'] = str(self.currentItem().text(0))
            print dic
            self.parent().parent().dock.updateUI(dic)
            # TODO show information in right window

    def addNormal(self):
        self.Window = AddWidget(self.currentItem())
        # self.Window.show()

    def delete(self):
        if self.currentItem().text(0) != 'root':
            dic = dict()
            fa = self.currentItem().parent()
            falist = list()
            while str(fa.text(0)) != 'root':
                falist.append(str(fa.text(0)))
                fa = fa.parent()
            dic['parent'] = falist
            dic['Key'] = str(self.currentItem().text(0))
            delete_node(dic)
            print dic
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
    sys.exit(app.exec_())