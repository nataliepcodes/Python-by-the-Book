print("\n-----> Exercise 7-1 Rental Car <-----\n")
# write a program asking the user what kind of car they would like
# print a message about that car
car = input("What kind of car would you like to rent? \n>> ")
print(f"Let me see if I can find you a {car.title()}.")

print("\n-----> Exercise 7-2 Restaurant Seating <-----\n")
# write a program asking the user how many people are in their group
# if more than eight, print that they will have to wait for a table
# otherwise, print that the table is ready
guests = int(input("How many people are in your group? \n>> "))
if guests > 8:
    print("Sorry, your table is not ready yet. Please wait in the reception area.")
else:
    print("Your table is ready. Follow me!")

print("\n-----> Exercise 7-3 Multiples of Ten <-----\n")
# ask a user for a numner, and then report if the number is multiple of 10 or not
prompt = "Let's check if the number is a multiple of 10!"
print(prompt)
number = int(input("Please enter a number: "))
if number % 10 == 0:
    print(f"Number {number} is a multiple of 10.")
else:
    print(f"Number {number} is not a multiple of 10.")
