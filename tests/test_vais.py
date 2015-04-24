# test_vais.py
# test_character.py  written by Duncan Murray 5/4/2015

import unittest
import os
import sys
import time
import vais.character as character
import vais.planet as planet

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'vais') 
ref_folder = root_folder + os.sep + "data" 
                  
class VaisTest(unittest.TestCase):
    def setup(self):
        print('Overall test for VAIS')
        
    def test_01_character(self):
        traits = character.CharacterCollection(ref_folder)
        c = traits.generate_random_character()
        self.assertEqual(len(str(c)) > 100, True)

    def test_02_planet(self):
        p = planet.Planet('Divitie', num_seeds=5, width=20, height=15, wind=0.2, rain=0.20, sun=0.2, lava=0.5)
        self.assertEqual(len(str(p)) > 10, True)
        
    def test_03_planet_evolve(self):
        """
        NOTE - p.evolve() has errors as there is path in module
        """
        p = planet.Planet('Divitie', num_seeds=5, width=20, height=15, wind=0.2, rain=0.20, sun=0.2, lava=0.5)
        # p.evolve(years=10000000)
        print('TODO = p.evolve(years=10000000)')
    
if __name__ == '__main__':
    unittest.main()        