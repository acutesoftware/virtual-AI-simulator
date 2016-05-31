# test_grid_walk.py
# Integration test example - in separate folder 
# to allow local system/integration tests that 
# would likely fail on travis-CI

import unittest
import os
import sys
import time


root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + 'vais') 
sys.path.append(root_folder)

import planet
import character   

ref_folder = root_folder + os.sep + "data" 

# overwrite  module level variable 'fldr' with correct path
planet.fldr = ref_folder
 
   
class IntegrationTestGridWalk(unittest.TestCase):
    def setup(self):
        print('Integration test for VAIS - Grid Walk')
        
    def test_01_create_planet(self):
        p = planet.Planet('planet_grid_walk', num_seeds=4, width=70, height=22, wind=0.5, rain=0.3, sun=0.5, lava=0.2)
        p.evolve(years=10000)
        print(p)
        self.assertEqual(str(p)[0:31], '\n-- Welcome to planet_grid_walk')
        


        
if __name__ == '__main__':
    unittest.main()        