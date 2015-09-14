#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_npc_web_users.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = os.path.join(root_folder, 'vais', 'npc')
sys.path.append(pth)

import web_users


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_module(self):
        self.assertEqual(web_users.params['name'], 'web_users')
        self.assertEqual(web_users.params['actions'] ,  ['browse', 'search', 'download', 'post'])

    def test_02_function_get_name(self):
        random_name = web_users.get_name()
        print('random_name of web_user = ' + random_name)
        self.assertEqual(len(random_name) > 6, True)  # random name so make sure it is a string


if __name__ == '__main__':
    unittest.main()
