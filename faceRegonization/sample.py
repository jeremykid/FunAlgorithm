# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "Bn7swhGpvtzxS9uMWG-0CkacJY-_gt-4"
secret = "tNCF8Wd-xjtw-qyQn47yjZh8RzLkVBkU"
filepath = r"./sample.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)

data.append('--%s' % boundary)
# print (data)
# '''
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
# data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
# data.append('gender')
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	print qrcont

except Exception,e:
	print 'http error',e
