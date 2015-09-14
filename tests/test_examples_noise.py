#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_examples_noise.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = os.path.join(root_folder, 'vais', 'examples')
sys.path.append(pth)

import example_noise


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_01_function_get_name(self):
        tot_land, tot_sea, freq = example_noise.create_random_terrain(78, 22)
        print('random terrain : tot_land=',tot_land , ' tot_sea=', tot_sea, ' freq=',  freq  )
        self.assertEqual(tot_land > 6, True)  # random name so make sure it is a string
        self.assertEqual(tot_sea > 6, True)  # random name so make sure it is a string
        self.assertEqual(freq > 0, True)  # random name so make sure it is a string


if __name__ == '__main__':
    unittest.main()
