import argparse
import json
from . import __version__
from . import core


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="yourtool")
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Run scan against target")
    scan_parser.add_argument("--target", required=True, help="Target to scan")

    return parser


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "scan":
        result = core.run_scan(args.target)
        print(json.dumps(result))


if __name__ == "__main__":
    main()
