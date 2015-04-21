# zombies.py
# saved to NPC folder as example of Non Player Characters
# in VAIS
params = {}
params['name']='zombie'   # can also be used to track diseases spreading
params['desc_short']='zombies roam and kill players - avoid or become infected!'
params['desc_long']="""
Zombies are walking the earth - they kill players when overrun (generally 2 or more)
although they move slowly.
They move by random travelling, and are attracted to noises and human smells (less than 4 cells)
Zombies can be killed only by headshot (hit>80%)
"""

params['speed']=0.5
params['hit']=0.2
params['dodge']=0.0
params['dmg']=99999



def TEST():
    """
    local test of parameters
    """
    for k,v in params.items():
        if k != 'desc_long':
            print(k.ljust(10) + ' = ' + str(v))
        
        
TEST()