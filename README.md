# pytd: a simple, CLI-based task manager.
No I swear this is not anything professional or good i just wanted the title to look good

## Contents
- [Installation](https://github.com/polecatttt/pytd/edit/main/README.md#installation)
- [Features](https://github.com/polecatttt/pytd/edit/main/README.md#features)
- [Usage Examples](https://github.com/polecatttt/pytd/edit/main/README.md#usage-examples)
- [Task Metadata](https://github.com/polecatttt/pytd/edit/main/README.md#task-metadata)

## Installation
pytd can be installed via pip or pipx:
```bash
# Installing via pip
python3 -m pip install 'git+https://github.com/polecatttt/pytd'

# Installing via pipx
pipx install 'git+https://github.com/polecatttt/pytd'
```

## Features
### Operations
- add: create a task
- list (ls): prints a list of your tasks in a neat table, with options for sorting methods and filters!
- edit: change a tasks metadata
- del (rm): delete a task
- info: get info on a selected task
### Configuration
- That comes in the future!

## Usage examples
```bash
# Adding a task with a certain due date
pytd add 'English Homework' --due-date 02-12-2013

# Deleting a task
pytd del 'English Homework'

# Editing a tasks due date
pytd edit 'English Homework' --due-date 03-11-1984

# Listing tasks sorted by name
pytd ls --method name

# Listing only tasks in a certain group
pytd ls --method group --filter default

# Listing a tasks information
pytd info 'English Homework'
```

## Task Metadata
- name: the name of the task
- group: the group the task belongs to
- status: the status of the tasks completion (Due [due], In Progress [inprogress], Done [done])
- priority: the priority of the task (1-4 inclusive)
- due_date: the due date of the task (format dd-mm-yyyy)
- description: task description (shows in task info)

## Changelog
Check the CHANGELOG.md for future planned changes and past updates!
