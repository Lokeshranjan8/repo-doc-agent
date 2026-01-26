from fastapi import FastAPI, HTTPException, Request
from app.gitfetch.git import fetch_github_repo
from app.gitfetch.filerepo import file_system
from app.Agent.node1 import build_judge_graph, node1state
from app.gitfetch.storingdata import storingdata
from app.Agent.generation_graph import generate_readme_graph

import json 
app = FastAPI()

graph = build_judge_graph()
readme_gen = generate_readme_graph()

@app.get("/")
def root():
    return {"message": "Hello, World!"}



@app.get("/fetchrepo")
def fetch_repo(repo_url: str):
    try:

        repo = fetch_github_repo(repo_url)

        payload = file_system(repo_url)
        
        result = graph.invoke(payload)

        data = {
            "repo": result["repo"],
            "readme_imp": result["readme_imp"]
        }

        raw_data = storingdata(data)
        # readme_gen.invoke(raw_data) //final stage 

        return raw_data
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/readtestfile")
def read_testfile():
    print("check this testing ")
    raw_file = reading_raw_data()
    print(type(raw_file))
    return raw_file
