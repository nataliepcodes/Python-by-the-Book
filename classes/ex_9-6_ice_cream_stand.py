from restaurant import Restaurant
# write a class called IceCreamStand that inherits from the restaurant class in ex 9-1 or 9-4
# add an attribute called flavours that stores a list of ice-cream flavours
# write a method that displays these flavours, create an instance of IceCreamStand and call this method

class IceCreamStand(Restaurant):
    """Represent aspects of IceCreamStand, a child of the Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        # initialize attribute specific to the child class
        self.flavours = ['strawberry', 'pistachio', 'chocolate']
    
    def display_flavours(self):
        for flavour in self.flavours:
            print(flavour.title())
        
ice_cream_stand = IceCreamStand("The Frozen Cup", "ice-cream stand")
ice_cream_stand.display_flavours()
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()

   

