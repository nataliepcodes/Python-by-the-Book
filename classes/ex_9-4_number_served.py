# start with the program from ex 9-1
# add an attribute named number_served with a default value of 0
# create an instance called restaurant from this class
# print the number of customers the restaurant has served, then change this value and print again
# add a method called set_number_served() that lets you set the number of customers that been served
# call this method with a new number and print the value again
# add a method called increment_number_served(), letting to increment the number of customers served
# call this method with any number of customers served in a day

class Restaurant:

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def set_number_served(self):
        self.number_served = 10
        return self.number_served
    
    def increment_number_served(self, number_served):
        self.number_served += number_served
        return self.number_served
    
restaurant_1 = Restaurant("The Black Crab", "seafood")
print(restaurant_1.set_number_served())
number_served = restaurant_1.increment_number_served(20)
print(f"Daily total of number served: {number_served}")

