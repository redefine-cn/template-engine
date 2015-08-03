# -*- coding=utf-8 -*-
import os
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import poster
import qiniu
import urllib
import urllib2
import cookielib
import zipfile
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

def get_file_directory(path):
    path_array = str(path).split(os.sep)
    path_array.remove(path_array[-1])
    fa = os.sep.join(path_array)
    return fa

def zip_directory(path):
    z = zipfile.ZipFile(unicode(path) + unicode(os.sep + 'test_zip.zip'), 'w')
    filelist = []
    if os.path.isfile(path):
       filelist.append(path)
    else:
       for root, dirs, files in os.walk(unicode(path)):
           for name in files:
               filelist.append(os.path.join(root, name))
    for tar in filelist:
        arcname = tar[len(path):]
        z.write(tar, arcname)
    z.close()
    return unicode(path) + unicode(os.sep + 'test_zip.zip')

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
opener = ''
def login_session(username, password, ip):
    print username, password, ip
    global opener
    opener = poster.streaminghttp.register_openers()
    opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    values = {'username': username, 'password': password}
    datagen, headers = poster.encode.multipart_encode(values)
    request = urllib2.Request(ip, datagen, headers)
    try:
        result_login = urllib2.urlopen(request)
        login_content = result_login.read()
        print login_content
        if login_content == "error":
            print "sorry, login failed"
            return u"对不起，登录失败"
        else:
            if login_content == "success":
                return "success"
            else:
                return u"检查服务器是否正确"
    except urllib2.URLError:
        return u"网络连接错误"
    except ValueError:
        return u"检查地址是否正确"

def http_upload(ip, file, file_name=u"模版文件", cover_file=None, video_script_id=1):
    # print username, password
    # username = 'devil'
    # password = '123456'
    # # Enable cookie support for urllib2
    # cookiejar = cookielib.CookieJar()
    # urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    # # Send username/password to the site and get the session cookie
    # values = {'username': username, 'password': password}
    # data = urllib.urlencode(values)
    # request = urllib2.Request("http://123.57.206.52/myadmin/login/", data)
    # url = urlOpener.open(request)  # Our cookiejar automatically receives the cookies
    # print url
    # # page = url.read(500000)
    # # Make sure we are logged in by checking the presence of the cookie "id".
    # # (which is the cookie containing the session identifier.)
    # for cookie in cookiejar:
    #     print cookie.name
    # if not 'sessionid' in [cookie.name for cookie in cookiejar]:
    #     raise ValueError, "Login failed with username=%s, password=%s" % (username, password)
    # print "We are logged in !"
    # # Make another request with our session cookie
    # # (Our urlOpener automatically uses cookies from our cookiejar)

    # opener = poster.streaminghttp.register_openers()
    # opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    # values = {'username': username, 'password': password}
    # datagen, headers = poster.encode.multipart_encode(values)
    # request = urllib2.Request("http://123.57.206.52/myadmin/login/", datagen, headers)
    # result_login = urllib2.urlopen(request)
    # login_content = result_login.read()
    # if login_content == "error":
    #     print "sorry, login failed"
    #     return "login_error"
    print file_name
    print ip
    url_t = str(ip)
    if cover_file is None:
        file_data = {'file_videoScript': open(file, "rb"), 'name': file_name}
    else:
        file_data = {"file": open(cover_file, 'rb'), "video_script_id": video_script_id}
    datagen, headers = poster.encode.multipart_encode(file_data)
    request = urllib2.Request(url_t, datagen, headers)
    try:
        result_upload = urllib2.urlopen(request)
    except urllib2.URLError:
        return u"网络连接错误"
    except ValueError:
        return u"请检查地址是否正确"
    upload_content = result_upload.read()
    print upload_content
    if upload_content == "error":
        print "sorry, upload failed"
        return u"上传失败，请检查改网站是否需要登录或者重新上传"
    else:
        try:
            return_id = int(upload_content)
        except:
            return u"检查服务器连接"
    return upload_content

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
    ip = "http://123.57.206.52/upload_videoScript/"
    fileUpload = 'C:\Users\Administrator\Desktop\models\蔚蓝之境'
    # print fileUpload
    # print http_upload(fileUpload, "test_pyqt", ip, "devil", "11111")
    zip_directory(fileUpload)