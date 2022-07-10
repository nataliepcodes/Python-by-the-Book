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