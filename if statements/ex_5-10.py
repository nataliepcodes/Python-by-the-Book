print("\n-----> Exercise 5-10 Checking Usernames <-----\n")
# make a list of 5 or more usernames called current users
# make a list of 5 or more usernames called new users, include 1 or 2 users from current users list
# loop through the new users list if the username has already been used
# if it has been used, print a message to that user that they need a new username
# else print a message that the usename is available
# make sure the comparison is in case insensitive
# if 'John' has been used 'JOHN should not be accepted
current_users = ['marie123', 'John_1', 'anne22', 'bunny3', 'joe.smith']
new_users = ['anne22', 'JOHN_1', 'john.black', 'marie123', 'charles.clark']
current_users_lower = [user.lower() for user in current_users]
print(current_users_lower)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} username already exists. Please select another username.")
    else:
        print(f"The {new_user} username is available.")

