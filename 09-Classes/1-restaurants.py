#!/usr/bin/python3
"""
Make a class called Restaurant The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open
Make an instance called restaurant from your class Print the two attributes individually, and then call both methods
"""

class Restaurant():
    """A class that represents a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initilizes the restaurant"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """A method that displays a summary of the restaurant"""
        msg = self.name + " serves delicious " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Displays a message saying that the restaurant is open"""
        msg = self.name + " is open. Yokouso!"
        print("\n" + msg)

restaurant = Restaurant('Hamazushi', 'sushi')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
