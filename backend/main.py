from fastapi import FastAPI
from backend.infrastructure.routers.tarea_router import router as tarea_router

app = FastAPI(title="API de Tareas", description="API para gestionar tareas", version="1.0.0")

app.include_router(tarea_router, tags=["Tareas"])
