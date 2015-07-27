# -*- coding=utf-8 -*-
import sys
import codecs
from os.path import isfile
import json
from plistlib import *


def update_plist(parent, child, new_data):
    f = file('../template-engine/settings.json')
    data = json.load(f)
    aim = None
    p_len = len(parent)
    for i in range(p_len - 1):
        if aim is None:
            aim = data[parent[i]]
        else:
            aim = aim[parent[i]]
    aim[parent[p_len - 1]] = new_data
    writePlist(data, "c:/zhaolong/test.xml")


def read_plist(path):
    pl = readPlist(path)
    print pl
    json.dump(pl, open('../template-engine/settings.json', 'w'))

def read_json(data):
    for key in data.keys():
        print data[key]

def ftp_login(username, password):
    if username == "test" and password == "test":
        return "success"
    else:
        return "failure"

if __name__ == '__main__':
    data = {}
    data['parent'] = "1"
    data['child'] = "01"
    data['data'] = "test_data"
    parent = []
    parent.append("segment1")
    parent.append("starttime")
    parent.append("second")
    # update_plist(parent, 1, data)
    read_plist("c:/zhaolong/test.xml")