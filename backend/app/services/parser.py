import os
import ast
import re
from app.services.graph_builder import build_graph
EXTENSIONS={
    ".py": "python",
    ".js": "javascript",
    ".ts": "javascript",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".h": "cpp",
}
def get_all_files(project_path):
    file_list=[]

    for root,_,files in os.walk(project_path):
        for file in files:
            full_path=os.path.join(root,file)
            file_list.append(full_path)
    return file_list
def detect_lang(file_path):
     _, ext=os.path.splitext(file_path)
     return EXTENSIONS.get(ext,"unknown")

def parse_python(file_path):
    imports=[]
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            tree=ast.parse(f.read())

        for node in ast.walk(tree):
            if isinstance(node,ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node,ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
    except Exception :
        pass
    return imports
    
def parse_javascript(file_path):
    imports = []
    pattern = r'import\s+(?:.*?\s+from\s+)?[\'"](.*?)[\'"]'

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        imports += re.findall(pattern, content)

        # require()
        requires = re.findall(r'require\([\'"](.*?)[\'"]\)', content)
        imports += requires

    except Exception:
        pass

    return imports


# ☕ Java
def parse_java(file_path):
    imports = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        imports = re.findall(r'import\s+([\w\.]+);', content)

    except Exception:
        pass

    return imports
def parse_cpp(file_path):
    imports = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        imports = re.findall(r'#include\s+[<"](.+?)[>"]', content)

    except Exception:
        pass

    return imports
def parse_generic(file_path):
    return []

def extract_imports(file_path):
    lang=detect_lang(file_path)
    if lang=="python":
        return parse_python(file_path)
    elif lang=="javascript":
        return parse_javascript(file_path)
    elif lang=="java":
        return parse_java(file_path)
    elif lang in ["c","cpp"]:
        return parse_cpp(file_path)
    else:
        return parse_generic(file_path)
def parse_project(project_path):
    files=get_all_files(project_path)
    dependency_map={}
    for file_path in files:
        file_name=os.path.relpath(file_path,project_path)
        imports = extract_imports(file_path)
        dependency_map[file_name]={
            "language": detect_lang(file_path),
            "imports":imports
        }
    return dependency_map

if __name__=="__main__":
    project_path="../../../sample_projects/project1"
    dependency_map=parse_project(project_path)
    graph=build_graph(dependency_map)
    print("\nNODES:")
    for n in graph["nodes"]:
        print(n)
    print("\nEDGES:")
    for e in graph["edges"]:
        print(e)