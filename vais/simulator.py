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
    s = SimAdventureGame('Test of SimWorld', world, [a1, a2, a3], [(2,2), (3,4), (4,4)], actions)
    print(s)
    s.run()
    s.command({'name':'walk', 'type':'move', 'direction':[0,1]}, a1)
    s.command({'name':'walk', 'type':'move', 'direction':[1,1]}, a2)
    s.command({'name':'attack', 'type':'fight', 'direction':[1,1]}, a3)
    
class Simulator():
    """
    Base simulator class
    """
    def __init__(self, name, world, agents, agent_locations, actions):
        self.name = name
        self.world = world
        self.actions = actions
        self.events = []
        #self.log = aikif.log
        self.log = []
        self.status = 'Started'
        self.agents = agents
        self._verify_agents()
        self.agent_locations = {}
        for num, a in enumerate(self.agents):
            print('a.name = ', a.name)
            self.agent_locations[a.name] = agent_locations
            print('self.agent_locations[a.name]',self.agent_locations[a.name])
     
    def __str__(self):
        res = ' -= ' + self.name + ' =--\n'
        res += 'world   = ' + self.world.name + ' (' + str(self.world.grid_width) + 'x' + str(self.world.grid_height) + ')\n'
        res += 'actions = [' + ', '.join([a for a in self.actions]) + ']\n'
        res += 'agents  = ' + str(len(self.agents)) + ' (' + ','.join([c.name for c in self.agents]) + ')\n'
        res += 'agent_locations\n'
        for a in self.agent_locations:
            res += '\nagent ' + str(a[0]) + str(a[1])
        return res
    
    def _verify_agents(self):
        """
        verify agents passed to simulator by:
        1. checking for unique names
        2. TODO - other checks if needed
        """
        print('verifying...')
        nmes = []
        for a in self.agents:
            nmes.append(a.name)
        if len(nmes) != len(set(nmes)):
            raise 'Error - you need to pass unique list of agent names to simulator'
    
    def run(self, num_iterations=-1):
        """
        Abstract method to be subclassed by calling function.
        This runs the simulation num_iterations times.
        If the default -1 is used for num_iteractions this means
        it is a turn based simulation which is controlled externally
        (e.g. for a game with players, or run by the class BattleSimulator)
        
        """
        
        if num_iterations == -1:    # controlled fully externally   
            self.status = 'Waiting for Command'
            return
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
        print(src, 'says ' + cmd['type']  + ' agent', agent.name, '', cmd['direction'])
        if cmd['type'] == 'move':
            print(agent.name, 'moves in direction', cmd['direction'])
        elif cmd['type'] == 'run':
            print(agent.name, 'runs in direction', cmd['direction'])
        elif cmd['type'] == 'fight':
            print(agent.name, 'fights')
            
    def _move_agent(self, agent, direction, wrap_allowed=True):
        """
        moves agent 'agent' in 'direction'
        """
    
    
class SimAdventureGame(Simulator):
    def __init__(self, name, world, agents, agent_locations, actions):
        Simulator.__init__(self, name, world, agents, agent_locations, actions)
        
    def __str__(self):
        return 'Adventure Game ' + Simulator.__str__(self)
    
class SimGameOfLife(Simulator):
    def __init__(self, name, world, agents, agent_locations, actions):
        Simulator.__init__(self, name, world, agents, agent_locations, actions)
        
    def __str__(self):
        return 'GAME OF LIFE ' + Simulator.__str__(self)
        
if __name__ == '__main__':        
    TEST()
        