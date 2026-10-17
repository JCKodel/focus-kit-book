"""The files a check looks at: tracked, plus untracked and not ignored, whatever their names."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def repo_files():
    listed = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout.decode("utf-8").split("\0")
    return [Path(name) for name in listed if name and (ROOT / name).is_file()]
