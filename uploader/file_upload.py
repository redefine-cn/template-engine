# -*- coding=utf-8 -*-
import qiniu
import urllib
import urllib2
import cookielib
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
    return content

def http_upload(file, file_name, ip):
    username = 'devil'
    password = '123456'

    # Enable cookie support for urllib2
    cookiejar = cookielib.CookieJar()
    urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

    # Send username/password to the site and get the session cookie
    values = {'username': username, 'password': password}
    data = urllib.urlencode(values)
    request = urllib2.Request("http://123.57.206.52/myadmin/login/", data)
    url = urlOpener.open(request)  # Our cookiejar automatically receives the cookies
    print url
    page = url.read(500000)

    # Make sure we are logged in by checking the presence of the cookie "id".
    # (which is the cookie containing the session identifier.)
    for cookie in cookiejar:
        print cookie.name
    if not 'id' in [cookie.name for cookie in cookiejar]:
        raise ValueError, "Login failed with username=%s, password=%s" % (username, password)

    print "We are logged in !"

    # Make another request with our session cookie
    # (Our urlOpener automatically uses cookies from our cookiejar)

    #定义传送的数据
    data_t = {}
    data_t['file_videoScript'] = file
    data_t['name'] = file_name
    #定义post的地址
    url_ = str(ip)
    post_data = urllib.urlencode(data)
    #提交，发送数据
    # req = urllib2.urlopen(url, post_data)
    req = urlOpener.open(url_, post_data)
    #获取提交后返回的信息
    content = req.read()
    print content
    return content

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

if __name__ == "__main__":
    http_upload("http://123.57.206.52/upload_videoScript", "test_pyqt", "http://123.57.206.52/upload_videoScript")