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

