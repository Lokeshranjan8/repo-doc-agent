from fastapi import FastAPI
from app.gitfetch.git import fetch_github_repo

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/fetchrepo")
def fetch_repo(repo_url: str):
    repo = fetch_github_repo(repo_url)
    return {"fetched_repo": repo}