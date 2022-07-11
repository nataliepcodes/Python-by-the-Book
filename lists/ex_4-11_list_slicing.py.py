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