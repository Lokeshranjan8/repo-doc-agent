from urllib.parse import urlparse
from fastapi import HTTPException
import requests

def fetch_github_repo(repo: str):
    path = urlparse(repo).path.strip("/").split("/")

    if(len(path)<2):
        raise HTTPException(status_code=400, detail="Invalid GitHub repository URL")

    user = path[0]
    repo_name = path[1]
    
    api_url = f"https://api.github.com/repos/{user}/{repo_name}"
    response = requests.get(api_url)
    

    if response.status_code ==200:
        return {
            "exists": True,
            "data":repo_name ,
            "error": None
        }
    elif response.status_code ==404:
        print("github repo not found in git file")

        raise HTTPException(
            status_code=404,
            detail="GitHub repository not found"
        )
    else:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch GitHub repository"
        )