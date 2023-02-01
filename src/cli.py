"""
Responsible for receiving data from client and forwarding as the controller.
"""
from src.controllers import cli_sign_up
from src.use_cases import UseCaseInterface
import typing


def create_cli(function: UseCaseInterface, args_name: typing.List[str]) -> None:

    kwargs = {}
    for arg_name in args_name:
        kwargs[arg_name] = input(f"Enter the {arg_name}:\n")

    view = function(**kwargs)

    print(view)


if __name__ == "__main__":
    create_cli(cli_sign_up, ["name", "email", "password"])
