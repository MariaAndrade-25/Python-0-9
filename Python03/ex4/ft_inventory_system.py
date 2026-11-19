#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py <item:quantity>...")
        return

    inventory: dict[str, int] = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    keys: list[str] = list(inventory.keys())
    print(f"Item list: {keys}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(keys)} items: {total}")

    if not inventory:
        print("Inventory is empty.")
        return

    print_statistics(inventory, total)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        parts: list[str] = arg.split(":")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name: str = parts[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity: int = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
            continue
        inventory.update({name: quantity})
    return inventory


def print_statistics(inventory: dict[str, int], total: int) -> None:
    keys: list[str] = list(inventory.keys())
    most_item: str = keys[0]
    least_item: str = keys[0]

    for item in keys:
        qty: int = inventory[item]
        pct: float = round((qty / total) * 100, 1) if total > 0 else 0.0
        print(f"Item {item} represents {pct}%")
        if qty > inventory[most_item]:
            most_item = item
        if qty < inventory[least_item]:
            least_item = item

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )


if __name__ == "__main__":
    main()
