# This file is part of pytd.
# pytd is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version. pytd is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details. You should have received a copy of the GNU General
# Public License along with pytd. If not, see <https://www.gnu.org/licenses/>.

import json
from sys import exit
from typing import Any

from tabulate import tabulate

import pytd.globals as g
from pytd import helpers
from pytd.helpers import Date, Task, TaskDataset


# List
def list_all() -> None:
    dataset: list[TaskDataset] = helpers.get_tasks_dataset(g.TASKS)
    if not dataset:
        print("No tasks matched parameters!")
        return

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
def add(
    name: str, due_date: Date, group: str, priority: int, description: str, status: str
) -> None:
    task_dict: Task = {
        "name": name,
        "status": status,
        "group": group,
        "priority": priority,
        "due_date": due_date,
        "description": description,
    }

    g.TASKS.append(task_dict)
    with open(g.TASKS_JSON, "w") as f:
        json.dump(g.TASKS, f, indent=4)


# Edit
def edit(name: str, key: str, new_val: Any) -> bool:
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
        return False

    if len(pending) > 1:
        choice: int = helpers.handle_multiple(pending)
        choice_idx: int = pending_idx[choice - 1]
        g.TASKS[choice_idx][key] = new_val

    else:
        g.TASKS[pending_idx[0]][key] = new_val

    helpers.update_tasks()
    return True


# Delete
def rm(name: str) -> bool:
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
        return False

    if len(pending) > 1:
        choice: int = helpers.handle_multiple(pending)
        idx: int = pending_idx[choice - 1]
        g.TASKS.pop(idx)

    else:
        g.TASKS.pop(pending_idx[0])

    helpers.update_tasks()
    return True


# Info
def info(name: str) -> bool:
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
        return False

    if len(pending) > 1:
        choice: int = helpers.handle_multiple(pending)
        idx: int = pending_idx[choice - 1]

    else:
        idx: int = pending_idx[0]

    task: Task = g.TASKS[idx]
    print(f"Name: {task["name"]}")
    print(f"Status: {task["status"]}")
    print(f"Group: {task["group"]}")
    print(f"Priority: {task["priority"]}")

    if task["due_date"]["year"] == -1:
        print("Due Date: None")
    else:
        print(
            f"Due Date: {task["due_date"]["day"]}-{task["due_date"]["month"]}-{task["due_date"]["year"]}"
        )
    print()
    if task["description"]:
        print(f"Description: {task["description"]}")

    return True


# Help
def help() -> None:
    print("Usage: pytd [command] [options]")
    print()

    print("Avaliable commands and options:")
    print("  add: add a new task ( pytd add [name] [-dgpDs] )")
    print("    -d, --due-date: due date of the task. no due date if not set")
    print("    -g, --group: group of the task. default if not set")
    print("    -p, --priority: priority of the task. 4 if not set. must be 1..4")
    print("    -D, --description: description of the task. empty if not set")
    print("    -s, --status: status of the task. Due if not set")
    print("  edit: edit an existing task ( pytd edit [name] [-ngspdD] )")
    print("    -n, --name: new name for the task")
    print("    -g, --group: new group for the task")
    print("    -s, --status: new status for the task")
    print("    -p, --priority: new priority for the task")
    print("    -d, --due-date: new due date for the task")
    print("    -D, --description: new description for the task")
    print("  del / rm: delete a task ( pytd del [name] )")
    print("  ls / list: list all tasks ( pytd ls [-mf] )")
    print("    -m, --method: method to list by (see above except description)")
    print(
        "    -f, --filter: a filter for some methods (see above except duedate) (unused if method is undefined!)"
    )
    print("  info: show info on a specific task ( pytd info [name] )")
    print("  help: view this message ( pytd help )")
    print("  version: get the version ( pytd version [-m] )")
    print("    -m, --minimal: only show the version number")
    print("    -M, --maximal: shows, like, a lotta info n stuff")
    print()
    print("Statuses used for commands: (due, inprogress, done)")
    print("Priorities used for commands range from 1-4 inclusive")
    print("Due date must be in the form dd-mm-yyyy")
    print("All commands have an additional -h option to show that commands options")


# Version
def version(minimal: bool = False, maximal: bool = False) -> None:
    if (not minimal) and (not maximal):
        print(f"{g.YELLOW}pytd{g.RESET} {g.DIM}{g.VERSION}{g.RESET}")
    elif (minimal) and (maximal):
        print(
            f"{g.RED}pytd{g.RESET} has been {g.GREEN}trapped{g.RESET} in a state of {g.BOLD}quantum {g.MAGENTA}madness.{g.RESET}"
        )
        exit(1)
    elif minimal:
        print(g.VERSION)
    elif maximal:
        print(f"{g.YELLOW}pytd{g.RESET} {g.DIM}{g.VERSION}{g.RESET}")
        print("By Polecat")
        print(f"License: {g.BLUE}GPL v3{g.RESET} (C. 2026)")
        print("Repository URL: <https://github.com/polecatttt/pytd>")
        print()
        print(f"Config location: {g.CONFIG_PATH}")
    else:
        print(g.VERSION)
