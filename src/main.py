import argparse
from sys import argv, exit

import pytd.globals as g
import pytd.helpers as helpers
import pytd.opers as oper
import pytd.parsers as parse


def main(args: list[str]) -> int:
    helpers.init()

    # Check if args exists
    if not args:
        oper.help()
        print("\nNo command given!")
        return 1

    # Check if command is valid
    if args[0] not in g.VALID_CMDS:
        oper.help()
        print("\nNot a valid command!")
        return 1

    # Collect and exec commands
    if args[0] == "help":
        oper.help()
        return 0

    elif args[0] == "version":
        cmd_args: argparse.Namespace = parse.parse_version(args[1:])
        if cmd_args.minimal:
            oper.version(minimal=True)
        else:
            oper.version()
        return 0

    elif args[0] == "info":
        if len(args) == 1:
            print("usage: pytd info [name]")
            print("error: need to provide a task name!")
            return 1
        name = args[1]
        if not oper.info(name):
            return 1
        return 0

    elif args[0] == "del":
        if len(args) == 1:
            print("usage: pytd del [name]")
            print("error: need to provide a task name!")
            return 1
        name = args[1]
        if not oper.rm(name):
            return 1
        return 0

    elif args[0] == "edit":
        if len(args) <= 2:
            print("usage: pytd edit [name] [-ngspdD]")
            print("error: need to provide a task name and 1 or more edits!")
            return 1
        name = args[1]

        cmd_args: argparse.Namespace = parse.parse_edit(args[2:])

        # Name last, to avoid name conflicts
        if cmd_args.group:
            if not oper.edit(name, "group", cmd_args.group):
                return 1

        if cmd_args.status:
            if cmd_args.status.lower() not in ("due", "inprogress", "done"):
                print("error: invalid status! must be (due, inprogress, done)")
                return 1

            if cmd_args.status.lower() == "due":
                if not oper.edit(name, "group", "Due"):
                    return 1

            elif cmd_args.status.lower() == "inprogress":
                if not oper.edit(name, "group", "In Progress"):
                    return 1

            elif cmd_args.status.lower() == "done":
                if not oper.edit(name, "group", "Done"):
                    return 1

        if cmd_args.priority:
            try:
                priority: int = int(cmd_args.priority)
            except ValueError:
                print("error: priority could not be converted to int")
                return 1

            if not (1 <= priority <= 4):
                print("error: priority must be 1-4 inclusive!")
                return 1

            if not oper.edit(name, "priority", priority):
                return 1

        if cmd_args.due_date:
            date: helpers.Date | bool = helpers.conv_day(cmd_args.due_date)
            if not date:
                return 1

            if not oper.edit(name, "due_date", date):
                return 1

        if cmd_args.description:
            if not oper.edit(name, "description", cmd_args.description):
                return 1

        return 0

    elif args[0] == "ls":
        cmd_args: argparse.Namespace = parse.parse_list(args[1:])
        if not cmd_args.method:
            if cmd_args.filter:
                print("error: filter cannot be applied to no method!")
                return 1
            oper.list_all()

        if (cmd_args.method not in g.LIST_METHODS) and (cmd_args.method):
            print("error: invalid method!")
            return 1

        elif cmd_args.method == "name":
            if cmd_args.filter:
                oper.list_name(cmd_args.filter)
            else:
                oper.list_name(None)

        elif cmd_args.method == "group":
            if cmd_args.filter:
                oper.list_group(cmd_args.filter)
            oper.list_group(None)

        elif cmd_args.method == "status":
            if cmd_args.filter:
                if cmd_args.filter not in ("due", "inprogress", "done"):
                    print("error: invalid status! must be (due, inprogress, done)")
                    return 1
                if cmd_args.filter == "due":
                    oper.list_status("Due")
                elif cmd_args.filter == "inprogress":
                    oper.list_status("In Progress")
                elif cmd_args.filter == "done":
                    oper.list_status("Done")
            else:
                oper.list_status(None)

        elif cmd_args.method == "priority":
            if cmd_args.filter:
                try:
                    priority: int = int(cmd_args.filter)
                except ValueError:
                    print("error: priority could not be converted to int")
                    return 1

                if not (1 <= priority <= 4):
                    print("error: priority must be 1-4 inclusive!")
                    return 1

                oper.list_priority(priority)

            else:
                oper.list_priority(None)

        elif cmd_args.method == "duedate":
            if cmd_args.filter:
                print("error: filters for duedate arent supported yet!")
                return 1

            oper.list_duedate()

        return 0

    return 0


if __name__ == "__main__":
    try:
        args: list[str] = argv[1:]
        code: int = main(args)
        exit(code)
    except KeyboardInterrupt:
        exit(130)
