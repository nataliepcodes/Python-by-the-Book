# write a function called make_tshirt() that accepts the size and the text of message to be printed
# the fuction should print a sentence summarizing the size and the message
# call the function once using positional arguments
# call the fucntion second time using keyword arguments
def make_tshirt(size, message):
    print(f'The t-shirt size is {size.title()}, the printed message is "{message}".')
make_tshirt("S", "I can and I will!")