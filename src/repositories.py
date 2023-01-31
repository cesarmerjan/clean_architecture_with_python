"""
Responsible for data access logic.
"""
import abc
import io

from src.entities import Entity


class RepositoryInterface(metaclass=abc.ABCMeta):
    def add(self, entity: Entity) -> None:
        raise NotImplementedError


class InMemoryRepository(RepositoryInterface):
    def __init__(self, session: set) -> None:
        self.session = session

    def add(self, entity: Entity) -> None:
        self.session.add(entity)


class FileRepository:
    def __init__(self, _file: io.TextIOWrapper) -> None:
        self.file = _file

    def add(self, entity: Entity) -> None:
        inline_data = ",".join(getattr(entity, attr) for attr in entity.__slots__)
        line = inline_data + "\n"
        self.file.write(line)
