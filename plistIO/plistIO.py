# -*- coding=utf-8 -*-
import os
import time
import json
from plistlib import *

# create tree and create the file.json, return the file name
Map = {}
import random
def new_tree():
    data = {}
    seed = (str(time.time()) + str(random.random() * 10000))
    # print random.random()
    file_name = 'new' + str(seed) + '.json'
    new_json = "../tmp_data/" + file_name
    json.dump(data, open(new_json, 'w'))
    return unicode(file_name)
# add node info to the tree

def add(addr, addrchild, node, file_json, root):
    try :
        Node = Map[str(addr)]
    except KeyError:
        Map[str(addr)] = {}
        Node = Map[str(addr)]
    if type(Node) == type({}):
        if node['Type'] == 'dict':
            Node[(node['Key'])] = {}
        elif node['Type'] == 'array':
            Node[(node['Key'])] = []
        else:
            if node['Type'] == 'integer':
                Node[(node['Key'])] = int(node['Value'])
            elif node['Type'] == 'string':
                Node[(node['Key'])] = (node['Value'])
            elif node['Type'] == 'real':
                Node[(node['Key'])] = float(node['Value'])
            elif node['Type'] == 'bool':
                if node['Value'] == 'True':
                    Node[node['Key']] = True
                else:
                    Node[node['Key']] = False
            else:
                Node[(node['Key'])] = (node['Value'])
        Map[str(addrchild)] = Node[(node['Key'])]
    elif type(Node) == type([]):
        if node['Type'] == 'dict':
            Node.append({})
        elif node['Type'] == 'array':
            Node.append([])
        else:
            if node['Type'] == 'integer':
                Node.append(int(node['Value']))
            elif node['Type'] == 'string':
                Node.append((node['Value']))
            elif node['Type'] == 'real':
                Node.append(float(node['Value']))
            elif node['Type'] == 'bool':
                if node['Value'] == 'True':
                    Node.append(True)
                else:
                    Node.append(False)
            else:
                Node.append((node['Value']))
        Map[str(addrchild)] = Node[-1]
    # print node
    write_json(Map[str(root)], file_json)

def delete(addr, addrchild, node, file_json, root):
    Node = Map[str(addr)]
    NodeChild = Map[str(addrchild)]
    if type(Node) == type({}):
        Node.pop(node['Key'])
    else:
        Node.remove(NodeChild)
    write_json(Map[str(root)], file_json)

def modify(addr, addrchild, node, file_json, root, changeType):
    Node = Map[str(addr)]
    NodeChild = Map[str(addrchild)]
    if changeType == 0:
        Node.pop(node['PreKey'])
        add(addr, addrchild, node, file_json, root)
    else:
        if type(Node) == type({}):
            if node['Type'] == 'integer':
                Node[(node['Key'])] = int(node['Value'])
            elif node['Type'] == 'string':
                Node[(node['Key'])] = (node['Value'])
            elif node['Type'] == 'real':
                Node[(node['Key'])] = float(node['Value'])
            elif node['Type'] == 'bool':
                if node['Value'] == 'True':
                    Node[node['Key']] = True
                else:
                    Node[node['Key']] = False
            elif node['Type'] == 'dict':
                Node[node['Key']] = {}
            elif node['Type'] == 'array':
                Node[node['Key']] = []
            Map[str(addrchild)] = Node[node['Key']]
        else:
            if node['Type'] == 'integer':
                index = Node.index(int(node['Value']))
                Node[index] = int(node['Value'])
            elif node['Type'] == 'string':
                index = Node.index(str(node['Value']))
                Node[index] = str(node['Value'])
            elif node['Type'] == 'real':
                index = Node.index(float(node['Value']))
                Node[index] = float(node['Value'])
            elif node['Type'] == 'bool':
                if node['Value'] == 'True':
                    index = Node.index(True)
                    Node[index] = True
                else:
                    index = Node.index(False)
                    Node[index] = False
            elif node['Type'] == 'dict':
                index = Node.index(node['Value'])
                Node[index] = {}
            elif node['Type'] == 'array':
                index = Node.index(node['Value'])
                Node[index] = []
            Map[str(addrchild)] = Node[index]
    write_json(Map[str(root)], file_json)

# insert the data to the file.json
def write_json(data, file_json):
    # print file_json
    # print data
    json.dump(data, open(unicode('../tmp_data/') + file_json, 'w'))

# save file while the tree was completed
def save_plist(file_save, file_json):
    json_data = file(unicode('../tmp_data/') + file_json)
    file_S = file(file_save, 'w')
    data = json.load(json_data)
    writePlist(data, file_S)

# read file.plist and create corresponding file.json & return file name
def read_plist(path):
    seed = int(time.time())
    read_data = readPlist(path)
    file_name = path.replace(':', "").replace("/", "_").split('.')[0] + str(seed) + '.json'
    new_json = "../tmp_data/" + file_name
    json.dump(read_data, open(new_json, 'w'))
    # print read_data
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
    read_plist("c:/test.xml")
