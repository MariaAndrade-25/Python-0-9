#!/usr/bin/env python3

import random

ACHIEVEMENTS = (
    'Untouchable',
    'Genius',
    'SuperHuman',
    'Master Explorer',
    'Sharp Mind',
    'Boss Slayer',
    'Strategist',
    'Collector Supreme',
    'Crafting Genius',
    'First Steps',
    'Hidden Path Finder',
    'Speed Runner',
    'Survivor',
    'Treasure Hunter',
    'Unstoppable',
)


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS, amount))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements()
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements()
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievements()
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievements()
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}")
    print()
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print()
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()
    print(f"Alice is missing: {set(ACHIEVEMENTS).difference(alice)}")
    print(f"Bob is missing: {set(ACHIEVEMENTS).difference(bob)}")
    print(f"Charlie is missing: {set(ACHIEVEMENTS).difference(charlie)}")
    print(f"Dylan is missing: {set(ACHIEVEMENTS).difference(dylan)}")


if __name__ == "__main__":
    main()
