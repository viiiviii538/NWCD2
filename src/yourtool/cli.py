import argparse
import json
from importlib import metadata

from .core import run_scan


def get_version() -> str:
    """Return package version or a default."""
    try:
        return metadata.version("yourtool")
    except metadata.PackageNotFoundError:
        return "0.1.0"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="yourtool")
    parser.add_argument("--version", action="version", version=get_version())
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Run scan")
    scan_parser.add_argument("--target", required=True, help="Target to scan")

    args = parser.parse_args(argv)

    if args.command == "scan":
        result = run_scan(args.target)
        print(json.dumps(result))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
