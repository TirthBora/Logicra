from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class GraphRequest(BaseModel):
    project_path: str

class Node(BaseModel):
    id: str
    name: str
    type: str  # "file", "function", "class"

class Edge(BaseModel):
    source: str
    target: str
    type: str  # "import", "call"

class GraphResponse(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@router.post("/", response_model=GraphResponse)
async def generate_graph(request: GraphRequest):
    # TODO: Implement graph generation
    return GraphResponse(nodes=[], edges=[])

