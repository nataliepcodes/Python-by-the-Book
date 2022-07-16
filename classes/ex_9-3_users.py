# make a class called User
# create two attributes called first_name and last_name
# then create other attributes that are typically stored in a user profile
# make a method called describe_user() that prints a summary of the user's information
# make another method called greet_user() that prints a personalised meeting to the user
# create different instances representing different users, call each method for each user

class User:

    def __init__(self, first_name, last_name, age, pronoun, location, interest):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pronoun = pronoun
        self.location = location
        self.interest = interest
        
    
    def describe_user(self):
        print(f"This is {self.first_name} {self.last_name}.")
        print(f"{self.first_name} is {self.age} years old and is based in {self.location}.")
        print(f"In {self.pronoun} spare time {self.first_name} likes to {self.interest}.")

    def greet_user(self):
        print(f">> Hello, {self.first_name}! Welcome to the Club! Thanks for joining! It is nice to have you with us! <<")

print("\n")
user_1 = User("Stuart", "Smart", 17, "his", "England", "bake brownies")
user_1.describe_user()
user_1.greet_user()
print("\n")
user_2 = User("Ellen", "Jones", 29, "her", "Sydney", "play golf")
user_2.describe_user()
user_2.greet_user()
print("\n")
user_3 = User("Alex", "Brown", 37, "her", "Houston", "play chess")
user_3.describe_user()
user_3.greet_user()
print("\n")
