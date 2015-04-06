# character.py  written by Duncan Murray 3/4/2015

import os
import random

## TODO - once 
fldr = os.getcwd() + os.sep + 'data'  


def TEST():
    """
    Module to handle character creation
    """
    print('creating random character')
    traits = CharacterCollection(fldr)
    print(traits)
    #c = traits.generate_random_character('Zoltar')
    #print(c)
    
class RefFile():
    """
    Class to handle a CSV type reference file for 
    stats, races, etc - generally has a header and
    any column can have mulitple values if enclosed
    by [] where values parsed by |
    """
    def __init__(self, fldr, fname):
        self.name = fname[0:-4]
        self.raw_data = read_file(fldr + os.sep + fname)
        self.dat = self.parse_to_dict(self.raw_data) # parse raw CSV into dictionary
        
    def __str__(self):
        res = ' === ' + self.name + ' Reference File ====\n'
        res += str(len(self.raw_data)) + ' lines\n' 
        return res
    
    def parse_to_dict(self, raw):
        """
        parse raw CSV into dictionary
        """
        lst = []
        for i in raw:
            lst.append({'name':i[0]})
        return lst
    
class CharacterCollection():
    """
    Class to handle all the character traits
    """
    def __init__(self, fldr):
        """
        loads all the ref_*.csv files relating 
        to character traits
        """
        self.ref_folder = fldr
        print('loading data files')
        self.races = RefFile(fldr, 'ref_races.csv')
        self.classes = RefFile(fldr, 'ref_classes.csv')
        self.stats = RefFile(fldr, 'ref_stats.csv')
        self.skills = RefFile(fldr, 'ref_skills.csv')
        self.stories = RefFile(fldr, 'ref_stories.csv')
        self.inventory = RefFile(fldr, 'ref_objects.csv')
         
    
    def __str__(self):
        res = '=== DUMP OF ALL CHARACTER TRAITS ===\n'
        res += 'Classes:\n' + str(self.classes)
        res += 'Races:\n' + str(self.races)
        res += 'STATS:\n' + str(self.stats)
        res += 'Story:\n' + str(self.stories)
        res += 'SKILLS:\n' + str(self.skills)
        res += 'INVENTORY:\n' + str(self.inventory)
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
 