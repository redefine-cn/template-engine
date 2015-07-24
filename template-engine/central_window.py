__author__ = 'Administrator'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class AddWidget(QWidget):

    def __init__(self, fa):
        super(AddWidget, self).__init__()
        self.fa = fa
        self.init()

    def init(self):
        L1 = QLabel('Name')
        L2 = QLabel('Type')
        L3 = QLabel('Value')

        self.E1 = QLineEdit()
        self.E2 = QLineEdit()
        self.E3 = QLineEdit()

        but = QPushButton('Save')
        but.clicked.connect(self.save)

        layout = QGridLayout()
        layout.addWidget(L1, 0, 0)
        layout.addWidget(self.E1, 0, 1)
        layout.addWidget(L2, 1, 0)
        layout.addWidget(self.E2, 1, 1)
        layout.addWidget(L3, 2, 0)
        layout.addWidget(self.E3, 2, 1)
        layout.addWidget(but, 3, 1)

        self.setLayout(layout)

    def save(self):
        child = QTreeWidgetItem(self.fa)
        child.setText(0, self.E1.text())
        child.setText(1, self.E2.text())
        child.setText(2, self.E3.text())
        self.close()



class CentralWindow(QTreeWidget):

    def __init__(self, parent):
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
        self.test_action1 = QAction('&delete', self)
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