#!/usr/bin/python3
"""
Start with your class from Exercise 9-1 Create three
different instances from the class, and call describe_restaurant() for each
instance
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

hamazushi = Restaurant('Hamazushi', 'sushi')
hamazushi.describe_restaurant()

futomichi = Restaurant("futomichi", "ramen")
futomichi.describe_restaurant()

yakinikuking = Restaurant("Yakiniku King", "yakiniku")
yakinikuking.describe_restaurant()
