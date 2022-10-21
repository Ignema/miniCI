from settings import s
from lib.cmd import exec_command

def deploy() -> None:
    # Navigate to project source directory
    exec_command(["cd", s.PROJECT_DIR])

    # Pull latest commits from server
    exec_command(["git", "pull", f"https://${s.GITHUB_USER}:${s.GITHUB_TOKEN}@${s.GITHUB_REPOSITORY}"])

    # Restart PM2 process
    exec_command(["pm2", "restart", "all"])