# input() function pauses the program and waits for the user to enter input
# input() function interprets the user input as a string, use int() for numbers
# once the input is received, it is assigned to a variable

name = input("What's your name: ")
print(f"Hello, {name.title()}! Wishing you a nice day!")

print("\n----------------\n")


# over two lines, concatinates the strings with +=
prompt = "Thanks for taking time to complete this survey"
prompt += "\nWhat's your name?"
name = input(prompt)
age = int(input("How old are you?"))
print(name.title())
print(age)

if age >= 18:
    print("You can enter.")
else:
    print("Sorry, you cannot enter without your parents.")

print("\n----------------\n")

# modulo operator: divides one number by another and returns a remainder
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
modulo = a % b
print(modulo)


