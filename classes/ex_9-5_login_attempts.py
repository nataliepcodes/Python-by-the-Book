# add an attribute login_attempts to the user class from ex 9-3
# write a method login_attempts() that increments the value of login attempts by 1
# write another method called reset_login_attempts(), that resets the attempts to 0
# make an instance of the user class and call increment_login_attempts() several times, print the value of login_attempts() to check it was incremented correctly
# then call reset_login_attempts()
# print login_attempts again to check it was reset to 0


class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempt = 0
    
    def login_attempts(self):
        self.login_attempt += 1
        return self.login_attempt
    
    def reset_login_attempts(self):
        self.login_attempt = 0
        return self.login_attempt

        
print("\n")
user_1 = User("Stuart", "Smart", 17)
login_attempt = user_1.login_attempts()
login_attempt = user_1.login_attempts()
login_attempt = user_1.login_attempts()
login_attempt = user_1.login_attempts()
print(login_attempt)
login_attempt = user_1.reset_login_attempts()
print(login_attempt)
print("\n")

