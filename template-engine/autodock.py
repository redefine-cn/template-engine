#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json
import sys
sys.path.append('../')
from plistIO.plistIO import modify
from central_window import check_integer, check_name_exist
f = file('../data/settings.json')
data = json.load(f)
from plistIO.plistIO import after_modify
name_list = data['name_list']


class autodock(QDockWidget):
    def __init__(self, parent=None):
        super(autodock, self).__init__(parent)
        self.fa = parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑"))
        self.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        self.row = -1
        self.labelCol = 0
        self.typeCol = 1
        self.contentCol = 2
        self.lv1 = 1
        self.lv2 = 2

        self.types = self.fa.data["Type"]
        self.gridLayout = QGridLayout()
        self.dialog = QDialog()
        self.updateUI(None)

    def addValue(self, key, tp, value, treeNode):
        self.row += 1
        labelEdit = QLineEdit()
        labelEdit.setText(key)
        key = unicode(key)
        tp = str(tp)
        value = unicode(value)

        combobox = QComboBox()

        if treeNode.childCount() != 0 or treeNode.parent() == None:
            combobox.addItem(tp)
        else:
            for i in range(len(self.types)):
                combobox.addItem(str(self.types[i]))
                if tp == str(self.types[i]):
                    combobox.setCurrentIndex(i)

        if treeNode.parent() == None:
            x = QLabel(key)
            self.gridLayout.addWidget(x, self.row, self.labelCol)
        elif str(treeNode.parent().text(1))== 'array':
            pass
        else:
            self.gridLayout.addWidget(labelEdit, self.row, self.labelCol)
        self.gridLayout.addWidget(combobox, self.row, self.typeCol)
        labelEdit.textChanged.connect(lambda :self.slotlabelEdit(treeNode, labelEdit.text()))
        # labelEdit.textChanged[QString].connect(partial(self.slotlabelEdit, treeNode))
        combobox.currentIndexChanged.connect(lambda :self.slotCombobox(treeNode, int(combobox.currentIndex())))
        # combobox.currentIndexChanged[int].connect(partial(self.slotCombobox, treeNode))

        if tp != 'dict' and tp != 'array' and treeNode.parent() != None:
            # 各种animation 放进一个QcoboBox来选择
            if unicode(key) == 'name' and str(treeNode.parent().text(0)).startswith('animation'):
                box = QComboBox()
                for i in range(len(data['actionList'])):
                    box.addItem(data['actionList'][i])
                    if data['actionList'][i] == unicode(value):
                        box.setCurrentIndex(i)
                box.currentIndexChanged.connect(lambda :self.slotValueEdit(treeNode, int(box.currentIndex())))
                # box.currentIndexChanged[QString].connect(partial(self.slotValueEdit, treeNode))
                self.gridLayout.addWidget(box, self.row, self.contentCol)
            # 如果类型不是bool(string, integer, real)
            elif tp != 'bool':
                edit = QLineEdit()
                edit.setText(value)
                edit.textChanged.connect(lambda :self.slotValueEdit(treeNode, edit.text()))
                # edit.textChanged[QString].connect(partial(self.slotValueEdit, treeNode))
                self.gridLayout.addWidget(edit, self.row, self.contentCol)
                if key in name_list:
                    but = QPushButton('select')
                    but.clicked.connect(lambda :self.openFile(treeNode))
                    self.gridLayout.addWidget(but, self.row, self.contentCol + 1)
            # 如果是bool型，则也是一个QComboBox来选择True, False
            else:
                box = QComboBox()
                box.addItem('True')
                box.addItem('False')
                if str(value) == 'True':
                    box.setCurrentIndex(0)
                else:
                    box.setCurrentIndex(1)
                box.currentIndexChanged.connect(lambda :self.slotValueEdit(treeNode, int(box.currentIndex())))
                # box.currentIndexChanged[QString].connect(partial(self.slotValueEdit, treeNode))
                self.gridLayout.addWidget(box, self.row, self.contentCol)

    def openFile(self, treeNode):
        fileName = unicode(QFileDialog.getOpenFileName(self, QString.fromUtf8('打开')))
        fi = QFileInfo(fileName)
        fileName = fi.fileName()
        self.slotValueEdit(treeNode, fileName)
        self.updateUI(treeNode.parent())

    def slotlabelEdit(self, treeNode, text):
        node = {}
        node['PreKey'] = unicode(treeNode.text(0))
        node['Key'] = unicode(text)
        node['Type'] = str(treeNode.text(1))
        node['Value'] = unicode(treeNode.text(2))
        if check_name_exist(treeNode.parent(), text):
            treeNode.setText(0, text)
            modify(treeNode.parent(), treeNode, node, self.parent().tab.currentWidget().path, self.parent().tab.currentWidget().root, 0)
        # self.updateUI(treeNode.parent())

    @after_modify
    def slotCombobox(self, treeNode, index):
        node = {}
        node['PreType'] = str(treeNode.text(1))
        treeNode.setText(1, QString.fromUtf8(self.types[index]))
        node['PreValue'] = unicode(treeNode.text(2))
        node['Key'] = unicode(treeNode.text(0))
        node['Type'] = str(self.types[index])
        if node['Type'] == 'dict' or node['Type'] == 'array':
            treeNode.setText(2, QString.fromUtf8(''))
        if node['Type'] == 'integer':
            try:
                node['Value'] = int(treeNode.text(2))
            except:
                node['Value'] = '-1'
        elif node['Type'] == 'real':
            try:
                node['Value'] = float(treeNode.text(2))
            except:
                node['Value'] = '-1.0'
        elif node['Type'] == 'bool':
            try:
                node['Value'] = str(treeNode.text(2))
            except:
                node['Value'] = 'True'
            if node['Value'] != 'True' and node['Value'] != 'False':
                node['Value'] = 'True'
        else:
            node['Value'] = unicode(treeNode.text(2))
        file_json, root = self.parent().tab.currentWidget().path, self.parent().tab.currentWidget().root
        if treeNode.text(2) == QString.fromUtf8(''):
            treeNode.setText(2, unicode(node['Value']))
            edit = QLineEdit(treeNode.text(2))
            self.gridLayout.addWidget(edit, self.row, self.contentCol)
        treeNode.setText(2, unicode(node['Value']))
        list_index = None
        if str(treeNode.parent().text(1)) == 'array':
            list_index = treeNode.parent().indexOfChild(treeNode)
        modify(treeNode.parent(), treeNode, node, file_json, root, 1, list_index)
        if treeNode != self.data:
            self.updateUI(treeNode.parent())
        else:
            self.updateUI(treeNode)
        return treeNode, file_json, root

    @after_modify
    def slotValueEdit(self, treeNode, text):
        print treeNode, text
        node = {}
        node['PreValue'] = unicode(treeNode.text(2))
        node['PreType'] = str(treeNode.text(1))
        node['Key'] = unicode(treeNode.text(0))
        node['Type'] = str(treeNode.text(1))
        node['Value'] = unicode(text)
        if node['Type'] == 'integer' and check_integer(node['Value']) == False:
            QMessageBox.critical(self, 'error', 'Value Error', QMessageBox.Ok)
            return None, None, None

        treeNode.setText(2, text)
        index = None
        file_json, root = self.parent().tab.currentWidget().path, self.parent().tab.currentWidget().root
        if str(treeNode.parent().text(1)) == 'array':
            index = treeNode.parent().indexOfChild(treeNode)
        modify(treeNode.parent(), treeNode, node, file_json, root, 1, index)
        return treeNode, file_json, root
        # modifyPositionScaleOpacity(treeNode, self.parent().tab.currentWidget().path, self.parent().tab.currentWidget().root)

    def updateUI(self, data):
        self.data = data
        if self.gridLayout :
            del self.gridLayout
            self.gridLayout = None

        if self.dialog :
            del self.dialog
            self.dialog = None

        self.gridLayout = QGridLayout()
        self.gridLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        if data:
            self.row = 0
            self.data = data
            self.addValue(data.text(0), data.text(1), data.text(2), data)
            if data.childCount() != 0:
                for i in range(data.childCount()):
                    self.addValue(data.child(i).text(0), data.child(i).text(1), data.child(i).text(2), data.child(i))

        self.dialog = QDialog()
        self.dialog.setLayout(self.gridLayout)
        self.setWidget(self.dialog)

if __name__ == '__main__':
    print unicode('aaa') == 'aaa'
