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