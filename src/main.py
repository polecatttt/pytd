from sys import argv, exit

import pytd.globals as g
import pytd.helpers as helpers
import pytd.opers as oper


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

    return 0


if __name__ == "__main__":
    try:
        args: list[str] = argv[1:]
        code: int = main(args)
        exit(code)
    except KeyboardInterrupt:
        exit(130)
