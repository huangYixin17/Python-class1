# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:01:53 2019

@author: user
"""

import logging #為應用程式,函示酷的類別進行事件紀錄
#import time    #時間模組

#handler是log的輸出方式,import RotatingFileHandler是可以讓文件到達一定大小(檔案大小)
#新增一個新的文件,例如:test.log.1,test.log.2
from logging.handlers import RotatingFileHandler   

def create_rotating_log(path):
    #creates a rotating log
    logger = logging.getLogger("Rotating Log")  #輸出日誌的總對象
    logger.setLevel(logging.INFO)   #設定級別為"INFO",代表如果是Debug的錯誤,不會回傳
    
    #add a rotating handler 
    #path是路徑,maxBytes是文件大小'0'代表文件無限大,backupCount是保留文件test.log.5
    handler = RotatingFileHandler(path, maxBytes =10,
                                  backupCount = 5)
    logger.addHandler(handler)  #新增handler
    
    for i in range(10):
        logger.info("This is test log time %s" % i)
        #time.sleep(1.5)

#一開始預設會是"__main__"
if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)