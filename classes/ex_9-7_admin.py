from users import User
# write a class called Admin that inherits from the User class in ex 9-3 or ex 9-5
# add an attribute privileges that stores a list of strings like "can add post", "can delete post", "can ban user"
# write a method called show_privileges() that shows the administrator's set of privileges
# create an instance Admin and call show_privileges() method

class Admin(User):
    """Replicate an Admin user privileges"""

    def __init__(self, first_name, last_name, age, pronoun, location, interest):
        """
        Initialize attributes of the parent class User.
        Then initialize attributes specific to the Admin user.
        """
        super().__init__(first_name, last_name, age, pronoun, location, interest)
        self.privileges = ["add post", "delete post", "ban user"]
    
    def show_privileges(self):
        print(f"As an Admin user {self.first_name} can:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("Laura", "Kay", 19, "her", "Warsaw", "hike")
admin.show_privileges()
