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
        c1 = character.Character( 'Bob', 'Human', 'Warrior', {'STR':7, 'CON':8, 'STA':5, 'AGI':8, 'INT':5}, ['fishing', 'charge'], 'just a test char', ['Apple', 'string', 'sword', 'ring of ice'])
        try:
            #os.remove(test_file)
            pass
        except:
            pass
        
        self.assertEqual(len(str(c1)), 213)
        
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
        self.assertEqual(len(str(traits)) > 800, True)
        self.assertEqual(len(traits.races.dat) > 7, True)
        self.assertEqual(len(traits.classes.dat) > 5, True)
        self.assertEqual(len(traits.skills.dat) > 11, True)
        self.assertEqual(len(traits.stats.dat) > 2, True)
        self.assertEqual(len(traits.stories.dat) > 2, True)
        self.assertEqual(len(traits.inventory.dat) > 5, True)
        
        # Random samples of data - comment out if needed, or if order changes
        self.assertEqual(traits.stats.dat[0]['stat'] , 'STA')
        self.assertEqual(traits.stats.dat[2]['name'] , 'Intellect')
        self.assertEqual(traits.races.dat[0]['name'] , 'Human')
        self.assertEqual(traits.races.dat[1]['name'] , 'Half-Elf')
        self.assertEqual(traits.classes.dat[0]['name'] , 'Warrior')
        self.assertEqual(traits.classes.dat[1]['name'] , 'Mage')
        self.assertEqual(traits.classes.dat[2]['name'] , 'Priest')
        self.assertEqual(traits.classes.dat[3]['name'] , 'Ranger')
        self.assertEqual(traits.classes.dat[0]['name'] , 'Warrior')
        self.assertEqual(traits.skills.dat[4]['name'] , 'Heal')
        self.assertEqual(traits.stories.dat[0]['name'] , 'A young scholar with a burning desire to learn')
        self.assertEqual(traits.inventory.dat[0]['name'] , 'leaf')
        
        
if __name__ == '__main__':
    unittest.main()        