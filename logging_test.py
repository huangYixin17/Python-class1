# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:14:47 2019

@author: user
"""

import logging
import time
from logging.handlers import TimedRotatingFileHandler

def create_timed_rotating_log(path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(path,
                                       when='m',
                                       interval = 1,
                                       backupCount = 5)
    logger.addHandler(handler)
    for i in range(20):
        logger.info("This is a test!")
        time.sleep(1.5)
if __name__ =="__main__":
    log_file = "tomed_test.log"
    create_timed_rotating_log(log_file)