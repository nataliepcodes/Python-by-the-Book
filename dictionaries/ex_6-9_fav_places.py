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

