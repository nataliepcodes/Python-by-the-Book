print("\n-----> Exercise 4-3 <-----\n")
# use for loop to print the numbers from 1 to 20, inclusive
for value in range(1, 21):
    print(value)

print("\n-----> Exercise 4-4 <-----\n")
# make a list of numbers from 1 to 1 million, then print using for loop
numbers = [value for value in range(1, 1_000_001)]
#print(numbers)

print("\n-----> Exercise 4-5 <-----\n")
# print min(), max(), sum() of 1 to 1 million list
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("\n-----> Exercise 4-6 <-----\n")
# print odd numbers from 1 to 20
for value in range(1, 20, 2):
    print(value)

print("\n-----> Exercise 4-7 <-----\n")
# threes: make a list of multiples of 3 from 3 to 30
multiples = []
for value in range(1, 11):
    temp = value * 3
    multiples.append(temp)
print(multiples)

print("\n-----> Exercise 4-8 <-----\n")
# cube: a number raised to the third power
# make a list of the first 10 cubes (int from 1 through 10), use for loop to print
cubes = []
for value in range (1, 11):
    temp = value ** 3
    cubes.append(temp)
print(cubes)

print("\n-----> Exercise 4-9 <-----\n")
# cube comprehension: use list comprehension to generate a list of 10 cubes
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)