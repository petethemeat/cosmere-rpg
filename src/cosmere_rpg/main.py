"""Small CLI entrypoint for the cosmere-rpg project.

Provides a minimal command to demonstrate packaging and testing.
"""
from __future__ import annotations

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cosmere-rpg", description="Cosmere RPG helper CLI")
    sub = p.add_subparsers(dest="cmd")

    hello = sub.add_parser("hello", help="Print a hello message")
    hello.add_argument("--name", "-n", default="Cosmere", help="Name to greet")

    return p


def main(argv: list[str] | None = None) -> int:
    argv = list(argv) if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "hello":
        print(f"Hello, {args.name}!")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
