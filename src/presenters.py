"""
Responsible for packaging the use case response into a view type object.
"""
import abc
import dataclasses
import typing
import json

from src.schemas import Schema
from src.views import TerminalJsonView, View, HttpView


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
        return self.View(data, True)

    def build_failure_view(self, exception: Exception) -> View:
        return self.View({"message": str(exception)}, False)


class HttpJsonPresenter(PresenterInterface):
    def __init__(self, View: HttpView) -> None:
        self.View = View

    def _jsonify(self, output: Schema) -> str:
        return json.dumps(dataclasses.asdict(output))

    def build_success_view(self, output: Schema) -> View:
        _json = self._jsonify(output)
        return self.View(200, [("Content-type", "application/json")], _json)

    def build_failure_view(self, exception: Exception) -> View:
        return self.View(500, [("Content-type", "application/json")], {"message": str(exception)})
