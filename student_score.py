# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:33:31 2019

@author: user
"""
"""
開啟socres.csv,並且輸出成績,平均
與student_w並用
"""

import csv

file = open('socres.csv' , newline='', encoding = 'utf-8')

f = csv.reader(file)
data = []

for row in f:
    while(row != []):
        data.append([row[0],int(row[1]),int(row[2]),int(row[3])])
        break
    
print("學生姓名  國文  英文  數學  平均")
print("-----------------------------")
for i in range(len(data)):
    print("%s %6d %4d %4d %4d" % ( data[i][0] , data[i][1] , data[i][2] , data[i][3] , (data[i][1]+data[i][2]+data[i][3])/3 ))

c = 0 
e = 0 
m = 0
for i in range(0,len(data)):
    c = c+data[i][1]
    e = e+data[i][2]
    m = m+data[i][3]
print("-----------------------------")
print("平均 %8d %4d %4d %4d" % (c/len(data),e/len(data),m/len(data),(c+e+m)/(3*len(data))))
    
file.close()