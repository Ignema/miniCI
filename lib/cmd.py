import subprocess
from typing import List
from settings import s

def exec_command(cmd: List[str]) -> None:
    subprocess.run(cmd, cwd=s.PROJECT_DIR)
