from github import Github
from urllib.parse import urlparse
from app.Agent.readfile import read_file
import os
from dotenv import load_dotenv
import json

load_dotenv()
GITHUBTOKEN = os.getenv('GITHUBTOKEN')

if not GITHUBTOKEN:
    raise ValueError("GITHUB_TOKEN not found in environment")

g = Github(GITHUBTOKEN)

metadata=[]

def traverse_repo(repo, path=""):
    contents = repo.get_contents(path)
    for x in contents:
        metadata.append({
            "path": x.path,
            "name": x.name
        })
        if x.type == "dir":
            traverse_repo(repo, x.path)


    

def file_system(repo_url: str):
    global metadata
    metadata = []
    print("filerepo calling ")
    path = urlparse(repo_url).path.strip("/").split("/")
    user = path[0]
    repo_name = path[1]

    full_repo_name = f"{user}/{repo_name}"
    print("repo name:", full_repo_name)

    repo = g.get_repo(full_repo_name)
    print(repo)

    traverse_repo(repo)
    
    metadata.append({"repository": repo.full_name})
    json_data = json.dumps(metadata, indent=4, ensure_ascii=False)
    # print(json_data)
    return json_data



