from fastapi import FastAPI, HTTPException, Request
from app.gitfetch.git import fetch_github_repo
from app.gitfetch.filerepo import file_system
from app.Agent.node1 import build_judge_graph, node1state
from app.gitfetch.storingdata import storingdata

import json 
app = FastAPI()

graph = build_judge_graph()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/fetchrepo")
def fetch_repo(repo_url: str):
    repo = fetch_github_repo(repo_url)
    
    files = file_system(repo_url)
    result = json.loads(files)
    
    return result


@app.post("/judge/docker-files")
def judge_docker_files_api(payload: node1state):
    try:
        result = graph.invoke(payload)
        print(type(result))

        data = {
            "repo": result["repo"],
            "readme_imp": result["readme_imp"]
        }
        print(type(data))
        raw_data = storingdata(data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
