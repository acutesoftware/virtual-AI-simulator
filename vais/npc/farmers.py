# farmers.py

params = {}
params['name']='farmer'   
params['desc_short']='farmers plant crops, tend plants, harvest and sell the produce'
params['desc_long']="""
Farmers work on their own farms growing crops and livestock.
They harvest fruit and vegetables and sell them at the market.
"""

goals = ['plant', 'water', 'weed', 'harvest', 'sell']

params['speed']=0.8     

params['actions'] = ['plant', 'water', 'weed', 'harvest', 'sell']
params['move_actions'] = ['walk', 'amble']

nps_pos = [100,100]    # random pos for farmer - overwritten when module used
taget_pos = [50,50]    # random pos for target - overwritten when module used

# Custom actions for NPC below
#def action():    
#    pass
