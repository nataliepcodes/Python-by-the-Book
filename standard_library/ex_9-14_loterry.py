# make a list or tuple containing a series of 10 numbers and 5 letters
# randomly select four numbers or letters from the list
# print a message that any ticket matching these four numbers or letters wins a prize

from random import choice

def random_selection():
    """
    Randomly selecting four elements from the list
    Printing a message of a winning ticket
    """
    print(f"\nCheck your ticket!\nAny ticket maching this combination wins: ", end="")
    i = 0
    while i < 4:
        random_character = choice(options)
        print(f"{random_character.title()}", end=" ")
        i += 1
    print("\n")

options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'w', 'x', 'y', 'z', 'c']
random_selection()
