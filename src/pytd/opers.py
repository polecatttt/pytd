from pytd.helpers import Task


def add(name: str, date: list[int]) -> bool: ...


def list(tasks: list[Task]) -> None: ...


def rm(name: str) -> bool: ...
