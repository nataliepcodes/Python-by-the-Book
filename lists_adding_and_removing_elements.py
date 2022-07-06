# using append() to append elements to the end of the list: list.append('value')
# you can start with an empty list, e.g. list = []
# then append elements as more data is received fromt he user during the execution of the program

colors = []
colors.append('blue')
colors.append('grey')
colors.append('black')
print(colors)

# inserting elements into any position in the list by using insert()

colors = ['blue', 'grey', 'black']
colors.insert(0, 'red')
print(colors)
colors.insert(2, 'yellow') 
print(colors) # ['red', 'blue', 'yellow', 'grey', 'black']

# del statement can be used if you know the position of the item to be deleted
# can no longer access the items in the list once the del statement has been used
colors = ['blue', 'grey', 'black']
del colors[0]
print(colors) # ['grey', 'black']

# pop() method can be used if you want to access the value of the item after it has been removed
# removes the last item from the list and you can work on it after it was removed
# pop - top of the stack - end of the list
colors = ['blue', 'grey', 'black']
popped_color = colors.pop() 
print(colors)       # ['blue', 'grey']
print(popped_color) # black

