#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_simulator.py

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'vais') 
ref_folder = root_folder + os.sep + "data" 
sys.path.append(root_folder)

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
        traits = character.CharacterCollection(ref_folder)
        a1 = traits.generate_random_character()
        a2 = traits.generate_random_character()
        a3 = traits.generate_random_character()
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk', 'run', 'fight', 'buy', 'sell', 'collect']
        s = simulator.SimAdventureGame('Test of SimWorld', world, [a1, a2, a3], [(2,2), (3,4), (4,4)], actions)
        s.run()
        self.assertEqual(len(str(s)), 231)  
        

    def test_02_move_character(self):
        """
        add a single character to a world and move them around
        """
        traits = character.CharacterCollection(ref_folder)
        a1 = traits.generate_random_character()
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk']
        s = simulator.SimAdventureGame('Test of SimWorld', world, [a1], [(2,2)], actions)
        s.run()
        self.assertEqual(len(str(s)), 143)  
        self.assertEqual(s.agent_locations[0]['x'], 2)  
        self.assertEqual(s.agent_locations[0]['y'], 2)  
        s.command({'name':'walk', 'type':'move', 'direction':[0,1]}, a1)
        self.assertEqual(s.agent_locations[0]['x'], 2)  
        self.assertEqual(s.agent_locations[0]['y'], 2)  
        
        s.command({'name':'walk', 'type':'move', 'direction':[1,1]}, a1)
        s.command({'name':'run', 'type':'run', 'direction':[2,1]}, a1)
        s.command({'name':'fight', 'type':'fight', 'direction':[2,1]}, a1)
       
        
    def test_03_sim_fail(self):
        self.assertNotEqual(1, 2)  
    
    def test_05_run_aikif_agent(self):
        """
        recreates agent list as per world_generator and puts them in a world.
        NOTE - uses World object, not planet
        """
        import math
        from random import randint
        import aikif.agents.explore.agent_explore_grid as agt

        log_folder = os.path.join( os.getcwd(), 'test_results')
        
        myWorld = worlds.World( 40, 40, ['.','X','#'])
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
    
    
    
    def test_11_SimGameOfLife(self):
        traits = character.CharacterCollection(ref_folder)
        a1 = traits.generate_random_character()
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk']
        s = simulator.SimAdventureGame('Test of Game of Life', world, [a1], [(2,2)], actions)
        s.run()
        print(s)
        self.assertEqual(len(str(s)), 147)  
        
        
    
    def test_21_SimAdventureGame(self):
        traits = character.CharacterCollection(ref_folder)
        a1 = traits.generate_random_character()
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk']
        s = simulator.SimAdventureGame('Test of SimAdventureGame', world, [a1], [(2,2)], actions)
        s.run()
        print(s)
        self.assertEqual(len(str(s)), 151)  
        
    
if __name__ == '__main__':
    unittest.main() 
         
        
