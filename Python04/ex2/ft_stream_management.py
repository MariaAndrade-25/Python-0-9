#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    content = read_file(sys.argv[1])
    if content == []:
        return

    print("\n---")
    print(f"File '{sys.argv[1]}' closed.")
    print()

    print("Transform data:")
    print("---\n")

    content = transform_data(content, '#')

    print("\n---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    save = sys.stdin.readline().strip()
    if save:
        save_data(content, save)
    else:
        print("Not saving data.")


def read_file(filename: str) -> list[str]:
    content: list[str] = []

    try:
        file = open(filename)
    except OSError as error:
        print(
                f"[STDERR] Error opening file '{filename}': {error}",
                file=sys.stderr
                )
        return []

    print("---\n")
    try:
        for line in file:
            print(line, end="")
            content.append(line)
    except OSError as error:
        print(
                f"[STDERR] Error reading file '{filename}': {error}",
                file=sys.stderr
                )
        file.close()
        return []

    file.close()
    return content


def transform_data(content: list[str], marker: str) -> list[str]:
    transformed: list[str] = []

    for line in content:
        line = line.rstrip("\n") + marker + "\n"
        transformed.append(line)
        print(line, end="")

    return transformed


def save_data(content: list[str], filename: str) -> None:
    print(f"Saving data to '{filename}'")

    try:
        file = open(filename, "w")
    except OSError as error:
        print(
                f"[STDERR] Error opening file '{filename}': {error}",
                file=sys.stderr
                )
        print("Data not saved.")
        return

    try:
        for line in content:
            file.write(line)
    except OSError as error:
        print(
                f"[STDERR] Error writing to file '{filename}': {error}",
                file=sys.stderr
                )
        print("Data not saved.")
        file.close()
        return

    print(f"Data saved in file '{filename}'")
    file.close()


if __name__ == "__main__":
    main()