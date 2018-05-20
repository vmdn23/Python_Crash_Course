#!/usr/bin/python3
"""
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the
Restaurant class you wrote in Exercise 9-1 (page 166) or
Exercise 9-4 (page 171). Either version of the class will work;
just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method
that displays these flavors. Create an instance of IceCreamStand,
and call this method.
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

class IceCreamStand(Restaurant):
    """A class that represents an ice cream stand."""

    def __init__(self, name, cuisine_type="ice_cream"):
        """Initializes an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors that are available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

smitten = IceCreamStand("Smitten Ice Cream")
smitten.flavors = ["Strawberry Buttermilk", "Salted Caramel", "Cookie Dough"]

smitten.describe_restaurant()
smitten.show_flavors()
