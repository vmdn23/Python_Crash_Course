#!/usr/bin/python3
"""Classes used for making an adming user account"""

from user import User

class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initializes Admin"""
        super().__init__(first_name, last_name, username, email, location)

        # Initializes an empty set of privileges
        self.privileges = Privileges([])

class Privileges():
    """A class used to store an admin's privileges."""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges that the admin has."""
        for privilege in self.privileges:
            print("- " + privilege)
