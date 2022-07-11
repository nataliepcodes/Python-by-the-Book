print("\n-----> Exercise 5-11 Ordinal Numbers <-----\n")
# store numbers 1 to 9 in a list
# loop through the list
# use if, elif, else statement to print the ordinal ending of each number
# output should read: 1st 2nd 3rd 4th 5th 6th 7th 8th 9th and each result on separate line
numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == 1:
        print(f"{number}st")
    if number == 2:
        print(f"{number}nd")
    if number == 3:
        print(f"{number}rd")
    if number > 3 and number <= 9:
        print(f"{number}th")