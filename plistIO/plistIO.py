# -*- coding=utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import codecs
from os.path import isfile
import json
from plistlib import *


def update_plist():
    f = file('../template-engine/settings.json')
    data = json.load(f)
    writePlist(data, "c:/zhaolong/test.xml")

def read_plist():
    pl = readPlist("c:/zhaolong/test.xml")
    print pl
    json.dump(pl, open('../template-engine/settings.json', 'w'))


if __name__ == '__main__':
    update_plist()
