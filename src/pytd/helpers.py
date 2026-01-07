import json
import os
from datetime import date
from sys import exit
from typing import TypedDict

from tabulate import tabulate

import pytd.globals as g


class Date(TypedDict):
    day: int
    month: int
    year: int


class Task(TypedDict):
    name: str
    status: str
    group: str
    priority: int
    due_date: Date
    description: str


class TaskDataset(TypedDict):
    name: str
    status: str
    group: str
    priority: str
    due_date: str
    due_in: str


# Config
def get_conf_path() -> str:
    if g.OS == "Windows":
        conf_path: str = f"{os.environ['LOCALAPPDATA']}\\pytd"

    elif g.OS == "Darwin":
        conf_path: str = f"{os.environ['HOME']}/Library/Application Support/pytd"

    elif g.OS == "Linux":
        try:
            conf_path: str = f"{os.environ['XDG_CONFIG_HOME']}/pytd"
        except KeyError:
            conf_path: str = f"{os.environ['HOME']}/.config/pytd"

    # I don't know...
    else:
        conf_path: str = f"{os.environ['HOME']}/.pytd"

    # Check config
    check_config(conf_path)

    return conf_path


def check_config(conf_path: str) -> None:
    # Check the directory exists
    if not os.path.exists(conf_path):
        try:
            os.mkdir(conf_path)
        except FileNotFoundError:
            print(f"{g.RED}FATAL:{g.RESET} config directory does not exist")
            exit(1)

    # Check the tasks file exists
    if not os.path.exists(f"{conf_path}/tasks.json"):
        with open(f"{conf_path}/tasks.json", "x") as f:
            f.close()

    # Check if the tasks file is empty
    if os.path.getsize(f"{conf_path}/tasks.json") == 0:
        with open(f"{conf_path}/tasks.json", "w") as f:
            f.write("[]")

    # Check if the config file exists
    if not os.path.exists(f"{conf_path}/pytd.conf"):
        with open(f"{conf_path}/pytd.conf", "x") as f:
            f.close()


def validate_json() -> None:
    current_task: int = 1
    for task in g.TASKS:
        try:
            task["name"]
            task["group"]
            task["status"]
            task["priority"]
            task["due_date"]
            task["description"]
        except KeyError as e:
            print(f"Invalid task format for task {current_task}: missing {e}")
            print(f"Full task: {task}")
            exit(1)

        current_task += 1


# Tasks
def get_tasks(filepath: str) -> list[Task]:
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError as e:
        print(f"Malformed tasks.json: {e}")
        exit(1)


def handle_multiple(tasks: list[Task]) -> int:
    dataset: list[TaskDataset] = get_tasks_dataset(tasks)

    print("There are multiple tasks with that name:")
    print(tabulate(dataset, g.LIST_HEADERS))
    print()

    choice: int = -1
    user_inp: str = ""
    while True:
        user_inp = input(
            f"Which task would you like to preform this operation on? (1 - {len(tasks)}): "
        )
        try:
            choice = int(user_inp)
            if choice > len(tasks):
                print(f"Choice cannot be more than {len(tasks)}")
                continue
            elif choice < 1:
                print("Choice cannot be lower than one")
                continue
            break
        except ValueError:
            print("Invalid number")
            continue

    return choice


def update_tasks() -> None:
    with open(g.TASKS_JSON, "w") as f:
        json.dump(g.TASKS, f, indent=4)


# Helpers for list
def get_today() -> Date:
    today: date = date.today()
    return {
        "day": today.day,
        "month": today.month,
        "year": today.year,
    }


def get_days_diff(date1: Date, date2: Date) -> int:
    d1_obj: date = date(date1["year"], date1["month"], date1["day"])
    d2_obj: date = date(date2["year"], date2["month"], date2["day"])
    return (d2_obj - d1_obj).days


def get_days_col(days: int) -> str:
    if days <= g.THRESHOLD_RED:
        return g.RED
    elif days <= g.THRESHOLD_YELLOW:
        return g.YELLOW
    return g.GREEN


def get_priority_col(priority: int) -> str:
    if priority == 1:
        return g.RED
    elif priority == 2:
        return g.YELLOW
    elif priority == 3:
        return g.GREEN
    return g.WHITE


def get_tasks_dataset(tasks: list[Task]) -> list[TaskDataset]:
    tasks_dataset: list[TaskDataset] = []

    for task in tasks:
        name: str = task["name"]
        status: str = task["status"]
        group: str = task["group"]
        priority: int = task["priority"]
        priority_col: str = get_priority_col(priority)
        priority_str: str = f"{priority_col}{priority}{g.RESET}"
        due: Date = task["due_date"]
        diff_str: str = ""
        due_str: str = "No due date"

        # Check if date is valid (task has no date if not)
        if due["year"] != -1:
            due_str = str(date(due["year"], due["month"], due["day"]))
            days_diff: int = get_days_diff(get_today(), due)
            diff_col: str = get_days_col(days_diff)
            diff_str = f"{diff_col}{days_diff}d{g.RESET}"

        dataset: TaskDataset = {
            "name": name,
            "status": status,
            "group": group,
            "priority": priority_str,
            "due_date": due_str,
            "due_in": diff_str,
        }
        tasks_dataset.append(dataset)

    return tasks_dataset
