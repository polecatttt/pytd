from sys import argv, exit

import pytd.globals as g
import pytd.helpers as helpers
import pytd.opers as oper


def main(args: list[str]) -> int:
    helpers.init()
    date1: helpers.Date = {
        "day": 12,
        "month": 3,
        "year": 2026,
    }

    oper.version()
    return 0


if __name__ == "__main__":
    try:
        args: list[str] = argv[1:]
        code: int = main(args)
        exit(code)
    except KeyboardInterrupt:
        exit(130)
