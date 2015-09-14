# zombies.py
# temporarily saved to NPC folder as example of Non Player Characters
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

goals = ['eat brains', 'move to sound', 'move to light']

params['speed']=0.5     # they move slowly and attack slowly
params['hit']=0.2       # zombies are terrible shots
params['dodge']=0.0     # no dodge
params['dmg']=99999     # massive damage (death actually) if bitten
params['dmg_delay']=10  # you have 10 moves from bite before death

params['actions'] = ['shuffle', 'lunge', 'bite']
params['move_actions'] = ['shuffle', 'lunge']
params['attack_actions'] = ['bite']

