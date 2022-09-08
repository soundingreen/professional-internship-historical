# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:36:57 2021

@author: sound
"""

import numpy as np

def merge_dicts(combiner, dicts):
    new_dict = {}
    for d in dicts:
       for k, v in d.items():
           if k in new_dict:
               new_dict[k] = combiner(new_dict[k], v)
           else:
               new_dict[k] = v
    return new_dict

x = {'a': 1, 'b': 2}
y = {'b': 2, 'c': 3}
#z = {'a': 1, 'd': 4}
#f'{x} AND {y}'
new=merge_dicts(combiner= lambda x, y:np.vstack((x,y)) , dicts=(x,y))

print(new)
