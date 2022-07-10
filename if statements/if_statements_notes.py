print("\n-----> If Statetements <-----\n")
drinks = ['coffee', 'tea', 'water']
for drink in drinks:
    if drink == 'coffee':
        print(drink.upper())
    else:
        print(drink.title())
# when if conditional test evaluates to True, the code is executed; if False, not executed
# checking equality is case sensitive in Python: 'audi' is not equal 'Audi'
# variable value can be converted to lower case: car = 'Audi car.lower() == 'audi'

# if conditional_test:
    # do something

# checking for inequality with !=
color = 'black'
if color != 'white':
    print("Color is black")

# numerical comparisons
age = 25
if age != 37:
    print(":)")

# keywords 'and' & 'or' can be used to check multiple conditions
# checking if value is in the list - use keyword 'in'
colors = ['yellow', 'black', 'green']
if 'yellow' in colors:
    print(True)

if 'white' in colors:
    print(True)
else:
    print(False)   

# checking if value is not in the list - use keyword 'not'
guest_list = ['anne', 'rufus', 'bob', 'george']
uninvited = 'marie'
if uninvited not in guest_list:
    print(f"{uninvited.title()}, you can attend if you are free!")


print("\n-----> If, Elif, Else Statetements <-----\n")
# if you want one block of code to run, use if, elif, else
# if more than one block of code needs to run, use if statement

print("\n-----> If Statements with Lists <-----\n")
# list = []
# if list has at least one value, the condition evaluates to True
# if list.. - loop  - else..


