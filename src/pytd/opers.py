import json
from typing import Any

from tabulate import tabulate

import pytd.globals as g
from pytd import helpers
from pytd.helpers import Date, Task, TaskDataset


# List
def list_all() -> None:
    dataset: list[TaskDataset] = helpers.get_tasks_dataset(g.TASKS)
    print(tabulate(dataset, g.LIST_HEADERS))


def list_name(name: str | None) -> None:
    dataset: list[TaskDataset] = helpers.get_tasks_dataset(g.TASKS)
    sorted_dataset: list[TaskDataset] = []
    if name:
        sorted_dataset = [task for task in dataset if task["name"] == name]
    else:
        sorted_dataset = sorted(dataset, key=lambda x: x["name"])

    if not sorted_dataset:
        print("No tasks matched parameters!")
        return

    print(tabulate(sorted_dataset, g.LIST_HEADERS))


def list_duedate() -> None:
    dataset: list[TaskDataset] = helpers.get_tasks_dataset(g.TASKS)

    # Removes ANSI from due_in to sort by the number alone
    sorted_dataset = sorted(dataset, key=lambda x: g.ANSI_RE.sub("", x["due_in"]))
    print(tabulate(sorted_dataset, g.LIST_HEADERS))


def list_status(status: str | None):
    dataset: list[TaskDataset] = helpers.get_tasks_dataset(g.TASKS)
    sorted_dataset: list[TaskDataset] = []

    if status:
        sorted_dataset = [task for task in dataset if task["status"] == status]
    else:
        sorted_dataset = sorted(dataset, key=lambda x: g.STATUS_ORDER[x["status"]])

    if not sorted_dataset:
        print("No tasks matched parameters!")
        return

    print(tabulate(sorted_dataset, g.LIST_HEADERS))


def list_group(group: str | None) -> None:
    dataset: list[TaskDataset] = helpers.get_tasks_dataset(g.TASKS)
    sorted_dataset: list[TaskDataset] = []

    if group:
        sorted_dataset = [task for task in dataset if task["group"] == group]
    else:
        sorted_dataset = sorted(dataset, key=lambda x: x["group"])

    if not sorted_dataset:
        print("No tasks matched parameters!")
        return

    print(tabulate(sorted_dataset, g.LIST_HEADERS))


def list_priority(priority: int | None) -> None:

    dataset: list[TaskDataset] = helpers.get_tasks_dataset(g.TASKS)
    sorted_dataset: list[TaskDataset] = []

    if priority:
        sorted_dataset = [
            task
            for task in dataset
            if g.ANSI_RE.sub("", task["priority"]) == str(priority)
        ]
    else:
        sorted_dataset = sorted(dataset, key=lambda x: g.ANSI_RE.sub("", x["priority"]))

    if not sorted_dataset:
        print("No tasks matched parameters!")
        return

    print(tabulate(sorted_dataset, g.LIST_HEADERS))


# Add
def add(name: str, due_date: Date, group: str, priority: int, description: str) -> None:
    task_dict: Task = {
        "name": name,
        "status": "Due",
        "group": group,
        "priority": priority,
        "due_date": due_date,
        "description": description,
    }

    g.TASKS.append(task_dict)
    with open(g.TASKS_JSON, "w") as f:
        json.dump(g.TASKS, f, indent=4)


# Edit
def edit(name: str, key: str, new_val: Any) -> None:
    found: bool = False
    pending: list[Task] = []
    pending_idx: list[int] = []

    for idx, task in enumerate(g.TASKS):
        if task["name"] == name:
            found = True
            pending.append(task)
            pending_idx.append(idx)

    if not found:
        print("Task not found!")
        return

    if len(pending) > 1:
        choice: int = helpers.handle_multiple(pending)
        choice_idx: int = pending_idx[choice - 1]
        g.TASKS[choice_idx][key] = new_val

    else:
        g.TASKS[pending_idx[0]][key] = new_val

    helpers.update_tasks()


# Delete
def rm(name: str) -> None:
    found: bool = False
    pending: list[Task] = []
    pending_idx: list[int] = []

    for idx, task in enumerate(g.TASKS):
        if task["name"] == name:
            found = True
            pending.append(task)
            pending_idx.append(idx)

    if not found:
        print("Task not found!")
        return

    if len(pending) > 1:
        choice: int = helpers.handle_multiple(pending)
        idx: int = pending_idx[choice - 1]
        g.TASKS.pop(idx)

    else:
        g.TASKS.pop(pending_idx[0])

    helpers.update_tasks()
