# simulation_types.py
# shows the list of simulations currently catered for

sim_types = []
sim_types.append({'type':'parameters_only', 'desc':'allows agent interactions without a world'})
sim_types.append({'type':'game_adventure', 'desc':'rogue type adventure games played on grid'})
sim_types.append({'type':'game_of_life', 'desc':'conways game of life in a grid based simulation'})
sim_types.append({'type':'evolution', 'desc':'npcs are plants / animals which grow in world'})

 
def TEST():
    for s in sim_types:
        print(s['type'].ljust(15), ':',s['desc'])
 
if __name__ == '__main__':
    TEST()
