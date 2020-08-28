#!/usr/bin/python3
# -*- coding: utf-8 -*-
# npc_generator.py
# module used to manage NPC's in VAIS

import random
import importlib


# danger mode
num_farmers = 4
num_zombies = 3
num_bandits = 5
num_traders = 2

# peaceful mode
num_farmers = 7
num_zombies = 1
num_bandits = 1
num_traders = 3

# grid size
min_x = 3
min_y = 3
max_x = 47
max_y = 11


def TEST():
    print('NPC simulator...')
    my_npcs = NPCs()
    print(my_npcs)


class NPCs(object):
    """
    generates and manages the full list of NPC's based on definitions from 
    npc subfolder and counts above.
    """
    def __init__(self):
        self.npc_def = []
        for _ in range(0,num_farmers):
            self.npc_def.append(self.generate_npc('farmers'))
        for _ in range(0,num_zombies):
            self.npc_def.append(self.generate_npc('zombies'))
        for _ in range(0,num_bandits):
            self.npc_def.append(self.generate_npc('bandits'))
        for _ in range(0,num_traders):
            self.npc_def.append(self.generate_npc('trader'))
        
        
    def __str__(self):
        res = 'List of my NPCs\n'
        for n in self.npc_def:
            res += str(n) + '\n'
        return res 

    def generate_npc(self, character_file):
        """

        """
        my_npc = {}
        mod_npc_def = importlib.import_module('npc.' + character_file)
        my_npc['type'] = mod_npc_def.params['name']
        my_npc['name'] = self.random_name()
        my_npc['coord_x'] = random.randint(min_x,max_x)
        my_npc['coord_y'] = random.randint(min_y,max_y)
        my_npc['goal'] = random.choice(mod_npc_def.goals)
        my_npc['mood'] = random.choice(['happy', 'sad', 'angry'])
        #my_npc['desc'] = mod_npc_def.params['desc_short']
        
        
        
        return my_npc

    def random_name(self):
        res = random.choice('BCDFGHJKLMNPRSTVW')
        res += random.choice(['al', 'or', 'en', 'au', 'ea', 'oa', 'ul', 'el'])
        res += random.choice(['orn', 'al', 'int', 'pot', 'wal', 'mor'])
        return res


if __name__ == '__main__':
	TEST()
