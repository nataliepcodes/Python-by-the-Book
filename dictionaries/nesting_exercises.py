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



