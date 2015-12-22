#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_planet.py 

import unittest
import os
import sys
import time

test_folder = os.getcwd()
test_file = test_folder + os.sep + 'character.txt'
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'vais') 
ref_folder = root_folder + os.sep + "data" 

sys.path.append(root_folder)

import planet 

class VaisCharacterTest(unittest.TestCase):
    def setup(self):
        print('running planet tests')
        
    def test_01_create_planet(self):
        p = planet.Planet('Divitie', num_seeds=5, width=20, height=15, wind=0.1, rain=0.50, sun=0.4, lava=0.2)
        p.evolve(years=10000000)
        print(p)

    def test_02_large_planet(self):
        p2 = planet.Planet('Jupiter', num_seeds=8, width=200, height=150, wind=0.5, rain=0.90, sun=0.6, lava=0.5)
        p2.evolve(years=10000000)
        #p2.save()
        print(p2)

    
if __name__ == '__main__':
    unittest.main()        