print("\n-----> Exercise 5-8 Hello Admin <-----\n")
usernames = ['username_1', 'username_2', 'admin', 'username_3', 'username_4', 'username_5']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again!")

