import json
import os
from sys import exit
from typing import TypedDict

import pytd.globals as g


class DueDate(TypedDict):
    day: int
    month: int
    year: int


class Task(TypedDict):
    name: str
    due_date: DueDate


# Config
def get_conf_dir() -> str:
    if g.OS == "Windows":
        return f"{os.environ['LOCALAPPDATA']}\\pytd"

    elif g.OS == "Darwin":
        return f"{os.environ['HOME']}/Library/Application Support/pytd"

    elif g.OS == "Linux":
        try:
            return f"{os.environ['XDG_CONFIG_HOME']}/pytd"
        except KeyError:
            return f"{os.environ['HOME']}/.config/pytd"

    # I don't know...
    else:
        return f"{os.environ['HOME']}/.pytd"


def check_config(config_dir: str) -> None:
    # Check the directory exists
    if not os.path.exists(config_dir):
        try:
            os.mkdir(config_dir)
        except FileNotFoundError:
            print(f"{g.RED}FATAL:{g.RESET} config directory does not exist")
            exit(1)

    # Check the tasks file exists
    if not os.path.exists(g.TASKS_JSON):
        with open(f"{config_dir}/tasks.json", "x") as f:
            f.close()

    # Check if the config file exists
    if not os.path.exists(g.PYTD_CONF):
        with open(f"{config_dir}/pytd.conf", "x") as f:
            f.close()


# Tasks
def get_tasks(filepath: str) -> list[Task]:
    with open(filepath, "r") as f:
        return json.load(f)
