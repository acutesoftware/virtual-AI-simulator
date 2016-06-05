#!/usr/bin/python3
# -*- coding: utf-8 -*-
# random_string_finder.py

import sys
import random

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler(__name__ + '.log')
handler.setLevel(logging.INFO)

words_to_find = ['MATHS', 'HELP', 'maths', 'ROCKS', 'Maths', 'Rules', 'LOL', 'WTF']


def main():
    #method1()
    #method2()
    get_found_locations()
    

def method1():
    for start_seed in range(1, 9999):
        random.seed(start_seed)
        if start_seed % 100 == 0:
            logger.debug('seed = ' + str(start_seed))
            sys.stdout.write('.') 
            sys.stdout.flush()
        garbage = ''.join([chr(random.randint(32,122)) for x in range(100000)])
        for word in words_to_find:
            if word in garbage:
                logger.info('found ' + word + ' in ' + str(start_seed))



def method2():
    for start_seed in range(1, 9999999):
        random.seed(start_seed)
        if start_seed % 1000 == 0:
            logger.debug('seed = ' + str(start_seed))
            sys.stdout.write('.') 
            sys.stdout.flush()
        garbage = ''.join([chr(random.randint(32,122)) for x in range(10)])
        for word in words_to_find:
            if word[0:len(word)] ==  garbage[0:len(word)]:
                logger.info('Starts with ' + word + ' in ' + str(start_seed))
                
  
def get_found_locations():
    """
    INFO:__main__:found HELP in 1572
    INFO:__main__:found MATHS in 1704
    INFO:__main__:found ROCKS in 1975
    #random.seed(1572)
    #garbage = ''.join([chr(random.randint(32,122)) for x in range(100000)])
    #wrd_location = garbage.find('HELP')
    #print(wrd_location) # 73834
    #print(garbage[wrd_location:wrd_location+4])  # HELP
    """
    #random.seed(1704)
    #garbage = ''.join([chr(random.randint(32,122)) for x in range(100000)])
    #wrd_location = garbage.find('MATHS')
    #print(wrd_location) # 73834
    #print(garbage[wrd_location:wrd_location+5])  # HELP
    
    random.seed(1704)
    print(''.join([chr(random.randint(32,122)) for x in range(100000)])[59741:59746])
    random.seed(1572)
    print(''.join([chr(random.randint(32,122)) for x in range(100000)])[73834:73838])
    
    random.seed(561240)
    print(''.join([chr(random.randint(32,122)) for x in range(3)]))  # WTF
    
    random.seed(706075)
    print(''.join([chr(random.randint(32,122)) for x in range(3)]))  # LOL
    
    
    
main()                