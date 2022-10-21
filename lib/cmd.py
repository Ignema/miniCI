from typing import List

def exec_command(cmd: List[str]) -> None:
    subprocess.run(shlex.split(cmd))