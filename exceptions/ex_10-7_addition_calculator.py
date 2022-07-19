# wrap the code from ex 10-6 in a while loop so the user can continue entering numbers
# even when they make a mistake and enter text instead of a number

print("\n>> Please enter two positive numbers, and the program will add them up for you!")
print(">> Enter -1 to quit the program.\n")

# make a loop
while True:
    # let the user enter the numbers
    try:
        number_1 = int(input("Please enter a first number: "))
        if number_1 == -1:
            break
        number_2 = int(input("Please enter a second number: "))
        if number_2 == -1:
            break
    # if the text was entered instead of number, then pass / fail silently
    except ValueError:
            pass
    #if the numbers have been entered correctly else statement applies
    else:
        addition = number_1 + number_2
        print(f"The result is {addition}\n")

   