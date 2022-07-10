# sorting a list permanently with sort() method - >> all values in lowercase

fruit = ['pear', 'apple', 'orange', 'banana', 'kiwi']
print(fruit)
fruit.sort() # the list sorted in alphabetical order, PERMANENTLY
print(fruit) # ['apple', 'banana', 'kiwi', 'orange', 'pear']

fruit.sort(reverse=True) # sort in reverse alphabetical order
print(fruit)

# sorting the list temporary with the sorted() function
# displays the list in particular order but doesnt affect the initial order
fruit = ['pear', 'apple', 'orange', 'banana', 'kiwi']
print("original list:")
print(fruit)            # ['pear', 'apple', 'orange', 'banana', 'kiwi']
print("sorted list:")
print(sorted(fruit))    # ['apple', 'banana', 'kiwi', 'orange', 'pear']

# print a list in reverse order - non-alphabetical order - just reverse from initial order
fruit = ['pear', 'apple', 'orange', 'banana', 'kiwi']
fruit.reverse() # changes the order permamently but applying reverse the 2nd time will revert it back to original order
print(fruit)
fruit.reverse()
print(fruit)

# finding a length of a list - count starts with 1
fruit = ['pear', 'apple', 'orange', 'banana', 'kiwi']
len(fruit)
print(len(fruit)) # 5

