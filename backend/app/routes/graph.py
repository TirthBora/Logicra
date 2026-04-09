from fastapi import APIRouter
from app.services.parser import parse_project
from app.services.graph_builder import build_graph

router=APIRouter()
@router.post("/graph")
def generate_graph(project_path:str):
    dependency_map=parse_project(project_path)
    print("Dependency Map:", dependency_map)
    
    graph=build_graph(dependency_map)
    print("Generated Graph:", graph)
    return graph
