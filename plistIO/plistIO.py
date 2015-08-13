# -*- coding=utf-8 -*-
import os
import time
import json
from plistlib import *
# create tree and create the file.json, return the file name
Map = {}
import random

def findFather(pos, text):
    while pos != None and unicode(pos.text(0)) != text:
        pos = pos.parent()
    return pos


def after_modify(func):
    def inner(*args, **kwargs):
        treeNode, file_json, root = func(*args, **kwargs)
        if not treeNode:return False
        # modify last value
        va_fa = findFather(treeNode, u'values')
        treeNode = va_fa.child(va_fa.childCount() - 1)
        if va_fa:
            ani_fa = va_fa.parent()
            if not ani_fa:return False
            lay_fa = findFather(ani_fa, u'layer1')
            if not lay_fa: lay_fa = findFather(ani_fa, u'head')
            if not lay_fa: lay_fa = findFather(ani_fa, u'subtitle1')
            if not lay_fa: lay_fa = findFather(ani_fa, u'foot')
            if not lay_fa: return False
            switch = {'straightline':u'position', 'scale':u'scale', 'opacity':u'opacity', 'rotate':None, 'still':None}
            name = switch[Map[unicode(ani_fa)][u'name']]
            if not name:return False
            Map[unicode(lay_fa)][name] = Map[unicode(va_fa)][-1]
            write_json(Map[str(root)], file_json)
            # TODO CHANGE WIDGETITEM IN TREELIST
            for i in range(lay_fa.childCount()):
                if unicode(lay_fa.child(i).text(0)) == unicode(name):
                    lay_fa.removeChild(lay_fa.child(i))
                    child = treeNode.clone()
                    child.setText(0, name)
                    lay_fa.insertChild(i, child)
                    child.setExpanded(True)
                    Map[str(child)] = Map[str(treeNode)]
        # modify animations/ starttime & duration
        st_fa = findFather(treeNode, u'starttime')
        if st_fa:
            ani_fa = st_fa.parent()
            if not ani_fa:return False
    return inner


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


def returnTrueData(data, type):
    if type == 'integer':
        return int(data)
    elif type == 'real':
        return float(data)
    elif type == 'string':
        return unicode(data)
    elif type == 'bool':
        if data == 'True':
            return True
        else:
            return False
    elif type == 'dict':
        return {}
    elif type == 'array':
        return []


def modify(addr, addrchild, node, file_json, root, changeType, index=None):
    Node = Map[str(addr)]
    NodeChild = Map[str(addrchild)]
    if changeType == 0:
        Node[node['Key']] = Node[node['PreKey']]
        Node.pop(node['PreKey'])
        Map[str(addrchild)] = Node[node['Key']]
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
            # print node['PreValue'] == u''
            if node['Type'] == 'integer':
                # index = Node.index(returnTrueData(node['PreValue'], node['PreType']))
                Node[index] = int(node['Value'])
            elif node['Type'] == 'string':
                # index = Node.index(returnTrueData(node['PreValue'], node['PreType']))
                Node[index] = str(node['Value'])
            elif node['Type'] == 'real':
                # index = Node.index(returnTrueData(node['PreValue'], node['PreType']))
                Node[index] = float(node['Value'])
            elif node['Type'] == 'bool':
                if node['Value'] == 'True':
                    # index = Node.index(returnTrueData(str(node['PreValue']), node['PreType']))
                    Node[index] = True
                else:
                    # index = Node.index(returnTrueData(str(node['PreValue']), node['PreType']))
                    Node[index] = False
            elif node['Type'] == 'dict':
                # index = Node.index(returnTrueData(node['PreValue'], node['PreType']))
                Node[index] = {}
            elif node['Type'] == 'array':
                # index = Node.index(returnTrueData(node['PreValue'], node['PreType']))
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
    def x(*args, **kwargs):
        return 1
    print x()
