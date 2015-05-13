# build_internet.py  

import os
import sys
import math
from random import randint 
import npc.web_users 

#import aikif.environments.internet as my_world

#import aikif.agents.explore.agent_web_user as agt

temp_folder = 'C:\\temp\\'

fldr = os.getcwd() + os.sep + 'data'  + os.sep + 'worlds' 

def main():
    """
    generates a virtual internet, sets pages and runs web_users on it
    
    myWorld = my_world.Internet( 5) 
    myWorld.build_random( 6)
    myWorld.grd.save(fldr + os.sep + 'vais_internet.txt')
    """

    
    #Create some users to browse the web and load test website
    print("TODO - wait for AIKIF 0.1.2 to be released")
    print(npc.web_users.params)
 
main()
