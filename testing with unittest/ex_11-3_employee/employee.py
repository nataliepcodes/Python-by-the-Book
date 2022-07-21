# create a class called Employee
# the __init__() method should take in a first name, last name and annual salary and store these as attributes
# write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount

class Employee:
    """A class to represent an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first = first_name
        self.last = last_name
        self.salary = annual_salary
    
    def give_raise(self, raise_amount=5_000):
        raised_salary = self.salary + raise_amount
        return raised_salary
    
employee = Employee('George', 'Black', 60_000)
employee.give_raise(1000)