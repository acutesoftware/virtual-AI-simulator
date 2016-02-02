#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_simulator.py

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'vais') 
ref_folder = root_folder + os.sep + "data" 
sys.path.append(root_folder)

import aikif.agents.agent as mod_agt

import planet as planet
import battle as battle
import character as character
import simulator as simulator
import worlds

test_folder = os.getcwd() + os.sep + 'test_results'
test_file = test_folder + os.sep + 'battle.txt'
  
class VaisSimulatorTest(unittest.TestCase):
    def setup(self):
        print('running simulator tests')
        
    def test_01_instantiate_sim(self):
    
        # make 3 agents
        a1 = mod_agt.Agent(name='a1', fldr=os.getcwd())
        a2 = mod_agt.Agent(name='a2', fldr=os.getcwd())
        a3 = mod_agt.Agent(name='a3', fldr=os.getcwd())
        # create 3 characters from the Character generator and assign to agents
        traits = character.CharacterCollection(ref_folder)
        a1.characteristics = traits.generate_random_character()
        a2.characteristics = traits.generate_random_character()
        a3.characteristics = traits.generate_random_character()

        
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk', 'run', 'fight', 'buy', 'sell', 'collect']
        s = simulator.SimAdventureGame('Test of SimWorld', world, [a1, a2, a3],  actions)
        s.run()
        self.assertEqual(len(str(s)), 354)  
        

    def test_02_move_character(self):
        """
        add a single character to a world and move them around
        """
        traits = character.CharacterCollection(ref_folder)
        a1 = mod_agt.Agent(name='a2', fldr=os.getcwd())
        a1.characteristics = traits.generate_random_character()
        world = planet.Planet('SimWorld', num_seeds=5, width=70, height=10, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        #world.build_random( 2, 30, 40, 1)
        
        actions = ['walk']
        s = simulator.SimAdventureGame('Test of SimWorld', world, [a1], actions)
        s.run()
        self.assertEqual(len(str(s)), 184)  
        
         
        s.command({'name':'walk', 'type':'move', 'direction':[1,1]}, a1)
        s.command({'name':'run', 'type':'run', 'direction':[2,1]}, a1)
        s.command({'name':'fight', 'type':'fight', 'direction':[2,1]}, a1)
       
        
    def test_03_sim_fail(self):
        self.assertNotEqual(1, 2)  
    
    def test_04_verify_agents(self):
        """
        check that a failed verify agent works
        simulator.Simulator('BadSim', name, world, agents, agent_locations, actions)
        """
        world = worlds.World( 40, 20, ['.','X','#'])
        world.build_random( 8, 40, 70, 30)
        agt1 = mod_agt.Agent(name='agt_9001', fldr=os.getcwd())
        agt2 = mod_agt.Agent(name='agt_9002', fldr=os.getcwd())
        agents = [agt1,agt2]

        agt1.set_coords({'x':2, 'y':1, 'z':0, 't':0})
        agt2.set_coords({'x':3, 'y':4, 'z':0, 't':0})
        
        actions = ['walk']
        
        s04 = simulator.Simulator('sim04', world, agents, actions)
        self.assertTrue(s04._verify_agents())
        
        # now add a duplicate agent name
        agents.append(agt1)
        print('DUPLICATE AGENT LIST = ', [str(a) for a in agents])
        self.assertFalse(s04._verify_agents())
        
        
    
    def test_05_run_aikif_agent(self):
        """
        recreates agent list as per world_generator and puts them in a world.
        NOTE - uses World object, not planet
        """
        import math
        from random import randint
        import aikif.agents.explore.agent_explore_grid as agt

        log_folder = os.path.join( os.getcwd(), 'test_results')
        
        myWorld = worlds.World( 70, 20, ['.','X','#'])
        myWorld.build_random( 5, 60, 30, 10)
        target_coords = [math.floor(myWorld.grd.grid_height/2) + randint(1, math.floor(myWorld.grd.grid_height/2)) - 3, \
             math.floor(myWorld.grd.grid_width /2) + randint(1, math.floor(myWorld.grd.grid_width/2)) - 5]
        agt_list = []
        for agt_num in range(0,4):

            ag = agt.ExploreAgent( 'exploring_agent' + str(agt_num),  log_folder, False,1)
            start_y, start_x = myWorld.grd.find_safe_starting_point()
            
            ag.set_world(myWorld.grd, [start_y, start_x], [target_coords[0], target_coords[1]])
            agt_list.append(ag)
        
    
        sim = worlds.WorldSimulation(myWorld, agt_list, 1)
        sim.run(9, 'Y', log_folder + os.sep)
        self.assertTrue(len(str(sim)) > 10)  
        #print(sim.agent_list[0].agent_locations)
        #print(sim.agent_list[0])
        
        self.assertFalse(agt_list[0].current_x == 4545) 
        self.assertFalse(agt_list[0].current_y == 9895) 
        
        agt_list[0].current_x = 4545
        agt_list[0].current_y = 9895
        
        self.assertEqual(agt_list[0].current_x, 4545) 
        self.assertEqual(agt_list[0].current_y, 9895) 
    
    
    def test_11_game_of_life(self):
        traits = character.CharacterCollection(ref_folder)
        a1 = mod_agt.Agent(name='Life', fldr=os.getcwd())
        a1.characteristics = traits.generate_random_character()  # No, this should not be a adventure character
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk']
        s = simulator.SimAdventureGame('Test of Game of Life', world, [a1], actions)
        s.run()
        print(s)
        self.assertTrue(len(str(s)) > 10)  
        
        
    
    def test_21_sim_adventure_game(self):
        traits = character.CharacterCollection(ref_folder)
        a21 = mod_agt.Agent(name='a1', fldr=os.getcwd())
        a21.characteristics = traits.generate_random_character()
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk']
        s = simulator.SimAdventureGame('Test of SimAdventureGame', world, [a21], actions)
        s.run()
        print(s)
        self.assertEqual(len(str(s)), 192)  
        
    
if __name__ == '__main__':
    unittest.main() 
         
        
