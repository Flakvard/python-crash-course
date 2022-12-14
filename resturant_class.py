

class Resturant:
    """A simple representation of a resturant"""

    def __init__(self, name, cusine_type):
        """Initialize attributes to describe a resturant"""
        self.name = name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_resturant(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"This is {self.name} a resturant with {self.cusine_type} food"
        return long_name

    def open_resturant(self):
        """Return message that the resturant is open"""
        open_message = f"{self.name} is now open"
        return open_message

    def read_customers_served(self):
        """Read how many customers have been served"""
        print(f"\nThis resturant has served {self.number_served} customers")

    def set_number_served(self, numbers_served):
        """set number of customers that have been served"""
        self.number_served = numbers_served


    def increment_number_served(self, numbers_served):
        """increment number of customers that have been served"""
        self.number_served += numbers_served


my_new_resturant = Resturant("Marni's Italieno Pizza","Italian")
resturant_nr1 = Resturant("Jumbo Pizza","Italien")
resturant_nr2 = Resturant("Burger King","American")
print(my_new_resturant.describe_resturant())
print(my_new_resturant.open_resturant())
print(resturant_nr1.describe_resturant())
print(resturant_nr2.describe_resturant())

print(my_new_resturant.read_customers_served())

my_new_resturant.set_number_served(88)
print(my_new_resturant.read_customers_served())
my_new_resturant.increment_number_served(12)
print(my_new_resturant.read_customers_served())
