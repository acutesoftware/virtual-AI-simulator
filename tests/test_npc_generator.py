#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_npc_generator.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'vais'
sys.path.append(pth)

import npc_generator


class TestEnvirosim(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        #npc_generator.TEST()
        my_npcs = npc_generator.NPCs()

        self.assertTrue(len(my_npcs.npc_def) > 4)
        self.assertTrue(my_npcs.npc_def[0]['coord_x'] > 1)
        self.assertTrue(my_npcs.npc_def[0]['coord_y'] > 1)
        self.assertTrue(len(my_npcs.npc_def[0]['name']) > 4)
        

        for n in my_npcs.npc_def:
            #print(n['type'])
            self.assertTrue(n['type'] in ['farmer', 'trader', 'bandit', 'zombie', 'villager'])
 


if __name__ == '__main__':
    unittest.main()
