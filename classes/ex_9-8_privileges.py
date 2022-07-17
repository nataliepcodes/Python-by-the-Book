# write a separate Privileges class
# the class should have one attribute 'privileges' that stores a list of strings as per ex 9-7
# move the show_privileges method to this class
# make a Privileges instance as an attribute in the Admin class
# create a new instance of Admin and use show_privileges() method to show the privileges

class User:
    """A simple attempt to represent a User"""
    def __init__(self, first_name, last_name, age, pronoun, location, interest, clearance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pronoun = pronoun
        self.location = location
        self.interest = interest
        self.clearance = clearance

class SetAdmin():
    """Setting user as Admin"""
    def __init__(self, first_name):
        self.status = first_name
    
    def display_user_status(self):
        print(f"{self.status} is an admin user.")

class Privileges():
    """Defines and shows Admin privileges"""
    def __init__(self, name, privileges=["add post", "delete post", "ban user"]):
        self.privileges = privileges
        self.first_name = name
        
    def show_privileges(self):
        print(f"As an Admin user {self.first_name} can:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Replicate an Admin user privileges"""

    def __init__(self, first_name, last_name, age, pronoun, location, interest, clearance):
        """
        Initialize attributes of the parent class User.
        Then calls privileges attribute which is specific to the Admin user.
        """
        super().__init__(first_name, last_name, age, pronoun, location, interest, clearance)
        #self.privileges = Privileges()

        if clearance == "True":
         self.status = SetAdmin(first_name)
         self.privileges = Privileges(first_name)
        elif (clearance == "False"): 
            print("This user cannot be an admin yet. Please check the admin clearance!\n")

print("\n:::: USER 1 ::::\n")
admin_1 = Admin("Laura", "Kay", 19, "her", "Warsaw", "hike", "True")
# remember to add .status to the call, it looks for the status attribute
admin_1.status.display_user_status()
# remember to add .privileges to the call, it looks for the privileges attribute 
admin_1.privileges.show_privileges()

print("\n:::: USER 2 ::::\n")
admin_2 = Admin("Bob", "Grey", 24, "his", "Bristol", "cook", "False")
