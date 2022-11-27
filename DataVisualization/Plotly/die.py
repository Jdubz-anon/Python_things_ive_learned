import random


class Die:
    '''A class representing a single die'''
    def __init__(self, num_side=6):
        self.num_sides = num_side

    def roll(self):
        return random.randint(1,self.num_sides)

