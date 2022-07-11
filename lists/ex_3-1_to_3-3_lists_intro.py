print("exercise 3-1")
# 3-1 names: store the names of a few of your friends in a list called names
# print each name by accessing each element in the list one at a time

names = ['Charlie', 'Name A', 'Name B']
print(names[0])
print(names[1])
print(names[2])

print("exercise 3-2")
# greetings: start with the list in ex 3-2, print a personalised name message; message text to be the same

message_one = f"Hello, {names[0]}! Hope you have a nice day!"
print(message_one)
message_two = f"Hello, {names[1]}! Hope you have a nice day!"
print(message_two)
message_three = f"Hello, {names[2]}! Hope you have a nice day!"
print(message_three)

print("exercise 3-3")
# your own list: think of your favourite mode of transportation, make a list storing several examples
# use your list to print a series of statments about these items

transportation = ['car', 'rocket', 'scooter']
statement_one = f"Black is a nice color for a {transportation[0]}."
print(statement_one)
statement_two = f"White {transportation[1]} just left the space station."
print(statement_two)
statement_three = f"A {transportation[2]} is parked in the park at the oak tree."
print(statement_three)

