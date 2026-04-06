from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import graph, clone, explain, error

app = FastAPI(title="Logicra API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graph.router, prefix="/api/graph", tags=["graph"])
app.include_router(clone.router, prefix="/api/clone", tags=["clone"])
app.include_router(explain.router, prefix="/api/explain", tags=["explain"])
app.include_router(error.router, prefix="/api/error", tags=["error"])

@app.get("/")
def read_root():
    return {"message": "Logicra API is running"}

