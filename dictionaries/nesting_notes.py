# nesting: storing list inside a dictionary or a dictionary inside a list or a dictionary inside a dictionary

print("\n-----> A list of dictionaries <-----\n")

# create dictionary for each shape
shape_1 = {'color':'blue', 'shape':'triangle'}
shape_2 = {'color':'yellow', 'shape':'circle'}
shape_3 = {'color':'grey', 'shape':'square'}

# store all dictionaries in a list
shapes = [shape_1, shape_2, shape_3]
print(shapes)

# all dict in a list should have identical structure so that we can loop through the list and work on each dictionary object in the same way
# dictionaries can be generated with loop  / range
print("\n")
shapes = []
for shape in range(5):
    new_shape = {'color':'red', 'shape':'rectangle'}
    shapes.append(new_shape)
print(shapes)

# slice the first 2 shapes and change the value
print("***")
for shape in shapes[:2]:
    if shape['color'] == 'red':
        shape['color'] = 'yellow'
        shape['shape'] = 'circle'
print(shapes)

print("\n-----> A list in a dictionary <-----\n")
# if nesting goes into too many layers, a simpler solution exists

pizza = {
    'crust':'thin',
    'toppings':['tomato', 'cheese', 'anchovies']
}
print(f"You ordered a {pizza['crust']}-crust pizza with these toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

print("\n-----> A dictionary in a dictionary <-----\n")
# first define a dictionary with 2 keys
# then the value of each key is a dictionary with first name, last name and location
# can be used in storing website users