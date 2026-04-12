from fastapi import FastAPI
from app.routes.graph import router as graph_router

app=FastAPI()
app.include_router(graph_router)

@app.get("/")
def home():
    return {
        "message":"Logicra API is running"
    }