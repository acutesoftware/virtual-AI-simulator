# trader.py

params = {}
params['name']='trader'   
params['desc_short']='traders will buy and sell items to players and other NPCs'
params['desc_long']="""
Traders buy and sell from shops or stalls / carts on the sides of roads.
They will harvest, collect and forage for objects and clean them up and 
sometimes turn them into useful or artistic items for sale.
"""

goals = ['money', 'forage']

params['speed']=1.0     

params['actions'] = ['collect', 'forage', 'buy', 'clean', 'paint', 'sell']
params['move_actions'] = ['walk', 'amble']

nps_pos = [30,78]    # random pos for farmer - overwritten when module used
taget_pos = [50,50]    # random pos for target - overwritten when module used
