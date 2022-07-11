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
