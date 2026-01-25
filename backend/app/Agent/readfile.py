import os
from dotenv import load_dotenv
import json
from github import Github


load_dotenv()
GITHUBTOKEN = os.getenv('GITHUBTOKEN')

if not GITHUBTOKEN:
    raise ValueError("GITHUB_TOKEN not found in environment")

g = Github(GITHUBTOKEN)


def read_file(repo, file_path: str):
    try:
        repo = g.get_repo(repo)

        file_content = repo.get_contents(file_path)
        files_data=file_content.decoded_content.decode("utf-8")
        return files_data

    except Exception as e:
        print(f"[read_file error] {file_path}: {e}")
        return None

