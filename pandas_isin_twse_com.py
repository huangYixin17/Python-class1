# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:02:11 2019

@author: user
"""

import pandas as pd
df=pd.read_html("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2",encoding = "big5hkscs" ,header = 0)
newdf = df[0][df[0]['產業別']>"0"]
#del newdf['國際證券辨識號碼(ISIN Code)'],newdf['CFICode'],newdf['備註']
del newdf['CFICode'],newdf['備註']
df2=newdf['有價證卷代碼及名稱'].str.split(' ',expand=True)
df2 = df2.reset_index(drop=True)
newdf = newdf.reset_index(drop=True)
for i in df2.index:
    if '  ' in df2.iat[i,0]:
        df2.iat[i,1]=df2.iat[i,0].split('  ')[1]
        df2.iat[i,0]=df2.iat[i,0].split('  ')[0]
newdf=df2.join(newdf)
newdf=newdf.rename(colums = {0:"股票代號",1:"股票名稱"})
del newdf['有價證卷代號及名稱']
newdf.to_excel("pandas_isin_twse_com",sheet_name='Sheet1',index=False)
