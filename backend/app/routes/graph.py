from fastapi import APIRouter
from pydantic import BaseModel
from app.services.parser import parse_project
from app.services.graph_builder import build_graph

router = APIRouter(prefix="/api")

class ProjectRequest(BaseModel):
    project_path: str

@router.post("/graph")
def generate_graph(req: ProjectRequest):
    dependency_map = parse_project(req.project_path)
    print("Dependency Map:", dependency_map)

    graph = build_graph(dependency_map)
    print("Generated Graph:", graph)

    return graph