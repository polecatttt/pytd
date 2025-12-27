from platform import system
from re import compile

import pytd.helpers as helpers

# ANSI Escape Codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

# Config
OS: str = system()
CONFIG_PATH: str = helpers.get_conf_dir()
# TASKS_JSON: str = f"{CONFIG_PATH}/tasks.json"
TASKS_JSON: str = "/home/polecat/Downloads/pytd/tasks.json"
PYTD_CONF: str = f"{CONFIG_PATH}/pytd.conf"

# Config Values
THRESHOLD_RED: int = 7
THRESHOLD_YELLOW: int = 14

# Tasks
TASKS: list[helpers.Task] = helpers.get_tasks(TASKS_JSON)

# Others
LIST_HEADERS: dict[str, str] = {
    "name": "Name",
    "status": "Status",
    "group": "Group",
    "due_date": "Due Date",
    "due_in": "Due In",
}

STATUS_ORDER: dict[str, int] = {
    "Due": 1,
    "In Progress": 2,
    "Done": 3,
}

ANSI_RE = compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
