# This file is part of pytd.
# pytd is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version. pytd is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details. You should have received a copy of the GNU General
# Public License along with pytd. If not, see <https://www.gnu.org/licenses/>.

import argparse as arg


def parse_version(args: list[str]) -> arg.Namespace:
    parser = arg.ArgumentParser()

    parser.add_argument(
        "-m",
        "--minimal",
        action="store_true",
    )

    parser.add_argument(
        "-M",
        "--maximal",
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


def parse_add(args: list[str]) -> arg.Namespace:
    parser = arg.ArgumentParser()

    parser.add_argument(
        "-d",
        "--due-date",
        action="store",
    )

    parser.add_argument(
        "-g",
        "--group",
        action="store",
    )

    parser.add_argument(
        "-p",
        "--priority",
        action="store",
    )

    parser.add_argument(
        "-D",
        "--description",
        action="store",
    )

    parser.add_argument(
        "-s",
        "--status",
        action="store",
    )

    return parser.parse_args(args)
