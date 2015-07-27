#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import  sys

class animation(QDockWidget):
    def __init__(self):
        super(animation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(QString.fromUtf8("编辑界面"))
        self.setFeatures(QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(Qt.RightDockWidgetArea)

        labelCol = 0
        contentCol = 1
        lv1 = 1
        lv2 = 2

        nameLabel = QLabel(QString.fromUtf8("name"))
        nameBox = QComboBox()
        nameBox.addItem(QString.fromUtf8("straightline"))
        nameBox.addItem(QString.fromUtf8("opacity"))
        nameBox.addItem(QString.fromUtf8("rotate"))

        startTimeLabel = QLabel(QString.fromUtf8("startime"))
        secondLabel1 = QLabel(QString.fromUtf8("second"))
        secondEdit1 = QLineEdit()
        frameLabel1 = QLabel(QString.fromUtf8("frame"))
        frameEdit1 = QLineEdit()

        durationLabel = QLabel(QString.fromUtf8("duration"))
        secondLabel2 = QLabel(QString.fromUtf8("second"))
        secondEdit2 = QLineEdit()
        frameLabel2 = QLabel(QString.fromUtf8("frame"))
        frameEdit2 = QLineEdit()

        valueLabel = QLabel(QString.fromUtf8("values"))
        self.IntRadioButton = QRadioButton(QString.fromUtf8("Integer"))
        self.IntRadioButton.setChecked(True)
        self.IntRadioButton.clicked.connect(self.slotValue)
        self.PointRadioButton = QRadioButton(QString.fromUtf8("Point"))
        self.PointRadioButton.clicked.connect(self.slotValue)

        # valueTypeBox.currentIndexChanged[int].connect(self.valueType)


        self.valueInt = QLineEdit()

        self.PointLayout = QHBoxLayout()
        xLayout = QHBoxLayout()
        xLabel = QLabel(QString.fromUtf8("x"))
        xEdit = QLineEdit()
        xLayout.addWidget(xLabel)
        xLayout.addWidget(xEdit)
        yLayout = QHBoxLayout()
        yLabel = QLabel(QString.fromUtf8("y"))
        yEdit = QLineEdit()
        yLayout.addWidget(yLabel)
        yLayout.addWidget(yEdit)

        self.PointLayout.addLayout(xLayout, 1)
        self.PointLayout.addLayout(yLayout, 1)


        timeLabel = QLabel(QString.fromUtf8("times"))
        secondLabel3 = QLabel(QString.fromUtf8("second"))
        secondEdit3 = QLineEdit()
        frameLabel3 = QLabel(QString.fromUtf8("frame"))
        frameEdit3 = QLineEdit()


        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(nameLabel, 0, labelCol )
        self.gridLayout.addWidget(nameBox, 0, contentCol )
        self.gridLayout.addWidget(startTimeLabel, 1, labelCol )
        self.gridLayout.addWidget(secondLabel1, 1, lv1 )
        self.gridLayout.addWidget(secondEdit1, 1, lv2 )
        self.gridLayout.addWidget(frameLabel1, 2, lv1 )
        self.gridLayout.addWidget(frameEdit1, 2, lv2)
        self.gridLayout.addWidget(durationLabel, 3, labelCol)
        self.gridLayout.addWidget(secondLabel2, 3, lv1)
        self.gridLayout.addWidget(secondEdit2, 3, lv2)
        self.gridLayout.addWidget(frameLabel2, 4, lv1)
        self.gridLayout.addWidget(frameEdit2, 4, lv2)

        self.gridLayout.addWidget(valueLabel, 5, labelCol)
        self.gridLayout.addWidget(self.IntRadioButton, 5, lv1 )
        self.gridLayout.addWidget(self.valueInt, 5, lv2)

        self.gridLayout.addWidget(self.PointRadioButton, 6, lv1)
        self.gridLayout.addLayout(self.PointLayout, 6, lv2)
        self.gridLayout.addWidget(timeLabel, 7, labelCol )
        self.gridLayout.addWidget(secondLabel3, 7, lv1 )
        self.gridLayout.addWidget(secondEdit3, 7, lv2 )
        self.gridLayout.addWidget(frameLabel3, 8, lv1 )
        self.gridLayout.addWidget(frameEdit3, 8, lv2 )

        dialog = QDialog()
        dialog.setLayout(self.gridLayout)
        self.setWidget(dialog)
        # self.adjustSize()
        # self.setLayout(gridLayout)

    def valueType(self, index):
        if index == 0:
            self.gridLayout.removeWidget(self.xLabel)
            self.gridLayout.removeWidget(self.xEdit)
            self.gridLayout.removeWidget(self.yLabel)
            self.gridLayout.removeWidget(self.yEdit)
            self.gridLayout.addWidget(self.valueInt, 5, 2)
        elif index == 1:
            self.gridLayout.removeWidget(self.valueInt)
            self.gridLayout.addWidget(self.xLabel, 5, 2)
            self.gridLayout.addWidget(self.xEdit, 5, 3)
            self.gridLayout.addWidget(self.yLabel, 5, 4)
            self.gridLayout.addWidget(self.yEdit, 5, 5)

    def slotValue(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    dock = animation(None)
    dock.setFeatures(QDockWidget.DockWidgetMovable)
    dock.setAllowedAreas(Qt.RightDockWidgetArea)
    win.addDockWidget(Qt.RightDockWidgetArea, dock)

    # win = animation(None)
    win.show()
    sys.exit(app.exec_())


