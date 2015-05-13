# build_internet.py  

import os
import sys
import math
from random import randint 
import npc.web_users 

import aikif.environments.internet as mod_env

#import aikif.agents.explore.agent_web_user as agt

fldr = os.getcwd() + os.sep + 'data'  + os.sep + 'worlds' 

def main():
    """
    generates a virtual internet, sets pages and runs web_users on it
    """
    e = mod_env.Internet('VAIS - Load testing',  'Simulation of several websites')
    e.create(50)
    print(e)
    
    #Create some users to browse the web and load test website
    print(npc.web_users.params)
 
    # Run the users over the sites at various reading speeds
    # TODO 
    
main()
