# one common problem when receiving an input is that users provide text instead of numbers
# when you try to convert input to an int you'll get a ValueError
# write a program that prompts for two numbers, add them together and print the result
# catch the ValueError if either input value is not a number, and print a friendly error message
# test your program by entering to numbers and then a text instead of a number

print("\n---- Please enter two numbers, and the program will add them up for you! ----\n")

active = True
while active:
    try:
        number_1 = int(input("Please enter a first number: "))
        number_2 = int(input("Please enter a second number: "))
        addition = number_1 + number_2
        print(f"The result is {addition}\n")
        active = False
    except ValueError:
            print("Please enter a number! Thank you!")
