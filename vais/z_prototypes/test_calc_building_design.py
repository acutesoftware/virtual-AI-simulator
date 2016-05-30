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
        
    def test_30_calc_basics_1_by_1(self):
        ans = mod_des.calc_basics(width=1, length=1, height=2.4, prevailing_wind=2.8)
        #print(ans)
        self.assertEqual(ans['area'] , 1) 
        self.assertEqual(ans['perim'] , 4) 
        self.assertEqual(ans['roof_cladding'] , 1) 
        self.assertEqual(ans['wall_cladding'] , 9.6) 

    def test_31_calc_basics_2_by_20(self):
        ans = mod_des.calc_basics(width=2, length=20, height=2.4, prevailing_wind=2.8)
        #print(ans)
        self.assertEqual(ans['area'] , 40) 
        self.assertEqual(ans['perim'] , 44) 
        self.assertEqual(ans['roof_cladding'] , 40) 
        self.assertEqual(ans['wall_cladding'] , 105.6) 


    def test_32_calc_basics_2_by_20_tall(self):
        ans = mod_des.calc_basics(width=2, length=20, height=2.7)
        #print(ans)
        self.assertEqual(ans['area'] , 40) 
        self.assertEqual(ans['perim'] , 44) 
        self.assertEqual(ans['roof_cladding'] , 40) 
        self.assertEqual(ans['wall_cladding'] , 118.80000000000001) 


if __name__ == '__main__':
    unittest.main()
