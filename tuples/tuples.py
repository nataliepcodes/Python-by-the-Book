print("\n-----> Tuples <-----\n")
# immutable means a value that cannot change
# an immutable list is called a tuple
# used to store values that should not change throughout the life of a program
# parantheses used instead of square brackets
# e.g. dimensions = (100, 50)
# if only one element, use a trailing comma, e.g. alpha = (8,)
# can't reassing a value (e.g. via variable[index] = 90) but can assign a new value to a variable

rectangle = (100, 50)
print(rectangle)

# loop through a tuple
for i in rectangle:
    print(i)

# writing over a tuple, assign a new value to original variable
print("original rectangle:")
rectangle = (100, 50)
print(rectangle)

print("modified rectangle:")
rectangle = (90, 45)
print(rectangle)

print("\n-----> Exercise 4-13 <-----\n")
# buffet: think of five foods and store them in a tuple
# use a loop to print each item
# try to modify an item, make sure python rejects a change
# restaurant changes the menu replacing two items with diffrent foods, rewrite and print changed tuple

print("Original menu:")
foods = ('pasta', 'rice', 'salad', 'pizza', 'pie')
for food in foods:
    print(food)

print("\nChanged menu:")
foods = ('vegetarian pasta', 'boiled rice', 'salad', 'pizza', 'pie')
for food in foods:
    print(food)
