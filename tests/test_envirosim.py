#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_envirosim.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'vais'
sys.path.append(pth)

import envirosim


class TestEnvirosim(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        envirosim.main()
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
