# bandits.py

params = {}
params['name']='bandit'   
params['desc_short']='bandits roam in groups and attack travellers, or steal from untended campsites'
params['desc_long']="""
Bandits attack kill players and usually travel in groups.
They move by random travelling, but can track travellers
"""

goals = ['steal', 'kills', 'track']

params['speed']=1     
params['hit']=2       
params['dodge']=4     
params['dmg']=12     
params['dmg_delay']=0 

params['actions'] = ['shoot', 'fight', 'walk', 'sprint']
params['move_actions'] = ['walk', 'sprint']
params['attack_actions'] = ['shoot', 'fight']

nps_pos = [100,100]    # random pos for bandit - overwritten when module used
taget_pos = [50,50]    # random pos for target - overwritten when module used

# Custom actions for NPC below
#def action():    
#    pass
