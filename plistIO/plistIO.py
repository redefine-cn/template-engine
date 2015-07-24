import sys
from PyQt4 import QtGui, QtCore
import codecs
from os.path import isfile


class PlistIO(QtGui.QWidget):
    def __init__(self):
        super(PlistIO, self).__init__()
        self.setWindowTitle("hello")
        self.resize(500, 500)
        grid_layout = QtGui.QGridLayout()
        button1 = QtGui.QPushButton("button1")
        grid_layout.addWidget(button1, 0, 0, 1, 3)
        self.setLayout(grid_layout)
        QtCore.QObject.connect(button1, QtCore.SIGNAL("clicked()"), self.file_save)

    def file_save(self):
        fd = QtGui.QFileDialog(self)
        new_file = fd.getSaveFileName()
        if new_file:
            s = codecs.open(new_file, 'w', 'utf-8')
            text = "test save file"
            s.write(unicode(text))
            s.close()


app = QtGui.QApplication(sys.argv)
my_window = PlistIO()
my_window.show()
app.exec_()
