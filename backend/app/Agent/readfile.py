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
        file_content = repo.get_contents(file_path)
        return file_content.decoded_content.decode("utf-8")
    except Exception as e:
        return f"Error reading file: {str(e)}"



def reading_raw_data():
    try:
        print("lets validate the data")
        repo = g.get_repo("Lokeshranjan8/repo-doc-agent")
        main_data = read_file(repo,"backend/app/main.py")
        
        # for pair in result:
        #  if "repository" in pair:
        #     print(pair["repository"])
        #  elif "path" in pair and "name" in pair:
        #     print(pair["path"], pair["name"])
        return main_data
    except Exception as e:
        return f"Error reading file: {str(e)}"
