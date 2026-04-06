import os
import glob

def read_project_files(project_path: str, extensions: List[str] = ['*.py', '*.js']) -> List[str]:
    """Read all files in project with given extensions"""
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(project_path, '**', ext), recursive=True))
    return files

def read_file_content(file_path: str) -> str:
    """Read file content safely"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as f:
            return f.read()

def ensure_project_path(path: str) -> str:
    """Ensure path exists and is absolute"""
    abs_path = os.path.abspath(path)
    if not os.path.exists(abs_path):
        raise ValueError(f"Project path does not exist: {abs_path}")
    return abs_path

