# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:32:47 2019

@author: user
"""

"""
在小視窗打以下文字,可以爬網址的內容
"""

import requests

#取回200是他們的狀態值 ,如果是404,405就是錯誤
print(requests.get("http://httpbin.org/get"))
print(requests.post("http://httpbin.org/post",data={'key':'10'}))
print(requests.put("http://httpbin.org/put"))
print(requests.delete("http://httpbin.org/delete"))
print(requests.head("http://httpbin.org/get"))
print(requests.options("http://httpbin.org/get"))

