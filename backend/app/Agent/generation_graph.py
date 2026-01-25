from typing_extensions import List, Dict, TypedDict
from langgraph.graph import StateGraph, END , START
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()


class Node2State(TypedDict):
    path: str
    content: str
    readme: str


#LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API"),
    temperature=0
)








def readme_gen_func(state: Node2State) -> Node2State:

    return state


def generate_readme_graph():
    readme_gen = StateGraph(Node2State)

    readme_gen.add_node("readme_gen_func", readme_gen_func)

    readme_gen.add_edge(START, "readme_gen_func")
    readme_gen.add_edge("readme_gen_func", END)


    return readme_gen.compile()