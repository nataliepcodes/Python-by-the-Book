# write a function that accepts a list of items a person wants on a sandwich
# function to have one parameter that collect many items and print a summary of the sandwitch that was ordered
# call a function three times using a different argument each time

def order_sandwich(*args):
    """Function takes an arbitrary number of arguments and prints these"""
    print(f"\nI want this in my sandwich:")
    for item in args:
        print(item)

order_sandwich('ham')
order_sandwich('egg', 'cress', 'cucumber')
order_sandwich('peanut butter', 'jam')