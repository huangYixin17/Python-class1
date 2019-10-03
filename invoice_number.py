# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:54:25 2019

@author: user
"""

from __future__ import unicode_literals, print_function 
import urllib
from bs4 import BeautifulSoup
import urllib.request

request_url = "http://invoice.etax.nat.gov.tw/"

htmlContent = urllib.request.urlopen(request_url).read()
soup = BeautifulSoup(htmlContent,"html.parser")
results = soup.find_all("span",class_="t18Red")
subTitle = ['特別獎','特獎','頭獎','增開六獎']
months = soup.find_all('h2',{'id':'tabTitle'})

month_new = months[0].find_next_sibling('h2').text

month_previous = months[0].find_next_sibling('h2').text

print("最新 ({0})".format(month_new))
for index,item in enumerate(results[:4]):
    print('>>{0} : {1}'.format(subTitle[index],item.text))
print("上期 ({0})".format(month_previous))
for index2,item2 in enumerate(results[4:8]):
    print('>>{0} : {1}'.format(subTitle[index2],item2.text))