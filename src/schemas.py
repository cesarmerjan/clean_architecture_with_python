"""
Responsible for establishing the input and output data structure of the use cases.
"""
import dataclasses


@dataclasses.dataclass
class Schema:
    pass


@dataclasses.dataclass(slots=True)
class SignInInput(Schema):
    name: str
    email: str
    password: str


@dataclasses.dataclass(slots=True)
class SignInOutput(Schema):
    name: str
    email: str
