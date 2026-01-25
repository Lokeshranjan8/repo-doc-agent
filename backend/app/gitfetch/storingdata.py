from app.Agent.readfile import read_file
from typing_extensions import List, Dict, TypedDict

class dat_response(TypedDict):
    raw_data: List[Dict[str,str]]



def storingdata(data) -> dat_response:
    try:
        repos = data["repo"]
        raw_content = []
        for path in data["readme_imp"]:
            content = read_file(repos,path)
            raw_content.append({
                "path":path,
                "content":content
            })

        return{
            "raw_data":raw_content
        }

    
    except Exception as e:
        return f"Error reading file: {str(e)}"