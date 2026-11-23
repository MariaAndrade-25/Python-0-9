#!/usr/bin/env python3

FRAGMENT: str = (
    "[FRAGMENT 001] Digital preservation protocols established 2087\n"
    "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
    "[FRAGMENT 003] Every byte saved is a victory against oblivion"
)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow", "r"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("content.txt", "w", FRAGMENT))
    print()


def secure_archive(
        filename: str,
        action: str = "r",
        content: str = ""
        ) -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, "Invalid action")
    try:
        with open(filename, action) as file:
            if action == "r":
                return (True, file.read())
            else:
                file.write(content)
                return (True, "Content successfully written to file")
    except OSError as error:
        return (False, str(error))


if __name__ == "__main__":
    main()