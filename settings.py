import os

class Settings:
    PROJECT_DIR = os.getenv("PROJECT_DIR")
    GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
    GITHUB_USER = os.getenv("GITHUB_USER")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

s = Settings()