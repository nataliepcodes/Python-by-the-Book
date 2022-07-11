print("\n-----> Exercise 6-7 People <-----\n")
# make three dictionaries representing different people
# store dictionaries in a list
# loop through the list
# print everything you know about each person
person_1 = {
    'first_name':'anne',
    'last_name':'smith',
    'age':'26',
    'city':'montreal'
}

person_2 = {
    'first_name':'jane',
    'last_name':'black',
    'age':'34',
    'city':'new york'
}

person_3 = {
    'first_name':'luke',
    'last_name':'black',
    'age':'36',
    'city':'oslo'
}

people = [person_1, person_2, person_3]
for person in people:
    # print(person)
    print("\n")
    print(f"Name:    {person['first_name'].title()}")
    print(f"Surname: {person['last_name'].title()}")
    print(f"Age:     {person['age']}")
    print(f"City:    {person['city'].title()}")

#print("\n-----> Exercise 6-8 Pets <-----\n")
# make several dictionaries where each dictionary represents a different pet


print("\n-----> Exercise 6-8 Pets <-----\n")
# make several dictionaries, each representing a dfferent pet
# inside include the kind of animal and the owner's name
# store in a list called pets
# print everything you know about each pet
pet_1 = {
    'kind':'turtle',
    'pet_name':'jo',
    'owner':'marie',
    'alergy_to':'dogs'
}
pet_2 = {
    'kind':'fish',
    'pet_name':'blue',
    'owner':'george',
    'alergy_to':'cats'
}
pets = [pet_1, pet_2]
for pet in pets:
    print(f"I am a pet {pet['kind']} called {pet['pet_name'].title()} and my owner's name is {pet['owner'].title()}.")
    print(f"My owner is alergic to {pet['alergy_to']} and that's why I make a great pet!\n")

print("\n-----> Exercise 6-9 Favourite Places <-----\n")
# make a dictionary called favourite_places
# think of 3 names to use as keys in the dict
# store one to three fav places for each person
# loop through the dictionary, and print each person's name and their favourite places

favourite_places = {
    'anne':{
        'fav_places':['the beach', 'lisbon']
    },
    'clark':{
        'fav_places':['amalfi coast', 'barcelona']
    },
    'rufus':{
        'fav_places':['mountains', 'new york']
    }
}
for person, info in favourite_places.items():
    print(f"\nUser: {person.title()}")
    print(f"{person.title()}'s favourite places are:")
    for places in info['fav_places']:
     print(f">> {places.title()}")

print("\n-----> Exercise 6-10 Favourite Numbers <-----\n")
# modify your program from 6-2 so each person can have more than 1 favourite number
# print each person's name along with their fav number
favourite_numbers = {
    'anne' : [5, 3, 4], 
    'john' : [10, 1, 4],
    'peter': [3, 5, 6],
    'lucy' : [2, 7, 9],
    'rufus': [3, 2, 1]
}
for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in numbers:
     print(number) 

print("\n-----> Exercise 6-11 Cities <-----\n")
# make a dictionary called cities
# use the name of three cities as keys in dict
# create a dic of info about each city, incl country, popuplation and one fact
# print the name of each city and the information you stored

cities = {
    'zurich':{
        'country' : 'switzerland',
        'population' : 400_000,
        'fact': 'Zurich is home to over 1,200 drinking fountains'
    },
    'edinburgh':{
        'country' : 'scotland',
        'population' : 488_000,
        'fact': 'The Edinburgh Fringe Festival is the largest arts festival in the world'
    },
    'bristol':{
        'country' : 'england',
        'population' : 440_000,
        'fact': 'JK Rowling was born in Yate, a town near Bristol.'
    }
}

for city, info in cities.items():
    print(f"\nCITY: {city.title()}")
    print("----------------------")
    for keys, values in info.items():
        if keys == 'country':
            values = values.title()
        print(f"{keys.title()}: {values}")

