#!/usr/bin/python3
# -*- coding: utf-8 -*-
# envirosim.py

def main():
    es = Params('Environment simulator', 'simulate evolution via parametric changes')
    es.add_param('orbit', 'planet')
    es.add_param('dist_to_sun', 'planet')
    es.add_param('num_moons', 'planet')
    es.add_param('heat', 'climate')
    es.add_param('rain', 'climate')
    es.add_param('wind', 'climate')
    es.add_param('land', 'terrain')
    es.add_param('water', 'terrain')
    es.add_param('rocks', 'terrain')
    es.add_param('grass', 'vegetation')
    es.add_param('bushes', 'vegetation')
    es.add_param('trees', 'vegetation')
    es.add_param('herbivore', 'animals')
    es.add_param('carnivore', 'animals')
    es.add_param('scavenger', 'animals')
    es.add_param('meteor', 'events')
    es.add_param('volcano', 'events')
    es.add_param('cyclone', 'events')
    es.add_param('', '')
    es.add_affect('heat grows grass', 'heat', 'grass', +4, 'heat < 50 AND heat > 5')
    print(es)

class Params(object):
    """
    handles full list of all params affecting the environment
    """
    def __init__(self, name, desc, derived_from='root'):
        self.name = name
        self.desc = desc
        self.params = []
        self.affects = []

    def __str__(self):
        res = '---------------------------------------------------\n'
        res += self.name + '\n'
        res += self.desc+ '\n'
        res += '---------------------------------------------------\n'
        
        for p in self.params:
            res += str(p)
        for f in self.affects:
            res += str(f)
        return res
    
    def add_param(self, nme, dsc):
        self.params.append(Param(nme, dsc))
        
    def add_affect(self, name, src, dest, val, condition = None ):
        """
        adds how param 'src' affects param 'dest' to the list
        """
        self.affects.append(ParamAffects(name, src, dest, val, condition))
    
    def get_by_name(self, nme):
        """
        searches list of all parameters and returns the first
        param that matches on name
        """
        for p in self.params:
            if p.name == nme:
                return p
        return None
 
    def get_affects_for_param(self, nme):
        """
        searches all affects and returns a list
        that affect the param named 'nme'
        """
        res = []
        for a in self.affects:
            if a.name == nme:
                res.append(a)
        return res

 
class Param(object):
    """
    handles the list of things that have an effect on the environment
    """
    def __init__(self, name, desc, derived_from='root'):
        self.name = name
        self.desc = desc

    def __str__(self):
        res = ''
        res += self.name + '\t'
        res += self.desc[0:60] + '\n'
        return res


class ParamAffects(object):
    """
    handles the list of things that have an effect on the environment
    """
    def __init__(self, name, src, dest, val, condition = None):
        self.name = name
        self.src = src
        self.dest = dest
        self.val = val
        self.condition = condition

    def __str__(self):
        res = ''
        res += self.name + '\t:'
        res += self.src + ' > '
        res += self.dest + ' = '
        res += str(self.val) + ' = '
        if self.condition is not None:
            res += ' (IF ' +self.condition + ')'
        res += '\n'
        return res






main()