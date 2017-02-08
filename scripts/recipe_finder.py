
# recipe_finder.py

import os
import sys

import rawdata.generate
import rawdata.content


fldr = os.path.join(rawdata.content.data_fldr, 'food') + os.sep

data_files =  [
    {'name':'Food Groups', 'file': fldr + 'food_groups.csv', 'col':'Dairy and Egg Products'}, # food_group_name
    {'name':'Ingredients', 'file': fldr + 'food_desc.csv', 'col':'Long_Desc'},
 ]   

 
dinner_guests = [
    {'name':'Frank', 'likes':['tofu', 'cucumber'], 'hates':['meat']},
    {'name':'Mary', 'likes':['fish'], 'hates':['lamb','curry']},
    {'name':'Shaz', 'likes':['steak','salad','indian','chocolate'], 'hates':['apple pie','scallops','corriander']},
    {'name':'David', 'likes':['fritz','cheese'], 'hates':['turnips']},
    {'name':'Stuart', 'likes':['steak','indian'], 'hates':['roast chicken','asparagus','tomatoe','prawns', 'fish']},
 ] 
 
ingredients_on_hand = ['steak','tofu','rice','pasta','chicken','asparagus','tomatoe','basil','chillie'] 
 

 
 
def main():
    """
    script to find a list of recipes for a group of people 
    with specific likes and dislikes.
    
    for f in data_files:
        print('name = ', f['name'], 'file = ', f['file'])
        data_list = s.get_collist_by_name(f['file'], f['col'])
        print(list(data_list[0])[0:5])
 
    
    print(dinner_guests)
     
    """
    s = rawdata.content.DataFiles()
    all_ingredients = list(s.get_collist_by_name(data_files[1]['file'], data_files[1]['col'])[0])
    print(all_ingredients[0])
    #find_best_ingredients(ingredients_on_hand, dinner_guests)
    find_best_ingredients(all_ingredients, dinner_guests)

def find_best_ingredients(ingredients, guests):
    """
    
    """
    ingredient_ranking = {}
    for i in ingredients:
        if i not in ingredient_ranking:
            ingredient_ranking[i] = 0
            
        for g in guests:
            if i in g['likes']:
                ingredient_ranking[i] += 1
            if i in g['hates']:
                ingredient_ranking[i] -= 5
                
    #print(ingredient_ranking)        

 
    for k,v in ingredient_ranking.items():
        if v > 0:
            print(k,v)
 
main()    