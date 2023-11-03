# Liquid Volume Calculator

from math import pi

def liquid_volune_calculator(h, r=10):
     vol = ((4 * pi * (r ** 3)) - (pi * (h ** 2) * ((3 * r) - h))) / 3
     return vol

print(liquid_volune_calculator(2))