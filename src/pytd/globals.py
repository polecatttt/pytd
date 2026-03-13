# This file is part of pytd.
# pytd is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version. pytd is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details. You should have received a copy of the GNU General
# Public License along with pytd. If not, see <https://www.gnu.org/licenses/>.

from platform import system
from re import compile

import pytd.helpers as helpers

VERSION: str = "1.0.0"

# ANSI Escape Codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

# Config
OS: str = system()
CONFIG_PATH: str
TASKS_JSON: str
PYTD_CONF: str

# Config Values
THRESHOLD_RED: int = 7
THRESHOLD_YELLOW: int = 14

# Tasks
TASKS: list[helpers.Task]

# Others
REQUIRED_TYPES: dict[str, type] = {
    "name": str,
    "status": str,
    "group": str,
    "priority": int,
    "due_date": helpers.Date,
    "description": str,
}

LIST_HEADERS: dict[str, str] = {
    "name": "Name",
    "status": "Status",
    "group": "Group",
    "priority": "Priority",
    "due_date": "Due Date",
    "due_in": "Due In",
}

STATUS_ORDER: dict[str, int] = {
    "Due": 1,
    "In Progress": 2,
    "Done": 3,
}

ANSI_RE = compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
VALID_CMDS: set[str] = {
    "add",
    "edit",
    "del",
    "rm",
    "ls",
    "list",
    "info",
    "help",
    "version",
}
LIST_METHODS: set[str] = {"name", "group", "status", "priority", "duedate"}
NO_DUEDATE: helpers.Date = {
    "day": 0,
    "month": 0,
    "year": -1,
}
