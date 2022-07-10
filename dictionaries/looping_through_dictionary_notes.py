# looping through key-value pairs
# assign temp variables for key and value and use .items()
user_1 = {
    'username':'msmith',
    'name':'marie',
    'surname':'smith'
}
for key, value in user_1.items():
    print(f"\nKey:   {key}")
    print(f"Value: {value}")

print("\n")
favourite_languages = {
    'anne':'german',
    'john':'english',
    'kate':'spanish',
    'eric':'english',
    'lucy':'spanish'
}
for key, value in favourite_languages.items():
    print(f"{key.title()}'s favourite language is {value.title()}.")
print("\n")

# looping through all keys in a dictionary
# use keys() method 
# or for name in favourite_languages has a default behaviour to loop through keys
print("These people took part in the language poll:")
for name in favourite_languages.keys():
    print(name.title())

print("These people took part in the language poll:")
for name in favourite_languages:
    print(name.title())

# loopint through keys in particular order - use sorted() - sorts the list before looping through it
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thanks for participating in the poll!")

# looping through all values in dictionary
# values() method returns only the list of values, but it does not check for repeats
print("\nThese languages have been identified in the poll:")
for values in favourite_languages.values():
    print(values.title())

# set() can be used to avoid the repeats
print("\nThese languages have been identified in the poll:")
for values in set(favourite_languages.values()):
    print(values.title())
# sets can be build by using curly braces and separating items with commas
languages = {'english', 'spanish', 'german', 'english'}
print(languages)