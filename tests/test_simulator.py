# test_simulator.py  written by Duncan Murray 28/4/2015

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

test_folder = os.getcwd() + os.sep + 'test_results'
test_file = test_folder + os.sep + 'battle.txt'

#rules_file = ref_folder + os.sep + 'battle.rules'
  
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
        
    def test_03_SimGameOfLife(self):
        traits = character.CharacterCollection(ref_folder)
        a1 = traits.generate_random_character()
        world = planet.Planet('SimWorld', num_seeds=5, width=20, height=15, wind=0.3, rain=0.10, sun=0.3, lava=0.4)
        actions = ['walk']
        s = simulator.SimAdventureGame('Test of SimWorld', world, [a1], [(2,2)], actions)
        s.run()
        print(s)
        self.assertEqual(len(str(s)), 143)  
    
        
if __name__ == '__main__':
    unittest.main() 
         
        
