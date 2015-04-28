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

def TEST():
    """
    local test of parameters
    """
    for k,v in params.items():
        if k != 'desc_long':
            print(k.ljust(15) + ' = ' + str(v))
        
    
if __name__ == '__main__':        
    TEST()