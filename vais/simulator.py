#!/usr/bin/python3
# -*- coding: utf-8 -*-
# simulator.py

class Simulator(object):
    """
    Base simulator class
    """
    def __init__(self, name, world, agents, actions):
        self.name = name
        self.world = world
        self.actions = actions
        self.events = []
        self.log = []
        self.status = 'Started'
        self.agents = agents
        self._verify_agents()
        #self.agent_locations = agent_locations #[]
        #for num, a in enumerate(self.agents):
        #    print('Sim __init__, agent num:', num, ' = ', a)
        #    ag_loc = {}
        #    ag_loc['name'] = a.name
        #    ag_loc['x'] = agent_locations[num][0]
        #    ag_loc['y'] = agent_locations[num][1]
        #    self.agent_locations.append(ag_loc)
     
    def __str__(self):
        res = ' -= ' + self.name + ' =--\n'
        res += 'world   = ' + self.world.name + ' (' + str(self.world.grid_width) + 'x' + str(self.world.grid_height) + ')\n'
        res += 'actions = [' + ', '.join([a for a in self.actions]) + ']\n'
        res += 'agents  = ' + str(len(self.agents)) + ' (' + ','.join([c.name for c in self.agents]) + ')\n'
        res += 'agent_locations\n'
        for a in self.agents:
            res += 'Agent: ' + a.name + '\n'
            print('agent a = ', str(a))
            print('coords = ', a.coords)
            for c,v in a.coords.items():
                res += '  coord ' + str(c) + ' = ' + str(v) + '\n'
        return res + '\n'
    
    def _verify_agents(self):
        """
        verify agents passed to simulator by:
        1. checking for unique names
        2. TODO - other checks if needed
        """
        #print('verifying...')
        nmes = []
        for a in self.agents:
            #print('a = ', a)
            nmes.append(a.name)
        if len(nmes) == len(set(nmes)):
            return True
        print('Error - you need to pass unique list of agent names to simulator')
        return False
            
    


    
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
        print(src, 'says ' + cmd['type']  + ' agent', agent.name, '', cmd['direction'],' password=', password)
        if cmd['type'] == 'move':
            print(agent.name, 'moves in direction', cmd['direction'])
            #x,y = self._get_location(agent.name)
            #self._set_location(agent.name, x + cmd['direction'][0], y + cmd['direction'][0] )
        elif cmd['type'] == 'run':
            print(agent.name, 'runs in direction', cmd['direction'])
        elif cmd['type'] == 'fight':
            print(agent.name, 'fights')
            
    def _move_agent(self, agent, direction, wrap_allowed=True):
        """
        moves agent 'agent' in 'direction'
        """
        
        #self._set_location(agent, direction[0], direction[0])
        print ('TODO')
        print('moving agent to x,y=', direction, 'wrap_allowed = ', wrap_allowed)
    
    
class SimAdventureGame(Simulator):
    def __init__(self, name, world, agents, actions):
        Simulator.__init__(self, name, world, agents, actions)
        
    def __str__(self):
        return 'Adventure Game ' + Simulator.__str__(self)
    
class SimGameOfLife(Simulator):
    def __init__(self, name, world, agents, actions):
        Simulator.__init__(self, name, world, agents, actions)
        
    def __str__(self):
        return 'GAME OF LIFE ' + Simulator.__str__(self)
        
