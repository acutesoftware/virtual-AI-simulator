# using noise to create maps
# based on example from http://gamedev.stackexchange.com/questions/29044/how-can-i-generate-random-lakes-and-rivers-in-my-game
from noise import pnoise2
import random
random.seed()
octaves = random.random()
# octaves = (random.random() * 0.5) + 0.5
freq = 16.0 * octaves
for y in range(50):
    row = ''
    for x in range(80):
        n = int(pnoise2(x/freq, y / freq, 1)*10+3)
        if n>=1:
            row += '.'
        else:
            row += 'x'
    print(row)