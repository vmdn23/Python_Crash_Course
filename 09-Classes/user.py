#!/usr/bin/python3
"""A class used for modeling users"""

class User():
    """A class that represents a simple user profile"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initializes the user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Displays a summary of the user's info"""
        print("\n" + self.first_name + " " + self.last_name)
        print("    Username: " + self.username)
        print("    Email: " + self.email)
        print("    Location: " + self.location)

    def greet_user(self):
        """Displays a personalized greeting for the user"""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
