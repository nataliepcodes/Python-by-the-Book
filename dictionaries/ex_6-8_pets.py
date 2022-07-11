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

