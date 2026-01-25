from typing_extensions import List, Dict, TypedDict
from langgraph.graph import StateGraph, END , START
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()

# STATE
class node1state(TypedDict,total=False):
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
You are an expert technical writer and senior software engineer.
Your task is to generate a high-quality, professional README.md file for a GitHub repository.

Task:
You are provided with:
- A GitHub repository URL
- Parsed repository metadata retrieved via the GitHub API, including:
  - File and folder structure
  - Source code contents
  - Package/config files (package.json, pyproject.toml, go.mod, etc.)
  - Scripts, environment files, and documentation (if any)

Rules:
- You must NOT invent features
- You must infer everything strictly from the parsed repository data
- Use ONLY file paths exactly as provided
- Do NOT explain
- Do NOT add extra text
- Return JSON only
- No markdown outside JSON
- No comments
- No analysis
- No assumptions

Objective:
Analyze the repository to:
- Understand the project purpose
- Identify the tech stack
- Infer features and working logic
- Understand project structure
- Extract setup and scripts
- Generate a complete professional README.md

README Structure (Mandatory Order):
1. Project Title  
2. Description  
3. Tech Stack  
4. Project Structure  
5. Features  
6. How It Works  
7. Setup & Installation  
8. Scripts / Commands  
9. Future Improvements  

Return JSON Format:

{
  "project_title": "",
  "description": "",
  "tech_stack": {
    "frontend": [],
    "backend": [],
    "database": [],
    "apis": [],
    "tooling": []
  },
  "project_structure": [
    {
      "path": "",
      "description": ""
    }
  ],
  "features": [],
  "how_it_works": [],
  "setup_installation": [],
  "scripts": [],
  "future_improvements": [],
  "readme_md": ""
}

Where:
- `project_structure.path` must use exact paths from {file_paths}
- `readme_md` must contain the full README in Markdown format
- All sections must be generated
- No field can be null
- Empty arrays allowed if data is not inferable

""")





# def functions:
def judge_files(state: node1state) -> node1state:
    file_paths = [f["path"] for f in state["files"]]

    chain = prompt | llm | parser
    result = chain.invoke({"file_paths": file_paths})

    state["readme_imp"] = result.get("readme_imp", [])
    return state


def build_judge_graph():
    graph = StateGraph(node1state)

    graph.add_node("judge_files", judge_files)
    # graph.add_node("read_data",read_data)

    graph.add_edge(START, "judge_files")
    # graph.add_edge("judge_files","read_data")
    graph.add_edge("judge_files", END)


    return graph.compile()