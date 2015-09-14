#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_npc_zombies.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = os.path.join(root_folder, 'vais', 'npc')
sys.path.append(pth)

import zombies


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_module(self):
        self.assertEqual(zombies.params['name'], 'zombie')
        self.assertEqual(zombies.params['attack_actions'] , ['bite'])


if __name__ == '__main__':
    unittest.main()
