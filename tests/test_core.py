import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from yourtool.core import run_scan


def test_run_scan_returns_dict():
    assert isinstance(run_scan("target"), dict)
