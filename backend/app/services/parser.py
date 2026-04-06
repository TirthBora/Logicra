import ast
import os
from typing import Dict, List

def parse_python_file(file_path: str) -> Dict:
    """Parse Python file to extract functions, classes, imports"""
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    
    imports = []
    functions = []
    classes = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.append([alias.name for alias in node.names])
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
    
    return {
        'file': file_path,
        'imports': imports,
        'functions': functions,
        'classes': classes
    }

def parse_project(project_path: str) -> List[Dict]:
    """Parse all Python files in project"""
    results = []
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                results.append(parse_python_file(file_path))
    return results

