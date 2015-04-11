# test_battle.py  written by Duncan Murray 9/4/2015

import unittest
import os
import sys
import time

test_folder = os.getcwd() + os.sep + 'test_results'
test_file = test_folder + os.sep + 'battle.txt'

# TODO ///////////////////////////////////////
# - remove these lines once VAIS packaged
# and replace with the following
# import vais.character as mod_char

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'vais') 
ref_folder = root_folder + os.sep + "data" 

sys.path.append(root_folder)

# END TODO //////////////////////////////////

import battle
import character
  
rules_file = ref_folder + os.sep + 'battle.rules'

  
class VaisBattleTest(unittest.TestCase):
    def setup(self):
        print('running battle tests')
        
    def test_01_traits(self):
        traits = character.CharacterCollection(ref_folder)
        self.assertEqual(len(str(traits)) > 800, True)  # Note - traits tested more in test_character
        
    def test_02_generate_random_character(self):
        traits = character.CharacterCollection(ref_folder)
        character1 = traits.generate_random_character()
        self.assertEqual(len(str(character1)) > 200, True)
        
    def test_03_battle_rules(self):
        rules = battle.BattleRules(rules_file)
        self.assertEqual(len(str(rules)) , 429)

        self.assertEqual(rules.all_rules['dmg_min'], '2')
    
    
    def test_04_battle_one_char(self):
        traits = character.CharacterCollection(ref_folder)
        c1 = traits.generate_random_character()
        c2 = traits.generate_random_character()
        rules = battle.BattleRules(rules_file)
        b = battle.Battle(c1, c2, traits, rules, print_console='No')
        self.assertEqual(len(str(b)) > 5, True)
        if c2.name in str(b) or c1.name in str(b):
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)
        
    def test_05_battle_multiple(self):
        traits = character.CharacterCollection(ref_folder)
        c1 = traits.generate_random_character()
        c2 = traits.generate_random_character()
        rules = battle.BattleRules(rules_file)
        sim = battle.BattleSimulator( c1, c2, traits, rules, 1000)
        if sim.winner == c2.name or sim.winner == c1.name:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main() 
    