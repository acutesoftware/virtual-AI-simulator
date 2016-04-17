# AI_sample_game.py     written by Duncan Murray 26/4/2015

import os
import planet
import simulator
import character
import aikif.agents.agent as agt

class ReallySimpleGameAI():
    """
    simple example of an AI which walks characters
    in a world 
    """
    def __init__(self):
        p = planet.Planet('SimpleAIWorld', 5, 20, 10, 0.2, 0.2, 0.2, 0.5)
        traits = character.CharacterCollection(os.getcwd() + os.sep + 'data')
        #self.a1 = traits.generate_random_character()
        self.a1 = agt.Agent('Jack')
        self.a2 = agt.Agent('Jill')
        #print('type(self.a1) = ', type(self.a1))
        actions = ['walk', 'fight']
        self.s = simulator.Simulator('Test of SimWorld', p, [self.a1, self.a2], actions)
        self.s.run()  # with no params, it defaults to turn based mode
        
    def __str__(self):
        return str(self.s)
    
    def run(self):
        """
        This AI simple moves the characters towards the opposite
        edges of the grid for 3 steps or until event halts the 
        simulation
        """
        x, y = 1,0  # set the direction
        num_steps = 0
        while self.s.get_state() != 'Halted':
            self.s.command({'name':'walk', 'type':'move', 'direction':[x, y]}, self.a1)
            self.s.command({'name':'walk', 'type':'run', 'direction':[x, y+1]}, self.a2)
            num_steps += 1
            if num_steps >= 3:
                break
        for a in self.s.agents:
            print(a.name, 'finished at position ', a.coords['x'], a.coords['y'])
        
        
if __name__ == '__main__':
    my_game = ReallySimpleGameAI()
    my_game.run()

 