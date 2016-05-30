# test_vais.py
# test_character.py  written by Duncan Murray 5/4/2015

import unittest
import os
import sys
import time

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)
import character
import planet


ref_folder = root_folder + os.sep + "data" 

# overwrite  module level variable 'fldr' with correct path
planet.fldr = ref_folder
                  
class VaisTest(unittest.TestCase):
    def setup(self):
        print('Overall test for VAIS')
        
    def test_01_character(self):
        traits = character.CharacterCollection(ref_folder)
        c = traits.generate_random_character()
        self.assertEqual(len(str(c)) > 100, True)

    def test_02_planet(self):
        p = planet.Planet('vais_test_planet', num_seeds=5, width=20, height=15, wind=0.2, rain=0.20, sun=0.2, lava=0.5)
        self.assertEqual(len(str(p)) > 10, True)
        
    def test_03_planet_evolve(self):
        """
        NOTE - p.evolve() has errors as there is path in module
        """
        p = planet.Planet('vais_test_planet', num_seeds=4, width=60, height=35, wind=0.4, rain=0.5, sun=0.5, lava=0.5)
        p.evolve(years=100000)

        self.assertTrue(os.path.exists(os.path.join(ref_folder, 'vais_test_planet.txt')))
        
if __name__ == '__main__':
    unittest.main()        