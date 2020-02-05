# game_incremental.py

import os
import sys
import time
import random

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..")
sys.path.append(root_folder)
#import character


ref_folder = root_folder + os.sep + "data"


my_char = {"name":"player1", "energy":100, "max_energy":100,"gold":400,
            "skills": [
                {"name":"mining", "level":1},
                {"name":"herb", "level":1},
                {"name":"recipe", "val":0},
            ],
            "experiance": [
                {"name":"level", "val":1},
                {"name":"mining", "val":1},
                {"name":"herb", "val":1},
                {"name":"recipe", "val":0},
            ],
            "inventory": [
                {"name":"stone", "val":0},
                {"name":"gold", "val":10},
                {"name":"herb", "val":0},
                {"name":"recipe", "val":0},
            ]
            }

# when user is away from game, this is how time is spent by bot doing your levelling
default_schedule = [
    {"name":"rest", "hours": 8},
    {"name":"work", "hours": 8},
    {"name":"fun", "hours": 4},
    {"name":"think", "hours": 1},
    {"name":"learn", "hours": 1},


]

materials = [
{"name":"gold", "buy_value":1.000, "sell_value":1.000, "msg":"You found gold"},
{"name":"stone", "buy_value":0.05, "sell_value":0.03, "msg":"You found stone"},
{"name":"herb", "buy_value":0.05, "sell_value":0.03, "msg":"You found a herb"},
{"name":"recipe", "buy_value":0.5, "sell_value":0.3, "msg":"You invented a recipe"},
]

actions = [
{"name":"walk", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.08,"reward_item":"herb", "exp_gain":0.0},
{"name":"run", "cost_energy":0.05, "cost_gold":0, "reward_chance":0.0002,"reward_item":"herb", "exp_gain":0.0},
{"name":"rest", "cost_energy":-1, "cost_gold":0, "reward_chance":0.09,"reward_item":"recipe", "exp_gain":0.0},
{"name":"mining", "cost_energy":1, "cost_gold":0, "reward_chance":0.9,"reward_item":"stone", "exp_gain":0.1},
{"name":"herb", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"herb", "exp_gain":0.1},
{"name":"think", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"recipe", "exp_gain":0.1},
{"name":"study", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"recipe", "exp_gain":0.1},
{"name":"tinker", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"recipe", "exp_gain":0.1},
]


walk = actions[0]
run = actions[1]
rest = actions[2]
mining = actions[3]
herb = actions[4]
think = actions[5]
study = actions[6]
tinker = actions[7]




object_types = [
{"name":"food", "placeable":"N", "wearable":"N", "wieldable":"N"},
{"name":"craft", "placeable":"Y", "wearable":"N", "wieldable":"N"},
{"name":"weapon", "placeable":"N", "wearable":"N", "wieldable":"Y"},
{"name":"armor", "placeable":"N", "wearable":"Y", "wieldable":"N"},
{"name":"tool", "placeable":"N", "wearable":"N", "wieldable":"N"},
]

objects = [
{"name":"cart", "type":"tool", "cost_gold":50, "uses":[],"outputs":"stone x50", "msg":"You carry stone with the cart"},
{"name":"furnace", "type":"craft", "cost_gold":200, "uses":["coal", "iron_ore"],"outputs":"iron"},
]

# ACTIONS and Scenarios

# AI will loop through list below in order and where nothing else, will just mine for stone
things_to_do_AI = [
    #{"name":"sleep", "WHERE_COL": "energy", "WHERE_COND":"<", "WHERE_VAL":10, "chance":0.5},
    {"name":"rest", "WHERE_COL": "energy",  "WHERE_VAL":10, "chance":0.8},
    {"name":"furnace", "WHERE_COL": "gold",  "WHERE_VAL":250, "chance":0.8},
    {"name":"polish_stone", "WHERE_COL": "stone",  "WHERE_VAL":100, "chance":0.5},
    {"name":"mining", "WHERE_COL": "energy",  "WHERE_VAL":20, "chance":0.5},
]




