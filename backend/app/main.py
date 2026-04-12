from fastapi import FastAPI
from app.routes.graph import router as graph_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(graph_router)

@app.get("/")
def home():
    return {
        "message":"Logicra API is running"
    }
