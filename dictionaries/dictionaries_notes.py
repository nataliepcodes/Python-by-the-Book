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