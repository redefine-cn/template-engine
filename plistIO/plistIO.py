# -*- coding=utf-8 -*-
import sys
import codecs
from os.path import isfile
import json
from plistlib import *


def update_plist():
    f = file('../template-engine/settings.json')
    data = json.load(f)
    writePlist(data, "c:/zhaolong/test.xml")

def read_plist(path):
    pl = readPlist(path)
    print pl
    json.dump(pl, open('../template-engine/settings.json', 'w'))

def ftp_login(username, password):
    if username == "test" and password == "test":
        return "success"
    else:
        return "failure"

if __name__ == '__main__':
    update_plist()
