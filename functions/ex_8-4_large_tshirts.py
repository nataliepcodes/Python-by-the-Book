# modify make_tshirt function from ex 8-3 so that shirts are large by default with a message that reads "I love Python"
# make a large shirt and a medium shirt with the default message, and shirt of any size with a different message
def make_tshirt(size="L", message="I love Python."):
    print(f"\nSize: {size} \nMessage: {message}\n")
make_tshirt()
make_tshirt("M")
make_tshirt("S", "5, 4, 3, 2, 1 ... Magic✨!")