# -*- coding=utf-8 -*-
import os
import time
import json
from plistlib import *

# create tree and create the file.json, return the file name
Map = {}

def new_tree():
    data = {}
    seed = int(time.time())
    file_name = 'new' + str(seed) + '.json'
    new_json = "../tmp_data/" + file_name
    json.dump(data, open(new_json, 'w'))
    return file_name
# add node info to the tree
def add_node(node, file_json):
    json_data = file('../tmp_data/' + file_json)
    data = json.load(json_data)
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
    write_json(data, file_json)
# delete node from tree
root = ''
def add(addr, addrchild, node):
    try :
        Node = Map[str(addr)]
    except KeyError:
        Map[str(addr)] = {}
        Node = Map[str(addr)]
        global root
        root = str(addr)

    if type(Node) == type({}):
        if node['Type'] == 'dict':
            Node[str(node['Key'])] = {}
        elif node['Type'] == 'array':
            Node[str(node['Key'])] = []
        else:
            if node['Type'] == 'integer':
                Node[str(node['Key'])] = int(node['Value'])
            if node['Type'] == 'string':
                Node[str(node['Key'])] = str(node['Value'])
            if node['Type'] == 'real':
                Node[str(node['Key'])] = float(node['Value'])
        Map[str(addrchild)] = Node[str(node['Key'])]
    elif type(Node) == type([]):
        if node['Type'] == 'dict':
            Node.append({})
        elif node['Type'] == 'array':
            Node.append([])
        else:
            if node['Type'] == 'integer':
                Node.append(int(node['Value']))
            if node['Type'] == 'string':
                Node.append(str(node['Value']))
            if node['Type'] == 'real':
                Node.append(float(node['Value']))
        Map[str(addrchild)] = Node[len(Node) - 1]
    global root
    write_json(Map[root],'../plistIO/data.json')

def delete_node(node, file_json):
    json_data = file('../tmp_data/' + file_json)
    data = json.load(json_data)
    parent = []
    parent_get = node['parent']
    for i in range(len(parent_get)):
        parent.append(parent_get[len(parent_get) - i - 1])
    pos = data
    for i in range(len(parent)):
        pos = pos[parent[i]]
    pos.pop(node['Key'], None)
    write_json(data, file_json)
# insert the data to the file.json
def write_json(data, file_json):
    json.dump(data, open('../tmp_data/' + file_json, 'w'))
# save file while the tree was completed
def save_plist(file_save, file_json):
    json_data = file('../tmp_data/' + file_json)
    data = json.load(json_data)
    writePlist(data, file_save)
    os.remove(json_data)
# read file.plist and create corresponding file.json & return file name
def read_plist(path):
    seed = int(time.time())
    read_data = readPlist(path)
    file_name = path.replace(':', "").replace("/", "_").split('.')[0] + str(seed) + '.json'
    new_json = "../tmp_data/" + file_name
    json.dump(read_data, open(new_json, 'w'))
    return file_name

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
    # add_node(parent, 1, data)
    read_plist("c:/zhaolong/test.xml")