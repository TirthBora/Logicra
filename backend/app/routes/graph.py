from fastapi import APIRouter
from app.services.parser import parse_project
from app.services.graph_builder import build_graph

router=APIRouter()
@router.post("/graph")
def generate_grapg(project_path:str):
    dependacy_map=parse_project(project_path)
    graph=build_graph(dependacy_map)
    return graph
