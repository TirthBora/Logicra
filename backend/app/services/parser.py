import os
import ast
import re

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

