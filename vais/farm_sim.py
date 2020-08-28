#!/usr/bin/python3
# -*- coding: utf-8 -*-
# farm_sim.py
# farming simulator


import npc_generator as mod_npc
import worlds as my_world

def main():
    print('Welcome to Farm Sim!')

    my_npcs = mod_npc.NPCs()
    print(my_npcs)

    myWorld = my_world.World( 12, 50, ['.','#',' '])  
    myWorld.build_random( 2, 6, 92,2)
    #myWorld.grd.save('farm_world.txt')


    # spawn characters
    for n in my_npcs.npc_def:
        print('n  =', str(n))
        x = n['coord_x']
        y = n['coord_y']
        tpe = n['type'][0:1].upper()

        # place the NPC
        myWorld.grd.set_tile(y, x, tpe)

        # if Farmer, then clear the land around them
        if tpe == 'F':
            blocks_to_clear = myWorld.grd.eight_neighbors(y, x)
            for blk in blocks_to_clear:
                myWorld.grd.set_tile(blk[0], blk[1], ' ')



    print(myWorld.grd)
    myWorld.grd.save('farm_world.txt')





if __name__ == '__main__':
	main()