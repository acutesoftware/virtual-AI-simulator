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
    #print(traits)
    #print("traits.stats.raw_data:", traits.stats.dat)
    #print("traits.stats:", str(traits.stats))
    c = traits.generate_random_character()
    print(c)
    
class RefFile():
    """
    Class to handle a CSV type reference file for 
    stats, races, etc - generally has a header and
    any column can have mulitple values if enclosed
    by [] where values parsed by |
    """
    def __init__(self, fldr, fname):
        self.name = fname[0:-4]
        self.fname = fldr + os.sep + fname
        self.hdrs = []
        self.dat = self.parse_to_dict() # read CSV file and parse into dictionary

    #def __iter__(self):
    #    return iter(self.dat)
            
    def __str__(self):
        res = ' === ' + self.name + ' Reference File ====\n'
        res += str(len(self.dat)) + ' lines = ' 
        for rownum, row in enumerate(self.dat):
            if 'name' in self.hdrs:
                res += row['name'] + ','
            else:
                #print("Headers for " + self.fname + " = " , self.hdrs)
                pass
            #for colnum, col in enumerate(row):
            #    print(str(rownum), str(colnum), col)
        return res
    
    def parse_to_dict(self):
        """
        parse raw CSV into dictionary
        """
        lst = []
        with open(self.fname, 'r') as f:
            hdr = f.readline()
            self.hdrs = hdr.split(',')
            #print("self.hdrs = ", self.hdrs)
            for line in f:
                cols = line.split(',')
                if len(cols) == len(self.hdrs):
                    #print(cols)
                    dict = {}
                    for ndx, col_header in enumerate(self.hdrs):
                        #print("i[ndx] = ", cols[ndx].strip('\n').strip())
                        dict[self.hdrs[ndx].strip('\n').strip()] = cols[ndx].strip('\n').strip()
                    lst.append(dict)
                else:
                    print("Error parsing " + self.fname + " line : " + line)
        return lst
    
    def get_random_choice(self):    
        """
        returns a random name from the class
        """
        i = random.randint(0,len(self.dat)-1)
        return self.dat[i]['name']
    
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
        #print('loading data files')
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
        res += '\nStory:\n' + str(self.stories)
        res += 'SKILLS:\n' + str(self.skills)
        res += 'INVENTORY:\n' + str(self.inventory)
        return res
        
    def generate_random_character(self):
        """
        uses the traits to create a random, but plausible
        character. Sample below:
            CHARACTER = Amador
            Race      = Halfling
            Class     = Priest
            STATS     = CON = 12, STA = 4, INT = 10, STR = 0, AGI = 5,
            Story     = A brave person looking to fight evil in the dark forests of Divitie
            SKILLS    = Remove Curse, Frost Ball, Frost Bolt
            INVENTORY = 5 gold, stick, leaf, sword
        """
        name = self.create_name()
        ch_class = self.classes.get_random_choice()
        race = self.races.get_random_choice()
        stats = self.random_stats(self.stats.dat, race, ch_class)
        skills = []
        story = self.stories.get_random_choice()
        inventory = [str(random.randint(21,29)) + ' gold']
        
        # pick random stuff here 
        for i in range(3):
            inventory.append(self.inventory.get_random_choice())
        for i in range(3):
            skills.append(self.skills.get_random_choice())
        return Character(name, race, ch_class, stats, skills, story, inventory)

    def random_stats(self, all_stats, race, ch_class):
        """
        create random stats based on the characters class and race
        This looks up the tables from CharacterCollection to get
        base stats and applies a close random fit
        """
        
        # create blank list of stats to be generated
        stats = []
        res = {}
        for s in all_stats:
            stats.append(s['stat'])
            res[s['stat']] = 0
        
        cur_stat = 0
        stat_name = ''
        for stat in stats:
            for ndx, i in enumerate(self.classes.dat):
                if i['name'] == ch_class:
                    cur_stat = int(i[stat])  # use stats for this class as baseline
            for ndx, i in enumerate(self.races.dat):
                if i['name'] == race:
                    cur_stat += int(i[stat])  # use stats for this race to modify base stats
            #print(stat, cur_stat)
            if cur_stat < 1:
                cur_stat = 1
            elif cur_stat > 10:
                if stat not in ('Health', 'max_health'): # dont trim down health
                    cur_stat = 10
           
            res[stat] = cur_stat
        
        return res
    
    def create_name(self):
        a = random.choice(['Vol','Ama','Zan','Fea','Cra','Por','Tra','Are','Rek','Wol','Zat','Pli'])
        b = random.choice(['mar','dor','mor','dar','dom','kaj','sij','lim','gri','put','eat','rey'])
        return a + b
    
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
        res =  'CHARACTER = ' + self.name + '\n'
        res += 'Race      = ' + self.race + '\n'
        res += 'Class     = ' + self.ch_class + '\n'
        res += 'STATS     = ' 
        for k,v in self.stats.items():
            res += k + ':' + str(v) + ' '

        res += '\nStory     = ' +  self.story
        res += '\nSKILLS    = ' + ', '.join([s for s in self.skills])
        res += '\nINVENTORY = ' + ', '.join([s for s in self.inventory])
        return res
    
    def load_from_file(self, fname):
        """
        OVERWRITES the current character object from stats in file
        """
        with open(fname, 'r') as f:
            for line in f:
                k,v = line.split(' = ')
                self._parse_char_line_to_self(k,v)
                
    def _parse_char_line_to_self(self, k,v):
        """
        takes a line from a saved file split into key and values
        and updates the appropriate self parameters of character.
        """
        k = k.strip(' ').strip('\n')
        v = v.strip(' ').strip('\n')
       # print('_parse_char_line_to_self(self, k,v): ' , k, v)
        if k == 'CHARACTER':
            self.name = v
        elif k == 'Race':
            self.race = v
        elif k == 'Class':
            self.ch_class = v
        elif k == 'STATS':
            self.stats = self._extract_stats_from_line(v)
        elif k == 'Story':
            self.story = v.strip(' ').strip('\n')
        elif k == 'SKILLS':
            self.skills = v.split(', ')
        elif k == 'INVENTORY':
            self.inventory = v.split(', ')
            
     
    def _extract_stats_from_line(self, txt, stats_delim=' ', val_delim=':'):
        """
        extracts the stats from a line of text to the class params
        STR:7 AGI:9 STA:5 INT:5 Health:21 CON:8 max_health:21
        """
        result = {}
        stats_txt = txt.split(stats_delim)
        for s in stats_txt:
            #print('s = ', s)
            if s.strip(' ').strip('\n') != '':
                k,v = s.split(val_delim)
                result[k.strip(' ')] = v.strip(' ').strip('\n')
        return result
    
    def save_to_file(self, fname):
        """
        saves a characters data to file
        """
        with open(fname, 'w') as f:
            f.write(str(self))
            
    def copy(self):
        """ 
        make an identical copy of the character
        """
        return Character(self.name, self.race,self.ch_class, self.stats, self.skills, self.story, self.inventory)
        
     
     
############################
#  Utility functions 

def read_file(fname):
    """
    read a CSV file (ref_classes.csv) and return the 
    list of names
    """
    print("NO - dont use this function read_file(fname):")
    exit(1)
    lst = []
    with open(fname, 'r') as f:
        #hdr = f.readline()
        for line in f:
            lst.append(line.strip('\n'))
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
 