# make a list called sandwich_orders and fill it with names of different sandwiches
# make a list finished_sandwiches
# loop through the list of sandwich_orders and pring a message for each order: e.g. I made your ".." sandwich.
# as each sandwich is made, move it to the list of finished_sanwiches
# after all the sandwiches have been made, print a message listing each sandwich that was made

sandwich_orders = ['ham & cheese', 'egg & cress', 'chicken & tomato', 'roast beef & cucumber']
finished_sandwiches = []

# the loop runs until the list is not empty
while sandwich_orders:
    # pop() the last value from the sandwich_orders list and assing it to the sandwich variable
    sandwich = sandwich_orders.pop()
    # print the sandwich name as it was popped
    print(f"I made your {sandwich} sandwich! Enjoy!🥪")
    # move the ready sandwich to the finished_sandwiches list
    finished_sandwiches.append(sandwich)
# loop through the ready sandwiches loop and print a message listing each sandwich that was made
print("\nThese sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f">> {sandwich} <<")
