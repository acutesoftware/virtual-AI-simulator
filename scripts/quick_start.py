# quick_start.py

import os
import sys

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..")
fldr = root_fldr + os.sep + "vais"
op_fldr = root_fldr + os.sep + "tests"
print(fldr)
sys.path.append(fldr )

import planet
import view_world
import character
import battle

# create a random world
p = planet.Planet('quick_planet', num_seeds=5, width=100, height=300, wind=0.2, rain=0.20, sun=0.2, lava=0.2)
p.evolve(100)
print(p)
p.world.grd.save(fldr + os.sep + 'data'  + os.sep + 'worlds'  + os.sep + 'quick_planet.txt')
# view the world (or view as text via /data/worlds/ExamplePlanets.txt)
view_world.display_map(fldr + os.sep + 'data'  + os.sep + 'worlds'  + os.sep + 'quick_planet.txt')



# create a character manually
c1 = character.Character( 'Jim', 'Orc', 'Mage', {'Health':20,'max_health':20,'INT':8,'STA':5,'STR':2,'AGI':5}, ['cast'], 'Example char', ['Apple', 'knife'])
print(c1)
"""
CHARACTER = Jim
Race      = Orc
Class     = Mage
STATS     = STA:5 AGI:5 INT:8 Health:20 max_health:20 STR:2
Story     = Example char
SKILLS    = cast
INVENTORY = Apple, knife
"""

# load rules and traits data
rules_file = fldr + os.sep + 'data' + os.sep + 'battle.rules'
traits = character.CharacterCollection(os.path.join(fldr,'data'))
rules = battle.BattleRules(rules_file)

# create a random character 
c2 = traits.generate_random_character()
c2.save_to_file(os.path.join(op_fldr, 'random_char.txt'))
print(c2)
"""
CHARACTER = Rekkaj
Race      = Orc
Class     = Ranger
STATS     = STA:9 AGI:7 INT:2 CON:8 Health:22 max_health:22 STR:6
Story     = A young scholar with a burning desire to learn
SKILLS    = Slow Monster, Teleport Other, Detect Monsters
INVENTORY = 27 gold, food, stick, stick
"""


# Battle the 2 characters

b = battle.Battle(c1, c2, traits, rules, print_console='Yes')
print(b.status + ' Wins')

"""
Jim [100%] hits Crador [100%] for 4
Crador  [80%] hits Jim [100%] for 4
Jim  [80%] miss Crador  [80%]
Crador  [80%] hits Jim  [80%] for 4
Jim  [60%] CRIT Crador  [80%] for 12
Crador  [20%] hits Jim  [60%] for 4
Jim  [40%] hits Crador  [20%] for 4
Jim Wins
"""

# simulate 10,000 fights
sim = battle.BattleSimulator(c1, c2, traits, rules, 10000)
print(sim)

"""
After 10000 fights Jim wins!
Jim = 9158 (92%)
Crador = 842 (8%)
"""

