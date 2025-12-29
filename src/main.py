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
    dataset = helpers.get_tasks_dataset(g.TASKS)
    # print(dataset)
    # oper.list_all(dataset)
    oper.list_priority(dataset, 1)

    return 0


if __name__ == "__main__":
    try:
        args: list[str] = argv[1:]
        code: int = main(args)
        exit(code)
    except KeyboardInterrupt:
        exit(130)
