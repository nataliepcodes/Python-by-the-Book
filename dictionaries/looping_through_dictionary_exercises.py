print("\n-----> Exercise 6-4 Glossary <-----\n")
# take ex 6-3 words and use a loop to print them
new_words = {
    'list':'a list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]', 
    'tuple':'tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples consist of values in parenthesis and separated by comma.', 
    'colon':'colon is a punctuation mark consisting of two equally sized dots placed on the same vertical line', 
    'dictionary':'dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values',
    'immutable':'unchanging over time or unable to be changed'
}
for keys, values in new_words.items():
    print(f"{keys}:\n{values}\n")

print("\n-----> Exercise 6-5 Rivers <-----\n")
# make a dictionary containing 3 major rivers and a country each river runs through
# must contain key-value pair 'nile':'egypt'
# use a loop to print a sentence about each river, e.g Nile runs through Egypt
rivers = {'thames':'uk', 'nile':'egypt', 'volga':'russia'}
for river, country in rivers.items():
    if country =='uk':
        print(f"{river.title()} runs through {country.upper()}.")
    else:
        print(f"{river.title()} runs through {country.title()}.")
print("\n")

# use a loop to print a name of each river
for river in rivers:
    print(river.title())
print("\n")

# use a loop to print a name of each country
for country in rivers.values():
    if country == 'uk':
        print(country.upper())
    else:
        print(country.title())
print("\n")


print("\n-----> Exercise 6-4 Pollings <-----\n")
# use the code in favourite_languages
# make a list of who should take the poll
# include names who are in the dictionary and some that are not
# loop through a list of people who should take the poll
# if they have taken the poll, print the message thanking them responding
# if they haven't taken the poll, print the message inviting them to take the poll
name_for_poll = ['anne', 'john', 'luc', 'kate', 'angela', 'eric', 'marie', 'lucy']
favourite_languages = {
    'anne':'german',
    'john':'english',
    'kate':'spanish',
    'eric':'english',
    'lucy':'spanish'
}
for name in name_for_poll:
    if name in favourite_languages.keys():
        print(f"Dear {name.title()}, thanks for participating in the language poll! 👏")
    else:
        print(f" *** Dear {name.title()}, please take the language poll by Saturday 31st December 2022!✨ *** ")
print("\n")