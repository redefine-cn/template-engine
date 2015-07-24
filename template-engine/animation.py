#-*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import  sys

class animation(QDockWidget):
    def __init__(self, parent):
        super(animation, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setWindowTitle(QString.fromUtf8("编辑界面"))
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
        valueTypeBox = QComboBox()
        valueTypeBox.addItem(QString.fromUtf8("Int"))
        valueTypeBox.addItem(QString.fromUtf8("Point"))

        valueInt = QLineEdit()

        xLabel = QLabel(QString.fromUtf8("x"))
        xEdit = QLineEdit()
        yLabel = QLabel(QString.fromUtf8("y"))
        yEdit = QLineEdit()

        timeLabel = QLabel(QString.fromUtf8("times"))
        secondLabel3 = QLabel(QString.fromUtf8("second"))
        secondEdit3 = QLineEdit()
        frameLabel3 = QLabel(QString.fromUtf8("frame"))
        frameEdit3 = QLineEdit()


        gridLayout = QGridLayout()
        gridLayout.addWidget(nameLabel, 0, labelCol )
        gridLayout.addWidget(nameBox, 0, contentCol )
        gridLayout.addWidget(startTimeLabel, 1, labelCol )
        gridLayout.addWidget(secondLabel1, 1, lv1 )
        gridLayout.addWidget(secondEdit1, 1, lv2 )
        gridLayout.addWidget(frameLabel1, 2, lv1 )
        gridLayout.addWidget(frameEdit1, 2, lv2)
        gridLayout.addWidget(durationLabel, 3, labelCol)
        gridLayout.addWidget(secondLabel2, 3, lv1)
        gridLayout.addWidget(secondEdit2, 3, lv2)
        gridLayout.addWidget(frameLabel2, 4, lv1)
        gridLayout.addWidget(frameEdit2, 4, lv2)
        gridLayout.addWidget(valueLabel, 5, labelCol)
        gridLayout.addWidget(valueTypeBox, 5, lv1 )
        gridLayout.addWidget(valueInt, 5, lv2)
        gridLayout.addWidget(timeLabel, 7, labelCol )
        gridLayout.addWidget(secondLabel3, 7, lv1 )
        gridLayout.addWidget(secondEdit3, 7, lv2 )
        gridLayout.addWidget(frameLabel3, 8, lv1 )
        gridLayout.addWidget(frameEdit3, 8, lv2 )

        self.setLayout(gridLayout)

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


