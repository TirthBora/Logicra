import networkx as nx
from .parser import parse_project

def build_graph(project_path: str) -> nx.DiGraph:
    """Build dependency graph from parsed files"""
    G = nx.DiGraph()
    parsed_files = parse_project(project_path)
    
    for parsed in parsed_files:
        file_node = parsed['file']
        G.add_node(file_node, type='file')
        
        for func in parsed['functions']:
            G.add_node(f"{file_node}:{func}", type='function')
            G.add_edge(file_node, f"{file_node}:{func}")
        
        for cls in parsed['classes']:
            G.add_node(f"{file_node}:{cls}", type='class')
            G.add_edge(file_node, f"{file_node}:{cls}")
    
    # TODO: Add cross-file edges based on imports
    return G

def graph_to_api_format(G: nx.DiGraph):
    nodes = [{'id': n, 'name': n.split(':')[-1], 'type': G.nodes[n]['type']} for n in G.nodes]
    edges = [{'source': u, 'target': v, 'type': 'depends'} for u, v in G.edges]
    return {'nodes': nodes, 'edges': edges}

