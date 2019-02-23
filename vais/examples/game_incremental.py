# game_incremental.py

import os
import sys
import time
import random

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..")
sys.path.append(root_folder)
import character


ref_folder = root_folder + os.sep + "data"


my_char = {"name":"player1", "energy":100, "max_energy":100,
            "skills": [
                {"name":"mining", "level":1},
            ],
            "experiance": [
                {"level":1},
                {"mining":1},
            ],
            "inventory": [
                {"stone":0},
                {"gold":10}
            ]
            }

materials = [
{"name":"gold", "buy_value":1.000, "sell_value":1.000, "msg":"You found gold"},
{"name":"stone", "buy_value":0.05, "sell_value":0.03, "msg":"You found stone"},
{"name":"herb", "buy_value":0.05, "sell_value":0.03, "msg":"You found a herb"},
{"name":"recipe", "buy_value":0.5, "sell_value":0.3, "msg":"You invented a recipe"},
]

actions = [
{"name":"walk", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.08,"reward_item":"herb"},
{"name":"run", "cost_energy":0.05, "cost_gold":0, "reward_chance":0.0002,"reward_item":"herb"},
{"name":"rest", "cost_energy":-1, "cost_gold":0, "reward_chance":0.001,"reward_item":"recipe"},
{"name":"mining", "cost_energy":1, "cost_gold":0, "reward_chance":0.9,"reward_item":"stone"},
]


def main():
  print('Welcome to click level')
  while my_char["energy"] > 10:
      for i in range(1,5):
        do_action(my_char, actions[3])
      print('my_char = ', my_char)
  for i in range(1,5):
      do_action(my_char, actions[2])

  print("Your character = ", my_char)


def do_action(character, action):
    """
    called by main game loop to run an action
    """
    stats = "Energy=" + str(character["energy"]) + ", "
    #stats += "Gold=" + str(character["gold"]) + ", "

    ndx_action_skill = get_skill_by_name(action["name"], character)
    stats += "Skill=" + str(character["skills"][ndx_action_skill]["level"])

    print(character["name"] + " is " + action["name"] + ". " + stats)
    my_char["energy"] -= action["cost_energy"]
    my_char["skills"][ndx_action_skill]["level"] += 1

    # get reward from action by running chance
    roll = random.randint(1,100)
    #print("you rolled a " + str(roll))
    act = get_action_by_name(character["skills"][ndx_action_skill]["name"])
    reward_item = actions[act]["reward_item"]
    #print('reward_item = ', reward_item)
    #print('act = ', actions[act])

    if roll > actions[act]["reward_chance"] * 100 :
        my_char["inventory"][get_inventory_by_name(reward_item, my_char)][reward_item] += 1



def get_inventory_by_name(nme, character):
    """
    returns the Action by name
    """

    for ndx, sk in enumerate(character["skills"]):
        if sk["name"] == nme:
            return ndx
    return 0

def get_action_by_name(nme):
    """
    returns the Action by name
    """

    for ndx, sk in enumerate(actions):
        if sk["name"] == nme:
            return ndx
    return 0


def get_skill_by_name(nme, character):
    """
    returns the skill by name in a character
    """

    for ndx, sk in enumerate(character["skills"]):
        if sk["name"] == nme:
            return ndx
    return 0


main()
