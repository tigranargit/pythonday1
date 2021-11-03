import math #import the whole module
from math import sqrt, factorial, floor, pi #import only what you need
#can also import your own fucntions from another .py file 
from near import near #import my own function
#if in a folder name_of_folder.name_of_file import name_of_function
import random

#def sqrt_of_number(num1):
 #   return math.sqrt(num1)

#print(sqrt_of_number(25))

def random_number():
    return random.randint(1, 20)

print(random_number())


