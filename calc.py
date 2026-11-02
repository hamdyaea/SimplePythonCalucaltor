#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Simple interactive and command-line decimal calculator."""
import argparse
from decimal import Decimal, InvalidOperation, DivisionByZero

OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
}

def calculate(operation: str, left: str, right: str) -> Decimal:
    operation = "subtract" if operation == "substract" else operation
    if operation not in OPERATIONS:
        raise ValueError(f"Unknown operation: {operation}")
    try:
        a, b = Decimal(left), Decimal(right)
        if not a.is_finite() or not b.is_finite():
            raise ValueError("Only finite numbers are accepted")
        if operation == "divide" and b == 0:
            raise ValueError("Cannot divide by zero")
        return OPERATIONS[operation](a, b)
    except (InvalidOperation, DivisionByZero) as exc:
        raise ValueError("Invalid decimal number") from exc

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", nargs="?", choices=(*OPERATIONS, "substract"))
    parser.add_argument("left", nargs="?")
    parser.add_argument("right", nargs="?")
    args = parser.parse_args()
    if args.operation is not None:
        if args.left is None or args.right is None:
            parser.error("Provide two numbers")
        try:
            print(calculate(args.operation, args.left, args.right))
        except ValueError as exc:
            parser.error(str(exc))
        return
    print("Operations: add, subtract, multiply, divide, quit")
    while True:
        try:
            operation = input("Operation: ").strip().lower()
            if operation in ("quit", "exit", "q"):
                break
            left = input("First number: ")
            right = input("Second number: ")
            print("Result:", calculate(operation, left, right))
        except (EOFError, KeyboardInterrupt):
            print()
            break
        except ValueError as exc:
            print("Error:", exc)

if __name__ == "__main__":
    main()
