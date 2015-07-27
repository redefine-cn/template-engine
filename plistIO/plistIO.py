# -*- coding=utf-8 -*-
import sys
import codecs
from os.path import isfile
import json
from plistlib import *


def update_plist(node):
    f = file('../plistIO/data.json')
    data = json.load(f)

    parent = []
    parent_get = node['parent']
    for i in range(len(parent_get)):
        parent.append(parent_get[len(parent_get) - i - 1])
    if node['Type'] == 'dict':
        node['Value'] = dict()
    elif node['Type'] == 'array':
        node['Value'] = list()
    elif node['Type'] == 'integer':
        node['Value'] = int(node['Value'])
    pos = data
    for i in range(len(parent)):
        pos = pos[parent[i]]
    if len(parent) >= 1:
        if node['Key'] == 'ARRAY':
            pos.append(node['Value'])
        else:
            pos[node['Key']] = node['Value']
    else:
        if node['Key'] == 'ARRAY':
            data.append(node['Value'])
        else:
            data[node['Key']] = node['Value']
    write_json(data)

def write_json(data):
    json.dump(data, open('../plistIO/data.json', 'w'))

def save_plist(path):
    f = file('../plistIO/data.json')
    data = json.load(f)
    writePlist(data, path)

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