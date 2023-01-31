"""
Responsible for packaging the use case response into a view type object.
"""
import abc
import dataclasses
import typing

from src.schemas import Schema
from src.views import TerminalJsonView, View


class PresenterInterface(metaclass=abc.ABCMeta):
    def __init__(self, View: typing.Type[View], *args, **kwargs) -> None:
        self.View = View

    @abc.abstractmethod
    def build_success_view(self, output: Schema) -> View:
        raise NotImplementedError

    @abc.abstractmethod
    def build_failure_view(self, exception: Exception) -> View:
        raise NotImplementedError


class TerminalPresenter(PresenterInterface):
    def __init__(self, View: TerminalJsonView) -> None:
        self.View = View

    def build_success_view(self, output: Schema) -> View:
        data = dataclasses.asdict(output)
        return TerminalJsonView(data, True)

    def build_failure_view(self, exception: Exception) -> View:
        return TerminalJsonView({"message": str(exception)}, False)
