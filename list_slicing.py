print("\n-----> Slicing <-----\n")
# to make slice specifiy the first and last index to work on
drinks = ['coffee', 'tea', 'water']
print(drinks[0:2])  # ['coffee', 'tea']
print(drinks[:2])   # ['coffee', 'tea']
print(drinks[1:])   # ['tea', 'water']
print(drinks[:1])   # ['coffee']
print(drinks[-2:])  # -index returns elements a certain distance from the end of the list: ['tea', 'water']

# looping through a slice
vegetables = ['carrot', 'tomato', 'potato', 'brocolli', 'cabbage']
            #   0           1          2           3          4
print("These are the first 2 vegetables on the shopping list:")
for veg in vegetables[:2]:
    print("# " + veg)

print("\n-----> Copying a list <-----\n")

her_friends = ['george', 'alex', 'anne', 'marta']
his_friends = her_friends[:]

print(her_friends)
print(his_friends)

her_friends.append('rufus')
his_friends.append('lucy')

print(her_friends)
print(his_friends)

print("\n-----> Exercise 4-10 <-----\n")

shopping_list = ['bread', 'milk', 'orange juice', 'biscuits', 'chocolate', 'bananas', 'avocado', 'popcorn']
                #   0       1           2              3           4            5         6          7
print("The first three items on the list are:")
print(shopping_list[:3])
print(shopping_list[0:3])

print("Three items from the middle of the list are:")
print(shopping_list[2:5])

print("The last three items on the list are:")
print(shopping_list[-3:])


print("\n-----> Exercise 4-11 <-----\n")
# my pizzas, your pizzas: take list from ex 4-1, make copy and call it friends-pizzas
print("my initial list of pizza:")
my_pizzas = ['pepperoni', 'margherita', 'vegetarian']
for pizza in my_pizzas:
    print(pizza)

print("\nfriend's initial list of pizza")
friends_pizzas = my_pizzas[:]
for pizza in friends_pizzas:
    print(pizza)

# add different pizza to each pizza, print the pizzas
print("\nMy favourite pizzas are:")
my_pizzas.append('thin pizza')
for pizza in my_pizzas:
    print(pizza)


print("\nMy friend's favourite pizzas are:")
friends_pizzas.append('brocolli ham mix')
for pizza in friends_pizzas:
    print(pizza)