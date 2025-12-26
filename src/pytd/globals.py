from platform import system

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
TASKS_JSON: str = f"{CONFIG_PATH}/tasks.json"
PYTD_CONF: str = f"{CONFIG_PATH}/pytd.conf"

# Tasks
TASKS: list[helpers.Task] = helpers.get_tasks(TASKS_JSON)
