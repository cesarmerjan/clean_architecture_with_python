from src.entities import User
from src import controllers
from src.repositories import FileRepository, InMemoryRepository
from src.units_of_work import FileUnitOfWork, InMemoryUnitOfWork
from src.presenters import TerminalPresenter
from src.schemas import SignInInput, SignInOutput
from src import use_cases

entities = [
    "User"
]

repositories = [
    "FileRepository",
    "InMemoryRepository"
]

units_of_work = [
    "FileUnitOfWork",
    "InMemoryUnitOfWork"
]

presenters = [
    "TerminalPresenter"
]

schemas = [
    "SignInInput",
    "SignInOutput"
]


print("---------------------------- You are in the Shell -----------------------------")
print("--- You have available:")
print(f"  - Entities: {', '.join(entities)};")
print(f"  - Schemas: {', '.join(schemas)};")
print(f"  - User Cases: all under use_cases.*;")
print(f"  - Repositories: {', '.join(repositories)};")
print(f"  - Units Of Work: {', '.join(units_of_work)};")
print(f"  - Presenters: {', '.join(presenters)};")
print(f"  - Controllers: all under controllers.*;")
print("-------------------------------------------------------------------------------")
