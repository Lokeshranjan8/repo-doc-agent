from github import Github
from urllib.parse import urlparse
from app.Agent.readfile import read_file
import os
from dotenv import load_dotenv


load_dotenv()
GITHUBTOKEN = os.getenv('GITHUBTOKEN')

if not GITHUBTOKEN:
    raise ValueError("GITHUB_TOKEN not found in environment")

g = Github(GITHUBTOKEN)

def traverse_repo(repo, path=""):
    contents = repo.get_contents(path)
    for x in contents:
        print(x.path)

        if x.name == "docker-compose.yml":
            content = read_file(repo, x.path)
            print("---- RAW DOCKER COMPOSE FILE ----")
            print(content)
            return
        if x.type == "dir":
            traverse_repo(repo, x.path)


    

def file_system(repo_url: str):
    print("filerepo calling ")
    path = urlparse(repo_url).path.strip("/").split("/")
    user = path[0]
    repo_name = path[1]

    full_repo_name = f"{user}/{repo_name}"
    print("repo name:", full_repo_name)

    repo = g.get_repo(full_repo_name)

    print("contents:")
    traverse_repo(repo)


