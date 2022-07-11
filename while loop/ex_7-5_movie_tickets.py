print("\n-----> Exercise 7-5 Movie Tickets <-----")
# if person under 3, the ticket is free
# if between 3 and 12, the ticket is $10
# if person is over 12, the ticket is $15
# write a loop asking for age and tell the cost of the ticket
print("The ticket price will depend on your age.")
age = int(input("How old are you? \nYour age: "))
if age < 3:
    print(f"Your ticket is free!")
elif age >= 3 and age <= 12:
    print(f"Your ticket costs $10!")
else:
    print(f"Your ticket costs $15!")
