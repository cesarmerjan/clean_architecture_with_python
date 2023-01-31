"""
Responsible for receiving and packaging the data and directing it to the use case.
"""
import functools

from config import TEXT_IO_FILE_PATH, TEXT_IO_MODE
from src import use_cases
from src.presenters import TerminalPresenter
from src.repositories import FileRepository
from src.schemas import SignInInput
from src.units_of_work import FileUnitOfWork, UnitOfWorkInterface
from src.views import TerminalJsonView


def _sign_in(
    name: str,
    email: str,
    password: str,
    unit_of_work: UnitOfWorkInterface,
    user_case: use_cases.UseCaseInterface,
) -> TerminalJsonView:
    _input = SignInInput(name, email, password)
    view = user_case(unit_of_work, _input)
    return view


presenter = TerminalPresenter(TerminalJsonView)
user_case = functools.partial(use_cases.sign_in, presenter=presenter)
unit_of_work = FileUnitOfWork(FileRepository, TEXT_IO_FILE_PATH, TEXT_IO_MODE)

sign_in = functools.partial(_sign_in, unit_of_work=unit_of_work, user_case=user_case)
