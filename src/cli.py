"""
Responsible for receiving data from client and forwarding as the controller.
"""
from src.controllers import cli_sign_up

name = input("Enter user name:\n")
email = input("Enter user email:\n")
password = input("Enter user password:\n")

view = cli_sign_up(name, email, password)

print(view)
