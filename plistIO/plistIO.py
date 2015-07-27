# -*- coding=utf-8 -*-
import sys
import codecs
from os.path import isfile
import json
from plistlib import *


def update_plist(node):
    f = file('../plistIO/data.json')
    data = json.load(f)

    new_data = {}
    parent = []
    parent_get = node['parent']
    for i in range(len(parent_get)):
        parent.append(parent_get[len(parent_get) - i - 1])
    print parent
    # if node['Type'] == "integer":
    #     new_data[node['Key']] = int(node['Value'])
    # elif node['Type'] == "dict":
    #     new_data[node['Key']] = dict()
    # elif node['Type'] == 'array':
    #     new_data[node['Key']] = list()
    # else:
    #     new_data[node['Key']] = node['Value']
    if node['Type'] == 'dict':
        node['Value'] = dict()
    elif node['Type'] == 'array':
        node['Value'] = list()
    elif node['Type'] == 'integer':
        node['Value'] = int(node['Value'])
    print data
    pos = data
    for i in range(len(parent)):
        pos = pos[parent[i]]
    print pos
    if len(parent) >= 1:
        if node['Key'] == 'ARRAY':
            pos.append(node['Value'])
        else :
            pos[node['Key']] = node['Value']
    else :
        if node['Key'] == 'ARRAY':
            data.append(node['Value'])
        else :
            data[node['Key']] = node['Value']
    writePlist(data, "c:/test.xml")
    # read_plist("c:/test.xml")

def read_plist(path):
    pl = readPlist(path)
    print pl
    json.dump(pl, open('../plistIO/data.json', 'w'))

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
    # data['parent'] = "1"
    # data['child'] = 10
    # data['data'] = "test_data"
    parent = []
    # parent.append("segment1")
    # parent.append("starttime")
    # parent.append("second")
    node = {'parent': ['segment1', 'starttime', 'second'], 'Type': 'integer', 'Value': '10', 'Key': 'child'}
    parent_get = node['parent']
    for i in range(len(parent_get)):
        parent.append(parent_get[i])
    if node['Type'] == "integer":
        data[node['Key']] = int(node['Value'])
    else:
        data[node['Key']] = node['Value']
    update_plist(parent, 1, data)
    # read_plist("c:/zhaolong/test.xml")