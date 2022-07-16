# start with class from exercise 9-1
# create three different instances from the class and call describe_restaurant for each

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe restaurant type"""
        print(f"The name of this restaurant is {self.restaurant_name}.\nThis is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Print a message that restaurant is open"""
        print(f"{self.restaurant_name} is currently open.")

print("------------------------------------------------")
restaurant_one = Restaurant("The Dried Olive", "vegetarian")
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()
print("------------------------------------------------")
restaurant_two = Restaurant("The Friendly Cow", "steak")
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()
print("------------------------------------------------")
restaurant_three = Restaurant("The Silver Fork", "fine food")
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
print("------------------------------------------------")