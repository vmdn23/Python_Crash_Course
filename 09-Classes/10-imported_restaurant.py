#!/usr/bin/python3
"""
Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant
instance, and call one of Restaurants methods to show that the
import statement is working properly.
"""


from restaurant import Restaurant


ikinari_steak = Restaurant('ikinari steak', 'steak, steak and more steak')
ikinari_steak.describe_restaurant()
ikinari_steak.open_restaurant()
