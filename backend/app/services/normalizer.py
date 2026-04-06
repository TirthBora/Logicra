import re

def normalize_code(code: str) -> str:
    """Normalize code for clone detection: remove comments, rename vars, normalize whitespace"""
    # Remove comments
    code = re.sub(r'#. *\\n', '\\n', code)
    
    # Remove strings (basic)
    code = re.sub(r'\'[^\']*\'', '"STR"', code)
    code = re.sub(r'\"[^\"]*\"', '"STR"', code)
    
    # Normalize whitespace
    code = re.sub(r'\\s+', ' ', code)
    
    # Rename variables (simple replacement of identifiers)
    # This is basic - production would need proper AST parsing
    words = re.findall(r'\\b[a-zA-Z_]\\w*\\b', code)
    var_map = {word: f'VAR{i}' for i, word in enumerate(set(w for w in words if len(w) < 20))}
    for old, new in var_map.items():
        code = re.sub(rf'\\b{re.escape(old)}\\b', new, code)
    
    return code.strip()

