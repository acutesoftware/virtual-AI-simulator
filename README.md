# VAIS - Virtual AI simulator
Last updated 9th-April-2015
VAIS Dev version 0.0.1

VAIS runs simulations of agents and players across multiple worlds


##Quick Start

See quick_start.py 

 create a random world
 
> p = planet.Planet('ExamplePlanet', num_seeds=5, width=60, height=45, wind=0.2, rain=0.20, sun=0.2, lava=0.5)
> p.evolve(100)
> print(p)

View the world 

> fldr = os.getcwd() + os.sep + 'data'  + os.sep + 'worlds' 
> view_world.display_map(os.getcwd() + os.sep + 'data'  + os.sep + 'worlds' + os.sep + 'ExamplePlanet.txt')


create a character manually

> c1 = character.Character( 'Jim', 'Orc', 'Mage', {'Health':20,'max_health':20,'INT':8,'STA':5,'STR':2,'AGI':5}, ['cast'], 'Example char', ['Apple', 'knife'])
> print(c1)


CHARACTER = Jim
Race      = Orc
Class     = Mage
STATS     = STA:5 AGI:5 INT:8 Health:20 max_health:20 STR:2
Story     = Example char
SKILLS    = cast
INVENTORY = Apple, knife


