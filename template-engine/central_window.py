__author__ = 'Administrator'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import json
f = file('settings.json')
data = json.load(f)


class AddWidget(QWidget):

    def __init__(self, fa):
        super(AddWidget, self).__init__()
        self.fa = fa
        self.init()

    def init(self):
        self.L1 = QLabel('Key')
        self.L2 = QLabel('Type')
        self.L3 = QLabel('Value')

        self.E1 = QLineEdit()
        self.E2 = QComboBox()
        for type in data['Type']:
            self.E2.addItem(type)
        self.E2.currentIndexChanged.connect(self.boxChange)
        self.E3 = QLineEdit()

        but = QPushButton('Save')
        but.clicked.connect(self.save)

        layout = QGridLayout()
        layout.addWidget(self.L1, 0, 0)
        layout.addWidget(self.E1, 0, 1)
        layout.addWidget(self.L2, 1, 0)
        layout.addWidget(self.E2, 1, 1)
        layout.addWidget(self.L3, 2, 0)
        layout.addWidget(self.E3, 2, 1)
        layout.addWidget(but, 3, 1)

        self.setLayout(layout)

    def boxChange(self):
        currentText = str(self.E2.currentText())
        if currentText == 'dict' or currentText == 'array':
            self.E3.hide()
            self.L3.hide()
        else :
            self.E3.show()
            self.L3.show()

    def save(self):
        child = QTreeWidgetItem(self.fa)
        type = str(self.E2.currentText())
        if type == 'dict' or type == 'array':
            child.setText(0, self.E1.text())
            child.setText(1, self.E2.currentText())
        else :
            child.setText(0, self.E1.text())
            child.setText(1, self.E2.currentText())
            child.setText(2, self.E3.text())
        self.close()


class CentralWindow(QTreeWidget):

    def __init__(self, parent=None):
        super(CentralWindow, self).__init__(parent)
        self.init()

    def init(self):
        self.setColumnCount(3)
        self.setHeaderLabels(['Key', 'Type', 'Value'])
        self.root = QTreeWidgetItem(self)
        self.root.setText(0, 'root')

    def addNormal(self):
        self.Window = AddWidget(self.currentItem())
        self.Window.show()

    def delete(self):
        self.currentItem().parent().removeChild(self.currentItem())


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