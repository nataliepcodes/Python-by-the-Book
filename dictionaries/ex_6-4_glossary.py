print("\n-----> Exercise 6-4 Glossary <-----\n")
# take ex 6-3 words and use a loop to print them
new_words = {
    'list':'a list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]', 
    'tuple':'tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples consist of values in parenthesis and separated by comma.', 
    'colon':'colon is a punctuation mark consisting of two equally sized dots placed on the same vertical line', 
    'dictionary':'dictionaries are used to store data values in key-value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values',
    'immutable':'unchanging over time or unable to be changed',
    'set':'a set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable. Set itself can be changed, items can be added or removed. A set is created by placing all the items (elements) inside curly braces {}, separated by comma, or by using the built-in set() function.'
}
for keys, values in new_words.items():
    print(f"{keys}:\n{values}\n")
