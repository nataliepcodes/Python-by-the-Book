print("\n-----> Exercise 7-2 Restaurant Seating <-----\n")
# write a program asking the user how many people are in their group
# if more than eight, print that they will have to wait for a table
# otherwise, print that the table is ready
guests = int(input("How many people are in your group? \n>> "))
if guests > 8:
    print("Sorry, your table is not ready yet. Please wait in the reception area.")
else:
    print("Your table is ready. Follow me!")
