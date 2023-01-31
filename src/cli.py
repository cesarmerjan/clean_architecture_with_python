"""
Responsible for receiving data from client and forwarding as the controller.
"""
from src.controllers import sign_in

name = input("Enter user name:\n")
email = input("Enter user email:\n")
password = input("Enter user password:\n")

view = sign_in(name, email, password)

print(view)
