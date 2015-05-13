# web_users.py
import random

def get_name():
    first = random.choice(['John', 'Jim', 'Jake', 'Jane', 'Joe', 'Joan'])
    last = random.choice(['Smith','Blurg','Taylor','Murphy','Brown','Green'])
    return first + ' ' + last

params = {}
params['name']='web_user'   
params['desc_short']='simulated person browsing the web'
params['desc_long']="""
Web users range in levels of competence, browsers, OS's and 
reading speed.
"""

goals = ['find article', 'download file', 'post on forum']

params['name'] = get_name()
params['browser']=random.choice(["Firefox", "Chrome", "Internet Explorer"])   
params['OS']=random.choice(["Linux", "Windows", "IOS", "Android"])       


params['actions'] = ['browse', 'search', 'download', 'post']


def TEST():
    """
    local test of parameters
    """
    for k,v in params.items():
        if k != 'desc_long':
            print(k.ljust(15) + ' = ' + str(v))
        
    
if __name__ == '__main__':        
    TEST()