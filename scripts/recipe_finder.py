
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
 
ingredients_on_hand = ['Steak','Tofu','Rice','Pasta','Chicken','Asparagus','Tomatoe','Cheese'] 
 

 
 
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
    #find_best_ingredients(ingredients_on_hand, dinner_guests)
    best_ingred, worst_ingred = find_best_ingredients(all_ingredients, dinner_guests)

    print('best ingred  = ', best_ingred)
    print('worst ingred = ', worst_ingred)
    
    for have in ingredients_on_hand:
        if have in best_ingred:
            print('Use this = ', have)
    
    
def find_best_ingredients(ingredients, guests):
    """
    
    """
    ingredient_ranking = {}
    for i in ingredients:
        if i not in ingredient_ranking:
            ingredient_ranking[i] = 0
            
        for g in guests:
            for sub_i in g['likes']:
                if i.lower() in sub_i.lower():
                    ingredient_ranking[i] += 1
            for sub_i in g['hates']:
                if i.lower() in sub_i.lower():
                    ingredient_ranking[i] -= 5
                
    #print(ingredient_ranking)        
    #print(ingredients)        
    #print(sorted(ingredient_ranking.items(), key=lambda x: x[1]))
    best = []
    avoid = []
    for k,v in sorted(ingredient_ranking.items(), key=lambda x: x[1]):
        #if v != 0:
        #    print(k,v)
        if v < 0:
            avoid.insert(0, k)  # to get a list of best ordered by value
        if v > 0:
            best.insert(0, k)  # to get a list of best ordered by value
    return best, avoid
 
main()    