#!/usr/bin/python3
"""
Start with your program from Exercise 9-1 (page 166)
Add an attribute called number_served with a default value of 0 Create an
instance called restaurant from this class Print the number of customers the
restaurant has served, and then change this value and print it again
Add a method called set_number_served() that lets you set the number
of customers that have been served Call this method with a new number and
print the value again
Add a method called increment_number_served() that lets you increment
the number of customers whove been served Call this method with any number you like that could represent how many customers were served in, say, a
day of business
"""

class Restaurant():
    """A class that represents a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initilizes the restaurant"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """A method that displays a summary of the restaurant"""
        msg = self.name + " serves delicious " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Displays a message saying that the restaurant is open"""
        msg = self.name + " is open. Yokouso!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow users to set the number of customers that have beend served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served

restaurant = Restaurant('Hamazushi', 'sushi')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 888
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(4615)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(920)
print("Number served: " + str(restaurant.number_served))
