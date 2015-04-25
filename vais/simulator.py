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
    s = SimGameOfLife('Test of SimWorld', world, [a1, a2, a3], actions)
    print(s)
    s.run()
    s.command({'name':'walk', 'type':'move', 'direction':[0,1]}, a1)
    s.command({'name':'walk', 'type':'move', 'direction':[1,1]}, a2)
    s.command({'name':'attack', 'type':'fight', 'direction':[1,1]}, a3)
    
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
        self.status = 'Started'
     
    def __str__(self):
        res = ' -= ' + self.name + ' =--\n'
        res += 'world   = ' + self.world.name + ' (' + str(self.world.grid_width) + 'x' + str(self.world.grid_height) + ')\n'
        res += 'agents  = ' + str(len(self.agents)) + ' (' + ','.join([c.name for c in self.agents]) + ')\n'
        res += 'actions = [' + ', '.join([a for a in self.actions]) + ']\n'
        return res
    
    def run(self, num_iterations=1000):
        """
        Abstract method to be subclassed by calling function.
        This runs the simulation num_iterations times.
        """
        self.status = 'Running'
        print('Running Simulation... TODO = subclass this method in your calling class')
     
    def stop(self):
        self.status = 'Halted'
    
    def add_event(self, event):
        """
        events can be added at the start of the sim in advance
        or during the simulation by AI or user.
        """
        self.events.append(event)
    
    def get_state(self):
        """
        called in loop by GUI display to get current state of
        simulation
        """
        return self.world, self.status, self.log # no this isn't permanent
    
    def command(self, cmd, agent, src='admin', password=''):
        """
        takes a command from a source 'src' and if 
        access is allowed (future implementation) 
        then execute the command on the 'agent'
        """
        print('received', cmd['type'], 'command for agent', agent.name, 'from', src)
        
        
    
    
class SimGameOfLife(Simulator):
    def __init__(self, name, world, agents, actions):
        Simulator.__init__(self, name, world, agents, actions)
        
    def __str__(self):
        return 'GAME OF LIFE ' + Simulator.__str__(self)
        
if __name__ == '__main__':        
    TEST()
        