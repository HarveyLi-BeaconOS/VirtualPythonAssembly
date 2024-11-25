import sys


def ConsolePrint(contents: str):
    for x in contents:
        sys.stdout.write(f"{x}")