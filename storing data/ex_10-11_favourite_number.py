# write a program that prompts for the user's favourite number
# use json.dump() to store this data in a file
# write a separate program that reads this value and prints a message "I know your favourite number! It'...!"

import json

def get_number():
    """Get a number from the user. The program runs until a number is entered"""
    while True:
        try:
            number = int(input("What's your favourite number?: "))
            return number
        except ValueError:
            print("Please enter a number!")


def store_data():
    """Storing number in JSON format"""
    # getting a number from the get_number() function
    number = get_number()
    # creating a filename variable
    filename = 'number.json'
    # open file in write mode
    with open(filename, 'w') as file:
        # move the number to the file with json.dump()
        json.dump(number, file)

store_data()

def read_data():
    """Reading number from JSON file"""
    # specify the filename
    filename = 'number.json'
    # open file in read mode
    with open(filename) as file:
        number = json.load(file)
        # print the number from the file
        print(f"I know your favourite number! It' {number}")

read_data()
