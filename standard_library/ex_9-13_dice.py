# make a class called Dice with an attribute called sides, which has a default value of 6
# write a method called roll_die() that prints a random number between 1 and a number of sides the dice has
# make a 6-sided dice and roll it 10 times

from random import randint

class Dice():
    """A class to roll a dice"""

    def __init__(self, sides):
        """Initializing die attribute"""
        self.sides = sides
    
    def roll_dice(self):
        """Printing a random number"""
        random = randint(1,self.sides)
        print(random)

dice = Dice(6)

current_roll = 1
while current_roll <= 10:
    print(f"--> ", end="")
    dice.roll_dice()
    current_roll += 1
