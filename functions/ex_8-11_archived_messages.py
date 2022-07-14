# start with the ex 8-10 program
# call function send_messages() with a copy of a list of messages
# after calling the function print both of the lists to show that the original list has retained information

# more notes on this in the ex 8-10
def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop()
        print(f"--- Printed (copy) message: {current.title()}")
        sent_messages.append(current)


# current list
messages = ["have a nice day", "you can do it", "learn to listen", "follow your own path", "keep trying", "be your own friend", "when you don't know the destination, enjoy the journey", "not every message needs a response"]

# new list
sent_messages = []

print("\n")

# calling send_messages function with 2 arguments - a copy of the current messages list and a new messages list
send_messages(messages[:], sent_messages)

# print both lists - messages and sent messages to check that the messages have been moved correctly

print("\n")

# if the messages' migration and the copy of the list was successful, the list should print the initial messages
for message in messages:
    print(f"*** This is the original message: {message}")

print("\n")

# if the messages' migration was successful, the list should include the messages (it was an empty list before)
for message in sent_messages:
    print(f">>> Sent Message: {message.title()}")

print("\n")
