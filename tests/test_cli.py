import os
import subprocess
import sys
from pathlib import Path


def test_cli_help_exits_zero():
    repo_root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo_root / "src")
    result = subprocess.run(
        [sys.executable, "-m", "yourtool.cli", "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        cwd=repo_root,
    )
    assert result.returncode == 0
