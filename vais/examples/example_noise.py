# using noise to create maps
# based on example from http://gamedev.stackexchange.com/questions/29044/how-can-i-generate-random-lakes-and-rivers-in-my-game
from noise import pnoise2
import random
random.seed()

def create_random_terrain(width, height):
    octaves = random.random()
    # octaves = (random.random() * 0.5) + 0.5
    tot_land = 0
    tot_sea = 0
    freq = 16.0 * octaves
    for y in range(height):
        row = ''
        for x in range(width):
            n = int(pnoise2(x/freq, y / freq, 1)*10+3)
            if n>=1:
                row += '.'
                tot_sea += 1
            else:
                row += 'x'
                tot_land += 1
        print(row)
    return tot_land, tot_sea, freq
        
create_random_terrain(78, 22)      
        