"""
Responsible for representing the subjects of the system.
"""


class Entity:
    __slots__ = ()


class User(Entity):

    __slots__ = ("name", "email", "password")

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
