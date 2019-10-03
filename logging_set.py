# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:01:53 2019

@author: user
"""

import logging 
import time

from logging.handlers import RotatingFileHandler

def create_rotating_log(path):
    #creates a rotating log
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    #add a rotating handler
    handler = RotatingFileHandler(path, maxBytes =20,
                                  backupCount = 5)
    logger.addHandler(handler)
    
    for i in range(10):
        logger.info("This is test log time %s" % i)
        time.sleep(1.5)
        
if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)