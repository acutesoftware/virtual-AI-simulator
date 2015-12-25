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

class VaisPlanetTest(unittest.TestCase):
    def test_01_create_planet(self):
        p = planet.Planet('Planet001', num_seeds=5, width=20, height=15, wind=0.1, rain=0.50, sun=0.4, lava=0.2)
        p.evolve(years=1000000)
        print(p)
        self.assertEqual(str(p)[0:24], '\n-- Welcome to Planet001')

    def test_02_large_planet(self):
        p2 = planet.Planet('Planet002', num_seeds=8, width=20, height=150, wind=0.5, rain=0.90, sun=0.6, lava=0.5)
        p2.evolve(years=1000000)
        self.assertEqual(str(p2)[0:24], '\n-- Welcome to Planet002')

    
if __name__ == '__main__':
    unittest.main()        