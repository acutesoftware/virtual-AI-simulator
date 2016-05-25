#!/usr/bin/python3
# -*- coding: utf-8 -*-
# calc_building_design.py
# 
# Example show how a program can be managed in VAIS
# This program does engineering calculations that can 
# be called with different parameters to test different
# scenarios.

from pprint import pprint

def main():
    print('calc_building_design')
    w = int(input('enter building width : '))
    l = int(input('enter building length : '))
    

    res = calc_structure(width=w, length=l, height=2.4, prevailing_wind=3.2)
    pprint(res)
    
def calc_structure(width, length, height, prevailing_wind=2.8 ):   
    """
    calculate various aspects of the structure 
    (WARNING - these are not complete engineering specs, 
     rather guideline as exercise for this software)
    """
    area = width * length
    perim =  2 * width + 2 * length
    roof_cladding = area
    wall_cladding = perim * height
    
    return ({'area':area, 'perim':perim, 'roof_cladding':roof_cladding, 'wall_cladding':wall_cladding})
    
if __name__ == '__main__':
    main()