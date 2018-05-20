#!/usr/bin/python3
"""
Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery().
This method should check the battery size and set the capacity
to 85 if it isnt already. Make an electric car with a default
battery size, call get_range() once, and then call get_range()
a second time after upgrading the battery.
You should see an increase in the cars range.
"""

class Car():
    """A class that represents a car"""

    def __init__(self, manufacturer, model, year):
        """Initializes attributes that describe a car"""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a beautifully formated descriptive name"""
        long_name = str(self.year) + " " + self.manufacturer + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Prints a statement that shows the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Sets the odometer to a given amount
        Rejects changes if there is an attempt
        to roll back the odometer value.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add a given amount to the odometer reading"""
        self.odometer_reading += miles

class Battery():
    """A class that represents a battery for an electric car"""

    def __init__(self, battery_size=60):
        """Initialize battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a statement that describes the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWH battery.")

    def get_range(self):
        """Prints a statement about the range this battery provides"""
        if self.battery_size == 60:
              range = 140
        elif self.battery_size == 85:
              range = 185

        message = "This car could probably go about " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrades the battery... if possible"""
        if self.battery_size == 60:
              self.battery_size = 85
              print("Upgraded the battery to 85 kWH.")
        else:
              print("The battery is already upgraded.")


class ElectricCar(Car):
    """Models aspects of a car that is specific to electric vehicles"""

    def __init__(self, manufacturer, model, year):
        """
        Initializes attributes of the parent class.
        Then initializes attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("Make an electric car and check the battery:")
my_tesla = ElectricCar("tesla", "model v", 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

print("\nUpgrade the battery and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery again.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
