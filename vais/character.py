# character.py  written by Duncan Murray 3/4/2015

import os
import random
fldr = os.getcwd() + os.sep + 'data'  


def TEST():
    """
    Module to handle character creation
    """
    print('creating random character')
    traits = CharacterCollection()
    print(traits)
    c = traits.generate_random_character('Zoltar')
    print(c)
    
    
class CharacterCollection():
    """
    Class to handle all the character traits
    """
    def __init__(self):
        """
        loads all the ref_*.csv files relating 
        to character traits
        """
        print('loading data files')
        self.stats = ['STA', 'INT', 'STR', 'CON', 'CHA', 'Health', 'XP']
        self.skills = read_file(fldr + os.sep + 'ref_skills.csv')
        self.story = ['A new character enters the game']
        self.inventory = read_file(fldr + os.sep + 'ref_objects.csv')
         
    
    def __str__(self):
        res = '=== DUMP OF ALL CHARACTER TRAITS ===\n'
        res += '\nSTATS = ' + ', '.join([s for s in self.stats])
        res += '\nStory = ' + ', '.join([s for s in self.story])
        res += '\nSKILLS = ' + ', '.join([s for s in self.skills])
        res += '\nINVENTORY = ' + ', '.join([s for s in self.inventory])
        return res
        
    def generate_random_character(self, name):
        """
        uses the traits to create a random, but plausible
        character
        """
        stats = []
        skills = []
        story = []
        inventory = ['5 gold']
        
        # pick random stuff here 
        for i in range(5):
            inventory.append(self.inventory[random.randint(0,len(self.inventory)-1)])
        
        return Character(name, stats, skills, story, inventory)


class Character():
    """
    character class
    """
    def __init__(self, name, stats, skills, story, inventory):
        """
        all params except name is a list
        """
        self.name = name
        self.stats = stats
        self.skills = skills
        self.story = story
        self.inventory = inventory

    def __str__(self):
        res = 'CHARACTER: ' + self.name + '\n'
        res += '\nSTATS = ' + ', '.join([s for s in self.stats])
        res += '\nStory = ' + ', '.join([s for s in self.story])
        res += '\nSKILLS = ' + ', '.join([s for s in self.skills])
        res += '\nINVENTORY = ' + ', '.join([s for s in self.inventory])
        return res
        

        
############################
#  Utility functions 

def read_file(fname):
    """
    read a CSV file (ref_classes.csv) and return the 
    list of names
    """
    lst = []
    with open(fname, 'r') as f:
        hdr = f.readline()
        for line in f:
            lst.append(line)
    return lst
    
def read_file_1st_col_only(fname):
    """
    read a CSV file (ref_classes.csv) and return the 
    list of names
    """
    lst = []
    with open(fname, 'r') as f:
        hdr = f.readline()
        for line in f:
            lst.append(line.split(',')[0])
    return lst
        
if __name__ == '__main__':
    TEST()    
 