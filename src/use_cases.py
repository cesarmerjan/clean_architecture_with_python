"""
Responsible for managing interaction with the entities and the business rules.
"""
import dataclasses
import typing

from src.entities import User
from src.presenters import PresenterInterface
from src.schemas import Schema, SignInInput, SignInOutput
from src.units_of_work import UnitOfWorkInterface
from src.views import View

UseCaseInterface = typing.Callable[
    [UnitOfWorkInterface, Schema, PresenterInterface], View
]


def sign_in(
    unit_of_work: UnitOfWorkInterface,
    _input: SignInInput,
    presenter: PresenterInterface,
) -> View:
    try:
        user = User(**dataclasses.asdict(_input))
        with unit_of_work:
            unit_of_work.repository.add(user)
            unit_of_work.commit()
        output = SignInOutput(user.name, user.email)
        view = presenter.build_success_view(output)
    except Exception as exception:
        view = presenter.build_failure_view(exception)
    return view
