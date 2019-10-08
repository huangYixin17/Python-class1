# -*- coding: utf-8 -*-
import requests
import json
url = 'http://ifconfig.me/all.json'  #網址ifconfig.me的json檔
response = requests.get(url)
#print('Content-Length:', response.headers['Content-Length'])
response = json.loads(response.text)

#找自己的ip位置
print("ip: %s" % response['ip_addr'])
print('host：%s' % response['remote_host'])
print('user：%s' % response['user_agent'])
print('port：%s' % response['port'])
print('method：%s' % response['method'])
print('via：%s' % response['via'])
print('forwared：%s' % response['forwarded'])