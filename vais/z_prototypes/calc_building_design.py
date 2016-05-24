#!/usr/bin/python3
# -*- coding: utf-8 -*-
# calc_building_design.py
# 
# Example show how a program can be managed in VAIS
# This program does engineering calculations that can 
# be called with different parameters to test different
# scenarios.

def main():
    print('calc_building_design')
    w = int(input('enter building width : '))
    l = int(input('enter building length : '))
    
    print('area =  ', w * l)
    print('perim = ', 2 * w + 2 * l)

if __name__ == '__main__':
    main()