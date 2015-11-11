# test_character.py  written by Duncan Murray 5/4/2015

import unittest
import os
import sys
import time
import vais.character as character

test_folder = os.getcwd()
test_file = test_folder + os.sep + 'character.txt'
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'vais') 
ref_folder = root_folder + os.sep + "data" 


class VaisCharacterTest(unittest.TestCase):
    def setup(self):
        print('running character tests')
        
    def test_01_create_character(self):
        c1 = character.Character( 'Bob', 'Human', 'Warrior', {'my_cool_stat':3,'STR':7, 'CON':8, 'STA':5, 'AGI':8, 'INT':5}, ['fishing', 'charge'], 'just a test char', ['Apple', 'string', 'sword', 'ring of ice'])
        
        c1.save_to_file(test_file)
        self.assertEqual(os.path.exists(test_file), True)
        self.assertEqual(os.path.getsize(test_file) > 120, True)
        self.assertEqual(len(str(c1)) > 114, True)
        
        # now check the parameters of the test character are in the correct place
        self.assertEqual(c1.name, 'Bob')
        self.assertEqual(c1.race, 'Human')
        self.assertEqual(c1.ch_class, 'Warrior')
        self.assertEqual(c1.stats['STR'], 7)
        self.assertEqual(c1.stats['CON'], 8)
        self.assertEqual(c1.stats['STA'], 5)
        self.assertEqual(c1.stats['AGI'], 8)
        self.assertEqual(c1.stats['INT'], 5)
        
        
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
        
    def test_04_character_collection(self):
        c2 = character.Character( 'Jane', 'Elf', 'Mage', {'my_cool_stat':3,'STR':7, 'CON':8, 'STA':5, 'AGI':8, 'INT':5}, ['network engineer', 'shoot'], 'random text', ['Rogue on 360k FDD', 'sword', 'Can of coke'])
        c2.save_to_file(test_folder + os.sep + 'character_sample.txt')
        
        # now create a new random character, then populate that from saved data for Jane
        traits = character.CharacterCollection(ref_folder)
        c3 = traits.generate_random_character()
        # confirm that the new random character is NOT the same as previous character (name not in list)
        self.assertEqual(c3.name == 'Jane', False)
        
        # overide the random character with our saved version
        c3.load_from_file(test_folder + os.sep + 'character_sample.txt')
        self.assertEqual(c3.name == 'Jane', True)
        
        
    
if __name__ == '__main__':
    unittest.main()        