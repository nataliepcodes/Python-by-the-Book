# start with a copy of ex 8-9 program
# write a function called send messages that prints each message and moves each message to a new list called sent_messages as it is printed
# after calling the function, print both of the lists to make sure messages were moved correctly

def send_messages(messages, sent_messages):
    """Print each message and move each message to a new list as it's printed"""
    # loop through the current messages list each element, if there is a message/element 
    while messages:
        # pop the message from the end of the current list to the current variable
        current = messages.pop()
        # print the current variable/message one at a time
        print(f"--- Printed message: {current.title()}")
        # move the printed message to the new list
        sent_messages.append(current)

# current list
messages = ["have a nice day", "you can do it", "learn to listen", "follow your own path", "keep trying", "be your own friend", "when you don't know the destination, enjoy the journey", "not every message needs a response"]

# new list
sent_messages = []

print("\n")

# calling send_messages function with 2 arguments - current messages list and new messages list
send_messages(messages, sent_messages)

# print both lists - messages and sent messages to check that the messages have been moved correctly

print("\n")

# if the messages' migration was successful, the list should be empty
for message in messages:
    print(f"This is an initial list: {message}")

# if the messages' migration was successful, the list should include the messages (it was an empty list before)
for message in sent_messages:
    print(f">>> Sent Message: {message.title()}")

print("\n")
