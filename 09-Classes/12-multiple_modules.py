#!/usr/bin/python3
"""Store the User class in one module, and store the Privileges
and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything
is still working correctly.
"""

from admin import Admin

musashi = Admin("musashi", "miyamoto", "m_miyamoto",
                "m_miyamoto@example.com", "Japan")
musashi.describe_user()

musashi_privileges = [
    "can destroy accounts",
    "can reset passwords",
    "can ban people into the void",
]
musashi.privileges.privileges = musashi_privileges

print("\nThe admin " + musashi.username + " has these privileges: ")
musashi.privileges.show_privileges()
