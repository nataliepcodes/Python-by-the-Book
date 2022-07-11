
print("\n-----> Numerical lists <-----\n")

# range()
for value in range (1, 5):
    print(value) # prints the values from 1 to 4, the loop stops at the second value
# 1
# 2
# 3
# 4

for value in range (5):
    print(value)
# 0
# 1
# 2
# 3
# 4

# range can be used to create a list of numbers
numbers = list(range(0, 6))
print(numbers) # [0, 1, 2, 3, 4, 5]

# range() can be used to skip numbers by adding a 3rd argument, e.g. print only even numbers
numbers = list(range(0, 11, 2))
print(numbers) # [0, 2, 4, 6, 8, 10]

print("\n-----> Squares <-----\n")

# create an empty list
squares = []

# loop through numbers 1 to 11 (11 not including)
for value in range(1, 11):
    # raise a value to the 2nd power
    square = value ** 2 # square is a temp variable
    # add value to the list
    squares.append(square) # or in one line without line 56: squares.append(value**2)
print(squares)

print("\n-----> List Comprehension <-----\n")
# same as above but fewer lines of code
squares = [value**2 for value in range(1, 11)]
print(squares)


print("\n-----> Min, Max, Sum <-----\n")
numbers = [4, 5, 1, 3]
print(numbers)
print(min(numbers)) # 1
print(max(numbers)) # 5
print(sum(numbers)) # 13

