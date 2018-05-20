#!/usr/bin/python3
"""
Make a class called User Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile Make a method called describe_user() that prints a summary
of the users information Make another method called greet_user() that prints
a personalized greeting to the user
Create several instances representing different users, and call both methods
for each user
"""

class User():
    """A class that represents a simple user profile"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initializes the user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Displays a summary of the user's info"""
        print("\n" + self.first_name + " " + self.last_name)
        print("    Username: " + self.username)
        print("    Email: " + self.email)
        print("    Location: " + self.location)

    def greet_user(self):
        """Displays a personalized greeting for the user"""
        print("\nWelcome back, " + self.username + "!")

musashi = User("musashi", "miyamoto", "m_miyamoto",
               "m_miyamoto@example.com", "Japan")
musashi.describe_user()
musashi.greet_user

kojiro = User("kojiro", "sasaki", "k_sasaki",
               "k_sasaki@example.com", "Japan")
kojiro.describe_user()
kojiro.greet_user
