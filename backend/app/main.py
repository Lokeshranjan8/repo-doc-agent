from fastapi import FastAPI, HTTPException, Request
from app.gitfetch.git import fetch_github_repo
from app.gitfetch.filerepo import file_system
from app.Agent.node1 import build_judge_graph, node1state
from app.gitfetch.storingdata import storingdata
from app.Agent.readfile import reading_raw_data

import json 
app = FastAPI()

graph = build_judge_graph()

@app.get("/")
def root():
    return {"message": "Hello, World!"}



@app.get("/fetchrepo")
def fetch_repo(repo_url: str):
    try:
        repo = fetch_github_repo(repo_url)
        print("github repo existing and user tooo   #1")
        payload = file_system(repo_url)
        print("files fetched successfully           #2")
        result = graph.invoke(payload)
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/judge/docker-files")
def judge_docker_files_api(payload: node1state):
    try:
        result = graph.invoke(payload)
        print(type(result))

        data = {
            "repo": result["repo"],
            "readme_imp": result["readme_imp"]
        }
        print("judje data",type(data))
        print(type(data))
        # raw_data = storingdata(data)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/readtestfile")
def read_testfile():
    print("check this testing ")
    raw_file = reading_raw_data()
    print(type(raw_file))
    return raw_file
