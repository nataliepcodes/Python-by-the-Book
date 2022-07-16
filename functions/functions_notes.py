# def : defining a function
# say_hello(): function name
# docstring: three quotes, explains what function does
# print(): what the function is executing - body of the function
# at the end call a function to execute what is inside the function: say_hello()
def say_hello():
    """Display a greeting to Jane"""
    print("Hello, Jane!")
say_hello()

print("--------------------------------")

# passing information to a function
def say_hello(name):
    """Display a greeting"""
    print(f"Hello, {name.title()}!")
say_hello("peter")
say_hello("rufus")
say_hello("charlie")
say_hello("anne")

print("--------------------------------")

# positional arguments: the same order as the parameters are written
def display_info(name, age):
    """Display user information"""
    print(f"My friend's name is {name.title()} and he is {age} years old.")
display_info("mark", 39)

print("--------------------------------")

# keyword arguments: name-value pair that is passed to a function, each arg consists of a variabe name and a value, and lists and dictionaries of values
def display_info(name, age):
    """Display user information"""
    print(f"My friend's name is {name.title()} and he is {age} years old.")
display_info(name = "mark", age = 39)

# a default value can be defined for each parameter; if argument for parameter is given in the function call,
# Python uses that, if not a parameter's default value is used. The arg can be excluded from the function call

# greet user
def greet_user(user_names):
    for name in user_names:
        message = f"\nHello, {name.title()}."
        print(message)

users = ["harry", "anne", "john"]
greet_user(users)

# passing an arbitrary number of arguments
# arbitrary meaning: based on random choice or personal whim, rather than any reason or system
# def make_pizza(*toppings):
# an asterisk in the parameter name tells Python to make an empty tuple and add values that it receives, add to tuple
# unlimited nbr of arguments can be received
# generic parameter name is *args


# mixing positional and arbitrary arguments
# parameter accepting arbitrary number of args must be last in the function defition
# python matches position and keyword args first, then any other args

# arbitrary keyword arguments
# def build_profile(first, last, **user_info)
# ** tells python to create an empty dictionary called user_info & add there wahever value pairs it receives
# generic parameter name for non-specific keyword arguments is **kwargs

############################################################################
# storing functions in modules
# to import function, first create a module: .py file containing a code to b eimported into the program e.g. pizza.py
# the module includes only the function(s)
# the program e.g. making_pizza.py need to be in the same directory as pizza.py
# pizza.py is then imported to making_pizza.py by 'import pizza'
# the line 'import pizza' at the top of the program opens the pizza.py file and copies all the functions into the progra
# to call a function use: pizza.making_pizza('cheese', 'olives') / module_name.function_name()

# sometimes only specific functions are necessary to be imported
# to import add a line at the top of the program:
# 'from module_name import function_name()' /e.g. from pizza import make_pizza()
# multiple import functions need to be separated by comma:
# 'from module_name import function_0, function_1, function_2'
# to call: use oly a function name without a dot notation -> function_0(arg_1, arg_2) / make_pizza('pepperoni', 'other')

# using 'as' to give a FUNCTION an alias if the function name conflicts wih an existing name in the program
# from 'module' import 'function' as 'rename function'
# e.g. from pizza import make_pizza as mp
# to call: use oly a function name without a dot notation -> renamed_func(arg_1, arg_2) / mp('pepperoni', 'other')

# using 'as' to give a MODULE an alias, this allows to call module function quicker
# e.g. import module_name as mn
# mn.function_name(arg_1, arg_2, arg_3)

# importing all functions in a module using * (asterisk operator)
# from module_name import *
# function_name(arg_1, arg_2)