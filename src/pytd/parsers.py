import argparse as arg


def parse_version(args: list[str]) -> arg.Namespace:
    parser = arg.ArgumentParser()

    parser.add_argument(
        "-m",
        "--minimal",
        action="store_true",
    )

    return parser.parse_args(args)


def parse_edit(args: list[str]) -> arg.Namespace:
    parser = arg.ArgumentParser()

    parser.add_argument(
        "-n",
        "--name",
        action="store",
    )

    parser.add_argument(
        "-g",
        "--group",
        action="store",
    )

    parser.add_argument(
        "-s",
        "--status",
        action="store",
    )

    parser.add_argument(
        "-p",
        "--priority",
        action="store",
    )

    parser.add_argument(
        "-d",
        "--due-date",
        action="store",
    )

    parser.add_argument(
        "-D",
        "--description",
        action="store",
    )

    return parser.parse_args(args)


def parse_list(args: list[str]) -> arg.Namespace:
    parser = arg.ArgumentParser()

    parser.add_argument(
        "-m",
        "--method",
        action="store",
    )

    parser.add_argument(
        "-f",
        "--filter",
        action="store",
    )

    return parser.parse_args(args)
