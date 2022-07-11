# initialization
current_nbr = 0

# condition
while current_nbr < 10:
    print(current_nbr)
    #increment
    current_nbr += 1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print("\n----------------\n")

# let the user choose when to stop the program
prompt = "\nEnter a word and it will be printed below."
prompt += "\nEnter 'quit' to stop the program. \nEnter here: "
word = ""
#print("\n")
while word != "quit":
    word = input(prompt)
    if word != "quit":
        print(f"\nYou entered word -- {word} -- ")
print("\n")

# flag: the program runs if it is set to True, stop the program (e.g. Game Over) if False
# break: used to exit the loop
# a loop that starts with while True will run forever unless it reaches the break statement
# continue: can be used to return to the beginning of the loop