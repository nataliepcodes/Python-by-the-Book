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