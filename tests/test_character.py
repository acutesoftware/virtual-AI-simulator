# test_character.py  written by Duncan Murray 5/4/2015

import unittest
import os
import sys


test_folder = os.getcwd() + os.sep + 'test_results'
test_file = test_folder + os.sep + 'character.txt'

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

import character
                    
class VaisCharacterTest(unittest.TestCase):
    def setup(self):
        print('running character tests')
        
    def test_01_create_character(self):
        c1 = character.Character( 'Bob', 'Human', 'Warrior', [], ['fishing', 'charge'], 'just a test char', ['Apple', 'string', 'sword', 'ring of ice'])
        try:
            #os.remove(test_file)
            pass
        except:
            pass
        
        self.assertEqual(len(str(c1)), 171)
        
    def test_02_get_properties(self):
        c2 = character.Character( 'Jan', 'Elf', 'Mage', [], ['fireball', 'teleport'], 'another test char', ['Orange', 'wand', 'dagger'])
        self.assertEqual(c2.name, 'Jan')
        self.assertEqual(c2.race, 'Elf')
        self.assertEqual(c2.skills[0], 'fireball')
        self.assertEqual(c2.skills[1], 'teleport')
        self.assertEqual(c2.story, 'another test char')
        self.assertEqual(c2.inventory[0], 'Orange')
        self.assertEqual(c2.inventory[1], 'wand')
        self.assertEqual(c2.inventory[2], 'dagger')
        
    def test_03_character_collection(self):
        traits = character.CharacterCollection(ref_folder)
        self.assertEqual(len(str(traits)) > 1234, True)
        self.assertEqual(len(traits.races.dat) , 8)
        
        
if __name__ == '__main__':
    unittest.main()        