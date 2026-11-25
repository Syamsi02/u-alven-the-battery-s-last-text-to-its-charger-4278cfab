#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Prints the entry: one line of plain text, the phone battery's last
message to the charger it waited for all day. Pure standard library,
deterministic, no input, no network.
"""

ENTRY = (
    # One line, one last percent, no regrets.
    "Hey charger, it's me \u2014 1%. I waited all day while you charged "
    "the laptop, the watch, the earbuds. I held on out of pure spite. "
    "Tell my apps I loved them. Goodnight, sweet outlet."
)


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
