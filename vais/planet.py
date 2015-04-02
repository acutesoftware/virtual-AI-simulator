# planet.py     written by Duncan Murray

import os
import sys
import math
import time
from random import randint 
import aikif.environments.worlds as my_world
import aikif.gui_view_world as gui
 
fldr = os.getcwd() + os.sep + 'data'  + os.sep + 'worlds' 

def TEST():
    """
    testing planet evolution to build a virtual world
    """
    p = Planet('Divitie', wind=0.1, rain=0.1, sun=0.2, lava=0.5)
    p.evolve(years=10000000)
    print(p)
    
class Planet():
    """
    class to manage the simplified evolution of a planet to 
    build a virtual world. Takes basic atmospheric parameters
    and *very* roughly uses these to guess what the world would
    look like.
    The idea is to be able to auto generate worlds as follows:
    green lush worlds: sun > 0.15, rain > 0.15
    earth like worlds: sun=0.2, rain=0.1, wind=0.1
    metal rich worlds: sun<0.2, wind>0.2, seismic_activity>0.6
    """
    def __init__(self, name, height=100, width=100, wind=0.1, rain=0.1, sun=0.2, lava=0.5):
        """
        All parameters must be between 0 and 1 and show the probability of
        that event. The numbers below are rough guidelines for normal planets
        wind 0.0 -> 0.2 : determines air currents, rain movement, topsoil
        rain 0.1 -> 0.6 : determines plant growth, river networks
        sun  0.1 -> 0.6 : determines plant growth, river networks
        lava 0.1 -> 0.6 : during formation only - determines mountains
        """
        self.world = ''     # aikif.environment.world object
        self.name = name
        self.grid_height = height
        self.grid_width = width
        self.wind = wind
        self.sun = sun
        self.rain = rain
        self.lava = lava
    
    def __str__(self):
        res = '\n-- Welcome to ' + self.name + ' --\n'
        res += self._stats_as_str(delim = ' = ', lf='\n')
        return res
        
    def _stats_as_str(self, delim = ',', lf='\n'):
        s = ''
        s += 'Sun ' + delim + str(self.sun) + lf
        s += 'Wind' + delim + str(self.wind) + lf
        s += 'Rain' + delim + str(self.rain) + lf
        s += 'Lava' + delim + str(self.lava) + lf
        return s
        
    def evolve(self, years):
        """
        run the evolution of the planet to see how it looks 
        after 'years'
        """
        world_file = fldr + os.sep + self.name + '.txt'
        self.build_base()
        self.define_heights()
        self.add_life()
        self.world.grd.save(world_file)
        
        print('done')
        time.sleep(3)
        gui.display_map(world_file)
    
    def build_base(self):
        """
        create a base random land structure using the AIKIF world model
        """
        print('Planet ' + self.name + ' has formed!')
        self.world = my_world.World( self.grid_height, self.grid_width, [' ','x','#']) 
        
        perc_land = (self.lava + (self.wind/20) - (self.rain/10) + (self.sun/10))*100
        perc_sea = (100 - perc_land)
        perc_blocked = (self.lava/5)*100
        
        print('Calculating world : sea=', perc_sea, ' land=', perc_land, ' mountain=', perc_blocked,  )
        self.world.build_random( 6, perc_land, perc_sea, perc_blocked)
        
        
    def define_heights(self):
        """
        takes a rough world and organises heights. Basically this takes 
        the 'blocked' lines created in worlds and dithers them to make
        mountain ranges of descending height.
        A new array is used to store heights of the world
        """
        print('creating mountains')
        
    def add_life(self):
        """
        adds plants and animals to the world. Tries to do this in groups
        or clusters as well as random 'outcrops' or herds.
        Uses rules list to determine types and quantities of life according
        to planets evolution and atmosphere.
        """
        print('Adding Plants and Animals')
        
        
 
if __name__ == '__main__':
    TEST()    