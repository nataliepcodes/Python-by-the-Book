# use a loop to see how hard it might be to win the kind of lottery you just modelled in ex 9-15
# make a list or tuple called my ticket
# write a loop that keeps pulling numbers until your ticket wins
# print a message reporting how many times the loop had to run to give you a winning ticket

from random import sample

# sample() function returns a particular length list of items chosen from the sequence 
# sequence: i.e. list, tuple, string or set

# initialize a list of numbers
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# initialize a ticket with 4 numbers
my_ticket = ['0', '3', '1', '5']
print(f"\nThis is your ticket: {my_ticket}")

# intialize a counter to 0
counter = 0

# loop and generate the random sample until there is a match with the ticket number
while True:
    random_sample = sample(list, 4)
    # count how many time it looped 
    counter +=1
    if random_sample == my_ticket:
        print(f"This is a matching random number: {random_sample}\n\n")
        print("----------------- Congratulations! You Won! ----------------- \n")
        break

# print the total counter        
print(f"The loop had to run {counter} times to get to your winning ticket.\n")
    