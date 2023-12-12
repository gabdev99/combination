from itertools import combinations
from itertools import product

def combs(iterable, num_of_items):
    possibilities = len(tuple(combinations(iterable, num_of_items)))
    return possibilities

def combs_order(iterable, num_of_items):
    possibilities = len(tuple(product(iterable, repeat=num_of_items)))
    return possibilities