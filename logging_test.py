# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:14:47 2019

@author: user
"""

import logging
import time
from logging.handlers import TimedRotatingFileHandler  #隨著時間去創建一個新檔案

def create_timed_rotating_log(path):
    logger = logging.getLogger("Rotating Log")  #輸出日誌的總對象
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(path,
                                       when='m',  #每個分鐘
                                       interval = 1, #1分鐘
                                       backupCount = 5)  #共有5個文件
    logger.addHandler(handler)
    #會在timed_test.log顯示20個This is a test!
    for i in range(20): 
        logger.info("This is a test!  %s" % (i))
        time.sleep(1.5)
if __name__ =="__main__":
    log_file = "tomed_test.log"
    create_timed_rotating_log(log_file)