print("\n-----> Exercise 5-2 <-----\n")
#  write 10 conditional tests - 5 evaluate to True, 5 evaluate to False
# test for equality or inequality of strings
# test using the lower() method
# numerical tests: equal, not equal, greater than, less that etc
# test using 'and' 'or' keywords
# test whether an item is in a list 
# test whether an item is not in a list

print("5 tests to evaluate to True")
print("test 1:")
#check if train is in the list, if True print statement, if False, print another statement
vehicles = ['car', 'bus', 'train', 'plane', 'tram']
print("If train in the list, I predict True")
print('train' in vehicles)


print("\ntest 2:")
#check if rocket is not in the list, if True print statement, if False, print another statement
print("If rocket not in the list, I predict True")
print('rocket' not in vehicles)


print("\ntest 3:")
# test using 'and' keyword
a = 3
b = 3
print("If a and b == 3, I predict True")
print(a and b == 3)


print("\ntest 4:")
# test using 'or' keyword
seat = 25
dependants = 'yes'
print("If seat < 15 or dependants == 'yes', I predict True")
print(seat < 15 or dependants == 'yes')
    

print("\ntest 5:")
fruit = 'apple'
print("If fruit == 'apple', I predict True")
print(fruit == 'apple')

print("\n5 tests to evaluate to False\n")
print("test 6:")
answer = 'No'
print("If answer.lower() == 'yes', I predict False")
print(answer.lower() == 'yes')

print("\ntest 7:")
color = 'red'
print("If color != 'white', I predict False")
print(color != 'red')

print("\ntest 8:")
a = 5
print("if a < 2, I predict False")
print(a < 3)

print("\ntest 9:")
age = 17
print("If age >= 18, I predict False")
print(age >= 18)

print("\ntest 10:")
a = 3
print("If a != 3, I predict False")
print(a != 3 and a % 2 == 0)


