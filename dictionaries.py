# allows to store related information
# a collection of key-value pairs, each key is connected to a value, use key to access the value associated with that key
# key's value can be a number, string, list or a dictionary
# dictionary is a dynamic stricture and key value pairs can be added anytime
# below dictionary stores alien's color and point value

alien_2 = {'color':'yellow', 'points': 10} # key is color, value is yellow
print(alien_2['color'])
print(alien_2['points'])

# adding additional key-value pairs
alien_2['x_position'] = 5
alien_2['y_position'] = 30
print(alien_2)

# starting with empty dictionary
alien_3 = {}
alien_3['color'] = 'blue'
alien_3['points'] = 15
print(alien_3)

#removing key-value pair
del alien_3['points'] # deleted permanently
print(alien_3)

# dictionary of similar objects
favourite_languages = {
    'anne':'german',
    'john':'english',
    'kate':'spanish'
}
print(f"Anne's favourite language is {favourite_languages['anne'].title()}.")
# or
language = favourite_languages['john'].title()
print(f"John's favourite language is {language}.")

# using get() to access value
# first argument is a key, second optional argument can be a specific value if the key doen't exist
alien_4 = {'color':'black', 'speed':'medium'}
point_value = alien_4.get('points', 'No value exists yet.')
print(point_value)

print("\n-----> Exercise 6-1 Person <-----\n")
# use dictionary to store information about the person you know
# first, last name, age, city
# print each piece stored in the dictionary
person = {
    'first_name':'anne',
    'last_name':'smith',
    'age':'26',
    'city':'montreal'
}
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

print("\n-----> Exercise 6-2 Favourite Numbers <-----\n")
# use dictionary to store people favourite numbers
# think of 5 names, use them as keys
# print each person's name and favourite number
favourite_numbers = {
    'anne' : 5, 
    'john' : 10,
    'peter' : 7,
    'lucy' : 2,
    'rufus' : 6,
}
print(f"Anne's favourite number is {favourite_numbers['anne']}.")
print(f"John's favourite number is {favourite_numbers['john']}.")
print(f"Peter's favourite number is {favourite_numbers['peter']}.")
print(f"Lucy's favourite number is {favourite_numbers['lucy']}.")
print(f"Rufus's favourite number is {favourite_numbers['rufus']}.")

print("\n-----> Exercise 6-3 Glossary <-----\n")
# python's dictionary can be used to model actual dictionary
# think of 5 new words learned in previous chapters
# store words as keys
# store words' meanings as values
# print each word and a meaning as neatly formatted output (word: meaning; or a word then a meaning on new line)
new_words = {
    'list':'a list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]', 
    'tuple':'tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples consist of values in parenthesis and separated by comma.', 
    'colon':'colon is a punctuation mark consisting of two equally sized dots placed on the same vertical line', 
    'dictionary':'dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values',
    'immutable':'unchanging over time or unable to be changed'
}
print(f"list:\n{new_words['list']}\n")
print(f"tuple:\n{new_words['tuple']}\n")
print(f"colon:\n{new_words['colon']}\n")
print(f"dictionary:\n{new_words['dictionary']}\n")
print(f"immutable:\n{new_words['immutable']}\n")