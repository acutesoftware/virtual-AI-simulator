# build_world.py    written by Duncan Murray 31/3/2015

import os
import sys
import math
from random import randint 
import aikif.environments.worlds as my_world
import aikif.agents.explore.agent_explore_grid as agt

log_folder = os.path.abspath(os.getcwd()+ os.sep + 'data' + os.sep + 'logs')
LOG_LEVEL = 2

def main():
    """
    generates a random world, sets terrain and runs agents in it
    """
    width       =  40   # grid width  (takes about 5 minutes to generate 500x400 grid with 8% blockages)
    height      =  20   # grid height
    num_seeds   =   6   # number of seed points to start land generation
    perc_land   =  20   # % of world that is land
    perc_sea    =  80   # % of world that is sea
    perc_blocked=   4   # % of world that is blocked
    
    myWorld = my_world.World( height, width, [' ','X','#']) 
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    myWorld.grd.save('vais_world.txt')
    
    #Create some agents to walk the grid
    iterations  = 20   # how many simulations to run
    num_agents  =  3   # number of agents to enter the world
    years       = 100   # how many times to run each simulation
    target_coords = [math.floor(myWorld.grd.grid_height/2) + randint(1, math.floor(myWorld.grd.grid_height/2)) - 3, \
                     math.floor(myWorld.grd.grid_width /2) + randint(1, math.floor(myWorld.grd.grid_width/2)) - 5]
    agt_list = []
    for agt_num in range(0,num_agents):
        ag = agt.ExploreAgent( 'exploring_agent' + str(agt_num),  log_folder, False, LOG_LEVEL)
        start_y, start_x = myWorld.grd.find_safe_starting_point()
        ag.set_world(myWorld.grd, start_y, start_x, target_coords[0], target_coords[1])
        agt_list.append(ag)
    sim = my_world.WorldSimulation(myWorld, agt_list, LOG_LEVEL)
    sim.run(iterations, 'N', log_folder)
    sim.world.grd.save('test_world_traversed.txt')
 
main()
