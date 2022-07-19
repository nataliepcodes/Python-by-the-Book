# write a while loop that prompts users for their name
# after the name is entered print the greeting to the screen
# add a line recording their visit in a file called guest_book.txt
# make sure each entry appears on a new line in the file

while True: 
    name = input("H-E-L-L-O, Guest! What is your name?: ")
    print(f"Welcome to the R-O-B-O-T P-A-R-T-Y, {name.title()}!")

    with open('ex_10-4_guest_book.txt', 'a') as file:
        file.write(f"{name.upper()}\n")
        break

# check that the name has been written to file
with open('ex_10-4_guest_book.txt', 'r') as file:
    for line in file:
        print(line)