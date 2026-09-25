"""The files a check looks at: tracked, plus untracked and not ignored."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def repo_files():
    listed = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    return [Path(name) for name in listed if (ROOT / name).is_file()]
