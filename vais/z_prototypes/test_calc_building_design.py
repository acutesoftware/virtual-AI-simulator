#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_calc_building_design.py

import unittest
import sys
import os

import calc_building_design as mod_des

class CalcBuildingDesignTest(unittest.TestCase):
    

    def test_01_instantiate(self):
        #self.assertEqual(len(str(self.c)) , 4) 
        pass
 
    def test_10_rafter_410UB53_7(self):
        ans = mod_des.bld_rafter_deflection(length=16000, force=6.72, E_mod_elasticity=2.1, I_moment_of_intertia=188)
        self.assertEqual(ans['max deflection - distrib load'] , 145.24822695035462) 
        self.assertEqual(ans['max deflection - centre load'] ,  0.014524822695035461) 
 
    def test_11_rafter_530UB82(self):
        ans = mod_des.bld_rafter_deflection(length=16000, force=6.72, E_mod_elasticity=2.1, I_moment_of_intertia=477)
        self.assertEqual(ans['max deflection - distrib load'] , 57.24668064290706) 
        self.assertEqual(ans['max deflection - centre load'] ,  0.005724668064290706) 
 

if __name__ == '__main__':
    unittest.main()
