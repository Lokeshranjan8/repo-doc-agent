from fastapi import FastAPI,HTTPException
from app.gitfetch.git import fetch_github_repo
from app.gitfetch.filerepo import file_system
import json 
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/fetchrepo")
def fetch_repo(repo_url: str):
    repo = fetch_github_repo(repo_url)
    
    files = file_system(repo_url)
    result = json.loads(files)
    return result