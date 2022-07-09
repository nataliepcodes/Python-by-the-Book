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


print("\n-----> Exercise 5-1 <-----\n")
# conditional tests
color = 'white'
print("Is color == 'white'? I predict True")
print(color == 'white')

print("\nIs color == 'red'? I predict False")
print(color == 'red')

print("\n-----> Exercise 5-2 <-----\n")
#  write 10 conditional tests - 5 evaluate to True, 5 evaluate to False
# test for equality or inequality of strings
# test using the lower() method
# numerical tests: equal, not equal, greater than, less that etc
# test using 'and' 'or' keywords
# test whether an item is in a list 
# test whether an item is not in a list

print("5 tests to evaluate to True")
print("test 1:")
#check if train is in the list, if True print statement, if False, print another statement
vehicles = ['car', 'bus', 'train', 'plane', 'tram']
print("If train in the list, I predict True")
print('train' in vehicles)


print("\ntest 2:")
#check if rocket is not in the list, if True print statement, if False, print another statement
print("If rocket not in the list, I predict True")
print('rocket' not in vehicles)


print("\ntest 3:")
# test using 'and' keyword
a = 3
b = 3
print("If a and b == 3, I predict True")
print(a and b == 3)


print("\ntest 4:")
# test using 'or' keyword
seat = 25
dependants = 'yes'
print("If seat < 15 or dependants == 'yes', I predict True")
print(seat < 15 or dependants == 'yes')
    

print("\ntest 5:")
fruit = 'apple'
print("If fruit == 'apple', I predict True")
print(fruit == 'apple')

print("\n5 tests to evaluate to False\n")
print("test 6:")
answer = 'No'
print("If answer.lower() == 'yes', I predict False")
print(answer.lower() == 'yes')

print("\ntest 7:")
color = 'red'
print("If color != 'white', I predict False")
print(color != 'red')

print("\ntest 8:")
a = 5
print("if a < 2, I predict False")
print(a < 3)

print("\ntest 9:")
age = 17
print("If age >= 18, I predict False")
print(age >= 18)

print("\ntest 10:")
a = 3
print("If a != 3, I predict False")
print(a != 3 and a % 2 == 0)

print("\n-----> If, Elif, Else Statetements <-----\n")
# if you want one block of code to run, use if, elif, else
# if more than one block of code needs to run, use if statement

print("\n-----> Exercise 5-3 Alien Colors #1 <-----\n")
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
print("if green is alien color, I predict True")
print('green' in alien_color)
print("if green is not alien color, I predict False")
print('green' not in alien_color)

print("\n-----> Exercise 5-4 Alien Colors #2 <-----\n")
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

print("\n-----> Exercise 5-5 Alien Colors #3 <-----\n")
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

print("\n-----> Exercise 5-6 Stages of Life <-----\n")
age = 25
if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
else: 
    print("You are an elder")


print("\n-----> Exercise 5-7 Different Fruit <-----\n")
fruit = ['apple', 'banana', 'mango']
if 'apple' in fruit:
    print("You really like bananas")
if 'kiwi' in fruit:
    print("You really like fruit")
if 'banana' in fruit:
    print("You really like bananas")
if 'pear' in fruit:
    print("You really like fruit")
if 'mango' in fruit:
    print("You really like bananas")


print("\n-----> If Statements with Lists <-----\n")
# list = []
# if list has at least one value, the condition evaluates to True
# if list.. - loop  - else..

print("\n-----> Exercise 5-8 Hello Admin <-----\n")
usernames = ['username_1', 'username_2', 'admin', 'username_3', 'username_4', 'username_5']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again!")

print("\n-----> Exercise 5-9 No Users <-----\n")
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again!")
else:
    print("We need to find some users!")


print("\n-----> Exercise 5-10 Checking Usernames <-----\n")
# make a list of 5 or more usernames called current users
# make a list of 5 or more usernames called new users, include 1 or 2 users from current users list
# loop through the new users list if the username has already been used
# if it has been used, print a message to that user that they need a new username
# else print a message that the usename is available
# make sure the comparison is in case insensitive
# if 'John' has been used 'JOHN should not be accepted
current_users = ['marie123', 'John_1', 'anne22', 'bunny3', 'joe.smith']
new_users = ['anne22', 'JOHN_1', 'john.black', 'marie123', 'charles.clark']
current_users_lower = [user.lower() for user in current_users]
print(current_users_lower)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} username already exists. Please select another username.")
    else:
        print(f"The {new_user} username is available.")


print("\n-----> Exercise 5-11 Ordinal Numbers <-----\n")
# store numbers 1 to 9 in a list
# loop through the list
# use if, elif, else statement to print the ordinal ending of each number
# output should read: 1st 2nd 3rd 4th 5th 6th 7th 8th 9th and each result on separate line
numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == 1:
        print(f"{number}st")
    if number == 2:
        print(f"{number}nd")
    if number == 3:
        print(f"{number}rd")
    if number > 3 and number <= 9:
        print(f"{number}th")