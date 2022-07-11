print("\n-----> Exercise 7-3 Multiples of Ten <-----\n")
# ask a user for a numner, and then report if the number is multiple of 10 or not
prompt = "Let's check if the number is a multiple of 10!"
print(prompt)
number = int(input("Please enter a number: "))
if number % 10 == 0:
    print(f"Number {number} is a multiple of 10.")
else:
    print(f"Number {number} is not a multiple of 10.")
