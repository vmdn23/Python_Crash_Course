#!/usr/bin/python3
"""Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges and Admin in one module.
Create a separate file, make an Admin instance, and call
show_priveleges() to show that everything is working correctly.
"""

from user import Admin


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
