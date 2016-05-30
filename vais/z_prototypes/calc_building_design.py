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
    
    
def calc_basics(width=-1, length=-1, height=2.4, prevailing_wind=2.8):   
    """
    calculate various aspects of the structure 
    """
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
 

def bld_rafter_deflection(length=-9, force=-9, E_mod_elasticity=-9, I_moment_of_intertia=-9):
    """
    calculate rafter deflections - see test_calc_building_design.py for 
    Sample values for equations below from Structures II course
    """
    
    
    if length == -9:
        length = float(input('enter rafter length : '))
        
    if force == -9:
        force = float(input('enter Force or weight applied to roof : '))
    
    if E_mod_elasticity == -9:
        E_mod_elasticity = float(input('enter modulus of elasticity x10**5 (Steel beam example=2.1) : '))
    
    if I_moment_of_intertia == -9:
        I_moment_of_intertia = float(input('enter members "moment of intertia x10**6" (for Steel beam 410UB53.7=188 ) :'))
        
    res = {}
    
    res['max deflection - centre load'] =  (1 * force * (length ** 3)) / (48  * (E_mod_elasticity * 10**5) * (I_moment_of_intertia * 10**6))
    res['max deflection - distrib load'] = (5 * force * (length ** 4)) / (384 * (E_mod_elasticity * 10**5) * (I_moment_of_intertia * 10**6))
    
    pprint(res)
    return res


 
if __name__ == '__main__':
    main()