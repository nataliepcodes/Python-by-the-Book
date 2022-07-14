# make a list containing short text messages
# pass the list to a function called show_messages(), which prints eact message

def show_messages(messages):
    """Print messages from a list"""
    for message in messages:
        print("-----------------------------------------------------------------")
        print(f"\n{message.title()}!\n")
    print("-----------------------------------------------------------------")

messages = ["have a nice day", "you can do it", "learn to listen", "follow your own path", "keep trying", "when you don't know the destination, enjoy the journey", "not every message needs a response"]
show_messages(messages)