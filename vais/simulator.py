# simulator.py
import os
import sys
import planet
import character

def TEST():
    """
    testing base class
    """
    traits = character.CharacterCollection(os.getcwd() + os.sep + 'data')
    a1 = traits.generate_random_character()
    a2 = traits.generate_random_character()
    a3 = traits.generate_random_character()
    world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
    actions = ['walk', 'run', 'fight', 'buy', 'sell', 'collect']
    s = Simulator('Test of SimWorld', world, [a1, a2, a3], actions)
    print(s)
    
class Simulator():
    """
    Base simulator class
    """
    def __init__(self, name, world, agents, actions):
        self.name = name
        self.world = world
        self.agents = agents
        self.actions = actions
        self.events = []
        #self.log = aikif.log
        self.log = []
     
    def __str__(self):
        res = ' -= ' + self.name + ' =--\n'
        res += 'world   = ' + self.world.name + ' (' + str(self.world.grid_width) + 'x' + str(self.world.grid_height) + ')\n'
        res += 'agents  = ' + str(len(self.agents)) + ' (' + ','.join([c.name for c in self.agents]) + ')\n'
        res += 'actions = [' + ', '.join([a for a in self.actions]) + ']\n'
        return res
        
   
        
        
if __name__ == '__main__':        
    TEST()
        