def main():
    print('Welcome to click level')
    scenario1_man()

    print("Your character = ", my_char)

def scenario1_man():
  """
  for loop in range(1, 50):
    do_action(my_char, mining)
  for loop in range(1, 50):
    do_action(my_char, herb)
  """
  for loop in range(1, 50):
    do_action(my_char, rest)
    do_action(my_char, think)
    do_action(my_char, study)
    do_action(my_char, tinker)




def scenario2_man():
  for loop in range(1, 5):
    do_action(my_char, mining)
  do_action(my_char, walk)
  do_action(my_char, walk)
  do_action(my_char, rest)
  for loop in range(1, 8):
    do_action(my_char, rest)

def scenario2_AI():
  for loop in range(1, 250):
    do_action(my_char, pick_action_todo())



def pick_action_todo():
    """
    only for testing and AI - user will usually choose an action
    Sort of works
    """
    for ndx, todo in enumerate(things_to_do):
        #print('todo = ', todo)
        if roll_dice(todo["chance"]):
            cur_act = actions[get_action_by_name(todo["name"])]
            if todo["WHERE_COL"] == "energy" and my_char["energy"] > todo["WHERE_VAL"]:
                return cur_act
            if todo["WHERE_COL"] == "gold" and my_char["gold"] > todo["WHERE_VAL"]:
                return cur_act


    return actions[3]  # return default mining


def do_action(character, action):
    """
    called by main game loop to run an action
    """
    #stats = "Energy=" + str(round(character["energy"], 0)) + ", "
    #stats += "Gold=" + str(round(character["gold"], 0)) + ", "

    ndx_action_skill = get_skill_by_name(action["name"], character)
    #stats += "Skill=" + str(round(character["skills"][ndx_action_skill]["level"], 1))


    stats = {}
    stats["Energy"] = round(character["energy"], 0)
    stats["gold"] = round(character["gold"], 0)
    stats["skills"] = round(character["skills"][ndx_action_skill]["level"], 1)
    

    my_char["energy"] -= action["cost_energy"]
    my_char["skills"][ndx_action_skill]["level"] += action["exp_gain"]

    # NOT NEEDED act = get_action_by_name(character["skills"][ndx_action_skill]["name"])
    reward_item = action["reward_item"]
    #print('reward_item = ', reward_item)
    #print('action = ', action)

    inv = get_inventory_by_name(reward_item, my_char)
    #print('inv=', inv)

    if roll_dice(action["reward_chance"]) :
        my_char["inventory"][inv]["val"] += 1
        #my_char["inventory"][inv] += 1
        #my_char["inventory"][inv][reward_item] += 1
        #print(character["name"] + " is " + action["name"] + ". " + str(stats) + ' FOUND ' + reward_item)
        print_line_stat(character["name"], action["name"], stats, ' FOUND ' + reward_item)

    else:
        print_line_stat(character["name"], action["name"], stats, '')
        time.sleep(0.06)


def print_line_stat(nme, action, stats, event):
    """
    prints progress on one line, formatted nicely
    """
    res = nme.ljust(9) + ' '
    res += action.ljust(9) + ': '
    for k,v in stats.items():
        res += k.ljust(10) + '='
        res += str(v).ljust(8) + ', '

    if event:
        res += event
        print(res.ljust(79) )
        time.sleep(0.1)
    else:   # print on same line
        res += '                       '
        print(res.ljust(79),  end='\r' )


def roll_dice(num):
    """
    rolls a dice  if > than num
    then it returns TRUE else FALSE
    """
    roll = random.randint(1,100)
    if roll < num * 100 :
        return True
    return False

def get_inventory_by_name(nme, character):
    """
    returns the inventory index by name
    """

    for ndx, sk in enumerate(character["inventory"]):
        #print("sk = ", sk, " , nme = ", nme)
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
