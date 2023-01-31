"""
Responsible for manage the atomicity (transactions, concurrency, commit and rollback).
"""
import abc
import io
import typing

from src.repositories import FileRepository, InMemoryRepository, RepositoryInterface


class UnitOfWorkInterface(metaclass=abc.ABCMeta):

    repository: RepositoryInterface

    def __init__(
        self, Repository: typing.Type[RepositoryInterface], *args, **kwargs
    ) -> None:
        self.Repository = Repository
        self.repository: Repository = None

    @abc.abstractmethod
    def __enter__(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError


class FileUnitOfWork(UnitOfWorkInterface):
    def __init__(
        self,
        Repository: typing.Type[FileRepository],
        path_to_file: str,
        mode: str = "a+",
    ) -> None:
        self.path = path_to_file
        self.mode = mode
        self.Repository = Repository

    def __enter__(self) -> None:
        self.file: io.TextIOWrapper = open(self.path, self.mode)
        self.repository = self.Repository(self.file)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type:
            self.rollback()
        self.file.close()

    def commit(self):
        self.file.flush()

    def rollback(self):
        self.file.close()


class InMemoryUnitOfWork(UnitOfWorkInterface):
    DATABASE = set([])

    def __init__(self, Repository: typing.Type[InMemoryRepository]) -> None:
        self.Repository = Repository

    def __enter__(self) -> None:
        self.session: set = set([])
        self.repository = self.Repository(self.session)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type:
            self.rollback()
        del self.session

    def commit(self):
        self.DATABASE |= self.session

    def rollback(self):
        self.session.clear()
