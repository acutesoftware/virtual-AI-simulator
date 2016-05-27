#!/usr/bin/python3
# -*- coding: utf-8 -*-
# calc_building_design.py
# 
# Example show how a program can be managed in VAIS
# This program does engineering calculations that can 
# be called with different parameters to test different
# scenarios.

from pprint import pprint

fn = {'1':[' 1 = basic structure', 'calc_structure()'],
      'x':[' x = exit', 'exit()'],
      }
  

def main():
    print(' --- calc_building_design --- ')
    for k,v in fn.items():
        print(v[0])
    a = input('enter selection : ')
    eval(fn[a][1])
    
    
def calc_structure( ):   
    """
    calculate various aspects of the structure 
    (WARNING - these are not complete engineering specs, 
     rather guideline as exercise for this software)
    """
    height=2.4
    prevailing_wind=2.8
    width = int(input('enter building width : '))
    length = int(input('enter building length : '))
    res = {}
    
    res['area'] = width * length
    res['perim'] =  2 * width + 2 * length
    res['roof_cladding'] = res['area']
    res['wall_cladding'] = res['perim'] * height
    pprint(res)
    return res
    
if __name__ == '__main__':
    main()