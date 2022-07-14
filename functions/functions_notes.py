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
