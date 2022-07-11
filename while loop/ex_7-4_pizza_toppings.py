print("\n-----> Exercise 7-4 Pizza Toppings <-----")
# write a loop prompting user to enter pizza toppings until they enter 'quit
# print message that the entered topping will be added to their pizza

prompt = "\nEnter a pizza topping below."
prompt += "\nEnter 'quit' to stop the program. \nYour topping: "
topping = ""
while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"\n{topping.title()} will be added to your pizza!")
    else:
        break

