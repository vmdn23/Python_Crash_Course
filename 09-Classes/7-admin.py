#!/usr/bin/python3
"""
An administrator is a special kind of user. Write a class
called Admin that inherits from the User class you wrote in
Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an
attribute, privileges, that stores a list of strings like
"can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrators
set of privileges. Create an instance of Admin, and call your method.
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

class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initializes Admin"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges that the admin has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

musashi = Admin("musashi", "miyamoto", "m_miyamoto",
               "m_miyamoto@example.com", "Japan")
musashi.describe_user()

musashi.privileges = [
    "can destroy accounts",
    "can reset passwords",
    "can ban people into the void",
]

musashi.show_privileges()
