#!/usr/bin/python3
"""
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166) Write a method called increment_
login_attempts() that increments the value of login_attempts by 1 Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0
Make an instance of the User class and call increment_login_attempts()
several times Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() Print login_attempts again to
make sure it was reset to 0
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

musashi = User("musashi", "miyamoto", "m_miyamoto",
               "m_miyamoto@example.com", "Japan")
musashi.describe_user()
musashi.greet_user()

print("\nMaking 3 login attempts...")
musashi.increment_login_attempts()
musashi.increment_login_attempts()
musashi.increment_login_attempts()
print(" Login attempts: " + str(musashi.login_attempts))

print("Resetting login attempts...")
musashi.reset_login_attempts()
print(" Login attempts: " + str(musashi.login_attempts))
