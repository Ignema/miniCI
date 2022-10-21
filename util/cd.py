from settings import s
from lib.cmd import exec_command

def deploy() -> None:
    # Pull latest commits from server
    exec_command(["git", "pull", f"https://{s.GITHUB_USER}:{s.GITHUB_TOKEN}@{s.GITHUB_REPOSITORY}"])

    # Restart PM2 process
    exec_command(["pm2", "restart", "all"])
