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

