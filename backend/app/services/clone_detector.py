import difflib
import hashlib
from .normalizer import normalize_code
from typing import List, Dict

def detect_clones(parsed_files: List[Dict], threshold: float = 0.8) -> List[Dict]:
    """Detect code clones using normalized code similarity"""
    clones = []
    normalized_codes = []
    
    for parsed in parsed_files:
        code = normalize_code(parsed['raw_code'])
        hash_val = hashlib.md5(code.encode()).hexdigest()
        normalized_codes.append({
            'file': parsed['file'],
            'code': code,
            'hash': hash_val
        })
    
    # Simple pairwise comparison
    for i in range(len(normalized_codes)):
        for j in range(i+1, len(normalized_codes)):
            similarity = difflib.SequenceMatcher(
                None, normalized_codes[i]['code'], normalized_codes[j]['code']
            ).ratio()
            
            if similarity > threshold:
                clones.append({
                    'file1': normalized_codes[i]['file'],
                    'file2': normalized_codes[j]['file'],
                    'similarity': similarity,
                    'hash1': normalized_codes[i]['hash'],
                    'hash2': normalized_codes[j]['hash']
                })
    
    return clones

