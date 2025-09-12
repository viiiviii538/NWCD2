import subprocess
import sys
import os
from pathlib import Path


def test_help_exits_zero():
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path(__file__).resolve().parent.parent / "src")
    result = subprocess.run(
        [sys.executable, "-m", "yourtool.cli", "--help"], env=env, capture_output=True
    )
    assert result.returncode == 0
