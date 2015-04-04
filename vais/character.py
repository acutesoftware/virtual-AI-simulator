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
    #print(traits)
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
        self.races = read_file(fldr + os.sep + 'ref_races.csv')
        self.classes = read_file(fldr + os.sep + 'ref_classes.csv')
        self.stats = ['STA', 'INT', 'STR', 'CON', 'CHA', 'Health', 'XP']
        self.skills = read_file(fldr + os.sep + 'ref_skills.csv')
        self.stories = read_file(fldr + os.sep + 'ref_stories.csv')
        self.inventory = read_file(fldr + os.sep + 'ref_objects.csv')
         
    
    def __str__(self):
        res = '=== DUMP OF ALL CHARACTER TRAITS ===\n'
        res += '\Classes = ' + ', '.join([s for s in self.classes])
        res += '\nRaces = ' + ', '.join([s for s in self.races])
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
        ch_class = random.choice(self.classes)
        race = random.choice(self.races)
        stats = self.random_stats(race, ch_class)
        skills = []
        story = random.choice(self.stories)
        inventory = ['5 gold']
        
        # pick random stuff here 
        for i in range(3):
            inventory.append(self.inventory[random.randint(0,len(self.inventory)-1)])
        for i in range(3):
            skills.append(self.skills[random.randint(0,len(self.skills)-1)])
        
        return Character(name, race, ch_class, stats, skills, story, inventory)

    def random_stats(self, race, ch_class):
        """
        create random stats based on the characters class and race
        This looks up the tables from CharacterCollection to get
        base stats and applies a close random fit
        """
        stats = []
        for ndx, i in enumerate(self.classes):
            if i == race:
                print(i)  # use stats for this class as baseline
        for ndx, i in enumerate(self.races):
            if i == race:
                print(i)  # use stats for this race to modify base stats
        
        # add 5 points to random stats
        
        
        return stats
        
class Character():
    """
    character class
    """
    def __init__(self, name, race, ch_class, stats, skills, story, inventory):
        """
        all params except name is a list
        """
        self.name = name
        self.race = race
        self.ch_class = ch_class
        self.stats = stats
        self.skills = skills
        self.story = story
        self.inventory = inventory

    def __str__(self):
        res = 'CHARACTER: ' + self.name + '\n'
        res += 'Race        = ' + self.race
        res += 'Class       = ' + self.ch_class
        res += '\nSTATS     = ' + ', '.join([s for s in self.stats])
        res += '\nStory     = ' +  self.story
        res += '\nSKILLS    =\n' + ', '.join([s for s in self.skills])
        res += '\nINVENTORY =\n' + ', '.join([s for s in self.inventory])
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
 