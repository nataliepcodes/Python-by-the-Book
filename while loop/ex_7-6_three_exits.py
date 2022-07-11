print("\n-----> Exercise 7-6 Three Exits <-----")
# select either ex 7-4 or ex 7-5
# write different versions that do each of the following at least once:

# 1. use a conditional statement in while statement to stop the loop
print("#1")
answer = 1
prompt = "\nEnter three pizza toppings below."
prompt += "\nYour topping: "
topping = ""
while answer <= 3:
    topping = input(prompt)
    answer += 1
    print(f"\n{topping.title()} will be added to your pizza!")

# 2. use an active variable to control how long the loop runs
print("\n#2")
active = True
prompt = "\nEnter a pizza topping below."
prompt += "\nEnter 'quit' to stop the program. \nYour topping: "
topping = ""
while active:
    topping = input(prompt)
    if topping != "quit":
        print(f"\n{topping.title()} will be added to your pizza!")
    else:
        active = False

# 3. use 'break' to exit the loop when the user enters 'quit' value
print("\n#3")
prompt = "\nEnter a pizza topping below."
prompt += "\nEnter 'quit' to stop the program. \nYour topping: "
topping = ""
while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"\n{topping.title()} will be added to your pizza!")
    else:
        break

