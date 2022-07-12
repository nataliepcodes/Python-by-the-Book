# write a program that polls the user about their dream vacation
# "If you could visit one place in the world, where would you go?"

# created an empty dictionary to store responses
poll_responses = {}

print("\n")
print("----- DREAM VACATION POLL -----")
# ask 5 users about their dream vacation
user = 0
while user < 5:
    user += 1
    print(f"\nUSER #{user}")
    name = input("Q: What is your name? \nA: ")
    response = input("Q: If you could visit one place in the world, where would you go? \nA: ")
    poll_responses[name] = response

print("\n----- POLL RESPONSES -----")
for name, vacation in poll_responses.items():
    print(f"{name.title()} would like to go to {vacation.title()}.")

print("\n")

