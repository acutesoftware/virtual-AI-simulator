#!/usr/bin/python3
# -*- coding: utf-8 -*-
# calc_building_design.py
# 
# Example show how a program can be managed in VAIS
# This program does engineering calculations that can 
# be called with different parameters to test different
# scenarios.

from pprint import pprint

fn = {  'x':[' x = exit', 'exit()'],
        '1':[' 1 = basic structure', 'calc_basics()'],
        '2':[' 2 = Rafter deflection', 'bld_rafter_deflection()' ],
     }
  

def main():
    print(' --- calc_building_design --- ')
    menu = []
    for k,v in fn.items():
        menu.append(v[0])
    for menuitem in sorted(menu):
        print(menuitem)
    a = input('enter selection : ')
    eval(fn[a][1])
    
    
def calc_basics(width=-1, height=-1):   
    """
    calculate various aspects of the structure 
    """
    height=2.4
    prevailing_wind=2.8
    if width == -1:
        width = int(input('enter building width : '))
    if length == -1:
        length = int(input('enter building length : '))
    res = {}
    
    res['area'] = width * length
    res['perim'] =  2 * width + 2 * length
    res['roof_cladding'] = res['area']
    res['wall_cladding'] = res['perim'] * height
    pprint(res)
    return res
 

def bld_rafter_deflection():
    """
    calculate rafter deflections
    """
    l = float(input('enter rafter length : '))
    f = float(input('enter Force or weight applied to roof : '))
#    E = float(input('enter modulus of elasticity x10**5 (Steel beam example=2.1) : '))
#    I = float(input('enter members "moment of intertia x10**6" (for Steel beam 410UB53.7=188 ) :'))
    E = 2.1
    I = 188
    res = {}
    
    res['max deflection - centre load'] = (f * (l ** 3)) / 48 * (E * 10**5) * (I * 10**6)
    res['max deflection - distrib load'] = (5 * f * (l ** 4)) / 384 * (E * 10**5) * (I * 10**6)
    
    pprint(res)
    return res
 

 
if __name__ == '__main__':
    main()