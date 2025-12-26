from pytd.helpers import Task, DueDate


def add(name: str, date: DueDate) -> bool: ...


def list(tasks: list[Task]) -> None: ...


def rm(name: str) -> bool: ...
