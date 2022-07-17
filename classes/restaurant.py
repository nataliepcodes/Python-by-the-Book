class Restaurant:
    # __init__ method shall store two attributes: a restaurant_name and a cuisine_type
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    # make a method called describe_restaurant() that prints name and cuisine type
    def describe_restaurant(self):
        """Describe restaurant type"""
        print(f"This is a {self.cuisine_type} restaurant.")

    # make a method called open_restaurant() that prints a message indicating a restaurant is open
    def open_restaurant(self):
        """Print a message that restaurant is open"""
        print(f"{self.restaurant_name} is currently open.")
