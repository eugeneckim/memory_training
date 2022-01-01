#!/usr/bin/python
import logging as logger
from orgparse import load, loads



def load_file(filename):
    x = load(filename)
    for y in x.children:
        logger.info(y.body)

def setup_logging():
    logger.getLogger('logger')
    logger.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y/%m/%d-%H:%M:%S', level=logger.INFO)
    return logger
    
if __name__ == "__main__":
    setup_logging()
    filename = '/Users/eugene/everything/development/memory_training/enchiridion/enchiridion.org'
    load_file(filename)
    
