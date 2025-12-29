from sys import argv, exit

import pytd.globals as g
import pytd.helpers as helpers
import pytd.opers as oper


def main(args: list[str]) -> int:
    date: helpers.Date = {
        "day": 12,
        "month": 1,
        "year": 2026,
    }
    date2: helpers.Date = {
        "day": 31,
        "month": 1,
        "year": 2027,
    }
    oper.add("hw", date, "default", 3, "")
    oper.add("hw", date2, "default", 1, "")
    oper.rm("hw")
    return 0


if __name__ == "__main__":
    try:
        args: list[str] = argv[1:]
        code: int = main(args)
        exit(code)
    except KeyboardInterrupt:
        exit(130)
