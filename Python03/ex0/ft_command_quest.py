#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    print_arguments()
    print(f"Total arguments: {len(sys.argv) - 1}")


def print_arguments() -> None:
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print("Arguments received:", len(sys.argv) - 1)
        i = 1
        while i < len(sys.argv):
            print("Argument", i, ":", sys.argv[i])
            i += 1


if __name__ == "__main__":
    main()
