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
print('root_folder = ', root_folder )
ref_folder = root_folder + os.sep + "data" 
print('ref_folder = ', ref_folder )

sys.path.append(root_folder)

# END TODO //////////////////////////////////

import battle
import character
  
rules_file = ref_folder + os.sep + 'battle.rules'

  
class VaisBattleTest(unittest.TestCase):
    def setup(self):
        print('running battle tests')
        
    def test_01_battle_init(self):
        traits = character.CharacterCollection(ref_folder)
        character1 = traits.generate_random_character()
        character2 = traits.generate_random_character()
        #print(character1)
        #print(character2)
        rules = battle.BattleRules(rules_file)
        #print(rules.all_rules['dmg_max'])
        #print(rules)
        
        b = battle.Battle(character1, character2, traits, rules, print_console='No')
        #print(b.status)
        self.assertEqual(len(str(b)) > 5, True)
        
    
if __name__ == '__main__':
    unittest.main() 
    