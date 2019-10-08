# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:53:28 2019

@author: user
"""
"""
用url方式取的網址json檔,再將其印出
"""

#import re
import urllib
import urllib.request
import urllib.error

url = 'http://ifconfig.me/all.json' 
html = urllib.request.urlopen(url)
htmlcontent = html.read().decode('utf-8')
print(htmlcontent)