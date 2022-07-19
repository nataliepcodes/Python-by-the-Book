# write a while loop that asks people why they like programming
# each time someone enters a reason, add the reason to a file that stores the responses

while True:
    reason = input("Why do you like programming?: ")
    with open('ex_10-5_programming_poll.txt', 'a') as file:
        file.write(f"{reason}\n")
        break

with open('ex_10-5_programming_poll.txt', 'r') as file:
    for line in file:
        print(line)
