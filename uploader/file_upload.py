# -*- coding=utf-8 -*-
import qiniu
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
