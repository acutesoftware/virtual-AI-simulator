=========================================
VAIS - Virtual AI simulator
=========================================

Last updated 24th-April-2015
VAIS Dev version 0.0.3

VAIS runs simulations of agents and players across multiple worlds

create a random world
--------------------------------

.. code:: python
 
    p = planet.Planet('ExamplePlanet', num_seeds=5, width=60, height=45, wind=0.2, rain=0.20, sun=0.2, lava=0.5)
    p.evolve(100)
    print(p)


View the world 
--------------------------------

.. code:: python

    fldr = os.getcwd() + os.sep + 'data'  + os.sep + 'worlds' 
    view_world.display_map(os.getcwd() + os.sep + 'data'  + os.sep + 'worlds' + os.sep + 'ExamplePlanet.txt')

create a character manually
--------------------------------

.. code:: python

    c1 = character.Character( 'Jim', 'Orc', 'Mage', {'Health':20,'max_health':20,'INT':8,'STA':5,'STR':2,'AGI':5}, ['cast'], 'Example char', ['Apple', 'knife'])
    print(c1)

        CHARACTER = Jim
        Race      = Orc
        Class     = Mage
        STATS     = STA:5 AGI:5 INT:8 Health:20 max_health:20 STR:2
        Story     = Example char
        SKILLS    = cast
        INVENTORY = Apple, knife


Create a 2nd random character and battle them
----------------------------------------------

.. code:: python

    traits = character.CharacterCollection(character.fldr)
    rules = battle.BattleRules('battle.rules')
    c2 = traits.generate_random_character()
    b = battle.Battle(c1, c2, traits, rules, print_console='Yes')
    print(b.status + ' Wins')

        Jim [100%] hits Crador [100%] for 4
        Crador  [80%] hits Jim [100%] for 4
        Jim  [80%] miss Crador  [80%]
        Crador  [80%] hits Jim  [80%] for 4
        Jim  [60%] CRIT Crador  [80%] for 12
        Crador  [20%] hits Jim  [60%] for 4
        Jim  [40%] hits Crador  [20%] for 4
        Jim Wins

Simulate 10,000 fights
--------------------------------

.. code:: python

    sim = battle.BattleSimulator(c1, c2, traits, rules, 10000)
    print(sim)

        After 10000 fights Jim wins!
        Jim = 9158 (92%)
        Crador = 842 (8%)


