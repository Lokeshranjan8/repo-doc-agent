from github import Github
from urllib.parse import urlparse

g = Github()
def traverse_repo(repo, path=""):
    contents = repo.get_contents(path)
    for x in contents:
        print(x.path)
        if x.type == "dir":
            traverse_repo(repo, x.path)


    

def file_system(repo_url: str):
    path = urlparse(repo_url).path.strip("/").split("/")
    user = path[0]
    repo_name = path[1]

    full_repo_name = f"{user}/{repo_name}"
    print("repo name:", full_repo_name)

    # get repo object
    repo = g.get_repo(full_repo_name)

    print("contents:")
    traverse_repo(repo)


