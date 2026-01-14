from urllib.parse import urlparse
import requests

def fetch_github_repo(repo: str):
    path = urlparse(repo).path.strip("/").split("/")

    if(len(path)<2):
        return {"error": "Invalid GitHub repository URL"}

    user = path[0]
    repo_name = path[1]
    
    api_url = f"https://api.github.com/repos/{user}/{repo_name}"
    response = requests.get(api_url)

    if response.status_code ==200:
        print(f"fetching github repo in git file : {repo}")

        return {
            "exists": True,
            "error": None
        }
    elif response.status_code ==404:
        print("github repo not found in git file")

        return {
            "exists": False,
            "error": "Repository not found"
        }
    else:
        print(f"failed to fetch github repo: {repo}, status code: {response.status_code}")
  
