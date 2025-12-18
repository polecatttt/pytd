from sys import argv, exit


def main(args: list[str]) -> int:
    print("Hello from pytd!")
    return 0


if __name__ == "__main__":
    try:
        args: list[str] = argv[1:]
        code: int = main(args)
        exit(code)
    except KeyboardInterrupt:
        exit(130)
