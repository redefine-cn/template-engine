# -*- coding=utf-8 -*-
import qiniu
import urllib
import urllib2
ACCESS_KEY = "vUQlBXXwgYNrGLunTtVbEi40TGU41MvT8rw8N2Qj"
SECRET_KEY = "fvoi1qSXnMlwpD1mG5hBkFdvoBUOLfHMPdG4FUTm"
bucket_name = "doco"
pre_url = 'http://7xir3h.com2.z0.glb.qiniucdn.com/'
url = ""
#解析结果
def parseRet(retData, respInfo):
    print retData
    if retData != None:
        return retData["key"]
    else:
        return "error"
def upload_without_key(bucket, filePath):
    auth = qiniu.Auth(ACCESS_KEY, SECRET_KEY)
    upToken = auth.upload_token(bucket, key=None)
    retData, respInfo = qiniu.put_file(upToken, None, filePath)
    return parseRet(retData, respInfo)

def file_upload(file):
    print "transport file :"
    print file
    url = upload_without_key(bucket_name, file)
    URL = pre_url + url
    print URL

def login(username, password, ip):
    user = dict()
    user['username'] = username
    user['password'] = password
    post_url = str(ip)
    post_data = urllib.urlencode(user)
    req = urllib2.urlopen(post_url, post_data)
    content = req.read()
    print content

def http_upload(file, ip):
    #定义传送的数据
    data = {}
    data['file'] = file
    data['video_script_id'] = "1"
    #定义post的地址
    url = str(ip)
    post_data = urllib.urlencode(data)
    #提交，发送数据
    req = urllib2.urlopen(url, post_data)
    #获取提交后返回的信息
    content = req.read()
    print content

def ftp_upload(file, ip, username, password):
    data = {}
    data['username'] = username
    data['password'] = password
    url = str(ip)
    post_data = urllib.urlencode(data)
    #提交，发送数据
    req = urllib2.urlopen(url, post_data)
    #获取提交后返回的信息
    content = req.read()
    print content
