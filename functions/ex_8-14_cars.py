# write a function that stores information about a car in dictionary
# the function should receive a manufacturer and a model name
# it should then accept an arbitrary number of key arguments
# call the function with the required information and two other name-value pairs
# your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package = True)

def make_car(manufacturer, model_name, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model_name
    return kwargs



car = make_car('nissan', 'duke', color = 'black', cup_holder=True)
print(car)