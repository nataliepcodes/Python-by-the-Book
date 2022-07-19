# write a program that prompts the user for their name
# when they respond write their name in the ex_10-3_guest.txt file

# open txt file in write mode
with open('ex_10-3_guest.txt', 'w') as file:
    # ask user for their name
    name = input("What is your name?: ")
    # write the name to file
    file.write(name.title())

# check that the name has been written to file
# open txt file in read mode
with open('ex_10-3_guest.txt', 'r') as file:
    for line in file:
        print(line)


