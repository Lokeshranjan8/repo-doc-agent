from typing_extensions import List, Dict, TypedDict
from langgraph.graph import StateGraph, END , START
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()

# STATE
class node1state(TypedDict):
    repo: str
    files: List[Dict[str, str]]
    readme_imp: List[str]

# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API"),
    temperature=0
)

parser = JsonOutputParser()
prompt = ChatPromptTemplate.from_template("""
You are a strict classifier.

Task:
From the given file paths, identify files that are important for writing a README.

Guidelines:
- If the project contains Python code, include requirements.txt or pyproject.toml
- If the project contains React/Node, include package.json
- Include Dockerfile and docker-compose.yml if present

Rules:
- Use ONLY the file paths exactly as given
- Do NOT explain
- Do NOT add extra text
- Return JSON only

File paths:
{file_paths}

Return format:
{{
  "readme_imp": [
    "docker-compose.yml",
    "server/package.json",
    "backend/Dockerfile"
  ]
}}
""")





# def functions:
def judge_files(state: node1state) -> node1state:
    file_paths = [f["path"] for f in state["files"]]

    chain = prompt | llm | parser
    result = chain.invoke({"file_paths": file_paths})

    state["readme_imp"] = result.get("readme_imp", [])
    return state


# reading 
# def read_data(state: node1state ) -> node1state:





def build_judge_graph():
    graph = StateGraph(node1state)

    graph.add_node("judge_files", judge_files)
    # graph.add_node("read_data",read_data)

    graph.add_edge(START, "judge_files")
    # graph.add_edge("judge_files","read_data")
    graph.add_edge("judge_files", END)


    return graph.compile()