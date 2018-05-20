#!/usr/bin/python3
"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described
in Exercise 9-7. Move the show_privileges() method to this class.
Make a Privileges instance as an attribute in the Admin class.
Create a new instance of Admin and use your method to show its privileges.
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

        # Initializes an empty set of privileges
        self.privileges = Privileges()

class Privileges():
    """A class used to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges that the admin has."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges whatsoever.")

musashi = Admin("musashi", "miyamoto", "m_miyamoto",
                "m_miyamoto@example.com", "Japan")
musashi.describe_user()

musashi.privileges.show_privileges()

print("\nAdding privileges...")
musashi_privileges = [
    "can destroy accounts",
    "can reset passwords",
    "can ban people into the void",
]

musashi.privileges.privileges = musashi_privileges
musashi.privileges.show_privileges()
