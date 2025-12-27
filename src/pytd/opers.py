import json

from tabulate import tabulate

import pytd.globals as g
from pytd import helpers
from pytd.helpers import Date, Task, TaskDataset


# List
def list_all(dataset: list[TaskDataset]) -> None:
    print(tabulate(dataset, g.LIST_HEADERS))


def list_name(dataset: list[TaskDataset], name: str | None) -> None:
    sorted_dataset: list[TaskDataset] = []
    if name:
        sorted_dataset = [task for task in dataset if task["name"] == name]
    else:
        sorted_dataset = sorted(dataset, key=lambda x: x["name"])

    if not sorted_dataset:
        print("No tasks matched parameters!")
        return

    print(tabulate(sorted_dataset, g.LIST_HEADERS))


def list_duedate(dataset: list[TaskDataset]) -> None:
    # Removes ANSI from due_in to sort by the number alone
    sorted_dataset = sorted(dataset, key=lambda x: g.ANSI_RE.sub("", x["due_in"]))
    print(tabulate(sorted_dataset, g.LIST_HEADERS))


def list_status(dataset: list[TaskDataset], status: str | None):
    sorted_dataset: list[TaskDataset] = []
    if status:
        sorted_dataset = [task for task in dataset if task["status"] == status]
    else:
        sorted_dataset = sorted(dataset, key=lambda x: g.STATUS_ORDER[x["status"]])

    if not sorted_dataset:
        print("No tasks matched parameters!")
        return

    print(tabulate(sorted_dataset, g.LIST_HEADERS))


def list_group(dataset: list[TaskDataset], group: str | None) -> None:
    sorted_dataset: list[TaskDataset] = []
    if group:
        sorted_dataset = [task for task in dataset if task["group"] == group]
    else:
        sorted_dataset = sorted(dataset, key=lambda x: x["group"])

    if not sorted_dataset:
        print("No tasks matched parameters!")
        return

    print(tabulate(sorted_dataset, g.LIST_HEADERS))


# Add
def add(name: str, due_date: Date, group: str) -> None:
    task_dict: Task = {
        "name": name,
        "status": "Due",
        "group": group,
        "due_date": due_date,
    }

    g.TASKS.append(task_dict)
    with open(g.TASKS_JSON, "w") as f:
        json.dump(g.TASKS, f, indent=4)


# Status
def status(name: str, new_status: str) -> None:
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
        g.TASKS[idx]["status"] = new_status

    else:
        g.TASKS[pending_idx[0]]["status"] = new_status

    with open(g.TASKS_JSON, "w") as f:
        json.dump(g.TASKS, f, indent=4)
