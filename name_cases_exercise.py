# 2-3 personal message: use a variable to represent person's name and print a message to that person
name = "Rufus"
print(f"Good morning, {name}!")

print("\n")

# 2-4 name cases: use a variable to represent a person's name and then print that person's name in lowercase, uppercase and title case
name = "rufus grey"
print(name.lower())
print(name.upper())
print(name.title())

print("*********************************************************************************")

# 2-5 famous quote: find a quote from a famous person you admire. print a quote and the name of its author
# in the following format -> This person once said, "........"
mandela_part_one = '\nNelson Mandela said:\n'
mandela_part_two = '"It always seems impossible until it'
mandela_part_three = "'s"
mandela_part_four = ' done"'
print(f"{mandela_part_one}{mandela_part_two}{mandela_part_three}{mandela_part_four}")

eleanor_part_one = '\nEleanor Roosevelt said:\n"Nothing has ever been achieved by the person who says,'
eleanor_part_two = "'It "
eleanor_part_three = "can’t"
eleanor_part_four =  " be done.'"
eleanor_part_five = '"\n'
print(f"{eleanor_part_one}{eleanor_part_two}{eleanor_part_three}{eleanor_part_four}{eleanor_part_five}")

jobs_part_one = 'Steve Jobs said:\n'
jobs_part_two = '"I'
jobs_part_three = "’m very excited about having the Internet in my den."
jobs_part_four = '"\n'

print(f"{jobs_part_one}{jobs_part_two}{jobs_part_three}{jobs_part_four}")

print("*********************************************************************************")