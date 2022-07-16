# in OOP (modelling real-world situations):
# classes are created to represent real-world things and situations
# objects are created based on the classes
# a classes represents a general behavior of a category of objects
# individual object is equipped with the general behavior
# instantiation: creating an object from a class / instances of a class

# for now methods move_forward and turn_left only print a message
# these can be extended to realistic situations to direct movements of an object
class Robot:
    """A simple attempt to model a robot"""
    
    def __init__(self, name, color):
        """Initializing the name and color attributes"""
        self.name = name
        self.color = color
    
    def move_forward(self):
        """Simulate a robot moving in response to a command"""
        print(f"{self.name} is now moving forward ^")
    
    def turn_left(self):
        """Simulate a robot moving in response to a command"""
        print(f"{self.name} is now turning left <")

# instance to represent a specific robot
# 'Robot' represents a class, 'my_robot' represents a single instance created from that class
# dot notation is used to access attributes of an instance, e.g. my_robot.name
my_robot = Robot('Bennie-X', 'grey')
print(f"This robot's name is {my_robot.name}")
print(f"{my_robot.name}'s color is {my_robot.color}")

# to call a method / function within the class, give a name of an instance & the name of the method separated by a dot
my_robot.move_forward()
my_robot.turn_left()

# can create as many instances as you need as long as these have a unique variable or unique place in a list or a dictionary
another_robot = Robot('Connie-L', 'purple')
print(f"This robot's name is {another_robot.name}")
print(f"{another_robot.name}'s color is {another_robot.color}")
another_robot.move_forward()
another_robot.turn_left()


